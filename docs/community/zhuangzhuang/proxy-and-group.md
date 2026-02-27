---
Title: Surge 配置详解 — Proxy & Proxy Group
Source: https://zhuangzhuang.io/2018/11/14/surge.html
Author: 壮壮 (zhuangzhuang)
Original Date: 2018-11-14
Last Updated: 2025-08-20
Crawl Date: 2026-02-27
Part: 2/5
Freshness Warning: >
  Community content, originally written in 2018, last updated 2025-08-20.
  Some options may be outdated or deprecated in newer Surge versions.
  Always cross-reference with official manual (docs/manual/) for
  authoritative and current information.
---

# Surge 配置详解 — [Proxy] & [Proxy Group]

# [Proxy]

`该段定义可用的代理策略`

写法是：策略名 = 代理类型, 代理地址, 端口号, 用户名, 密码

不同的类型填写的具体项目会有差异, 建议在 UI 界面中填写

策略名不可重复, 策略名须先定义才能在其它部分引用
```
ProxyHTTP = http, [SERVER ADDRESS], [GENERATED PORT], username = 用户名, password = 密码
ProxyHTTPS = https, [SERVER ADDRESS], [GENERATED PORT], username = 用户名, password = 密码
ProxySOCKS5 = socks5, [SERVER ADDRESS], [GENERATED PORT], username = 用户名, password = 密码
ProxySOCKS5TLS = socks5-tls, [SERVER ADDRESS], [GENERATED PORT], username = 用户名, password = 密码, skip-common-name-verify=true
ProxySnell = snell, [SERVER ADDRESS], [GENERATED PORT], psk=[GENERATED PSK], obfs=http
ProxyShadowsocks01 = custom, [SERVER ADDRESS], [GENERATED PORT], chacha20-ietf-poly1305, password, https://raw.githubusercontent.com/ydzydzydz/Rules/master/SSEncrypt/SSEncrypt.module
ProxyShadowsocks02 = ss, [SERVER ADDRESS], [GENERATED PORT], encrypt-method = rc4-md5, password = 密码
ProxyVmess= vmess, [SERVER ADDRESS], [GENERATED PORT], username = [UUID], ws=true, tls=true, ws-path=/v2, ws-headers=X-Header-1:value|X-Header-2:value
ProxyTrojan = trojan, [SERVER ADDRESS], [GENERATED PORT], password = [PASSWORD]
```

可选参数：

开启 TCP Fast Open
```
tfo = true
```

开启 UDP
```
udp-relay = true
```

开启 MPTCP
```
mptcp = true
```

利用服务器定义的方式实现的广告通过选择

Ad-Pass 不拦截广告, Ad-Block 直接拒绝, Ad-GIF 返回一个透明像素图
```
Ad-Pass = direct
Ad-Block = reject
Ad-GIF = reject-tinygif
```

# [Proxy Group]

`该段定义可用的策略组`

**有 5 种策略组类型: select、url-test、fallback、ssid 和 load-balance**

select: 具体哪个子策略将被使用, 由用户界面上进行选择

ssid: 具体哪个子策略将被使用, 根据 Wi-FI 的 SSID 决定

url-test: 具体哪个子策略将被使用, 通过测试到具体 URL 的访问速度选择

fallback: 具体哪个子策略将被使用, 通过测试到具体 URL 的可用性决定

load-balance: 随机选用一个可用的子策略

手动选择：Auto, Proxy01, Proxy02, Proxy03
```
Proxy = select, Auto, Proxy01 , Proxy02, Proxy03
```

根据 Wi-FI 的 SSID 决定：默认策略 Auto, 数据网络策略 ProxyA, 连接到 123 的 Wi-FI 网络策略 ProxyB, 连接到 456 的 Wi-FI 网络策略 ProxyC
```
Scene = ssid, default = Auto, cellular = ProxyA, "123" = ProxyB, "456" = ProxyC
```

可用性自动测试：包含策略 Proxy01, Proxy02, Proxy03, 测试 url 为 http://www.bing.com/, **选出可用的第一个策略**,测试完成前使用第一个策略
```
Video = fallback, Proxy01, Proxy02, Proxy03, url = http://www.bing.com/, evaluate-before-use = true
```

延迟自动测试：包含策略 Proxy01, Proxy02, Proxy03, 测试 url 为 http://www.bing.com/, 600s后上次的测试结果将被抛弃, 比原优选线路的响应时间, 大于100ms的时候, 触发线路变更, 如果某策略在5s后依然没有完成, 放弃该策略。 **选出延迟最低的策略**，测试完成前使用第一个策略
```
Auto = url-test, Proxy01, Proxy02, Proxy03, url = http://www.bing.com/, interval = 600s, tolerance = 100ms, timeout = 5s, evaluate-before-use = true
```

均衡策略：包含策略 Proxy01, Proxy02, Proxy03, 每个连接随机使用一个子策略，当维持策略打开时，同一个主机名一定会使用同一个子策略
```
Balance = load-balance, Proxy01, Proxy02, Proxy03, persistent=1
```

以代理服务器的选择模式实现广告的通过选择
```
AdBlock = select, Ad-GIF, Ad-Block, Ad-Pass
```

策略组的另一种写法：引用远程或者本地list文件, **本地须将list文件放置在iCloud云盘Surge文件夹中**, [list文件示例](https://raw.githubusercontent.com/ydzydzydz/Rules/master/proxy/all.list)

远程list
```
AdBlock = select, policy-path = https://raw.githubusercontent.com/ydzydzydz/Rules/master/Surge/resources/policy/ad.list
```

本地list
```
AdBlock = select, policy-path = ad.list
```

外部策略组默认更新间隔时间为 24h，可自定义
```
🚦 Ad-Block = select, policy-path = https://raw.githubusercontent.com/ydzydzydz/Rules/master/Surge/resources/policy/ad.list, update-interval=300
```
