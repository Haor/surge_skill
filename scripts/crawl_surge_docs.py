#!/usr/bin/env python3
"""爬取 Surge 官方文档并通过 Jina Reader 转为 Markdown 格式保存到本地.

策略：顺序请求，每次请求间间隔 3 秒，跳过已存在的文件，失败时带退避重试。
"""

import asyncio
import aiohttp
import sys
from pathlib import Path

BASE_URL = "https://manual.nssurge.com/"
JINA_PREFIX = "https://r.jina.ai/"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "manual"
TIMEOUT = 90  # 每个请求超时秒数
REQUEST_DELAY = 3  # 请求间隔秒数
MAX_RETRIES = 3  # 每个页面最多重试次数
RETRY_BACKOFF = 10  # 重试退避基础秒数

# 所有页面: (URL 路径, 输出文件路径)
PAGES = [
    ("", "index.md"),
    ("overview/components.html", "overview/components.md"),
    ("overview/configuration.html", "overview/configuration.md"),
    ("rule.html", "rule.md"),
    ("rule/domain-based.html", "rule/domain-based.md"),
    ("rule/ip-based.html", "rule/ip-based.md"),
    ("rule/http.html", "rule/http.md"),
    ("rule/process.html", "rule/process.md"),
    ("rule/logical-rule.html", "rule/logical-rule.md"),
    ("rule/subnet.html", "rule/subnet.md"),
    ("rule/misc-rule.html", "rule/misc-rule.md"),
    ("rule/ruleset.html", "rule/ruleset.md"),
    ("rule/final.html", "rule/final.md"),
    ("policy.html", "policy.md"),
    ("policy/built-in.html", "policy/built-in.md"),
    ("policy/reject.html", "policy/reject.md"),
    ("policy/proxy.html", "policy/proxy.md"),
    ("policy/wireguard.html", "policy/wireguard.md"),
    ("policy/ssh.html", "policy/ssh.md"),
    ("policy/parameters.html", "policy/parameters.md"),
    ("policy/external-proxy.html", "policy/external-proxy.md"),
    ("policy-group/group.html", "policy-group/group.md"),
    ("policy-group/select.html", "policy-group/select.md"),
    ("policy-group/url-test.html", "policy-group/url-test.md"),
    ("policy-group/fallback.html", "policy-group/fallback.md"),
    ("policy-group/subnet.html", "policy-group/subnet.md"),
    ("policy-group/load-balance.html", "policy-group/load-balance.md"),
    ("policy-group/policy-including.html", "policy-group/policy-including.md"),
    ("policy-group/common-parameters.html", "policy-group/common-parameters.md"),
    ("dns/dns-override.html", "dns/dns-override.md"),
    ("dns/local-dns-mapping.html", "dns/local-dns-mapping.md"),
    ("dns/doh.html", "dns/doh.md"),
    ("http-processing.html", "http-processing.md"),
    ("http-processing/mitm.html", "http-processing/mitm.md"),
    ("http-processing/url-rewrite.html", "http-processing/url-rewrite.md"),
    ("http-processing/header-rewrite.html", "http-processing/header-rewrite.md"),
    ("http-processing/body-rewrite.html", "http-processing/body-rewrite.md"),
    ("http-processing/mock.html", "http-processing/mock.md"),
    ("scripting/common.html", "scripting/common.md"),
    ("scripting/http-request.html", "scripting/http-request.md"),
    ("scripting/http-response.html", "scripting/http-response.md"),
    ("scripting/rule.html", "scripting/rule.md"),
    ("scripting/event.html", "scripting/event.md"),
    ("scripting/dns.html", "scripting/dns.md"),
    ("scripting/cron.html", "scripting/cron.md"),
    ("others/misc-options.html", "others/misc-options.md"),
    ("others/managed-profile.html", "others/managed-profile.md"),
    ("others/enhanced-mode.html", "others/enhanced-mode.md"),
    ("others/subnet-settings.html", "others/subnet-settings.md"),
    ("others/host-list.html", "others/host-list.md"),
    ("others/url-scheme.html", "others/url-scheme.md"),
    ("others/module.html", "others/module.md"),
    ("others/http-api.html", "others/http-api.md"),
    ("others/panel.html", "others/panel.md"),
    ("others/port-forwarding.html", "others/port-forwarding.md"),
    ("others/cli.html", "others/cli.md"),
    ("book/understanding-surge/en/", "book/understanding-surge/en.md"),
    ("book/understanding-surge/cn/", "book/understanding-surge/cn.md"),
]


async def fetch_one(
    session: aiohttp.ClientSession,
    url_path: str,
    output_file: str,
    index: int,
    total: int,
) -> bool:
    """获取单个页面，带指数退避重试."""
    jina_url = f"{JINA_PREFIX}{BASE_URL}{url_path}"
    out_path = OUTPUT_DIR / output_file

    # 跳过已存在且非空的文件
    if out_path.exists() and out_path.stat().st_size > 100:
        print(f"  ⊘ [{index}/{total}] {output_file} (已存在，跳过)")
        return True

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with session.get(
                jina_url,
                timeout=aiohttp.ClientTimeout(total=TIMEOUT),
                headers={"Accept": "text/markdown"},
            ) as resp:
                if resp.status == 429:
                    wait = RETRY_BACKOFF * attempt
                    print(f"  ⏳ [{index}/{total}] {output_file} — 429 限流，等待 {wait}s (尝试 {attempt}/{MAX_RETRIES})")
                    await asyncio.sleep(wait)
                    continue

                if resp.status != 200:
                    print(f"  ✗ [{index}/{total}] {output_file} — HTTP {resp.status} (尝试 {attempt}/{MAX_RETRIES})")
                    await asyncio.sleep(RETRY_BACKOFF)
                    continue

                content = await resp.text()

            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
            print(f"  ✓ [{index}/{total}] {output_file}")
            return True

        except Exception as e:
            wait = RETRY_BACKOFF * attempt
            print(f"  ✗ [{index}/{total}] {output_file} — {e} (尝试 {attempt}/{MAX_RETRIES}，等待 {wait}s)")
            await asyncio.sleep(wait)

    print(f"  ✗✗ [{index}/{total}] {output_file} — 最终失败")
    return False


async def main():
    total = len(PAGES)
    print(f"开始爬取 Surge 文档，共 {total} 个页面")
    print(f"请求间隔 {REQUEST_DELAY}s，每页最多重试 {MAX_RETRIES} 次\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    success = 0
    failed_pages = []

    async with aiohttp.ClientSession() as session:
        for i, (url_path, out_file) in enumerate(PAGES, 1):
            ok = await fetch_one(session, url_path, out_file, i, total)
            if ok:
                success += 1
            else:
                failed_pages.append(out_file)

            # 请求间延迟（跳过的页面不延迟）
            if i < total:
                await asyncio.sleep(REQUEST_DELAY)

    print(f"\n{'='*50}")
    print(f"完成: {success}/{total} 个页面成功保存到 {OUTPUT_DIR}/")

    if failed_pages:
        print(f"\n以下 {len(failed_pages)} 个页面最终失败:")
        for f in failed_pages:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print("所有页面均已成功下载！")


if __name__ == "__main__":
    asyncio.run(main())
