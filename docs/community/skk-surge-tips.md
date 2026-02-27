---
Title: 我有特别的 Surge 配置和使用技巧
Source: https://blog.skk.moe/post/i-have-my-unique-surge-setup/
Author: Sukka (SKK)
Published: 2024-04-17
Last Updated: 2026-01-02
Crawl Date: 2026-02-27
Freshness Warning: >
  Community content, not official documentation. Cross-reference
  with official manual for authoritative information.
---

# 我有特别的 Surge 配置和使用技巧

我使用 Surge Mac 作为网络核心有一段时间了。虽然 Surge 官方提供了一份「[中国区用户推荐最小配置](https://community.nssurge.com/d/1214/16)」，但是为了发挥 Surge 全部潜力的话、彻底值回 Surge 的售价、实现我的复杂需求，我添加了许多自定义的配置。

## 基础知识储备

如果没有相关的知识储备，你在阅读本文时可能会难以理解分流规则和配置。你可以阅读我之前写过的 [数篇关于 DNS 的文章](https://blog.skk.moe/tags/DNS/)，本文不会再做详细赘述。
- [浅谈在代理环境中的 DNS 解析行为](https://blog.skk.moe/post/what-happend-to-dns-in-proxy/)。
- [我有特别的 DNS 配置和使用技巧](https://blog.skk.moe/post/i-have-my-unique-dns-setup/)
## 规则和规则集

避免 DNS 污染和 DNS 泄漏最有效的办法就是永远不在本地进行 DNS 解析，而 Surge 和 Clash **能且只能通过 Fake IP 和域名规则匹配的方式** 可以实现非直连域名 **一定不在本地本机进行任何 DNS 解析**。在 Surge 和 Clash 中，规则自上而下匹配，只有当遇到 IP 类规则（如 `IP-CIDR`、`IP-CIDR6`、`GEOIP` 和 `IP-ASN`）时才会发起 DNS 解析。因此，在 Surge 中，将会触发 DNS 解析的规则放在域名和 URL 匹配规则后面非常重要。

我在 Surge 中主要使用我自己维护的规则集 [SukkaW/Surge](https://github.com/SukkaW/Surge) 进行流量分流，规则集现在还增加了对 Clash Premium 和 Mihomo（Clash Meta）的支持，欢迎大家 [去 GitHub 上点个星星](https://github.com/SukkaW/Surge)。在我维护的规则集中，IP 类规则和非 IP 类规则是分开的，在 Surge Profile 中先引用所有的非 IP 类规则再引用 IP 类规则，可以避免 DNS 泄漏和 DNS 污染。
### 搜狗输入法

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/sogouinput.conf,[替换为你的策略名] # REJECT-DROP, DIRECT
```

我早在 2021 年就发现搜狗输入法使用 HTTP 协议明文记录用户输入用于云词库（`http://get.sogou.com/q`）。云词库功能本身无可厚非（一个典型的牺牲隐私换取便利的功能），但是 HTTP 协议意味着除了搜狗之外的任何中间人（如运营商）也可以窃取这些数据。因此，我维护了专门的搜狗输入法相关域名，默认使用 Surge 的 `REJECT-DROP`、将搜狗输入法发送的数据包直接丢弃。只有在需要同步搜狗输入法配置时，临时切换到 `DIRECT` 给搜狗输入法放行。
### 广告拦截 / 隐私保护 / 病毒拦截 / 钓鱼和诈骗域名拦截

```
DOMAIN-SET,https://ruleset.skk.moe/List/domainset/reject.conf,REJECT
RULE-SET,https://ruleset.skk.moe/List/non_ip/reject.conf,REJECT,extended-matching
```

应该是目前市面上拦截最全面、几乎零误杀的 Surge / Clash 域名集，域名数据来源为 uBlock Origin、AdGuard、EasyList 等共 38 个来源，截至本文写就，条目数量已经达到 30 万级别。

由于大部分上游数据的格式为 AdBlock Syntax，而 AdBlock Syntax 非常灵活，支持路径拦截、正则表达式匹配、拦截指定请求类型（如仅拦截图片、仅拦截脚本等），还支持在页面中注入 JavaScript 代码片段，这些都是 Surge / Clash 作为网络工具无法实现的。如果需要转换成 Surge / Clash 兼容的 DOMAIN-SET 格式，那么相对应的 AdBlock Syntax 就必须是 block 整个域名的。因此我写了一个工具、抽取 AdBlock Syntax 中的 NetworkRule 并转换为 Surge / Clash 的 DOMAIN-SET 格式：

```
# 纯网络规则、匹配 a.example.com 及其所有子域名，可以转换，输出 `+.a.example.com`
||a.example.com
||a.example.com^

# 属于正则类规则，但是可以匹配出具体的域名，可以转换，输出 `c.example.com`、不包含其子域名
://c.example.com

# 白名单规则，后续其他规则里的遇到 b.example.com 及其所有子域名的规则都不能添加到 DOMAIN-SET 中
@@||b.example.com
@@||b.example.com^

# 虽然 Surge / Clash 不能区分请求是否是浏览器页面，但是整个 d.example.com 依然需要被加白
@@||d.example.com$document

# Surge / Clash 在不启用极其昂贵的 MITM 的情况下无法对 URL 进行匹配，不转换
||e.example.com/d/

# Surge / Clash 无法处理浏览器弹窗、无法匹配 CNAME、也无法区分是否是第三方请求，不转换
||f.example.com$popup
||f.example.com^$cname
||f.example.com^$third-party

# Surge / Clash 不能区分一个请求是否是某个页面的下属资源、不转换
||g.example.com$domain=example.com
```

相比市面上其它同类规则，我实现的 AdBlock Syntax 转换工具更精确、相比 AdGuard 的 Hosts Compiler 又更保守、不会导致任何误杀。

需要注意的是，Surge / Clash **完全无法替代浏览器内的去广告插件（如 AdBlock Plus）和运行在操作系统上的去广告软件（如 AdGuard）**。正如上述范例展示出来的 AdGuard Syntax 的能力，Surge / Clash 只能拦截整个域名，对于某个域名下的具体路径无能为力、更不能处理复杂的匹配条件。

`extended-matching` 是 Surge 新增的功能。一般的，Surge 通过 Fake IP 获取某个网络连接的目标域名。但是极少数软件有罕见的非标准特殊逻辑，例如，应用通过 DNS 解析域名 `a.example.org`、得到解析结果（会是 Surge 返回的 Fake IP）以后，对 `b.example.org` 的请求却使用 `a.example.org` 的解析结果。这样后续发给 `b.example.org` 的请求会被 Surge 误认为是 `a.example.org`。**这种情况并不影响请求，只会导致分流不准确**。通过 HTTP 嗅探 Host 和 HTTPS 嗅探 TLS SNI **试图获取** 请求的真实域名、并将其用于规则匹配。
### 其它域名拦截

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/reject-no-drop.conf,REJECT-NO-DROP,extended-matching
RULE-SET,https://ruleset.skk.moe/List/non_ip/reject-drop.conf,REJECT-DROP,extended-matching
```

其它拦截规则不涉及广告、病毒、钓鱼等的拦截，主要是通过屏蔽特定类型的网络连接改善日常上网体验。第一个规则组会阻止 YouTube、Bilibili 和斗鱼的视频 CDN 的 QUIC，以及阻止斗鱼将用户的手机电脑变成 PCDN；第二个规则组是直接丢弃发往 Adobe 系列软件内部的跟踪打点域名的数据包 —— Adobe 软件的打点 SDK 所使用的 HTTP 请求库实现不当、会无限重试请求，导致 Surge / Clash 内存泄漏。
### 测速网站及其测速点域名

```
DOMAIN-SET,https://ruleset.skk.moe/List/domainset/speedtest.conf,[替换你的策略名],extended-matching
```

测速类网站及其测速点的域名。除了手工维护以外，每日还会定时从 `speedtest.net` 的 API 接口爬取常见地区的测速点及其域名；至于 `fast.com` 的测速点基本复用 Netflix 自己的视频推流 CDN 节点、会和流媒体规则组（后文会介绍）冲突、没有包括在内。

我主要使用这个规则集实现切换使用某个 Surge 策略进行测速的同时、不影响通过默认策略正常上网。
### 静态 CDN 域名

```
DOMAIN-SET,https://ruleset.skk.moe/List/domainset/cdn.conf,[替换你的策略名],extended-matching
RULE-SET,https://ruleset.skk.moe/List/non_ip/cdn.conf,[替换你的策略名],extended-matching
```

一般正常访问网站、调用 API 接口时，我倾向于使用比较干净的网络出口（例如各个国家的家宽、商宽）避免风控、撞验证码，但是这部分网络出口一般带宽较小；而大部分网站的静态资源（如图片、视频、音频、字体、JS、CSS）都有独立域名、不设置风控措施、不设置鉴权，这些静态资源可以使用 IP 不一定干净（例如 IDC 类 IP）、但是带宽更大、延时更低、而且有和大部分主流 CDN（如 Cloudflare、Akamai、Fastly、EdgeCast）在 IXP 有互联的网络出口。

这两个规则集就是收集了常见的静态资源 CDN 域名。一般就实践经验来看，在正常上网中这部分域名产生的流量占据约 70% 左右。如果你在使用商业性质的远端策略服务提供商、且该服务上提供了低倍率节点，你可以将这部分域名分流至低倍率节点以节省流量。

需要注意的是，**部分海外域名我只收录在了 `cdn.conf` 中、没有重复收录在 `global.conf`（后文会介绍）**。因此即使没有将 CDN 分流至独立网络出口需求，我也强烈建议使用 `domainset/cdn.conf` 和 `non_ip/cdn.conf`。
### 流媒体域名

```
# RULE-SET,https://ruleset.skk.moe/List/non_ip/stream_hk.conf,[替换你的策略名],extended-matching
# RULE-SET,https://ruleset.skk.moe/List/non_ip/stream_jp.conf,[替换你的策略名],extended-matching
# RULE-SET,https://ruleset.skk.moe/List/non_ip/stream_us.conf,[替换你的策略名],extended-matching
# RULE-SET,https://ruleset.skk.moe/List/non_ip/stream_tw.conf,[替换你的策略名],extended-matching
# RULE-SET,https://ruleset.skk.moe/List/non_ip/stream_kr.conf,[替换你的策略名],extended-matching
# RULE-SET,https://ruleset.skk.moe/List/non_ip/stream_eu.conf,[替换你的策略名],extended-matching
RULE-SET,https://ruleset.skk.moe/List/non_ip/stream.conf,[替换你的策略名],extended-matching
```

包含 4gtv、AbemaTV、All4、Amazon Prime Video、Apple TV、Apple Music TV、Bahamut、BBC、Bilibili Intl、DAZN、Deezer、Disney+、Discovery+、DMM、encoreTVB、Fox Now、Fox+、HBO GO/Now/Max/Asia、Hulu、HWTV、JOOX、Jwplayer、KKBOX、KKTV、Line TV、Naver TV、myTV Super、Netflix、niconico、Now E、Paramount+、PBS、Peacock、Pandora、PBS、Pornhub、SoundCloud、PBS、Spotify、TaiwanGood、Tiktok Intl、Twitch、ViuTV、ShowTime、iQiYi Global、Himalaya Podcast、Overcast、WeTV 等流媒体平台的规则组。

其中，`stream_[xx].conf` 包含 **限定地区访问的流媒体**（例如 BBC 直播只允许在英国访问）的规则，而 `stream.conf` 则包含所有流媒体的全部规则。你可以根据自己的需求选择性引用 `stream_[xx].conf` 规则划分独立策略、并使用 `stream.conf` 为剩下所有的常用流媒体做兜底。
### Telegram 域名

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/telegram.conf,[替换你的策略名],extended-matching
```

包含 Telegram 及其旗下其他服务（Telegraph）的域名。
### Apple & Microsoft 国内 CDN 域名

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/apple_cdn.conf,[替换你的策略名]
RULE-SET,https://ruleset.skk.moe/List/non_ip/microsoft_cdn.conf,[替换你的策略名]
```

大部分苹果和微软的 CDN 服务（如应用商店下载、操作系统和补丁的更新）都使用了在国内 ICP 备案的域名、并在国内有 CDN 节点。这个规则集就是收集了这些可以使用国内直连访问的域名。

有的时候，由于新资源（如新版本操作系统或软件刚刚发布）或冷门资源未被国内 CDN 节点缓存、导致国内直连访问缓慢的时候，也可以使用其他策略不通过国内直连访问。
### 软件、游戏和驱动的下载和更新域名

```
DOMAIN-SET,https://ruleset.skk.moe/List/domainset/download.conf,[替换你的策略名],extended-matching
RULE-SET,https://ruleset.skk.moe/List/non_ip/download.conf,[替换你的策略名],extended-matching
```

收集了操作系统、软件、驱动、游戏（例如 Steam 和 Epic）的下载和更新域名。这部分域名在国内没有 CDN 节点的域名（那部分域名已经包括在前文 `apple_cdn.conf` 和 `microsoft_cdn.conf`），作用和静态 CDN 规则集类似：可以使用 IP 不一定干净（例如 IDC 类 IP）、但是带宽更大、延时更低、而且有和大部分主流 CDN（如 Cloudflare、Akamai、Fastly、EdgeCast）在 IXP 有互联的网络出口。

但是考虑到大部分操作系统、软件、驱动、游戏的下载域名在国内可达，大家可以根据自身需要、酌情设置 `download.conf` 走直连，或者在下载开始前手动调整策略。

由于 Microsoft 部分域名冲突（如 `.delivery.mp.microsoft.com` 绝大部分子域名没有国内 CDN 节点、存在于 `download.conf` 中，但子域名 `dl.delivery.mp.microsoft.com` 却又有国内 CDN 节点），因此建议将这两个规则组放在 `apple_cdn.conf` 和 `microsoft_cdn.conf` 之后。
### Apple CN 域名

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/apple_cn.conf,DIRECT
```

云上贵州（`icloud.com.cn`）和苹果地图国内版等服务的域名，这部分域名需要国内直连访问。
### 苹果和微软服务域名

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/apple_services.conf,[替换你的策略名],extended-matching
RULE-SET,https://ruleset.skk.moe/List/non_ip/microsoft.conf,[替换你的策略名],extended-matching
```

排除了有国内 CDN 节点的域名和国区专用域名以后，苹果和微软其余的域名。
### AIGC 类服务域名

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/ai.conf,[替换你的策略名],extended-matching
```

大部分内容生成式 AI 服务（如 OpenAI 及 ChatGPT、Google Gemini 等）都会限制特定国家和地区的访问。由于这部分服务的公司一般位于美国、美国对于 AI 的立法也较为宽松，我建议这个规则组在分配策略时、优先选用位于美国的策略组访问。
### 常见海外域名

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/global.conf,[替换你的策略名],extended-matching
```

常见海外服务和互联网公司的域名。其中部分域名被 DNS 污染，将其收录在域名类规则中、配合远端策略可以避免 Surge 在本机解析这些域名、有效避免 DNS 污染和 DNS 泄漏。
### 网易云音乐的域名

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/neteasemusic.conf,[替换你的策略名],extended-matching
```

网易云音乐的 API 域名和网易云音乐客户端的进程名。这个规则主要用于不侵入式修改网易云音乐客户端、将某些网易云音乐使用特殊策略以实现某些特殊需求。
### 国内常见域名

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/domestic.conf,DIRECT,extended-matching
```

这两个规则集分别包含了我人工维护的国内常见互联网公司和服务的域名。这部分域名一般需要通过国内直连访问。

其中 `domestic.conf` 刻意没有使用 felixonmars 的 `dnsmasq-china-list`，**因为 `dnsmasq-china-list` 设计之初是为国内域名的 DNS 解析优化、完全不适用于流量分流**（`dnsmasq-china-list` 只检查域名的权威 DNS 服务器，因此有部分海外域名、因为 DNS 服务器位于中国大陆、依然被包含在 `accelerated-domains.china.conf` 中）。**因此，`Loyalsoldier/v2ray-rules-dat` 和 `MetaCubeX/meta-rules-dat` 项目的 GEOSITE 规则使用 `dnsmasq-china-list` 作为上游数据来源 是大错特错的**。

除此以外，在 Surge 和 Clash 中，也 **完全不需要完整的国内域名列表来做分流**，因为海外网站的域名，**只要不包含在 `global.conf`、`cdn.conf`、`stream.conf` 等域名规则组中，就一定会触发在 Surge / Clash 在本机的 DNS 解析。通过一个完整的国内域名列表 `domestic.conf` 是不能避免所谓 DNS 污染的**。如果真的需要避免海外网站的域名在本机进行 DNS 解析、只能不断完善 `global.conf`。没有包含在 `domestic.conf` 规则组的国内的网站，通过国内 IP 段进行分流即可。
### 内网域名

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/lan.conf,DIRECT
```

包含 `.local` 和局域网 IP 的 `in-addr.arpa` 域名（即 AS112 域名）。这部分域名一般会被解析到局域网 IP、需要走内网 DNS 解析、需要直连访问。
### 广告拦截 IP

```
RULE-SET,https://ruleset.skk.moe/List/ip/reject.conf,REJECT-DROP
```

早年间，如果用户访问了一个不存在的域名（`NXDOMAIN`），运营商的递归 DNS 会污染 NXDOMAIN、返回一个广告页面的 IP 地址。felixonmars 的 `dnsmasq-china-list` 中的 `bogus-nxdomain.china.conf` 就是收集了这些广告页面的 IP 地址。`ip/reject.conf` 规则组的数据来源就是 `bogus-nxdomain.china.conf`，也包含了一些自己手动收集的地方运营商的拦截页面的 IP。
### Telegram IP 规则

```
RULE-SET,https://ruleset.skk.moe/List/ip/telegram.conf,[替换你的策略名]
PROCESS-NAME,Telegram,REJECT-DROP
```

`telegram.conf` 是每天定时抓取 Telegram 官方发布的 IP CIDR（`https://core.telegram.org/resources/cidr.txt`）生成的规则组。相比其它规则组自行收集 Telegram 的 ASN，采用官方发布的 IP 和 CIDR 列表分流更准确。

Telegram 的 macOS Swift 客户端（不论是从 Telegram 官网下载、还是 macOS App Store 下载）经常会连接一些不属于 Telegram 的、甚至是不存在的（例如 `0.0.0.0`、`0.1.2.3`）的 IP。我向 Telegram macOS Swift 客户端的开发者、Telegram 官方的 bugtracker 反馈（[GitHub Issue](https://github.com/overtake/TelegramSwift/issues/1060)、[Telegram 官方的 Bugtracker](https://bugs.telegram.org/c/36949)），没有得到任何回应。因此我认定 Telegram 的 macOS Swift 客户端存在隐私泄露风险。将两条规则搭配使用，可以实现仅放行 Telegram IP、对 Telegram 进程的其余网络连接使用 REJECT-DROP 全部丢弃。与此同时，读者也可以前往 [Telegram 官方的 Bugtracker](https://bugs.telegram.org/c/36949) 为该 Issue 点赞、引起 Telegram 官方的重视。
### 流媒体 IP

```
# RULE-SET,https://ruleset.skk.moe/List/ip/stream_hk.conf,[替换你的策略名]
# RULE-SET,https://ruleset.skk.moe/List/ip/stream_jp.conf,[替换你的策略名]
# RULE-SET,https://ruleset.skk.moe/List/ip/stream_us.conf,[替换你的策略名]
# RULE-SET,https://ruleset.skk.moe/List/ip/stream_tw.conf,[替换你的策略名]
# RULE-SET,https://ruleset.skk.moe/List/ip/stream_kr.conf,[替换你的策略名]
# RULE-SET,https://ruleset.skk.moe/List/ip/stream_eu.conf,[替换你的策略名]
RULE-SET,https://ruleset.skk.moe/List/ip/stream.conf,[替换你的策略名]
```

按照流媒体限定区域区分的常见流媒体服务 IP 列表。你可以根据自己的需求选择性引用 `stream_[xx].conf` 规则、并使用 `stream.conf` 为剩下所有流媒体 IP 做兜底。
### 局域网 IP

```
RULE-SET,https://ruleset.skk.moe/List/ip/lan.conf,DIRECT
```

按照 [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) 划分的局域网 IP 和保留 IP 列表，这部分 IP 需要直连访问。
### 国内 IP 段

```
RULE-SET,https://ruleset.skk.moe/List/ip/domestic.conf,DIRECT
RULE-SET,https://ruleset.skk.moe/List/ip/china_ip.conf,DIRECT
```

国内 IP 列表。其中，`domestic.conf` 是我手工维护的腾讯云 AIA Anycast 业务的 IP 段和阿里云 Anycast 业务的 IP 段；`china_ip.conf` 的数据主要来自 Misaka Networks, Inc. 维护的 [chnroutes2](https://github.com/misakaio/chnroutes2) 项目，并针对一些特殊情况进行了处理：补充合并了 Misaka Networks, Inc. 收不到 BGP 路由的国内 IP 段、排除了中国移动和中国移动国际（CMI）在香港广播的几个段。
### FINAL

```
FINAL,[替换你的策略名],dns-failed
```

不能被域名和 IP 规则匹配到的请求、或者 Surge 本机 DNS 解析失败的请求，都使用 FINAL 策略。
### 其他规则列表

上述就是我自用的全部规则列表。我也维护有其他规则列表满足特殊需求，大家可以按需去用。

**iCloud Private Relay 域名列表**

```
DOMAIN-SET,https://ruleset.skk.moe/List/domainset/icloud_private_relay.conf,[替换你的策略名]
```

**常见直连规则列表**

需要走直连的进程和域名，包含大部分 BT 和 BT Based 下载器的进程名、PT 站的域名、AdGuard 程序往网页中注入去广告增强脚本的域名（如 `local.adguard.org` 和 `injections.adguard.org`）、常见学术科研类网站的域名（通常在教育网或科技网环境下需要直连访问）等。

```
RULE-SET,https://ruleset.skk.moe/List/non_ip/direct.conf,DIRECT,extended-matching
```

## 通用（General）设置

**skip-proxy**

```
skip-proxy = 127.0.0.0/8, 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, 100.64.0.0/10, 162.14.0.0/16, 211.99.96.0/19, 162.159.192.0/24, 162.159.193.0/24, 162.159.195.0/24, fc00::/7, fe80::/10, localhost, *.local, captive.apple.com, passenger.t3go.cn, *.ccb.com, wxh.wo.cn, *.abcchina.com, *.abcchina.com.cn
```

在 Surge iOS 中，包含在 `skip-proxy` 的 IP 段和域名会绕过 Surge Proxy、直接通过 Surge VIF 虚拟网卡处理；而在 Surge Mac 中，`skip-proxy` 会被写入系统偏好设置中的 `Skip Proxy`。这个设置主要是为了避免某些 iOS 应用检测到系统代理，以及一些会读环境变量的软件（例如 curl、Node.js 和 Bun 的 `HttpAgent`）能够正确处理内网流量。

**always-real-ip**

在 `always-real-ip` 内置的域名，Surge 的 DNS 在解析时不会返回 Fake IP、主要改善部分 UDP 流量和部分软件的兼容性。我使用脚本自动化生成的 Surge Module 去设置这个值：

```
https://ruleset.skk.moe/Modules/sukka_common_always_realip.sgmodule
```

**exclude-simple-hostnames**

```
exclude-simple-hostnames = true
```

控制不带点的域名（如 `localhost`、`DEVICE-A114514` 这类 mDNS 名）是否绕过 Surge Proxy、直接使用 Surge VIF 虚拟网卡处理。

**hijack-dns**

```
hijack-dns = 8.8.8.8:53, 8.8.4.4:53
```

让 Surge 劫持目标为 8.8.8.8 和 8.8.4.4 的 53 端口，解决 Google 系家用产品（如 Chromecast）强制使用 8.8.8.8 和 8.8.4.4、不使用 Surge DNS 的问题。

**ipv6 / ipv6-vif**

```
ipv6 = false
ipv6-vif = off
```

`ipv6` 选项主要控制 Surge 的 DNS，`true` 时 Surge 的 DNS 会同时请求 `AAAA` 和 `A` 记录、`false` 时 Surge 只会请求 `A` 记录。注意，**即使在 Surge 中设置了 `ipv6 = false`，在 `global.conf`、`stream.conf` 和 `cdn.conf` 规则组中的域名仍然可以使用 IPv6，因为那些域名 Surge 会直接把请求转发到远端策略在远端上直接解析、不在本地通过 Surge 进行 DNS 解析**，不受 `ipv6 = false` 影响，即：

```
本机 -- IPv4 -> 远端策略 -- IPv6 -> 目标网站
```

`ipv6-vif` 选项主要控制 Surge Helper 修改路由表的行为、是否将 IPv6 的网段也添加到本机路由表通过 Surge 虚拟网卡。

一般的，建议将两个 IPv6 都禁用，因为在国内使用 IPv6 可能导致网络体验劣化，而且即使在 Surge 中禁用了 IPv6、也不影响海外网站和流媒体的 IPv6。

2024 年 4 月 18 日更新：从 Surge 5.7.0 Build 2685 开始，如果设置了 `ipv6-vif = always`，即使没有设置 `ipv6 = true` 也会开启 IPv6 功能。

**show-error-page-for-reject**

```
show-error-page-for-reject = true
```

当一个请求被 Surge 的 REJCT-* 策略拦截时，返回一个 HTML 拦截页。

**read-etc-hosts**

```
read-etc-hosts = true
```

控制是否让 Surge for Mac 读取 `/etc/hosts` 文件并在 Surge DNS 中模拟该行为。

**internet-test-url / proxy-test-url / proxy-test-udp**

```
internet-test-url = http://connectivitycheck.platform.hicloud.com/generate_204
proxy-test-url = http://latency-test.skk.moe/endpoint
proxy-test-udp = www.apple.com@64.6.64.6
```

这三个选项控制 Surge 如何测试本地和远端策略的可用性、以及远端策略的 UDP 可达性。Surge 会使用 HEAD 方式请求 `internet-test-url` 和 `proxy-test-url` 的地址，并且无视响应的状态码、只要有响应就视为网络可达。Surge 会通过远端策略、对 `proxy-test-url` 中指定的 DNS 服务器和域名进行一次 DNS 解析请求，如果远端 DNS 解析成功则视为远端策略 UDP 可达。

我编写了一个小工具 [Compare Captive Portal](https://lab.skk.moe/test-204) 专门测试最适合你的 `internet-test-url` 和 `proxy-test-url` 地址。需要注意的是，部分 商业性质的远端策略服务提供商 可能存在劫持 `proxy-test-url` 的问题，有能力的可以自建。

不建议在 `proxy-test-url` 中使用 `www.gstatic.com`、容易引起 Google 对 IP 的风控。

`proxy-test-udp` 建议使用非常见的海外公共 DNS（如 Vercara、原 UltraDNS / NeuStar 的公共 DNS）解析常见域名（如 `www.apple.com`）。

**vif-mode**

```
vif-mode = v3
```

控制 Surge for Mac 的 VIF 虚拟网卡使用的底层机制，详情可以查看 [Surge 文档中对 vif-mode 的介绍](https://manual.nssurge.com/others/misc-options.html#vif-mode) 和 [Surge 5 VIF 模式与性能报告](https://community.nssurge.com/d/1915-surge-mac-5-vif-m3)。简单来说：
- `auto`：让 Surge 自动决定最适合的模式。 截至本文写就，
- Apple Silicon 处理器的 Mac，Surge 会使用 `v1` 模式
- Intel 处理器的 Mac，Surge 会检测虚拟机软件（Parallels Desktop、VMWare、Docker），存在则使用 `v3`、否则使用 `v2`；如果遇到内核网络栈重置、自动重启并降级到 v1
- `v1`：传统模式。兼容性最好，性能相对另外两种模式最差（Surge 仍然在不断优化，目前在 Apple Silicon 平台上已经可以实现约 10 Gbps 网络）
- `v2`：通过 pf（BSD Packet Filter）使用 macOS 系统的 TCP 协议栈，大幅提升了性能；但是由于修改了 pf 配置、不兼容虚拟机和 Docker，且有内核网络栈的内存限制
- `v3`：不通过 pf 去调用 macOS 的 TCP 协议栈，因此没有修改 pf 配置导致的虚拟机兼容性问题，但是依然有内核网络栈的内存限制

`v2` 和 `v3` 都依赖 macOS 的 TCP 协议栈、因此会受到 macOS 内核限制。具体地，macOS 内核网络栈有 256 MiB 的内存限制、当 Surge for Mac 处理的连接数过高（如通过 Surge 进行 BT 下载时）时极易超出内存限制、导致 macOS 主动关闭 Surge 建立的连接。

推荐大部分人使用 `auto`、由 Surge 自动选择最适合的 VIF 模式。我自己不存在产生大量连接数的场景、又存在使用 Docker 和虚拟机的场景、因此手动选择了性能相对更好且兼容虚拟机的 `v3` 模式。

**udp-policy-not-supported-behaviour**

```
udp-policy-not-supported-behaviour = REJECT
```

当前流量选用的策略不支持 UDP 转发时、如何处理这部分流量，可以设置 `DIRECT` 和 `REJECT`。推荐用 `REJECT`，防止 UDP 流量被直连漏出去。
## DNS 分流设置

我在 Surge 中，根据当前所在的网络环境选择默认 DNS：如果网络环境比较文明、则使用由 运营商/路由器 提供的 DNS 作为默认 DNS（运营商提供的 DNS 对国内 CDN 的解析最准确）；如果网络环境并不是很文明、则使用国内公共 DNS 提供的加密 DNS 服务、牺牲国内 CDN 体验换取整体的网络体验。

```
[General]
encrypted-dns-server = quic://223.5.5.5, quic://223.6.6.6, https://1.12.12.12/dns-query, https://120.53.53.53/dns-query
```

关于为什么需要尽可能使用运营商提供的 DNS 作为默认 DNS、运营商的默认 DNS 有什么优势，我在之前的文章 [我有特别的 DNS 配置和使用技巧](https://blog.skk.moe/post/i-have-my-unique-dns-setup/) 中有详细介绍。

即使使用了国内公共 DNS 提供的服务，整体的网络体验也不一定能得到保证，因为 [阿里或者腾讯提供的公共 DNS 存在歧视（例如刻意劣化竞争对手的域名的解析）](https://github.com/pymumu/smartdns/issues/656)。因此针对这些公司的域名需要做 DNS 分流处理，即阿里的域名使用阿里云的公共 DNS、腾讯的域名使用 DNSPod 的公共 DNS，百度、字节、360 也分别用各自家的公共 DNS（自家的公共 DNS 也不打自己人嘛）。除此以外，局域网域名必须交给内网 DNS 解析、不能交给公共 DNS。

Surge 的 [Local DNS Mapping](https://manual.nssurge.com/dns/local-dns-mapping.html) 功能可以解决 DNS 分流的问题。在项目中我使用 [domestic.ts](https://github.com/SukkaW/Surge/blob/master/Source/non_ip/domestic.ts) 文件记录域名和需要使用的 DNS，然后脚本会自动化生成 DNS Mapping 的 Surge Module：

```
https://ruleset.skk.moe/Modules/sukka_local_dns_mapping.sgmodule
```

## Surge 多网络环境自动切换

有一段时间，我经常需要带着我的笔记本在不同的网络环境下切换，所以我配置了如下的 Proxy 和 Proxy Group、由 Surge 实现自动切换网络：

```
[Proxy]
# 无线网卡。在 MacBook Pro 上，无线网卡的接口名一定是 en0
Wi-Fi = direct, interface=en0, test-url=http://connectivitycheck.platform.hicloud.com/generate_204
# 需要根据 ifconfig 自己判断。而且，Thunderbolt 自带的网卡 和 通过 Thunderbolt 的 PCIE 转接的网卡 的接口名也不一样
Thunderbolt = direct, interface=en10, test-url=http://connectivitycheck.platform.hicloud.com/generate_204
# 国内测速地址如前文所说，可以按需选择。这里是因为将 direct 作为一个特殊的 Proxy Policy、所以需要手动指定测速地址、否则 Surge 会使用 `proxt-test-url` 来测活

[Proxy Group]
# 新建一个策略组 Domestic，使用 fallback、每 30 秒测活一次
# 这个策略组还同时包含了 Surge 内置的 DIRECT 策略、即由 macOS 系统决定的当前活跃的网络接口（也就是 Surge 的 Primary Interface Changed 中的 Primary Interface）
Domestic = fallback, Thunderbolt, Wi-Fi, DIRECT, interval=30, timeout=3
# 如果策略组使用 load-balance，还可以实现多网卡负载均衡和叠加、适合下载没有限制 IP 的大文件
Domestic Dual = load-balance, Thunderbolt, Wi-Fi, interval=30, timeout=3
```

---

> **Author's Notice**: This content is based on the blog post "我有特别的 Surge 配置和使用技巧" from Sukka's Blog (blog.skk.moe). It does not represent any views or positions of Sukka or Sukka's Blog. Please read the original article for full context: https://blog.skk.moe/post/i-have-my-unique-surge-setup/

License: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)