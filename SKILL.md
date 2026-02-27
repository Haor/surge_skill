---
name: surge
description: >
  Surge proxy documentation reference. Use when the user asks about Surge
  configuration, profiles, rules (DOMAIN, DOMAIN-SUFFIX, DOMAIN-SET, IP-CIDR,
  GEOIP, RULE-SET, FINAL), policies (Shadowsocks, SS, Trojan, VMess, TUIC,
  Hysteria 2, Snell, AnyTLS, SOCKS5, HTTPS proxy, SSH, WireGuard, DIRECT,
  REJECT, external proxy, proxy chain), policy groups (select, url-test,
  fallback, load-balance, 策略组), DNS (DoH, DoQ, encrypted DNS, local
  mapping, [Host]), HTTP processing (URL rewrite, header rewrite, body rewrite,
  JQ rewrite, MITM, HTTPS 解密, 抓包, mock, Map Local), scripting (cron,
  HTTP request/response, event, rule, DNS, $httpClient, $notification),
  modules (sgmodule), enhanced mode (增强模式, TUN, VIF, Fake IP), HTTP API,
  panel, CLI, managed profile (托管配置), port forwarding, subnet settings,
  URL scheme, troubleshooting (故障排除), gateway mode (旁路由, 透明代理),
  Surge Ponte, tvOS, licensing, FAQ (常见问题), release notes, skip-proxy,
  block-quic, always-real-ip, or proxy subscription (机场订阅).
---

# Surge Documentation Skill

## How to use

1. Match the user's question to one or more topics in the **Routing Table** below.
2. Use the `Read` tool to load the matched file(s). All paths are relative to this skill's directory (`.claude/skills/surge/`). Prepend the project root to form absolute paths (e.g., `{project_root}/.claude/skills/surge/docs/manual/rule/domain-based.md`). Read at most **3 files** per query.
3. Synthesize an answer from the loaded content. Always **cite the source file path**.
4. If the documentation does not cover the question, say so explicitly.

## Language rules

- The manual (`docs/manual/`) is English-only.
- The knowledge base (`docs/kb/`) has both `en/` and `zh/` versions.
- When the user asks in **Chinese**, prefer `docs/kb/zh/` files for KB topics.
- When the user asks in **English**, prefer `docs/kb/en/` files for KB topics.
- For manual topics, always use `docs/manual/` regardless of language, then answer in the user's language.

## Cross-topic dependencies

Some queries require reading files from multiple sections. Key relationships:

- **MITM is prerequisite for HTTPS processing**: URL rewrite, header rewrite, body rewrite, and HTTP scripting on HTTPS traffic all require MITM to be enabled. If the user asks "why doesn't my rewrite work on HTTPS", read `mitm.md` alongside the relevant rewrite doc.
- **Enhanced mode is prerequisite for gateway mode**: Gateway setup requires enhanced mode (TUN/VIF). Read `enhanced-mode.md` alongside `gateway.md`.
- **IP rules interact with DNS**: IP-based rules trigger DNS resolution unless `no-resolve` is specified. If the user asks about DNS + rule interaction, read `kb/technotes/dns.md` alongside `rule/ip-based.md`.
- **Module authoring spans multiple topics**: Writing a module typically requires `module.md` + one of the rewrite/scripting docs + `mitm.md`.
- **Proxy subscription + policy group**: Setting up proxy subscriptions usually involves `external-proxy.md` + a policy group doc (e.g., `url-test.md` or `select.md`) + `policy-including.md`.
- **Scripting common API is shared**: `scripting/common.md` contains `$httpClient`, `$notification`, `$persistentStore` used by all script types. Read it alongside specific script docs when the user asks about scripting APIs.

## Routing Table

All paths below are relative to this skill's directory (`.claude/skills/surge/`).

### Getting Started & Overview

| Topic | File |
|-------|------|
| Surge components overview (架构) | `docs/manual/overview/components.md` |
| Configuration file format (配置文件, [Proxy], [Rule], [General], #!include, Linked Profile, #!REQUIREMENT) | `docs/manual/overview/configuration.md` |
| Understanding Surge (EN) | `docs/manual/book/understanding-surge/en.md` |
| Understanding Surge (CN) | `docs/manual/book/understanding-surge/cn.md` |
| Manual index | `docs/manual/index.md` |

### Rules (规则, 分流)

| Topic | File |
|-------|------|
| Rules overview (规则概述) | `docs/manual/rule.md` |
| Domain-based rules (DOMAIN, DOMAIN-SUFFIX, DOMAIN-KEYWORD, DOMAIN-SET, DOMAIN-WILDCARD) | `docs/manual/rule/domain-based.md` |
| IP-based rules (IP-CIDR, IP-CIDR6, GEOIP, IP-ASN, no-resolve) | `docs/manual/rule/ip-based.md` |
| HTTP rules (USER-AGENT, URL-REGEX, HEADER) | `docs/manual/rule/http.md` |
| Process rules (PROCESS-NAME, macOS) | `docs/manual/rule/process.md` |
| Subnet rules (SUBNET, SSID) | `docs/manual/rule/subnet.md` |
| Logical rules (AND, OR, NOT) | `docs/manual/rule/logical-rule.md` |
| Miscellaneous rules (DEST-PORT, IN-PORT, SRC-IP, PROTOCOL, SCRIPT) | `docs/manual/rule/misc-rule.md` |
| Rule sets (RULE-SET, external rule files, Inline Ruleset, extended-matching, 规则集) | `docs/manual/rule/ruleset.md` |
| FINAL rule | `docs/manual/rule/final.md` |

### Policies (代理, 策略)

| Topic | File |
|-------|------|
| Policies overview (策略概述, [Proxy]) | `docs/manual/policy.md` |
| Built-in policies (DIRECT, REJECT, REJECT-DROP, REJECT-TINYGIF, REJECT-NO-DROP, CELLULAR, HYBRID, NO-HYBRID) | `docs/manual/policy/built-in.md` |
| Proxy protocols (Shadowsocks/SS, Snell, SOCKS5, SOCKS5-TLS, HTTP/HTTPS proxy, Trojan, VMess, TUIC, Hysteria 2, AnyTLS, Shadow TLS, proxy chain/underlying-proxy, obfs, WebSocket, UDP relay, port-hopping, SNI, [Keystore]) | `docs/manual/policy/proxy.md` |
| Policy parameters (TFO, ECN, MPTCP, test-url, test-timeout, block-quic) | `docs/manual/policy/parameters.md` |
| External proxy provider (机场订阅, proxy subscription, proxy-provider, filter) | `docs/manual/policy/external-proxy.md` |
| REJECT policy behavior (REJECT variants deep-dive) | `docs/manual/policy/reject.md` |
| SSH proxy (SSH 代理, SSH tunnel) | `docs/manual/policy/ssh.md` |
| WireGuard proxy (WG, [WireGuard *], DSCP, ECN, peer, private-key) | `docs/manual/policy/wireguard.md` |

### Policy Groups (策略组, [Proxy Group])

| Topic | File |
|-------|------|
| Policy groups overview (策略组概述) | `docs/manual/policy-group/group.md` |
| Select group (手动选择, manual selection) | `docs/manual/policy-group/select.md` |
| URL-Test group (自动测速, auto best latency) | `docs/manual/policy-group/url-test.md` |
| Fallback group (故障切换, 备用) | `docs/manual/policy-group/fallback.md` |
| Load-Balance group (负载均衡) | `docs/manual/policy-group/load-balance.md` |
| Subnet group (SSID-based) | `docs/manual/policy-group/subnet.md` |
| Policy including (嵌套/外部引用, nested, external, policy-path, filter) | `docs/manual/policy-group/policy-including.md` |
| Common group parameters (timeout, interval, tolerance) | `docs/manual/policy-group/common-parameters.md` |

### DNS

| Topic | File |
|-------|------|
| DNS override (DNS 服务器配置, encrypted-dns-server) | `docs/manual/dns/dns-override.md` |
| DNS-over-HTTPS / DNS-over-QUIC (DoH, DoQ, 加密 DNS) | `docs/manual/dns/doh.md` |
| Local DNS mapping ([Host], 本地 DNS 映射, server:system, server:syslib) | `docs/manual/dns/local-dns-mapping.md` |

### HTTP Processing (HTTP 处理, 重写)

| Topic | File |
|-------|------|
| HTTP processing overview (HTTP 处理概述) | `docs/manual/http-processing.md` |
| URL rewrite (URL 重写, [URL Rewrite], 302 redirect, header/reject) | `docs/manual/http-processing/url-rewrite.md` |
| Header rewrite ([Header Rewrite], 修改请求/响应头) | `docs/manual/http-processing/header-rewrite.md` |
| Body rewrite ([Body Rewrite], JQ rewrite, JSON body, 正则替换) | `docs/manual/http-processing/body-rewrite.md` |
| MITM (HTTPS 解密, 抓包, [MITM], Man-in-the-Middle, CA 证书, SSL Pinning, auto-quic-block, h2) | `docs/manual/http-processing/mitm.md` |
| Mock (Map Local, 本地映射, mock response) | `docs/manual/http-processing/mock.md` |

### Scripting (脚本, [Script])

| Topic | File |
|-------|------|
| Scripting common API ($httpClient, $notification, $persistentStore, $utils, $environment, JavaScriptCore, binary-body-mode) | `docs/manual/scripting/common.md` |
| HTTP request script (修改请求, request body/header) | `docs/manual/scripting/http-request.md` |
| HTTP response script (修改响应, response body/header) | `docs/manual/scripting/http-response.md` |
| Cron script (定时脚本, scheduled task) | `docs/manual/scripting/cron.md` |
| DNS script (DNS 脚本) | `docs/manual/scripting/dns.md` |
| Event script (事件脚本, network-changed) | `docs/manual/scripting/event.md` |
| Rule script (规则脚本) | `docs/manual/scripting/rule.md` |

### Other Features

| Topic | File |
|-------|------|
| Enhanced mode (增强模式, Fake IP, TUN, VIF, 虚拟网卡, 198.18.0.0/15, Surge VM Gateway, UDP Fast Path) | `docs/manual/others/enhanced-mode.md` |
| HTTP API (API 控制, 远程控制, external controller) | `docs/manual/others/http-api.md` |
| Module system (模块, sgmodule, .sgmodule, #!arguments, parameter tables) | `docs/manual/others/module.md` |
| Panel (面板, dashboard widgets) | `docs/manual/others/panel.md` |
| CLI (命令行, surge-cli, Surge Mac CLI) | `docs/manual/others/cli.md` |
| Managed profile (托管配置, 远程配置, remote profile) | `docs/manual/others/managed-profile.md` |
| Miscellaneous options ([General], skip-proxy, always-real-ip, hijack-dns, block-quic, force-http-engine-hosts, compatibility-mode, include-all-networks, include-local-networks, all-hybrid, wifi-assist, loglevel) | `docs/manual/others/misc-options.md` |
| Host list (主机列表, host list type) | `docs/manual/others/host-list.md` |
| Port forwarding (端口转发, 端口映射) | `docs/manual/others/port-forwarding.md` |
| Subnet settings (子网设置, per-SSID options) | `docs/manual/others/subnet-settings.md` |
| URL scheme (surge://, surge-action://) | `docs/manual/others/url-scheme.md` |

### KB: Guidelines

| Topic | EN | ZH |
|-------|----|----|
| Gateway setup (旁路由, 透明代理, 网关模式, DHCP, pre-matching) | `docs/kb/en/guidelines/gateway.md` | `docs/kb/zh/guidelines/gateway.md` |
| Gateway performance issue (网关性能问题) | `docs/kb/en/guidelines/gateway-performance-issue.md` | `docs/kb/zh/guidelines/gateway-performance-issue.md` |
| Troubleshooting (故障排除, 问题排查, debug, 系统代理) | `docs/kb/en/guidelines/troubleshooting.md` | `docs/kb/zh/guidelines/troubleshooting.md` |
| Detached profile (关联配置, 分离配置, #!include) | `docs/kb/en/guidelines/detached-profile.md` | `docs/kb/zh/guidelines/detached-profile.md` |
| Surge Ponte (远程访问) | `docs/kb/en/guidelines/ponte.md` | `docs/kb/zh/guidelines/ponte.md` |
| Smart group (智能策略组) | `docs/kb/en/guidelines/smart-group.md` | `docs/kb/zh/guidelines/smart-group.md` |
| tvOS | `docs/kb/en/guidelines/tvos.md` | `docs/kb/zh/guidelines/tvos.md` |
| Proxy provider (代理提供者, 机场订阅) | — | `docs/kb/zh/guidelines/proxy-provider.md` |

### KB: Technical Notes

| Topic | EN | ZH |
|-------|----|----|
| DNS deep-dive (本地 DNS vs 代理 DNS, dns-failed, Fake IP 原理) | `docs/kb/en/technotes/dns.md` | `docs/kb/zh/technotes/dns.md` |
| HTTP protocol version (HTTP/2, HTTP/3, QUIC) | `docs/kb/en/technotes/http-protocol-version.md` | `docs/kb/zh/technotes/http-protocol-version.md` |
| IPv6 Router Advertisement (IPv6 RA, 路由器通告) | `docs/kb/en/technotes/ipv6-ra.md` | `docs/kb/zh/technotes/ipv6-ra.md` |
| NAT type (NAT 类型, Full Cone, Symmetric) | `docs/kb/en/technotes/nat-type.md` | `docs/kb/zh/technotes/nat-type.md` |
| REJECT policy behavior (REJECT 行为差异) | `docs/kb/en/technotes/reject.md` | `docs/kb/zh/technotes/reject.md` |
| Testing / benchmark group (测速策略组) | `docs/kb/en/technotes/testing-group.md` | `docs/kb/zh/technotes/testing-group.md` |
| TCP Fast Open (TFO) | `docs/kb/en/technotes/tfo.md` | `docs/kb/zh/technotes/tfo.md` |
| UDP fast path | `docs/kb/en/technotes/udp-fast-path.md` | `docs/kb/zh/technotes/udp-fast-path.md` |
| User-Agent policy | `docs/kb/en/technotes/user-agent.md` | `docs/kb/zh/technotes/user-agent.md` |

### KB: FAQ

| Topic | EN | ZH |
|-------|----|----|
| Common FAQs (常见问题, 耗电, 助手程序, QUIC, 接管) | `docs/kb/en/faq/common-faqs.md` | `docs/kb/zh/faq/common-faqs.md` |
| iOS TestFlight | `docs/kb/en/faq/ios-testflight.md` | `docs/kb/zh/faq/ios-testflight.md` |
| Mac reset (重置 Surge Mac) | `docs/kb/en/faq/mac-reset.md` | `docs/kb/zh/faq/mac-reset.md` |

### KB: Licensing

| Topic | EN | ZH |
|-------|----|----|
| Pre-sale FAQ (购买前常见问题) | `docs/kb/en/license/pre-sale.md` | `docs/kb/zh/license/pre-sale.md` |
| iOS license FAQ (iOS 授权) | `docs/kb/en/license/ios-faq.md` | `docs/kb/zh/license/ios-faq.md` |
| iOS feature unlock (iOS 功能解锁) | `docs/kb/en/license/ios-fus.md` | `docs/kb/zh/license/ios-fus.md` |
| Mac license FAQ (Mac 授权) | `docs/kb/en/license/mac-faq.md` | `docs/kb/zh/license/mac-faq.md` |
| Mac feature unlock (Mac 功能解锁) | `docs/kb/en/license/mac-fus.md` | `docs/kb/zh/license/mac-fus.md` |

### KB: Release Notes

| Topic | EN | ZH |
|-------|----|----|
| Surge iOS release notes (iOS 更新日志) | `docs/kb/en/release-notes/surge-ios.md` | `docs/kb/zh/release-notes/surge-ios.md` |
| Surge Mac 6 release note (Mac 6 发布说明) | `docs/kb/en/release-notes/surge-mac-6-release-note.md` | `docs/kb/zh/release-notes/surge-mac-6-release-note.md` |
| Surge Mac 6 overview (Mac 6 概览) | `docs/kb/en/release-notes/surge-mac-6.md` | `docs/kb/zh/release-notes/surge-mac-6.md` |
| Surge Mac legacy (旧版本) | `docs/kb/en/release-notes/surge-mac-legacy.md` | `docs/kb/zh/release-notes/surge-mac-legacy.md` |
| Snell protocol (Snell 协议) | `docs/kb/en/release-notes/snell.md` | `docs/kb/zh/release-notes/snell.md` |

### Community Tutorials (社区教程)

| Topic | File |
|-------|------|
| Advanced Surge tips (进阶技巧, DNS 防泄漏, Fake IP, 规则集排序, TUN 引擎模式, 广告拦截, extended-matching, CDN 分流, 流媒体规则, 多网卡切换, SukkaW/Surge 规则集) | `docs/community/skk-surge-tips.md` |
| Config guide: General & Replica (配置详解, [General] 参数, loglevel, skip-proxy, dns-server, doh, 兼容模式, [Replica]) | `docs/community/zhuangzhuang/general.md` |
| Config guide: Proxy & Proxy Group (配置详解, [Proxy] 写法, http/https/socks5/snell/ss/vmess/trojan, [Proxy Group], select/url-test/fallback/ssid/load-balance, policy-path) | `docs/community/zhuangzhuang/proxy-and-group.md` |
| Config guide: Rule (配置详解, [Rule] 全部规则类型, DOMAIN/IP-CIDR/GEOIP/USER-AGENT/URL-REGEX/PROCESS-NAME/RULE-SET/DOMAIN-SET/逻辑规则/FINAL, notification-text) | `docs/community/zhuangzhuang/rule.md` |
| Config guide: Host, Rewrite & MITM (配置详解, [Host]/[URL Rewrite]/[Header Rewrite]/[Map Local]/[SSID Setting]/[MITM]/[Snell Server], ca-p12, hostname) | `docs/community/zhuangzhuang/rewrite-and-mitm.md` |
| Config guide: Script & Module (配置详解, [Script] http-request/http-response/cron/event/rule/dns, 模块 sgmodule, %APPEND%/%INSERT%, 大佬规则集) | `docs/community/zhuangzhuang/script-and-module.md` |
| Policy group icons (策略图标, 图标订阅, icon subscription JSON) | `docs/community/policy-icons.md` |

> **Freshness note**: Community tutorials may be outdated. Always cross-reference with official `docs/manual/` for authoritative information. When citing community content, note the source and date.

## Query handling instructions

- **Scope**: Only read **1–3 files** per query. Pick the most relevant entries from the routing table.
- **Large files**: For release notes or FAQ files that may be long, use the `limit` parameter (e.g., first 200 lines) to avoid flooding the context.
- **Citations**: Always mention which file(s) you referenced, e.g., "Source: `docs/manual/rule/domain-based.md`".
- **Out of scope**: If the user's question is not covered by any file in the routing table, state clearly: "This topic is not covered in the local Surge documentation."
- **Cross-referencing**: Check the "Cross-topic dependencies" section above before answering. If a topic spans multiple areas, read one file from each relevant section.
- **Version specifics**: Release notes files cover version history. For "what's new" questions, read the appropriate release notes file.
- **Config section questions**: When the user asks about a specific INI section (e.g., `[General]`, `[Proxy]`, `[MITM]`), match it to the relevant topic via the aliases in parentheses.
