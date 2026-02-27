#!/usr/bin/env python3
"""爬取 Surge Knowledge Base 文档.

基于 llms.txt 提供的页面列表，直接获取 GitBook 原始 Markdown 文件。
内容已经是干净的 Markdown（含 GitBook 模板标签），无需额外清理。
"""

import asyncio
import aiohttp
import sys
from pathlib import Path

BASE_URL = "https://kb.nssurge.com/"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "kb"
TIMEOUT = 60
REQUEST_DELAY = 1  # 直接获取 .md，比 Jina Reader 快，间隔可更短
MAX_RETRIES = 3
RETRY_BACKOFF = 5

# 从 llms.txt 提取的所有页面: (URL 路径, 输出文件路径)
PAGES = [
    # === 中文 ===
    ("surge-knowledge-base/zh/readme.md", "zh/readme.md"),
    ("surge-knowledge-base/zh/guidelines/troubleshooting.md", "zh/guidelines/troubleshooting.md"),
    ("surge-knowledge-base/zh/guidelines/gateway.md", "zh/guidelines/gateway.md"),
    ("surge-knowledge-base/zh/guidelines/smart-group.md", "zh/guidelines/smart-group.md"),
    ("surge-knowledge-base/zh/guidelines/ponte.md", "zh/guidelines/ponte.md"),
    ("surge-knowledge-base/zh/guidelines/tvos.md", "zh/guidelines/tvos.md"),
    ("surge-knowledge-base/zh/guidelines/gateway-performance-issue.md", "zh/guidelines/gateway-performance-issue.md"),
    ("surge-knowledge-base/zh/guidelines/detached-profile.md", "zh/guidelines/detached-profile.md"),
    ("surge-knowledge-base/zh/guidelines/proxy-provider.md", "zh/guidelines/proxy-provider.md"),
    ("surge-knowledge-base/zh/technotes/tfo.md", "zh/technotes/tfo.md"),
    ("surge-knowledge-base/zh/technotes/http-protocol-version.md", "zh/technotes/http-protocol-version.md"),
    ("surge-knowledge-base/zh/technotes/dns.md", "zh/technotes/dns.md"),
    ("surge-knowledge-base/zh/technotes/testing-group.md", "zh/technotes/testing-group.md"),
    ("surge-knowledge-base/zh/technotes/reject.md", "zh/technotes/reject.md"),
    ("surge-knowledge-base/zh/technotes/user-agent.md", "zh/technotes/user-agent.md"),
    ("surge-knowledge-base/zh/technotes/nat-type.md", "zh/technotes/nat-type.md"),
    ("surge-knowledge-base/zh/technotes/ipv6-ra.md", "zh/technotes/ipv6-ra.md"),
    ("surge-knowledge-base/zh/technotes/udp-fast-path.md", "zh/technotes/udp-fast-path.md"),
    ("surge-knowledge-base/zh/faq/common-faqs.md", "zh/faq/common-faqs.md"),
    ("surge-knowledge-base/zh/faq/ios-testflight.md", "zh/faq/ios-testflight.md"),
    ("surge-knowledge-base/zh/faq/mac-reset.md", "zh/faq/mac-reset.md"),
    ("surge-knowledge-base/zh/license/pre-sale.md", "zh/license/pre-sale.md"),
    ("surge-knowledge-base/zh/license/ios-faq.md", "zh/license/ios-faq.md"),
    ("surge-knowledge-base/zh/license/ios-fus.md", "zh/license/ios-fus.md"),
    ("surge-knowledge-base/zh/license/mac-faq.md", "zh/license/mac-faq.md"),
    ("surge-knowledge-base/zh/license/mac-fus.md", "zh/license/mac-fus.md"),
    ("surge-knowledge-base/zh/release-notes/surge-mac-6.md", "zh/release-notes/surge-mac-6.md"),
    ("surge-knowledge-base/zh/release-notes/surge-mac-6-release-note.md", "zh/release-notes/surge-mac-6-release-note.md"),
    ("surge-knowledge-base/zh/release-notes/surge-ios.md", "zh/release-notes/surge-ios.md"),
    ("surge-knowledge-base/zh/release-notes/surge-mac-legacy.md", "zh/release-notes/surge-mac-legacy.md"),
    ("surge-knowledge-base/zh/release-notes/snell.md", "zh/release-notes/snell.md"),
    # === English ===
    ("surge-knowledge-base/readme.md", "en/readme.md"),
    ("surge-knowledge-base/guidelines/troubleshooting.md", "en/guidelines/troubleshooting.md"),
    ("surge-knowledge-base/guidelines/gateway.md", "en/guidelines/gateway.md"),
    ("surge-knowledge-base/guidelines/smart-group.md", "en/guidelines/smart-group.md"),
    ("surge-knowledge-base/guidelines/ponte.md", "en/guidelines/ponte.md"),
    ("surge-knowledge-base/guidelines/tvos.md", "en/guidelines/tvos.md"),
    ("surge-knowledge-base/guidelines/gateway-performance-issue.md", "en/guidelines/gateway-performance-issue.md"),
    ("surge-knowledge-base/guidelines/detached-profile.md", "en/guidelines/detached-profile.md"),
    ("surge-knowledge-base/technotes/tfo.md", "en/technotes/tfo.md"),
    ("surge-knowledge-base/technotes/http-protocol-version.md", "en/technotes/http-protocol-version.md"),
    ("surge-knowledge-base/technotes/dns.md", "en/technotes/dns.md"),
    ("surge-knowledge-base/technotes/testing-group.md", "en/technotes/testing-group.md"),
    ("surge-knowledge-base/technotes/reject.md", "en/technotes/reject.md"),
    ("surge-knowledge-base/technotes/user-agent.md", "en/technotes/user-agent.md"),
    ("surge-knowledge-base/technotes/nat-type.md", "en/technotes/nat-type.md"),
    ("surge-knowledge-base/technotes/ipv6-ra.md", "en/technotes/ipv6-ra.md"),
    ("surge-knowledge-base/technotes/udp-fast-path.md", "en/technotes/udp-fast-path.md"),
    ("surge-knowledge-base/faq/common-faqs.md", "en/faq/common-faqs.md"),
    ("surge-knowledge-base/faq/ios-testflight.md", "en/faq/ios-testflight.md"),
    ("surge-knowledge-base/faq/mac-reset.md", "en/faq/mac-reset.md"),
    ("surge-knowledge-base/license/pre-sale.md", "en/license/pre-sale.md"),
    ("surge-knowledge-base/license/ios-faq.md", "en/license/ios-faq.md"),
    ("surge-knowledge-base/license/ios-fus.md", "en/license/ios-fus.md"),
    ("surge-knowledge-base/license/mac-faq.md", "en/license/mac-faq.md"),
    ("surge-knowledge-base/license/mac-fus.md", "en/license/mac-fus.md"),
    ("surge-knowledge-base/release-notes/surge-mac-6.md", "en/release-notes/surge-mac-6.md"),
    ("surge-knowledge-base/release-notes/surge-mac-6-release-note.md", "en/release-notes/surge-mac-6-release-note.md"),
    ("surge-knowledge-base/release-notes/surge-ios.md", "en/release-notes/surge-ios.md"),
    ("surge-knowledge-base/release-notes/surge-mac-legacy.md", "en/release-notes/surge-mac-legacy.md"),
    ("surge-knowledge-base/release-notes/snell.md", "en/release-notes/snell.md"),
]


async def fetch_one(
    session: aiohttp.ClientSession,
    url_path: str,
    output_file: str,
    index: int,
    total: int,
) -> bool:
    """获取单个页面，带指数退避重试."""
    url = f"{BASE_URL}{url_path}"
    out_path = OUTPUT_DIR / output_file

    if out_path.exists() and out_path.stat().st_size > 50:
        print(f"  skip [{index}/{total}] {output_file}")
        return True

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with session.get(
                url,
                timeout=aiohttp.ClientTimeout(total=TIMEOUT),
            ) as resp:
                if resp.status == 429:
                    wait = RETRY_BACKOFF * attempt
                    print(f"  wait [{index}/{total}] {output_file} — 429, {wait}s (attempt {attempt})")
                    await asyncio.sleep(wait)
                    continue

                if resp.status != 200:
                    print(f"  fail [{index}/{total}] {output_file} — HTTP {resp.status} (attempt {attempt})")
                    await asyncio.sleep(RETRY_BACKOFF)
                    continue

                content = await resp.text()

            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
            print(f"    ok [{index}/{total}] {output_file}")
            return True

        except Exception as e:
            wait = RETRY_BACKOFF * attempt
            print(f"  fail [{index}/{total}] {output_file} — {e} (attempt {attempt}, wait {wait}s)")
            await asyncio.sleep(wait)

    print(f"  FAIL [{index}/{total}] {output_file}")
    return False


async def main():
    total = len(PAGES)
    print(f"Crawling Surge Knowledge Base: {total} pages")
    print(f"Output: {OUTPUT_DIR}/\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    success = 0
    failed = []

    async with aiohttp.ClientSession() as session:
        for i, (url_path, out_file) in enumerate(PAGES, 1):
            ok = await fetch_one(session, url_path, out_file, i, total)
            if ok:
                success += 1
            else:
                failed.append(out_file)
            if i < total:
                await asyncio.sleep(REQUEST_DELAY)

    print(f"\nDone: {success}/{total} saved to {OUTPUT_DIR}/")
    if failed:
        print(f"\nFailed ({len(failed)}):")
        for f in failed:
            print(f"  - {f}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
