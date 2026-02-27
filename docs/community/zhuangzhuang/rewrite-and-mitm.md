---
Title: Surge 配置详解 — Host, Rewrite & MITM
Source: https://zhuangzhuang.io/2018/11/14/surge.html
Author: 壮壮 (zhuangzhuang)
Original Date: 2018-11-14
Last Updated: 2025-08-20
Crawl Date: 2026-02-27
Part: 4/5
Freshness Warning: >
  Community content, originally written in 2018, last updated 2025-08-20.
  Some options may be outdated or deprecated in newer Surge versions.
  Always cross-reference with official manual (docs/manual/) for
  authoritative and current information.
---

# Surge 配置详解 — [Host], [URL Rewrite], [Header Rewrite], [Map Local], [SSID Setting], [MITM], [Snell Server]

# [Host]

`该段定义本地 DNS 记录`

该功能等同于 /etc/hosts, 加上了泛解析和别名支持。
```
*.taobao.com = server:223.5.5.5
*.jd.com = server:223.5.5.5
*.tmall.com = server:223.5.5.5
*.example.com = server:https://cloudflare-dns.com/dns-query
cloudflare-dns.com = server:1.1.1.1
```

# [URL Rewrite]

`该段定义针对 HTTP 请求的 URL 重定向规则`

**Header模式**

Surge将修改Header, 并在必要时将请求重定向到另一台主机。客户端不会注意到这个重定向操作。
```
^http://www\.google\.cn http://www.google.com header
```

**302模式**

Surge只会返回302重定向响应。如果启用了主机名的MitM, 则可以重定向HTTPS请求。
```
^http://yachen\.com https://yach.me 302
```

**Reject模式**

如果模式匹配, 则拒绝请求。替换参数将被忽略。如果启用了主机名的MitM, 将拒绝HTTPS请求。
```
^http://ad\.com/ad\.png _ reject
```

# [Header Rewrite]

`重定向HTTP请求或者篡改请求Header`

**header-add**

为请求头添加一个新的header line，即使header line已存在
```
^http://example.com header-add DNT 1

# 修改前
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate

# 修改后:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1     # 请求某个网页应用程序停止跟踪某个用户
```

**header-del**

从请求头中删除header line
```
^http://example.com header-del DNT

# 修改前:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1

# 修改后:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
```

**header-replace**

替换请求头，如果请求头字段不存在，则不做任何修改
```
^http://example.com header-replace DNT 1

# 修改前:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 0

# 修改后:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1
```

如果要在请求头字段存在时添加或替换header line，可以一起使用header-add和header-del。
```
^http://example.com header-del DNT
^http://example.com header-add DNT 1
```

# [Map Local]

`Mock 可返回任意二进制的静态内容，empty.json 内容为 {}`
```
^http://example\.com/json data=empty.json
```

# [SSID Setting]

连接到 Apple Store 的 Wi-Fi 网络时 Surge 暂停工作
需要 Web 验证登录的 Wi-Fi 网络以及路由器已经科学上网的 Surge 挂起
```
"Apple Store" suspend=true
```

计费网络模式, 当连接到热点名为 iPhone X 的网络时自动切换为计费模式
```
"iPhone X" cellular-mode=true
```

# [MITM]

`Surge可以通过MitM解密HTTPS通信`

跳过服务端证书验证
```
skip-server-cert-verify = true
```

用于TCP连接
```
tcp-Connection = true
```

自动旁路（最新版已经删掉了）
```
auto-bypass = on
```

主机名（默认只解密`443端口`，使用`suffix:0`为主机名上的所有端口启用Mitm，使用`suffix:port`为主机名上的特定端口启用Mitm）
```
hostname = api.chelaile.net.cnn.cn
```

最新版 Surge 的 URL-REGEX 规则支持 Mitm，可以通过添加前缀`-`排除域名
```
hostname = -*.apple.com,-*.icloud.com,*
```

证书生成器将帮助您生成用于调试的新CA证书, 并使证书受到系统的信任。

它可以在 Surge Dashboard ( Mac 版 )和 Surge iOS 配置编辑器中使用。

这个证书是本地生成的, 只会保存在配置文件和系统密钥链中。

证书密钥是使用OpenSSL随机生成的。

还可以使用现有的CA证书。将证书导出到PKCS#12格式(.p12)。

请注意, 由于系统限制, 密码不能为空。使用`base64命令`对p12进行编码, 并将这些设置附加到配置文件中。
```
# P12密码
ca-passphrase = zhuangzhuang

# base64编码过的P12文件
ca-p12 = [BASE64_CERTIFICATE_DATA_OMITTED]
```

**安装证书**

配置根证书-安装证书-设置-通用描述文件与设备管理-安装

**设置-通用-关于本机-证书信任设置-信任**

# [Snell Server]

`使用Surge Mac作为Snell代理服务器（从3.1.0版本开始）。`
```
interface = 0.0.0.0
port = 6160
psk = RANDOM_KEY_HERE
obfs = off
```
