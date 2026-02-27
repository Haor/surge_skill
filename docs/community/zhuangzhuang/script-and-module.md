---
Title: Surge 配置详解 — Script & Module
Source: https://zhuangzhuang.io/2018/11/14/surge.html
Author: 壮壮 (zhuangzhuang)
Original Date: 2018-11-14
Last Updated: 2025-08-20
Crawl Date: 2026-02-27
Part: 5/5
Freshness Warning: >
  Community content, originally written in 2018, last updated 2025-08-20.
  Some options may be outdated or deprecated in newer Surge versions.
  Always cross-reference with official manual (docs/manual/) for
  authoritative and current information.
---

# Surge 配置详解 — [Script] & 模块

# [Script]

`使用 Surge 执行 JavaScript 脚本`

**http-request**

用于修改 HTTP 请求体，该类型下第二参数为匹配 URL 的正则表达式，被匹配到的请求会被执行脚本。
```
script1 = type=http-request,pattern=^http://httpbin.org script-path=http-request.js,max-size=16384,debug=true,requires-body=true
```

**http-response**

用于修改 HTTP 返回体，该类型下第二参数为匹配 URL 的正则表达式，被匹配到的请求会被执行脚本。
```
script2 = type=http-response,pattern=^http://www.example.com/test script-path=test.js,max-size=16384,debug=true
```

**cron**

可配置 Surge 在特定的时间执行脚本，触发时间配置使用 crontab 的样式。该类型下第二参数为 crontab 表达式，常见的 crontab 为五位表示，即 * * * * * 表示每分钟执行一次，Surge 兼容五位表示和六位表示，可用 * * * * * * 表示每秒钟执行一次。但不支持 @daily 这样的别名。
```
script3 = type=cron,cronexp="* * * * *",script-path=fired.js
```

**event**

在发生特定事件时执行脚本，该类型下第二参数为事件名称，目前只有 network-changed 一个事件。
```
script4 = type=event,event-name=network-changed,script-path=network-changed.js
```

**rule**

使用脚本进行规则判定，该类型下第二参数为规则名
```
script5 = type=rule,script-path=rule.js
```

**policy-group**

使用脚本去决定 policy-group，该类型下第二参数为脚本名。
```
# 换了写法，我也不知道怎么写了，也可能是删了，有大佬知道可以联系 zhuangzhuang
```

**dns**

使用脚本去执行 DNS 解析操作，该类型下第二参数为脚本名。
```
script7 = type=dns,script-path=dns.js,debug=true
```

壮壮只做了简单介绍，具体内容请参考[官方论坛](https://community.nssurge.com/d/33-scripting)

# 模块

`模块是一系列设置的集合，可以覆盖追加当前配置的部分设定`

**内置模块**

Surge 会预置一些模块，随着 Surge 更新而更新

**本地模块**

放置配置文件目录（iCloud Drive/Surge/）的 `*.sgmodule` 文件，本地模块搜索路径包含子目录

**远程模块**

从某个 URL 安装模块，远程模块不会自动更新，可以手动更新

模块开启状态仅保存于当前配置，不会进行同步，切换配置也不影响模块的开启状态

模块的内容和标准配置基本一致，目前支持调整字段的有：

[General]、[Replica]

key = value：直接覆盖原始值

key = %APPEND% value：在原始值的末尾进行追加（仅适用于适用逗号分隔的字段）

key = %INSERT% value：在原始值的开始进行插入（仅适用于适用逗号分隔的字段）
```
# 模块名
#!name=Game Console SNAT
# 模块简介
#!desc=Let Surge handle SNAT conversation properly for PlayStation, Xbox, and Nintendo Switch. Only useful if Surge Mac acts the router for these devices.
# 限制模块的使用范围 (ios、mac)
#!system=mac

[General]
always-real-ip = %APPEND% *.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com
```

[MITM]
```
#!name=MitM All Hostnames
#!desc=Perform MitM on all hostnames with port 443, except those to Apple and other common sites which can't be inspected. You still need configure CA certificate and enable the main switch of MitM.

[MITM]
# 模块内容，与标准配置基本一致，仅支持操作 hostname 字段
# 跳过 Apple 相关
hostname = %APPEND% -*.apple.com, -*.icloud.com, -*.mzstatic.com, -*.crashlytics.com, -*.facebook.com, -*.instagram.com
```

[Script]、[URL Rewrite]、[Header Rewrite]、[Host]
```
#!name=URL Rewrite
#!desc=After enabling the module, you may access the router configure webpage by accessing http://router.com in your bowser. The URL will always rediect to the gateway address in the current network.
#!system=ios

[URL Rewrite]
# 模块内容，与标准配置基本一致，新加入的定义将会插入在原始内容的最顶部。
# 网关重定向
^http://router.com {{{GATEWAY_ADDRESS}}} 302
^http://www.router.com {{{GATEWAY_ADDRESS}}} 302
```

[Rule]
```
#!name=Rule Module
#!desc=Rule Module

[Rule]
# 新配置的规则将被插入在最顶部
# 规则只适用于 DIRECT、REJECT、REJECT-TINYGIF 三种策略
DOMAIN-SUFFIX, zhuangzhuang.cf, DIRECT
```

具体内容请参考[官方论坛](https://community.nssurge.com/d/225-module)

# 大佬们的规则

| 项目地址 | 捷径/JSBOX |
|----------|-----------|
| [Blankwonder/surge-list](https://github.com/Blankwonder/surge-list) | |
| [Choler/Surge](https://github.com/Choler/Surge) | [Surge](https://www.icloud.com/shortcuts/6da9a6c09618464d85c11580d81b1e51) |
| [ConnersHua/Profiles](https://github.com/ConnersHua/Profiles) | [Surge2](https://www.icloud.com/shortcuts/0913876d77d647f7b229903edb3a9be0) / [Surge3](https://www.icloud.com/shortcuts/bbb973be542a4c4bba94101f2ae16bcf) |
| [Hackl0us/SS-Rule-Snippet](https://github.com/Hackl0us/SS-Rule-Snippet) | [Surge2](https://www.icloud.com/shortcuts/eb5f7930bf8e414993452c3cae1906ca) / [Surge3](https://www.icloud.com/shortcuts/5dee27f365974ba7bec536adc543b24d) |
| [lhie1/Rules](https://github.com/lhie1/Rules) | [Rules-lhie1](https://xteko.com/redir?name=Rules-lhie1&url=https://raw.githubusercontent.com/Fndroid/jsbox_script/master/Rules-lhie1/.output/Rules-lhie1.box) |
| [scomper/surge-list](https://github.com/scomper/surge-list) | |
| [tudi1909/Surge_iOS_Rules](https://github.com/tudi1909/Surge_iOS_Rules) | |
| [tudi1909/Surge_macOS_Rules](https://github.com/tudi1909/Surge_macOS_Rules) | |
| Neurogram | [Surge³](https://xteko.com/redir?name=Surge%C2%B3&url=https%3A%2F%2Fraw.githubusercontent.com%2FNeurogram-R%2FJSBox%2Fmaster%2FSurge%25c2%25b3.box&icon=icon_053.png&version=0.7.4&author=Neurogram) |
| [huanz/surge-hosts](https://github.com/huanz/surge-hosts) | |
| [XinSSS/Conf-for-Surge-Shadowrocket](https://github.com/XinSSS/Conf-for-Surge-Shadowrocket) | |
| [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) | |

# 如何自己写配置

推荐神机大佬的：[Surge 使用手册](https://chua.pro/more/subject-index/surge-manual/)

## 参考

- [scomper/Surge config](https://github.com/scomper/Surge/blob/master/surge3.conf.ini)
- [Surge Official Manual](https://manual.nssurge.com/)
