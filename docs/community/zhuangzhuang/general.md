---
Title: Surge 配置详解 — General & Replica
Source: https://zhuangzhuang.io/2018/11/14/surge.html
Author: 壮壮 (zhuangzhuang)
Original Date: 2018-11-14
Last Updated: 2025-08-20
Crawl Date: 2026-02-27
Part: 1/5
Freshness Warning: >
  Community content, originally written in 2018, last updated 2025-08-20.
  Some options may be outdated or deprecated in newer Surge versions.
  Always cross-reference with official manual (docs/manual/) for
  authoritative and current information.
---

# Surge 配置详解 — [General] & [Replica]

本文最后更新于 2025-08-20，文章内容可能已经过时，如需更新请联系：[mail@zhuangzhuang.io](mailto:mail@zhuangzhuang.io)

**仅供参考，不建议使用**

保护配置, 在Surge中不可修改（**慎用：会导致配置无法编辑、分享**）
```
#!REQUIRE-PROTECTED
```

托管配置，24h更新一次（**托管配置不可编辑**）
```
#!MANAGED-CONFIG https://raw.githubusercontent.com/ydzydzydz/Rules/master/conf/zhuangzhuang/zhuangzhuang.conf interval=86400 strict=true
```

# [General]

日志等级: warning, notify, info, verbose (默认值: notify)
```
loglevel = notify
```

跳过某个域名或者 IP 段, 这些目标主机将不会由 Surge Proxy 处理

(macOS 版本中, 如果启用了 Set as System Proxy, 这些值会被写入到系统网络代理设置)
```
skip-proxy = 127.0.0.1, 192.168.0.0/16, 193.168.0.0/24, 10.0.0.0/8, 172.16.0.0/12, 100.64.0.0/10, localhost, *.local
```

强制使用特定的 DNS 服务器
```
dns-server = 223.5.5.5, 119.29.29.29, 114.114.114.114, 8.8.8.8, system, https://9.9.9.9/dns-query, https://cloudflare-dns.com/dns-query
```

使用 DNS over HTTPS （dns-server 仅会用作进行网络状态检查和解析 doh 域名）
```
doh-server = https://doh.zhuangzhuang.ga/dns-query
```

设置 DOH 请求可以使用规则系统走代理策略，但该策略必须是一个直接使用 IP 的代理策略
```
doh-follow-outbound-mode = true
```

设置 DOH 默认格式请求 (json、wireformat)
```
doh-format = json
```

允许外部控制器访问 Surge, Surge Dashboard 或 Surge CLI 进行管理控制
```
external-controller-access = passw@127.0.0.1:6170
```

是否启动完整的 IPv6 支持 (默认值: false)
```
ipv6 = false
```

TUN规则匹配模式 (默认值: false)
```
enhanced-mode-by-rule = 1
```

拒绝页面显示错误
```
show-error-page-for-reject = true
```

不包括简单主机名
```
exclude-simple-hostnames = true
```

Surge 作为 HTTP/SOCKS5 代理服务器向 Wi-Fi 网络下的其他设备提供服务器
```
allow-wifi-access = true
```

Surge Mac 供外网访问的服务端口
HTTP 代理服务端口 (默认值: 6152)
```
http-listen = 0.0.0.0:8888
```

SOCKS5 代理服务端口 (默认值: 6153)
```
socks5-listen = 0.0.0.0:8889
```

Surge iOS 供外网访问的服务端口 HTTP 代理服务端口 (默认值: 6152)
```
wifi-access-http-port = 8888
```

SOCKS5 代理服务端口 (默认值: 6153)
```
wifi-access-socks5-port = 8889
```

兼容模式（默认禁用）

禁用
```
compatibility-mode = 0
```

Proxy with Loopback Address
```
compatibility-mode = 1
```

Proxy Only
```
compatibility-mode = 2
```

TUN Only
```
compatibility-mode = 3
```

启用 Network.framework (默认值: false)
```
network-framework = true
```

INTERNET 测试 URL (使用网络诊断功能时访问的 URL)
```
internet-test-url = http://wwww.gstatick.com/generate_204
```

代理测速 URL (测试代理策略时的 URL)
```
proxy-test-url = http://wwww.gstatick.com/generate_204
```

测速超时 (秒)
```
test-timeout = 5
```

强制 TCP 连接为 HTTP 连接
```
force-http-engine-hosts = api.joybj.com
```

返回真实 IP
```
always-real-ip = *.apple.com
```

劫持其它 DNS 服务器
```
hijack-dns = 8.8.8.8:53
```

绕过特定 IP 范围
```
tun-excluded-routes = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12
```

包含特定 IP 范围
```
tun-included-routes = 192.168.1.12/32
```

TLS 引擎 (default、secure-transport、openssl、network-framework)

OpenSSL 或者 Network.Framework，可开启 TLS 1.3 支持

OpenSSL 更稳定，Network.Framework 可提供更多功能
```
tls-provider = default
```

如果 Wi-Fi 信号弱或网络异常，会在 2 秒后尝试使用数据网络建立连接
```
wifi-assist = true
```

在 [Host] 段有为某主机名指定 IP，在使用代理访问该主机名时，将使用该 IP 地址进行代理请求，不再依赖远端解析。
```
use-local-host-item-for-proxy = true
```

# [Replica]

`该段定义抓取流量的过滤`

隐藏所有发往 *.Apple.com 和 *.icloud.com 的请求（该选项只是在抓取结果中隐藏了请求）
```
hide-apple-request = true
```

隐藏Crashlytics请求
```
hide-crashlytics-request = true
```

隐藏UDP会话（默认值: false）
```
hide-udp = false
```

使用关键词过滤器（默认值: false）
```
use-keyword-filter = false
```

仅记录不包含关键字的请求
```
keyword-filter-type = blacklist
```

仅记录包含关键字的请求
```
keyword-filter-type = whitelist
```

关键字 (例：abc def)
```
keyword-filter = abc,def
```
