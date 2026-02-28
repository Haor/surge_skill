# Surge 文档

Surge 官方文档的本地镜像 + 社区教程，供 Claude Code Skill 按需索引。

## 官方文档

| 目录 | 来源 | 语言 | 文件数 | 说明 |
|------|------|------|--------|------|
| `manual/` | [manual.nssurge.com](https://manual.nssurge.com) | EN | 58 | 配置参考：规则、策略、DNS、脚本、HTTP 处理等 |
| `kb/zh/` | [kb.nssurge.com](https://kb.nssurge.com) | ZH | 32 | 知识库：指南、技术笔记、FAQ、授权、更新日志 |
| `kb/en/` | [kb.nssurge.com](https://kb.nssurge.com) | EN | 31 | 知识库（英文版） |

**共计 121 个官方文件，约 14,600 行。**

## 社区内容

| 目录 | 来源 | 作者 | 最后更新 | 文件数 |
|------|------|------|---------|--------|
| `community/skk-surge-tips.md` | [Sukka's Blog](https://blog.skk.moe/post/i-have-my-unique-surge-setup/) | Sukka (SKK) | 2026-01-02 | 1 |
| `community/zhuangzhuang/` | [壮壮配置详解](https://zhuangzhuang.io/2018/11/14/surge.html) | 壮壮 | 2025-08-20 | 5 |
| `community/policy-icons.md` | [Telegraph](https://telegra.ph/策略图标订阅-合集-03-12-2) | 社区 | — | 1 |

> **注意**：社区教程可能已过时，请以 `manual/` 官方文档为准。SKK 博客采用 CC BY-NC-SA 4.0 许可。

---

## manual/ — 配置参考手册

Surge 每个配置段的详细文档。

### 入门

| 文件 | 话题 |
|------|------|
| `index.md` | Surge 概览与功能列表 |
| `overview/components.md` | 架构组件 |
| `overview/configuration.md` | 配置文件结构 |
| `book/understanding-surge/en.md` | 理解 Surge（EN） |
| `book/understanding-surge/cn.md` | 理解 Surge（ZH） |

### 规则

| 文件 | 话题 |
|------|------|
| `rule.md` | 规则系统概述 |
| `rule/domain-based.md` | DOMAIN、DOMAIN-SUFFIX、DOMAIN-KEYWORD |
| `rule/ip-based.md` | IP-CIDR、IP-CIDR6、GEOIP、IP-ASN |
| `rule/http.md` | USER-AGENT、URL-REGEX、HEADER |
| `rule/process.md` | PROCESS-NAME（macOS） |
| `rule/logical-rule.md` | AND、OR、NOT |
| `rule/subnet.md` | SUBNET |
| `rule/misc-rule.md` | DEST-PORT、IN-PORT、SRC-IP、PROTOCOL |
| `rule/ruleset.md` | RULE-SET |
| `rule/final.md` | FINAL |

### 策略

| 文件 | 话题 |
|------|------|
| `policy.md` | 策略概述 |
| `policy/built-in.md` | DIRECT、REJECT |
| `policy/reject.md` | REJECT 变体 |
| `policy/proxy.md` | 代理协议（SS、HTTPS、SOCKS5、Trojan 等） |
| `policy/wireguard.md` | WireGuard |
| `policy/ssh.md` | SSH 隧道 |
| `policy/parameters.md` | 通用参数（TFO、ECN 等） |
| `policy/external-proxy.md` | 外部代理 |

### 策略组

| 文件 | 话题 |
|------|------|
| `policy-group/group.md` | 策略组概述 |
| `policy-group/select.md` | 手动选择 |
| `policy-group/url-test.md` | 自动测速 |
| `policy-group/fallback.md` | 故障切换 |
| `policy-group/subnet.md` | SSID/子网 |
| `policy-group/load-balance.md` | 负载均衡 |
| `policy-group/policy-including.md` | 策略嵌套引用 |
| `policy-group/common-parameters.md` | 通用参数 |

### DNS

| 文件 | 话题 |
|------|------|
| `dns/dns-override.md` | DNS 服务器配置 |
| `dns/local-dns-mapping.md` | 本地 DNS 映射 |
| `dns/doh.md` | DNS-over-HTTPS / DNS-over-QUIC |

### HTTP 处理

| 文件 | 话题 |
|------|------|
| `http-processing.md` | 概述 |
| `http-processing/mitm.md` | HTTPS 解密（MitM） |
| `http-processing/url-rewrite.md` | URL 重写 |
| `http-processing/header-rewrite.md` | Header 重写 |
| `http-processing/body-rewrite.md` | Body 重写 |
| `http-processing/mock.md` | Mock（Map Local） |

### 脚本

| 文件 | 话题 |
|------|------|
| `scripting/common.md` | 脚本基础与公共 API |
| `scripting/http-request.md` | HTTP 请求脚本 |
| `scripting/http-response.md` | HTTP 响应脚本 |
| `scripting/rule.md` | 规则脚本 |
| `scripting/event.md` | 事件脚本 |
| `scripting/dns.md` | DNS 脚本 |
| `scripting/cron.md` | 定时脚本 |

### 其它

| 文件 | 话题 |
|------|------|
| `others/misc-options.md` | `[General]` 选项 |
| `others/managed-profile.md` | 托管配置 |
| `others/enhanced-mode.md` | 增强模式（VIF） |
| `others/subnet-settings.md` | 子网设置 |
| `others/host-list.md` | 主机列表参数类型 |
| `others/url-scheme.md` | URL Scheme |
| `others/module.md` | 模块 |
| `others/http-api.md` | HTTP API |
| `others/panel.md` | 信息面板 |
| `others/port-forwarding.md` | 端口转发 |
| `others/cli.md` | Surge Mac CLI |

---

## kb/ — 知识库

实用指南、技术深入、FAQ 和更新日志。提供 `zh/`（中文）和 `en/`（英文）两个版本。

### 指南 (guidelines/)

| 文件 | 话题 |
|------|------|
| `troubleshooting.md` | 故障排除 |
| `gateway.md` | 网关模式配置 |
| `gateway-performance-issue.md` | 网关性能问题 |
| `smart-group.md` | 智能策略组 |
| `ponte.md` | Surge Ponte |
| `tvos.md` | Surge tvOS |
| `detached-profile.md` | 分离配置 |
| `proxy-provider.md` | 代理提供者（仅中文） |

### 技术笔记 (technotes/)

| 文件 | 话题 |
|------|------|
| `dns.md` | 本地 DNS vs 代理 DNS |
| `http-protocol-version.md` | HTTP 协议版本 |
| `tfo.md` | TCP Fast Open |
| `testing-group.md` | 自动策略组测速策略 |
| `reject.md` | REJECT 策略差异 |
| `user-agent.md` | User-Agent 规则 |
| `nat-type.md` | NAT 类型 |
| `ipv6-ra.md` | IPv6 RA Override |
| `udp-fast-path.md` | VM UDP Fast Path |

### 常见问题 (faq/)

| 文件 | 话题 |
|------|------|
| `common-faqs.md` | 常见问题 |
| `ios-testflight.md` | iOS TestFlight |
| `mac-reset.md` | 重置 Surge Mac |

### 授权 (license/)

| 文件 | 话题 |
|------|------|
| `pre-sale.md` | 购买前常见问题 |
| `ios-faq.md` | iOS 授权 |
| `ios-fus.md` | iOS 功能解锁订阅 |
| `mac-faq.md` | Mac 授权 |
| `mac-fus.md` | Mac 功能解锁订阅 |

### 更新日志 (release-notes/)

| 文件 | 话题 |
|------|------|
| `surge-mac-6.md` | Surge Mac 6 概览 |
| `surge-mac-6-release-note.md` | Surge Mac 6.0 发布说明 |
| `surge-ios.md` | Surge iOS 更新日志 |
| `surge-mac-legacy.md` | Surge Mac 旧版本 |
| `snell.md` | Snell 协议 |

---

## community/ — 社区教程

### SKK 进阶技巧

`skk-surge-tips.md` — Sukka 的 Surge 进阶使用技巧，涵盖 DNS 防泄漏、Fake IP、规则排序、TUN 引擎模式、广告拦截、CDN 分流、流媒体规则、多网卡切换等。

### 壮壮配置详解

按 INI 配置段拆分为 5 个文件，便于按需加载：

| 文件 | 内容 |
|------|------|
| `zhuangzhuang/general.md` | `[General]`、`[Replica]` 参数 |
| `zhuangzhuang/proxy-and-group.md` | `[Proxy]`、`[Proxy Group]` 写法 |
| `zhuangzhuang/rule.md` | `[Rule]` 全部规则类型 |
| `zhuangzhuang/rewrite-and-mitm.md` | `[Host]`、`[URL Rewrite]`、`[Header Rewrite]`、`[Map Local]`、`[SSID Setting]`、`[MITM]`、`[Snell Server]` |
| `zhuangzhuang/script-and-module.md` | `[Script]`、模块系统、社区规则集 |

### 策略图标

`policy-icons.md` — 策略组图标订阅 JSON URL 合集。

---

## 维护

重新爬取和清洗（脚本使用 `__file__` 相对路径，任意目录均可运行）：

```bash
# 重新爬取 manual（通过 Jina Reader）并清洗
python3 scripts/crawl_surge_docs.py   # → docs/manual/
python3 scripts/clean_surge_docs.py   # 原地清洗

# 重新爬取知识库（直接获取 .md）
python3 scripts/crawl_surge_kb.py     # → docs/kb/
```

> **注意**：脚本默认跳过已有文件。如需强制重新下载，先删除对应目录再运行：
> ```bash
> rm -rf docs/manual && python3 scripts/crawl_surge_docs.py && python3 scripts/clean_surge_docs.py
> rm -rf docs/kb && python3 scripts/crawl_surge_kb.py
> ```

## 格式说明

- **manual/**：清洗后的 Markdown。每个文件顶部保留元数据头（`Title:`、`URL Source:`、`Published Time:`）。
- **kb/**：GitBook 原始 Markdown。包含 GitBook 模板标签（`{% hint %}`、`{% tabs %}`、`{% stepper %}`），这些是有意义的内容结构，非噪声。
- **community/**：从 HTML 手动保存后提取清洗的 Markdown。每个文件顶部有 YAML frontmatter 标注来源、作者和时效性。
