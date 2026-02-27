---
Title: Surge 配置详解 — Rule
Source: https://zhuangzhuang.io/2018/11/14/surge.html
Author: 壮壮 (zhuangzhuang)
Original Date: 2018-11-14
Last Updated: 2025-08-20
Crawl Date: 2026-02-27
Part: 3/5
Freshness Warning: >
  Community content, originally written in 2018, last updated 2025-08-20.
  Some options may be outdated or deprecated in newer Surge versions.
  Always cross-reference with official manual (docs/manual/) for
  authoritative and current information.
---

# Surge 配置详解 — [Rule]

# [Rule]

`规则定义部分`

一条规则有三个基础部分:

| 类型 | 值 | 策略 | 注释(非必需) |
|------|------|------|------|
| DOMAIN, | www.apple.com, | DIRECT | //注释 |
| DOMAIN-SUFFIX, | apple.com, | DIRECT | //注释 |
| DOMAIN-KEYWORD, | apple, | DIRECT | //注释 |
| IP-CIDR, | 10.0.0.0/8, | DIRECT | //注释 |
| GEOIP, | CN, | DIRECT | //注释 |
| USER-AGENT, | Instagram*, | ProxyA | //注释 |
| URL-REGEX, | ^http://google\.com, | ProxyA | //注释 |
| PROCESS-NAME, | Telegram, | ProxyA | //注释 |
| RULE-SET, | SYSTEM, | DIRECT | //注释 |
| DOMAIN-SET, | hostname.txt, | DIRECT | //注释 |
| AND, | ((DOMAIN, abc.com), (USER-AGENT, Surge*)), | DIRECT | //注释 |
| OR, | ((DOMAIN, abc.com), (USER-AGENT, Surge*)), | DIRECT | //注释 |
| NOT, | ((DOMAIN, abc.com)), | ProxyA | //注释 |
| DEST-PORT, | 80, | DIRECT | //注释 |
| SRC-IP, | 192.168.20.100, | DIRECT | //注释 |
| IN-PORT, | 6152, | DIRECT | //注释 |
| FINAL, | ProxyA | | //注释 |

**有三种基于域名的规则: "DOMAIN", "DOMAIN-SUFFIX" 和 "DOMAIN-KEYWORD"**

如果请求域完全匹配, 则匹配规则。
```
DOMAIN, www.apple.com, DIRECT
```

如果请求的域与后缀匹配, 则匹配规则。例如:google.com匹配www.google.com, mail.google.com 和 google.com, 但不匹配 content-google.com。
```
DOMAIN-SUFFIX, google.com, DIRECT
```

如果请求的域包含关键字, 则匹配规则。
```
DOMAIN-KEYWORD, apple, DIRECT
```

参数: force-remote-dns (默认值: false)
如果某请求被该规则匹配, 且策略不是DIRECT. 那么 DNS 查询将永远在远端代理服务器执行, 即使该请求由 Surge TUN 处理
```
DOMAIN-KEYWORD, google, ProxyHTTP, force-remote-dns
```

**有两种基于IP的规则: "IP-CIDR" , "GEOIP"**

如果是一个使用域名进行访问的请求, 那么 Surge 将进行 DNS 查询以确认是否应该被该规则匹配. 若 DNS 查询失败, 将放弃规则匹配过程并直接给出错误。
```
IP-CIDR, 10.0.0.0/8, DIRECT
```

OPTIONS: no-resolve:(默认值: false)
如果是一个使用域名进行访问的请求, 跳过该条规则, 不触发 DNS 查询。
```
IP-CIDR, 192.168.0.0/16, DIRECT, no-resolve
```

GeoIP CN, 基于 GeoIP 数据库判断域名和 IP 的归属地
```
GEOIP, CN, DIRECT
```

**有两种HTTP规则: "USER-AGENT", "URL-REGEX"**

HTTP规则用于HTTP请求或HTTPS请求。它不会影响TCP连接。

USER-AGENT, 如果请求的用户代理匹配, 则匹配规则。通配符*和?都受支持。
```
USER-AGENT, Instagram*, DIRECT
```

URL-REGEX, 如果URL与正则表达式匹配, 则匹配规则。**最新版 Surge 的 URL-REGEX 规则支持 Mitm**
```
URL-REGEX, ^http://google\.com, DIRECT
```

PROCESS-NAME, 可以为指定的进程分配策略, 规则仅适用于Surge Mac, Surge iOS 会忽略了这些规则。
```
PROCESS-NAME, Telegram, Proxy
```

**RULESET规则集**

规则集包含多条子规则, 可以是另一个本地 list 文件, 或者是一个 URL（当前版本中固定为每 24 小时进行一次自动更新）

内置了两个规则集：[SYSTEM](https://raw.githubusercontent.com/ydzydzydz/Rules/master/special/system.list) 和 [LAN](https://raw.githubusercontent.com/ydzydzydz/Rules/master/special/lan.list)
```
RULE-SET, SYSTEM, DIRECT
RULE-SET, LAN, DIRECT
```

list 文件是一个纯文本文件, 每一行为一个规则, **最后不可写上策略名,** [list文件示例](https://raw.githubusercontent.com/ydzydzydz/Rules/master/special/apple.list)
```
RULE-SET, https://raw.githubusercontent.com/ydzydzydz/Rules/master/special/apple.list, Proxy
```

外部规则集默认更新间隔时间为 24h，可自定义
```
RULE-SET,https://raw.githubusercontent.com/ydzydzydz/Rules/master/special/telegram.list,🛩 Telegram,update-interval=300
```

**DOMAINSET 规则**

支持百万级别的规则集，在 hostname.txt 文件中，每一行表示一个主机名（域名或 IP），以 . 开头表示匹配所有子域名
```
DOMAIN-SET, hostname.txt, DIRECT
```

**逻辑规则三种："AND", "OR"和"NOT"**

可以组合多个子规则, 且可进行多层嵌套, 用于某些复杂场景的判断

AND 运算符表示所有子规则都匹配时, 使用该策略。
```
AND, ((#Rule1), (#Rule2), (#Rule3)...), Policy
```

OR 运算符表示任何子规则匹配时, 使用该策略。
```
OR, ((#Rule1), (#Rule2), (#Rule3)...), Policy
```

NOT 运算符表示子规则未匹配时, 使用该策略。
```
NOT, ((#Rule1)), Policy
```

**Miscellaneous规则三种:"DEST-PORT", "SRC-IP"和"IN-PORT"**

DEST-PORT 如果请求的目标端口匹配, 则规则匹配。
```
DEST-PORT, 80, DIRECT
```

SRC-IP 如果请求的客户端IP地址匹配, 则规则匹配。仅适用于远程机器。
```
SRC-IP, 192.168.20.100, DIRECT
```

IN-PORT 如果请求的传入端口匹配, 则规则匹配。Surge在多个端口上监听时很有用。
```
IN-PORT, 6152, DIRECT
```

**Final规则**
FINAL规则必须在所有其他规则之后编写。它定义了与任何其他规则不匹配的请求的默认策略。

DNS 查询失败走 Final 规则
```
FINAL, Proxy, dns-failed
```

**触发通知**

匹配规则时弹出 notification-text 定义的字符串
```
AND, ((DOMAIN, raw.githubusercontent.com), (USER-AGENT, Surge*)), DIRECT, notification-text="规则集更新", notification-interval=3 //更新提醒
```
