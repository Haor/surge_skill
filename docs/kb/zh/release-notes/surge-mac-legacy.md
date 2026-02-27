# Surge Mac 历史版本

## Surge Mac 旧版本

{% hint style="success" %}
自 v6 版本开始，请从这里查看更新日志：<https://nssurge.com/support/mac/release-notes>
{% endhint %}

* 自 Surge Mac v5.8.0 版本起，Surge 对 macOS 的最低版本需求提高至 macOS 12.0。如果你的操作系统为 10.13/10.14/10.15/11。请下载 5.7.5 版本：<https://dl.nssurge.com/mac/v5/Surge-5.7.5-2826-4f19761fb2275ebbe2acf43907bd9371.zip>
* Surge Mac v5 的最后一个版本下载链接：<https://dl.nssurge.com/mac/v5/Surge-latest.zip>
* Surge Mac v4 的最后一个版本下载链接：<https://dl.nssurge.com/mac/v4/Surge-latest.zip>
* Surge Mac v3 的最后一个版本下载链接：<https://dl.nssurge.com/mac/v3/Surge-latest.zip>
* Surge Mac v2 的最后一个版本下载链接：<https://dl.nssurge.com/mac/v2/Surge-latest.zip>

## Surge Mac v5 更新日志

#### 版本 5.10.3

* 新增 `[General]` 参数 `block-quic`，用于全局覆盖是否阻止 QUIC 流量的行为。可设置为：
  * `per-policy`：由 policy 的 `block-quic` 参数决定，默认为当前版本行为。
  * `all-proxy`：覆盖代理 policy 的 `block-quic` 参数，全部阻止
  * `all`：覆盖所有 policy 的 `block-quic` 参数，包括 DIRECT policy 在内全部阻止
  * `always-allow`：覆盖代理 policy 的 `block-quic` 参数，全部允许
* 新增规则添加视图现在可以记住上一次的选项。
* 错误页面新增深色模式支持。
* 增加对 Dia 浏览器的集成支持。
* 修复了 bug 并进行了其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.10.3-3272-5cf851de0c9af2bf96ab410244010f9a.zip>

#### 版本 5.10.2

* 访问 Ponte 设备的远程 Dashboard 不再需要启用增强模式。
* 新增对 DNS over TLS 的支持，例如 `tls://8.8.8.8`
* 优化了通过 Dashboard 添加规则的流程。
* Surge Dashboard 现在可以远程操作目标 Surge 实例的临时规则。
* 修复了一些错误并进行了其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.10.2-3235-9255a55c4af59cbf0ed01b245ef86dcc.zip>

#### 版本 5.10.1

* 当启用 HTTP 捕获开关时，现在会强制中断所有活动连接，以确保不会因现有长连接而漏捕任何请求。
* 优化了对部分 QUIC 客户端（如 Lark）的兼容性。
* 修复了通过脚本或其他机制修改请求 HTTP 后，统计中的下载数据字节数不正确的问题。
* 调整了转发 QUIC 时的处理逻辑优先级。现在，对于不支持 UDP 转发的代理 policy，会优先考虑 QUIC Block，然后再回退到 DIRECT 或 REJECT。
* 修复了绑定出站接口时无法使用 utun 设备的问题。
* 修复了 Ponte Server 重试失败期间可能持续出现重复通知的问题。
* 解决了 Surge Ponte 转发的特定请求在某些网络下可能卡住的问题。
* Bug 修复及其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.10.1-3207-1e925800c695a40e8a34ceca6d856b0d.zip>

#### 版本 5.10.0

**新功能：端口转发**

示例

```
[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy
```

policy 参数为可选项；如果未指定，将使用标准代理匹配来确定 policy。 该功能常用于开发和调试场景，例如通过 SSH 连接 MariaDB 等服务器。

**#!REQUIREMENT 升级**

* 现在提供三种简单标记：#!IOS-ONLY、#!MACOS-ONLY 和 #!TVOS-ONLY。
* 被此行尾注释禁用的内容现在可以在 UI 中显示和编辑。当条件不满足时会显示为已禁用，若启用则会自动移除限制。

示例

```
DOMAIN,reject.com,REJECT #!MACOS-ONLY
```

**\[Host] 优化**

\[Host] 部分支持使用 DOMAIN-SET 和 RULE-SET 配置，以提升匹配效率。使用案例：

```
[Host]
DOMAIN-SET:https://example.com/domains.txt = server:https://doh.com/dns-query
RULE-SET:https://example.com/rules.txt = server:https://doh.com/dns-query
```

**其他改进**

* 优化以 Smart policy 分组作为底层代理的情况。。现在，在这种使用场景下，可以充分发挥 Smart policy 分组的特性。
* Surge Ponte 在出现异常 NAT 类型后，现在可以自动重试恢复。
* 修复了一些 bug 并进行了其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.10.0-3195-d468f4e99b54bcde0432f2b5a0e38296.zip>

#### 版本 5.9.3

* 修复了漏洞并进行了其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.9.3-3122-0244efc5738b3cebde7c87c556cfddb8.zip>

#### 版本 5.9.2

* 菜单栏图标现在可以显示出站模式。
* 修复了与 Ponte 相关的一些问题。
* 修复了在 DHCP 配置页面上错误信息有时无法显示，导致无法继续操作的问题。
* 修复了为 .local 域名配置的 \[Host] 条目可能无效的问题。
* 优化了代理和规则编辑页面；UI 中不可编辑的参数现在也会被保留。
* 其他 bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.9.2-3098-643c195efc1153b6d4993af6bba73a59.zip>

#### 版本 5.9.0

#### 新功能

* 添加了低开销请求拒绝的预匹配规则。详情请参阅文档：<https://manual.nssurge.com/policy/reject.html>
* Body Rewrite 支持使用 JQ 表达式操作 JSON。
* shadowsocks 协议新增支持 `2022-blake3-aes-256-gcm` 和 `2022-blake3-aes-128-gcm` 加密模式。

#### 改进

* URL-REGEX 规则现在支持 `extended-matching` 标签。
* 允许使用 Ponte 策略作为底层代理。
* 修改 HTTP 脚本的终止逻辑。如果需要中断请求，请使用 $done({abort: true})。其他失败不会修改或终止请求。
* 全面优化和改进 UDP 转发。

#### 错误修复

* 修复在增强模式下 DNS 请求无法根据路由表选择正确接口的问题。
* 修复 macOS 12 上无法获取系统路由的问题。
* 修正某些情况下判断 IPv6 是否存在可能不正确的问题。
* 修复有时错误提示代理设置已被其他程序修改的问题。
* 其他错误修复。

<https://dl.nssurge.com/mac/v5/Surge-5.9.0-3025-f8d045da66079150d4a281ed3770b3f6.zip>

#### 版本 5.8.2

* 修复启用 `gateway-restricted-to-lan` 参数时 IPv6 VIF 无法接管请求的问题。
* 对 `use-application-dns.net` 的 DNS 查询将返回 NXDOMAIN，导致 Firefox 自动禁用应用程序 DNS（即 DoH）。直接在浏览器中使用加密 DNS 会阻止 Surge 正确获取请求的域名。
* 错误修复和小幅改进。

<https://dl.nssurge.com/mac/v5/Surge-5.8.2-2946-b739968f1d90da3b755d3bf82941e8c2.zip>

#### 版本 5.8.1

* 新参数：proxy-restricted-to-lan/gateway-restricted-to-lan 一些用户由于缺乏网络安全知识，意外地将代理和网关服务暴露在互联网上（例如，配置了 DMZ）。因此，添加了这两个参数以限制代理和网关服务仅接受来自当前子网的设备。这两个参数默认启用。
* 修复增强模式与 PPPoE 直接拨号之间的兼容性。
* 支持使用 ETag 避免在请求外部资源时下载重复数据。
* Surge 现在支持处理系统的 DNS 搜索域设置。
* 其他错误修复和兼容性改进。

<https://dl.nssurge.com/mac/v5/Surge-5.8.1-2929-5220af95366dfacec7ca84cb8ddd122c.zip>

#### 版本 5.8.0

**网络扩展**

* 鉴于传统 utun 接管方案在新系统版本中出现了诸多问题，从 Surge Mac 5.8.0 开始，Surge Mac 将使用 Network Extension 作为增强模式来接管系统网络。
* Surge Mac 的最低系统版本要求提升至 macOS 12。
* 因为所需权限不同，更新后需要手动授权操作。
* `vif-mode` 参数将不再有效。
* 增强模式现在可以与网络共享功能结合使用，这意味着你可以直接创建由 Surge 管理的 Wi-Fi（需要有线网络）。

**端口跳跃**

Hysteria2 和 TUIC 协议现在支持端口跳跃，以改善 ISP 对 UDP 的 QoS 问题。详情请参阅服务器文档。

`Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234;5000-6000;7044;8000-9000", port-hopping-interval=30`

配置 `port-hopping` 参数后，前面配置的主端口号将不再有效。

参数：

* `port-h-hopping`: 用于配置端口范围。用逗号分隔，并支持用连字符配置的范围。
* `port-hopping-interval`: 更换端口号的间隔时间。默认为30秒

**其他改进**

* 鉴于新 macOS 系统中大量需要权限的功能，新增了一个专门用于管理系统权限的页面。
* 本地 DNS 映射中的 `syslib` 关键字现在可以在增强模式下使用。然而，在非增强模式下，解析完全由系统处理。在增强模式下，Surge 使用系统的 DNS 地址进行解析。
* 新增 `[General]` 参数 `show-error-page`, 用于控制当发生错误时是否显示 Surge 的 HTTP 错误页面。此参数默认启用，其行为与之前版本一致。

<https://dl.nssurge.com/mac/v5/Surge-5.8.0-2900-6379c9d5240ae1555772aed2eb977e69.zip>

#### 版本 5.7.5

* 面板现在可以在 Surge Mac 中使用。
* DNS 转发子系统优化
* 当 DNS 查询的域名是不应转发到公共网络的域名（例如 .home.arpa, 1.0.168.192.in-addr.arpa）时，将自动确定上游 DNS 地址并仅转发到局域网 DNS 服务器。
* Surge 现在可以正确响应假 IP 的 PTR 请求，这意味着使用 `dig -x 198.18.23.87` 命令可以确定与假 IP 对应的原始域名。
* DNS 转发器现在将根据 `[Host]` 部分配置将 DNS 请求转发到特定的上游服务器。
* 对于不支持的假 IP 的 DNS-SD PTR 请求，直接以 NOTIMP 响应，而不进行转发。
* 为当前网页添加规则时，可以选择添加到现有规则集中。
* 修复了一些错误。

<https://dl.nssurge.com/mac/v5/Surge-5.7.5-2826-4f19761fb2275ebbe2acf43907bd9371.zip>

#### 版本 5.7.4

* 由于 Surge Ponte 所依赖的公共 STUN 服务器突然关闭，导致 Surge Ponte 无法使用，我们进行了紧急替换。此外，我们将在未来建立自己的 STUN 服务器，以避免此类问题。
* 增强与 VPN 和多网卡的兼容性

在之前的版本中，如果启用了增强模式，由于 Surge 覆盖了系统的路由表，所有出站数据包将被强制使用主接口。这绕过了路由表以避免创建循环。

然而，这也导致在有多个网卡或其他 VPN 的情况下，数据包无法从正确的接口发送的问题。

本版本改进了这一设计。现在，在增强模式下，如果存在更高优先级的子路由，Surge 将自动检查路由，并仍然对 TCP/UDP 数据包使用标准路由，从而提高兼容性。

* 修复包含重复 DOMAIN 和 DOMAIN-SUFFIX 规则时可能导致 DOMAIN-SUFFIX 规则失效的问题。
* 其他错误修复。

<https://dl.nssurge.com/mac/v5/Surge-5.7.4-2806-afe67661ef616b7bbab189dec1473b68.zip>

#### 版本 5.7.3

* 现在可以在规则列表中看到某条规则被使用的次数
* 优化了阻拦 QUIC 流量的实现方法，以提高让客户端正确回退的可能性
* Smart 组当不存在子策略时，也会使用 SUBSTITUTE 策略(DIRECT)而非直接失败。
* 修正 TLS 类协议，在 sni=off 的设置下，server-cert-fingerprint-sha256 参数未能生效的问题
* 新增规则类型 HOSTNAME-TYPE，用于判断请求的主机名的类型，可选值有：IPv4, IPv6, DOMAIN, SIMPLE。（SIMPLE 指的是不包含 . 的主机名，如 localhost）
* 优化了 DNS 的请求日志，现在会显示更多的信息，且在规则系统未触发 DNS 时，如果是 DIRECT 策略直连也可以显示 DNS 的相关日志了
* 在删除策略时，如果该策略被策略组所使用，现在允许直接删除并将自动从所有策略组移除

<https://dl.nssurge.com/mac/v5/Surge-5.7.3-2785-048c0bdc5ee2b05dab39852d51a19ff4.zip>

#### 版本 5.7.2

* 优化规则集中 ASN 规则的匹配性能
* 修复无法通过 UI 编辑 FINAL 规则的问题
* 修复无效的 cron 表达式会导致脚本被重复执行的问题
* 优化了脚本引擎的管理机制
* 其他小问题修复

<https://dl.nssurge.com/mac/v5/Surge-5.7.2-2762-9a963758f386b5da00e7744b2a7f254d.zip>

#### 版本 5.7.1

* 优化小型规则集的匹配性能，在旧型号 CPU 上效果尤为明显
* 外置资源更新页面可以显示规则集处理产生的错误信息
* 自动忽略规则集中的无效空行
* 修正应用临时规则后，如果产生了策略变化，不会打断原有连接的问题
* 修正在 Smart 组内使用 Ponte 策略时，如果目标设备是自身，未能自动转换为 DIRECT 策略的问题
* 修正 Ponte 设备请求在请求日志中显示的时间错误的问题
* 修正当外部策略组产生变化时，可能导致的崩溃
* 修正配置升级功能未能对托管配置和企业配置正确生效的问题
* 在 Smart 组初始化阶段，不再显示最常使用标签，以避免产生误解
* 修正在建立策略组时，如果勾选了外部策略但是没有填写 URL，会导致崩溃的问题
* 修正密钥库管理页面，进行移动操作后的项目未能正确显示存储位置的问题

<https://dl.nssurge.com/mac/v5/Surge-5.7.1-2757-e7b680d5dc23e1258188adc4d81116d7.zip>

#### 版本 5.7.0

**Smart Group**

这是一种全新的策略组类型，由我们精心设计的算法引擎所驱动，可以自动从该策略组的子策略中选择合适的策略。Smart 策略组的目标是取代原有的自动测试组（url/load-balance/fallback），大幅优化体验的同时，尽可能减少用户需要手动干预策略组的情况，用户只需将可用策略放入该组即可。

详情请见：<https://kb.nssurge.com/surge-knowledge-base/v/zh/guidelines/smart-group>

**规则系统**

* 规则系统整体性能优化。
* 大幅优化大型域名规则集中的索引算法，对于十万条以上的规则集，检索效率提高了十倍以上。
* 修正规则集内的逻辑规则的子规则无法被规则集的 no-resolve 和 extended-matching 参数覆盖的问题
* 新增规则类型 DOMAIN-WILDCARD，支持 ? 与 \* 匹配域名
* DOMAIN-SET 与 RULE-SET 改为强校验，当文件中包含无效行时将导致整个规则集无效，以避免误用产生问题

**IPv6**

* ipv6-vif 参数行为修改，当设置为 always 时，即使未设置 ipv6=true，也会开启 IPv6 功能。
* 为 ipv6-vif=always 参数增加了警告
* 调整了自动重试机制，在非 IPv6 网络下访问 IPv6 地址不再会进入重试流程，请求会立刻失败（以此解决在非 IPv6 环境下开启 IPv6 VIF 造成部分应用卡顿的问题，如微信和淘宝，但是应用仍然会持续发出 IPv6 请求）

**其他优化**

* $notification.post 增强，新增媒体资源支持、声音提示和自动消除。
* 优化 WireGuard 失败处理
* 降低 TUIC 协议在休眠时对电量的消耗
* 请求日志系统时间统计精度提高，现在可精确到 µs 级
* 优化各种异常的重试机制，避免在出现一些特定问题时持续重试导致高资源占用。对于需要持续重试的操作（如 WireGuard 重连、Ponte 服务端上报 iCloud），现在 Surge 会在出错后的 0.1s, 0.5s, 1s, 5s, 10s, 30s 后重试。
* 优化外部资源的缓存系统
* 新增配置文件行命令 #!REQUIREMENT

**细节调整**

* 限制了脚本在 debug 模式下，可以往请求 notes 中写入的日志的长度
* 默认 UDP 测试目标改为 1.0.0.1
* 在脚本中使用 API 时如果传入了错误类型的字段，将产生脚本异常
* 当脚本已完成或超时后，未完成的 $httpClient 不再会调用回调函数

**问题修正**

* 修正 Dashboard 查看远端设备时，无法读取截取的 HTTP Body 的问题
* 修正 Header Rewrite 规则无法根据 Host 字段进行 URL 匹配的问题
* 修正了在测试代理时，ip-version 和 tos 参数无法生效的问题
* 修正通过 HTTP-API 执行脚本时，若果错误的传入 null 会导致崩溃的问题

<https://dl.nssurge.com/mac/v5/Surge-5.7.0-2724-acaafccea020f6afdc758c83057ffcbb.zip>

#### 版本 5.6.0

**新功能**

* Mock (本地映射) 功能全面增强。
  * 新增数据类型如 `text`, `tiny-gif`, `base64` 以便直接内联返回数据。
  * 新增 `status-code` 参数
  * UI 相关配置尚未更新。使用方法见文档：<https://manual.nssurge.com/http-processing/mock.html>
* 当配置了参数 `encrypted-dns-follow-outbound-mode=true`，如果 DoH/DoQ/DoH3 连接匹配到使用域名的代理服务器，并且该代理服务器的域名存在 DNS 本地映射记录含有 IP 地址或传统 DNS 服务器，则允许通过该代理服务器查询。（通过代理服务器查询 DNS 会破坏 CDN 优化，导致加载图片和视频时严重缓慢。除非有非常特殊的需求并且不必这样配置，应使用域规则确保请求直接由代理服务器查询。）
* 新增 Body Rewrite 功能，详情见文档：<https://manual.nssurge.com/http-processing/body-rewrite.html>
* 新增对 STUN 数据包的识别，可使用 PROTOCOL,STUN 进行匹配。类似 QUIC，为确保兼容性，PROTOCOL,UDP 也可继续匹配 STUN 流量。

**增强**

* 优化请求日志记录。现在将显示匹配到的 URL Rewrite 和 Header Rewrite 的具体规则。
* 调整了 DNS 引擎处理空结果的逻辑。现在当配置了多个 DNS 服务器时，不再等待所有服务器响应空结果，以避免在 AAAA 记录不存在时产生额外等待。（然而，由于 DNS 服务器在不同环境下的表现可能有所不同，观察此更改是否引起副作用；如果出现问题导致异常结果，请提供反馈。）
* 取消了 ICMP 超限时的警告通知

#### 修正

* 增强了 HTTP Body 解压时的兼容性。
* 修正了 Surge 由于传入某些错误类型的参数而导致的崩溃。
* 适应新系统限制，修正了在某些情况下选择显示主窗口无效的问题
* 修正了代理模式下非 https WebSocket 与新版 Safari 的兼容性问题

<https://dl.nssurge.com/mac/v5/Surge-5.6.0-2611-efc3b7ebb3872061e9a6a4917742e203.zip>

#### 版本 5.5.0

**模块**

* 新增了多个新的官方模块；现在可以动态更新官方模块了。
* 模块新增了一个用于在 UI 中便捷访问和分类的分类字段。
* 模块现在接受参数表，支持多个参数。参数将用于通过文本替换修改模块内容。

**脚本**

* 新的脚本执行引擎。优化了执行性能和内存使用。
* $httpClient 增加了几个实用参数。 有关上述更新的更多详情，请参阅文档。

**增强功能**

* 新参数：always-raw-tcp-keywords。使用方法，请参见文档。
* 增加了 SRC-PORT 规则用于匹配客户端端口号。
* IN-PORT/SRC-PORT/DEST-PORT 三条规则被归类为端口号规则类型，支持三种表达式：
  * 直接写端口号，如 IN-PORT,6153
  * 端口号闭区间：如 DEST-PORT,10000-20000
  * 使用 >, <, <=, >= 操作符，如 SRC-PORT,>=50000
* UI 现在可以在编辑后保持原始配置中的纯空行。

**修复**

* 修正了 QUIC 流量控制的一个细节问题并针对 Ponte/TUIC/Hysteria2 协议优化了延迟性能。
* 编辑单个规则后，通知相关参数将被保留。

<https://dl.nssurge.com/mac/v5/Surge-5.5.0-2586-ed7ce88d6b2a286537ff5402324cb7fe.zip>

#### 版本 5.4.3

* 重写了虚拟 IP 数据库，现在数据库可以基于最后一次使用时间自动清理数据。
* 修复了在使用 Snell v4 与 WireGuard 并启用复用时可能出现的一些问题。
* 对于带有非法域名的 DNS 请求，将生成一个空结果响应，而不是被直接忽略。
* `tun-included-routes` 和 `tun-excluded-routes` 参数现在支持在启用 IPv6 VIF 时使用 IPv6 CIDR 块。
* 支持为内置规则集/内联规则集配置 no-resolve。
* Surge Ponte 连接不再验证对等地址，以确保在某些特殊场景下的正常运行。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.4.3-2540-511d4692c27626166bbcbb61fdd56bc8.zip>

#### 版本 5.4.2

* 修复了内置规则集 LAN 无法正确触发 DNS 解析的问题。
* 修复了处理某些格式错误的 UDP 包时可能导致崩溃的问题。
* 修复了一个系统可能错误判断已经重启，导致 Fake IP 表被清除的问题。
* 修复了与特定 HTTP 服务器的兼容性问题。
* 兼容了一些非标准 SOCKS5 UDP 服务器实现，将错误调整为警告。
* 其他 bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.4.2-2502-001dc6b9672b7e79f92ca5cd3be6baf2.zip>

#### 版本 5.4.1

**规则引擎优化**

RULE-SET 与 DOMAIN-SET 的实现完全重写，现在 Surge 会在资源更新时自动对规则集进行预处理，建立索引数据结构，大幅提高匹配速度。

1. RULE-SET 和 DOMAIN-SET 两种类型规则集不再有性能和内存占用区别，可以随意使用。
2. DOMAIN-SET 规则集不再存在不可以使用 eTLD 的限制。
3. RULE-SET 中的 DOMAIN, DOMAIN-SUFFIX, IP-CIDR, IP-CIDR6 规则匹配速度得到大幅提升。
   * 十万条左右的 DOMAIN/DOMAIN-SUFFIX 规则集，在旧版中单次匹配需要 100ms，现在只需要个位数 ms。
   * 一万条左右的 IP-CIDR 规则集，在旧版中单次匹配需要约 0.1ms。新版只需要0.0002ms，提升了约 500 倍。IP-CIDR6 规则的性能提升幅度更高。
4. 在新版本中，自行通过 IP-CIDR 规则集构建出地区的 IP 地址集合，与直接使用内部的 GEOIP 规则的性能已经完全一致。
5. 先前版本加入的 Inline Ruleset 无法享受该优化，但是在百条数量级下几乎无差异。
6. 先前版本中，Ruleset 中的规则也是按照从上至下的方式逐条匹配，如果规则集中同时包含了需要 DNS 解析的规则，也只有当开始匹配该子规则时才会触发 DNS。新版本中，只要规则集中包含任意一条需要 DNS 解析的规则，在测试该规则集前就会先进行 DNS 解析。（绝大多数情况下没有任何区别）

* 主规则匹配效率小幅优化。
* IP-CIDR6 规则在非索引情况下的效率也得到大幅提升。
* RULE-SET 规则可直接配置参数 no-resolve 和 extended-matching，均等价于为所有子规则配置了该参数。
* DOMAIN-SET 规则集也支持配置 extended-matching。

**Minor Optimizations**

* MITM 时发送签名所使用的证书（证书链），以支持使用 intermediate 证书作为签发证书。
* 行首与行末注释，现在可以随意使用 `#` `//` `;` 等三种常见写法
* 配置文件错误消息提示优化，现在它可以更准确地给出发生错误的确切行号。
* 优化 Surge Ponte 错误处理流程，修正某些错误下不会自动更新设备信息的问题
* Bug 修正。

<https://dl.nssurge.com/mac/v5/Surge-5.4.1-2495-041f47425e9ecf56580562ce01560448.zip>

#### 版本 5.4.0

**新功能**

* 协议嗅探

  发往 80 与 443 端口的请求，会等待客户端发送第一个数据包后，提取 SNI 等信息用于规则系统判断。

  * `DOMAIN`、`DOMAIN-SUFFIX`、`DOMAIN-KEYWORD` 规则新增可选参数 `extended-matching`。开启该参数后，该规则将同时尝试匹配 SNI 和 HTTP Host Header （或 :authority）中的字段。
  * 新增参数 `always-raw-tcp-hosts`，用于强行关闭对特定主机名的主动协议探测。
* 新代理协议支持：Hysteria 2

  Hysteria 2 是一个为不稳定和容易丢包的网络环境所优化的代理协议，基于 UDP/QUIC。
* 自动 QUIC 阻止

  由于大部分代理协议并不适合用于转发 QUIC 流量，现在 Surge 会自动阻止 QUIC 流量使其回退 HTTPS/TCP 协议，以保证性能，对于命中了 MITM 主机名的 QUIC 流量，同样将自动拒绝。
* QUIC 类协议的 ECN (Explicit Congestion Notification) 支持

  显著改善了 Vector(Surge Ponte)/TUIC/Hysteria 2 协议的性能表现。

**优化**

* 重新设计了 HTTP 捕获功能
  * 相关设置不再存储在配置中，`[Replica]` 部分已被弃用。
  * 在打开捕获开关后增加了一个自动关闭设置，可以根据时间、大小或请求次数自动停止捕获。
  * 在打开捕获开关后增加了自动激活 MITM，可以额外为特定主机名打开。 (即使主 MITM 开关关闭)。
  * 增加了在打开捕获开关后仅保存 HTTP/HTTPS 请求的选项。
* 提高了与某些非标准协议的兼容性。
* 在测试 Ponte 策略时，测试 URL 已从 `proxy-test-url` 更改为 `internet-test-url`。
* 按照 WireGuard 协议标准推荐，现在 WireGuard 握手数据包将被标记为 0x88 (AF41) DSCP 以提高成功率。
* 当通过 WireGuard 转发 UDP 数据包时，它支持保留隧道内数据包的 TOS(DSCP/ECN) 标签。
* 根据 WireGuard 协议标准推荐，Surge 将从隧道内的数据包复制 ECN 标签到外部数据包。收到带有 ECN 标签的数据包时，它们将根据 RFC6040 严格合并。 (`ecn=true` 必须为策略设置)。
* UDP NAT 可以根据 ICMP 消息提前关闭 UDP 会话。
* 改进了 QUIC 的 PMTU 支持。

**Bug 修复**

* 修复了规则集的外部资源需要重新加载才能在更新后生效的问题。
* 在网络切换后，它将强制断开原始的 DoH/DoQ/DoH3 长连接，以避免获得不适合当前网络环境的结果。
* 修复了无效证书可能导致密钥存储界面崩溃的问题。
* 在对直接使用 IP 地址进行连接的 HTTPS 请求执行 MITM 时，不应将 IP 地址发送为 SNI，因为这可能导致兼容性问题。
* 其他 bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.4.0-2470-d6f513ab6e647abc29490f1f3506667f.zip>

#### 版本 5.3.2

* Surge Mac 现已准备好支持 macOS Sonoma。
* 外部资源现在可以由 Surge iOS 远程管理和更新。
* 修复了位置权限请求不能正确触发的问题。
* Surge Web 仪表板升级到版本 2.0.4。
* 其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.3.2-2393-f4b3e5e9a7bc5b73106ace7b0776eefe.zip>

#### 版本 5.3.1

* Surge 仪表板现在可以直接为本地和远程 Surge 实例创建临时规则。
* Surge Web 仪表板现已升级到版本 2.0。
* 添加了 Inline Ruleset，允许直接在主配置文件中编写 Ruleset。
* 模块增强。模块现在可以操作 \[WireGuard \*] 和 \[Ruleset \*] 部分。
* 添加了用于获取 CA 证书（DER 格式）的 HTTP API：GET /v1/mitm/ca。
* 修复了 MITM 失败记录无法正确生成的问题。

<https://dl.nssurge.com/mac/v5/Surge-5.3.1-2383-066f883d96a472655c9ea7be50475b8b.zip>

#### 版本 5.3.0

* 现在您可以直接通过 Surge Ponte 访问已注册设备的远程仪表板。
* Surge 仪表板现在可以操作远程设备的策略组和出站选项。
* macOS Sonoma 现在需要位置权限以获取 SSID。如果使用相关规则和子网设置，Surge 将提示位置权限。
* 修复了策略组的覆盖不能被远程取消的 bug。
* 更正了 VIF 和特定设备之间的兼容性问题。
* Surge Ponte 改进。

<https://dl.nssurge.com/mac/v5/Surge-5.3.0-2375-bc1b4791973df9aba493c3190a7b0050.zip>

#### 版本 5.2.3

* 您现在可以基于现有的配置文件创建一个新的可修改的配置文件。在这个新的配置文件中，选中的部分将引用原始配置文件中的相应内容，并自动与原始配置文件同步。同时，新配置文件中未选中的部分可以自由修改，不受原始配置文件的影响。（用于分离配置文件功能的 UI。）
* 分离的配置文件现在可以包括企业配置文件。
* 修复了当 SSH 服务器配置了横幅时无法连接的问题。
* 您现在可以使用 UI 来编辑 ShadowTLS 参数。
* 优化 ARM64 架构下的 VIF v1 模式的性能。当 VIF 模式设置为自动时，新版本将在 M1/M2 处理器下自动使用 v1 引擎，最大性能为 \~8Gbps，从而避免兼容性和稳定性问题。
* 纠正了 Dashboard 主窗口的打开位置可能不正确的问题。

<https://dl.nssurge.com/mac/v5/Surge-5.2.3-2354-ce8606235be8df196c0e9619a9c8cbbd.zip>

#### 版本 5.2.2

* 修复了在没有有效网络时可能会有关于系统代理设置被其他应用程序修改的错误提示的问题。
* 修复了使用 TUIC v5 作为底层代理时可能出现的一些问题。
* 修复了当启用 WebSocket 时，如果直接使用 IPv6 地址作为 vmess 主机名，无法正确构建 WebSocket 请求的问题。
* 当 SOCKS5 服务器不支持 UDP 转发时，提供更清晰的错误提示。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.2.2-2340-74b1e55a52888040394976468a61d973.zip>

#### 版本 5.2.1

* Surge Ponte 现在可以在 NAT 类型不满足要求时以 LAN-only 模式工作。同一 LAN 上的设备仍然可以访问。
* 在上一个版本中添加的连接限制器机制已被暂时移除。
* 优化设置为系统代理功能的逻辑。
* 修复了一个内存泄漏问题。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.2.1-2333-ef97cd79e935d838387dc99712fb38b3.zip>

#### 版本 5.2.0

* 由于 macOS 网络栈内存的大小固定，当网络栈缓冲区耗尽时，内核将自动关闭占用最高的程序以释放资源。使用 Surge 接管 P2P 下载器时可能出现这个问题。此版本将自动检查此问题并自动进入安全模式。
* Surge VIF 引擎已升级至 v3，不再依赖 Packet Filter (pf)，解决了与虚拟机和网络共享功能的兼容性问题。同时，增加了连接数限制，以避免由过多并发请求导致的系统资源耗尽。
* 为单个进程和单个设备添加了连接限制器，以避免个别设备消耗大量资源。
* 支持 QUIC 的 PMTU 发现，提高了 Surge Ponte 和 TUIC 协议的性能。
* 优化了基于 QUIC 的协议的错误处理逻辑。
* 使用 TUIC v5 转发 UDP 数据包时，遵循 IP 数据包的 DF 标志。避免了使用 TUIC v5 访问 QUIC 网站时可能出现的问题。
* 其他 bug 修复和优化。

<https://dl.nssurge.com/mac/v5/Surge-5.2.0-2302-721d7db5429609c5a54af922f045a509.zip>

#### 版本 5.1.1

* 增加了对 TUIC v5 协议的支持。
* 优化了 Surge Ponte/TUIC 的性能。
* 当策略组异常时，优化了请求 Note 的记录。
* 修复了在 MITM H2 模式下未正确进行连接复用的问题。
* 修复了 $httpClient/DoH 的请求可能有时会被误取消的问题。
* 调整了 Snell v4 协议的流量特性。
* 其他 bug 修复和优化。

<https://dl.nssurge.com/mac/v5/Surge-5.1.1-2264-6f04d8ac1bbf1c91178a09124e45e37e.zip>

#### 版本 5.1.0

**Surge Ponte**

* Surge Ponte 支持跨 iCloud 账户共享。
* 修复了通过 Surge Ponte 或 TUIC 协议访问 HTTP/1.0 服务器时可能出现的问题（例如 ASUS 路由器管理页面）。

**界面**

* 图标库：您现在可以从约 7000 个图标的库中为您的设备选择图标。

**代理协议相关**

* 修复了 Snell V4 下复用功能无法正常工作的问题。
* SSH 协议现在支持服务器公钥指纹 pinning，查看手册以获取使用方法。

**脚本**

* $httpClient 支持二进制模式。
  * 请求的 body 支持 TypedArray。
  * 在请求参数中传入 binary-mode: true 允许返回结果作为 TypedArray 返回。
* 修复了 `http-request` 类型脚本无法直接使用二进制数据作为响应的问题。

**其他**

* 策略组添加了参数 `external-policy-modifier`，可用于调整外部策略。
* 优化了请求日志系统
  * 在日志中添加了类别标记。
  * 规则系统为 DNS 和规则集添加了更多输出。
* 其他 bug 修复和优化。

<https://dl.nssurge.com/mac/v5/Surge-5.1.0-2216-82115a08df678cfa87137a506f7df061.zip>

#### 版本 5.0.3

* 为 VMess 协议添加了 UDP 中继支持
  * 由于 VMess 服务器端默认支持 UDP 转发，因此无需添加额外参数即可使用。
  * 由于 VMess 协议的设计缺陷，当使用 VMess 转发 UDP 流量时，P2P 场景可能无法工作，如语音通话、在线游戏等。因此，不建议使用 VMess 协议。
* SSH 协议现在支持指定服务器的公钥指纹。查看手册获取更多信息。
* 现在通过 STUN 协议获取外部 IP 地址，不再依赖 api.my-ip.io。
* DDNS 现在在选择 IPv6 时使用安全的 IPv6 地址而非临时地址。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.0.3-2199-c241935acf37b3ec7f7fa4f5120e8690.zip>

#### 版本 5.0.2

* 由于 macOS 的新隐私限制，如果使用了与 Wi-Fi BSSID 相关的功能，Surge 将请求位置服务权限以读取 Wi-Fi BSSID。
* 现在支持 Shadow TLS v3。附加 `shadow-tls-version=3` 以启用它。
* Surge Mac 现在支持 Adaptive TLS Fingerprint。有关更多信息，请查看社区线程。
* 支持了一个新参数 `external-policy-modifier`，用于修改外部策略的参数。
* 新的代理客户端通知只有在接收到真正的请求时才会提示，被端口扫描时将不再显示。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.0.2-2186-2ab1aba0dc49688683b2e4d43200e468.zip>

#### 版本 5.0.1

* 当 Ponte 开关关闭时，现在可以查看已注册的 Ponte 设备视图。
* 修复了通过 USB 使用 Surge Dashboard 时的崩溃。
* $httpClient 现在支持二进制模式。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.0.1-2162-22743a4d2f1e0aeb0b872e8f544c2e69.zip>

### Surge Mac v4

#### Version 4.11.2 (May 6, 2023)

* Replace the API service provider for obtaining external IP.

<https://dl.nssurge.com/mac/v4/Surge-4.11.2-2016-b4c9dad3472594b01ef3d8ac9b05c78e.zip>

#### Version 4.11.1 (Apr 15, 2023)

* Fixed a bug that Surge VIF v6 may not be enabled automatically when set to auto.
* Fixed a bug that requests sent by $httpClient may not obey the ip-version parameter of the selected policy.
* Fixed a bug that DDNS can’t be enabled if the user deleted the iCloud data of Surge.
* Fixed a bug that domain rules can’t match if the requests’ domain is in uppercase.
* Fixed a bug that the UI can’t add listeners in the advanced proxy service settings.
* Fixed a bug that the UI can’t add new items in the metered network SSID view.
* Fixed a WireGuard related crash.
* Other bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.11.1-2013-eac717436d753b5ea2b82a206d5851e7.zip>

#### Version 4.10.3 (Feb 16, 2023)

* The installed modules are now synced between Mac devices via iCloud.
* Performance optimization.
* Fixed an issue that the DHCP service might not be able to start after auto-upgrading.
* Fixed an issue that the remove helper script can't be executed on macOS Ventura.
* Fixed menu bar icon issues when using multiple displays.
* WireGuard related optimizations.
* Support for customizing the reserved bits of WireGuard, also known as the client ID or routing ID.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.10.3-2004-d730cb305e3cbb949f82d01771624b4e.zip>

#### Version 4.10.2 (Feb 3, 2023)

* UDP performance optimization.
* Change the way connections are rejected from ICMP to TCP RST. This ensures that the Windows operating system can correctly detect the rejection.
* Fixed the proxy editing view layout issue.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.10.2-1981-d99d487bbd9f9109a00dd5a5b7915be4.zip>

#### Version 4.10.1 (Dec 3, 2022)

**New Feature**

* Gaming Optimization Mode: `udp-priority = true`. Enabling it will prioritize UDP packets when the system load is very high, and packet processing is delayed.
* SOCKS5 proxy now supports UDP forwarding, as the server side does not consistently support UDP forwarding, the parameter udp-relay=true needs to be explicitly configured.
* The `ipv6-vif` parameter now supports `always` and `auto` like Surge iOS. If set to `auto`, IPv6 VIF will only be enabled if a valid Internet IPv6 address (2000::/3) exists.

**Minor Improvements**

* URL regular expressions for Script, Rewrite, Mock, etc. will try to match URLs constructed in many different ways (e.g. Host field in Header) to solve the problem that some apps use custom DNS logic to request directly to IP addresses.
* Removed the silencing mechanism after UDP forwarding errors to avoid extra waiting time after switching networks.
* The IPv6 switch no longer prevents direct access to IPv6 addresses when turned off. The switch is now limited to controlling whether the DNS Client requests AAAA records.
* Automatic disabling of AAAA queries due to DNS issues will be prompted in the Event Center instead of just in the logs.
* Fixed handling issue of generating IPv6 fragmentation when forwarding IPv6 UDP packets via WireGuard.
* The external policy group will skip the line and continue processing when it encounters invalid content instead of returning an error directly.
* Adjusted the buffering mechanism of raw TCP forwarding to avoid conflicts with some apps.
* Fixed REJECT requests not being marked as failed under MITM H2.
* Adjusted the output text under diagnostics.
* Other bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.10.1-1964-34ee4f3efbd20065ad808cf0cab6d380.zip>

#### Version 4.10.0 (Nov 10, 2022)

**Support New Proxy Protocol**

* New proxy protocol supported: TUIC. (<https://github.com/EAimTY/tuic>).
* New proxy protocol supported: Snell V4. (<https://manual.nssurge.com/others/snell.html>)
* New proxy transport layer protocol supported: Shadow TLS. (<https://github.com/ihciah/shadow-tls>). You may append `shadow-tls-password=pwd` to any proxy to utilize it.

**Other Improvements**

* shadowsocks now supports the none cipher.
* Modified the handshake packet construction logic when forwarding HTTPS requests to proxies, which can slightly optimize latency.
* Surge HTTP requests for proxy testing no longer contain a User-Agent header.
* A new option to allow to disable system processes combining in the process view.
* Fixes an issue on M1 processors where the system would move Surge to the efficiency core when using an application in full screen causing a significant drop in performance.

**Bug fixes**

* Fixed a memory leak that could occur when HTTP capturing is enabled.
* Fixed an issue that may not work properly when nesting proxy chains with a specific protocol combination.
* Fixed an issue that the module could not configure the MITM h2 parameter.

<https://dl.nssurge.com/mac/v4/Surge-4.10.0-1927-f009d35c5da9df00cccf818edd74b20d.zip>

#### Version 4.9.1 (Sep 29, 2022)

* Overall performance optimization.
* Added an alert when using router mode in an IPv6 network.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.9.1-1866-e90f4c1609827e5669c21803ac8e90a3.zip>

#### Version 4.9.0 (Sep 11, 2022)

**Router Mode**

* Overall performance optimization.
* Fixed a performance issue with PS5.

**Surge VIF IPv6**

* You may use the parameter `ipv6-vif = always` to let Surge configure IPv6 address and the default route for Surge VIF.
* Surge VIF now supports handling raw TCP and UDP traffic with IPv6.
* ICMPv6 relay is now supported.

**MITM**

* New parameter `client-source-address`. Use this parameter to enable the MITM function on some devices only.
  * It's a list parameter, using commas as the separator.
  * You may specify a single IP address or use a CIDR block, both IPv4 and IPv6 are supported.
  * You may use the `-` prefix to exclude some clients, e.g., `client-source-address = -192.168.1.2, 0.0.0.0/0`
  * If the parameter is not set, MITM is enabled for all clients. A equivalent to `client-source-address = 0.0.0.0/0, ::/0`
  * `127.0.0.1` should be included if you want to enable MITM for the current device.

**WireGuard**

* WireGuard now supports IPv6 tunneling.
  * Use parameter `self-ip-v6` to assign an IPv6 address for Surge.
  * You may configure `self-ip` and `self-ip-v6` to utilize the IPv4 & IPv6 dual stack, or just one of them to use the single stack.
  * Make sure to use the correct `dns-server` address for the enabled IP protocol version.
  * The `allowed-ips` parameter supports IPv6 CIDR now, e.g., `allowed-ips = 0.0.0.0/0, ::0/0`

**Others**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.9.0-1850-c52ab2531bb82ff6f8d72df65f65c76a.zip>

#### Version 4.8.0 (Aug 9, 2022)

**Experimental function: DNS over QUIC and DNS over HTTP/3**

* Surge now supports DNS over QUIC. (e.g.: `encrypted-dns-server = quic://example.com`)
* Surge now supports DNS over HTTP/3. (e.g.: `encrypted-dns-server = h3://example.com/dns-query`)
* Parameter `doh-server` renames to `encrypted-dns-server`.
* Parameter `doh-follow-outbound-mode` renames to `encrypted-dns-follow-outbound-mode`.
* Parameter `doh-skip-cert-verification` renames to `encrypted-dns-skip-cert-verification`.
* The DNS relay (`always-real-ip` and non-A/AAAA record lookup) in the Enhanced Mode now uses the encrypted DNS servers.
* You may use `encrypted-dns-skip-cert-verification=true` to disable server certificate verification for DNS-over-HTTPS.

**Scripting**

* New helper functions: `$utils.ipasn(ipAddress<String>)`, `$utils.ipaso(ipAddress<String>)` and `$utils.ungzip(binary<Uint8Array>)`.
* New subtype of the event script: `notification`. You may use a script to forward Surge notifications to a third-party message service.

**Others**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.8.0-1788-3b96ac4d92f39b6a4a8e195708aae8d8.zip>

#### Version 4.7.0 (Jun 30, 2022)

**MITM over HTTP/2**

* Surge now supports performing MITM with HTTP/2 protocol to improve concurrent performance.
* Surge now supports performing MITM on WebSocket connections.

**Others**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.7.0-1757-0b3d1ec3c3f7067386361dd582ad964a.zip>

#### Version 4.6.1 (Jun 10, 2022)

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.6.1-1718-a39555f74c3f6d43fdcaa8501d55d26a.zip>

#### Version 4.6.0 (Jun 8, 2022)

**SSH Proxy Support**

* You can use SSH protocol as a proxy protocol. The feature is equivalent to the `ssh -D` command.
* Both password and public key authentications are supported.
* All the four types of private keys, RSA/ECDSA/ED25519/DSA, are supported.
* Surge only supports `curve25519-sha256` as the kex algorithm and `aes128-gcm` as the encryption algorithm. The SSH server must use OpenSSH v7.3 or above. (It should not be a problem since OpenSSH 7.3 was released on 2016-08-01.)

**Keystore**

* You may now save sensitive keystore items to the system keychain. (More, Profile, Manage Keystore)

**Others**

* New rule type: IP-ASN. You may use the rule to match the autonomous system number of the remote address.
* Dashboard now shows more details about the remote address, including the ASN.
* Surge will try to fix the system proxy settings after applying fails.
* You can now enable/disable the rewrite rules and DNS local mapping items.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.6.0-1708-9ef4eecae3a0cc5dfebd74e5e850cb2f.zip>

#### Version 4.5.2

**Dashboard**

* You can now export HTTP/HTTPS requests to a HAR file, which is a standard format and can be opened by many web analysis tools

**Proxy**

* New parameter `server-cert-fingerprint-sha256` for TLS proxy policies. Use a pinned server certificate instead of the standard X.509 validation.
* `tls-engine` option is now deprecated. OpenSSL is now the only TLS engine.
* You may use `%PROFILE_DIR%` in the external proxy arguments, which will be replaced to the path of the profile directory.
* You can now use a full profile as the external policy group (policy-path). All proxies in the \[Proxy] section will be used.

**DHCP Server**

* Surge DNS is now integrated with the DHCP device management. You can use a device name to get the IP address directly. Reverse IP lookup is also supported.
* The helper upgrade is now optional to prevent the interrupt after an auto-upgrade.
* Surge now can relaunch itself after a crash.

**CLI**

* surge-cli just got a refresh. Use `surge-cli --help` to know what you can do with it.

**Others**

* Header rewrite now supports using the regex to replace the value.
* Header rewrite now supports modifying the response headers.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.5.2-1663-d480512b326806e7e850f98efe875bec.zip>

#### Version 4.5.1

* There is a kernel bug in macOS 12.3, which significantly degrades performance of the Enhanced Mode and Router Mode. A workaround is deployed in this version.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.5.1-1621-c2a973ddb992df5c34757daacc632598.zip>

#### Version 4.5.0

**WireGuard**

* WireGuard supports multiple peers.
* The allowed-ips now support multiple IP ranges.
* WireGuard supports preshared-key and keepalive.
* WireGuard supports peers with IPv6 endpoints. (But still no IPv6 tunnel support)
* WireGuard and shadowsocks policy now support underlying-proxy.
* The raw TCP connections are now relayed on the L3 layer if no high-level features are used.

**Detached Profile**

* You can now include multiple detached profiles into one section. But the section will be marked read-only and can't be edited with UI.

`#!include A.dconf, B.dconf`

**Policy Group**

* You can now temporarily override an auto test group or an SSID group's optimal option, until Surge restart or reload.
* The new parameter include-all-proxies=true is added to the policy group, which will include all proxy policies defined in the \[Proxy] section, and can be used with the policy-regex-filter parameter for filtering.
* The new parameter include-other-group="group1,group2" is added to include policies from another policy group, and can include multiple policy groups separated by commas, also can be used with the policy-regex-filter parameter for filtering.
* include-all-proxies, include-other-group, and policy-path parameters are allowed to be used in a single policy group at the same time. The policy-regex-filter parameter applies to all three.
* There is an order of precedence among the policy groups for the include-other-group parameter, but there is no order of precedence among the include-all-proxies, include-other-group, and policy-path parameters. For scenarios where the order of sub-policies makes sense (e.g., fallback groups), use policy groups nesting with include-other-group.

**Subnet expression**

* SSID Group is now upgraded to Subnet Group, which supports subnet expression.
* SSID Setting now supports subnet expression.
* The SUBNET rule now supports subnet expression.
* A subnet expression can be one of these:
  * Use SSID:value to match the Wi-Fi SSID, wildcard character is allowed.
  * Use BSSID:value to match the Wi-Fi BSSID, wildcard character is allowed.
  * Use ROUTER:value to match the router IP address.
  * Use TYPE:WIFI to match all Wi-Fi networks.
  * Use TYPE:WIRED to match all wired networks.
  * Use TYPE:CELLULAR to match all cellular networks. (iOS Only)
  * Use MCCMNC:100-200 to match a cellular network. (iOS Only)
* The \[SSID Setting] can control the TCP Fast Open behavior now. Read the manual for more information.

**Others**

* Performance improvements.
* The default timeout of $httpClient is 5 seconds now.
* New Official Module: Block HTTP3/QUIC
* You can now adjust the effective order among modules.
* Modules allow to modify the skip-server-cert-verify and tcp-connection parameters of \[MITM].
* The client will get an ICMP connection refused message instead of TCP RST if a REJECT policy matches.
* Supports IPv6 addresses with scope ID.
* The Network diagnostics can test proxy UDP relay now.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.5.0-1618-5d2042223762269c5322520810dd7e0c.zip>

#### Version 4.4.1

* You may click a proxy of a select group in the main menu with holding the Option key, to test the proxy alone.
* Fixed a bug that UDP NAT can't be released if a REJECT policy is matched.
* Other bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.4.1-1532-abe4b5471dcb3eaeec51fcda768cc635.zip>

#### Version 4.4.0

* Uses Surge as a WireGuard client, converting L3 VPN as an outbound proxy policy. More information: <https://manual.nssurge.com/policy/wireguard.html>
* Supports VmessAEAD. (Policy parameter: vmess-aead = true)
* Trojan protocol now supports UDP relay. (No additional parameter required)
* The underlying proxy now supports using a policy group.
* Performance optimization.
* Added a release note window to show update history.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.4.0-1521-a0024e9fbe33f5ccaa41316d63cdefee.zip>

#### Version 4.3.1

* Snell Protocol v3, which brings UDP over TCP relay support
  * Optimized for high throughput.
  * Port Restricted Cone NAT support. (aka NAT type 2)
* The http-response scripts can read request headers via $request.headers now.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.3.1-1461-829471a307259fe1729cf06a7cd13d06.zip>

#### Version 4.3.0

* Surge Dashboard now supports managing DHCP devices. All of the properties (name, icon, static IP address, gateway mode) can be edited locally and remotely.
* The traffic statistics data is now persistent between sessions. And you may use Dashboard to view all the detailed statistical data.
* The statistics data range is extended to 24 hours.
* Performance improvements.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.3.0-1430-bde27671bfdadfab143338a7cd5b2fa3.zip>

#### Version 4.2.5

* Performance improvements.
* Supports remote rule editing for Surge iOS remote controller.
* Kill other processes that take over port 53 when starting DHCP service.
* Surge now only executes reloading if the profile is valid.
* Supports custom the policy IP TOS field. Example: test-policy = direct, tos=0xb8.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.5-1414-764146258a319c307056593a1309cf89.zip>

#### Version 4.2.4

* New option: Menubar icon display mode. You can now hide the icon and display the real-time speed only, to save the precious menubar space.
* New HTTP API: GET /policies/benchmark\_results
* Supports IP Fragmentation for UDP and ICMP packets. (IP Fragmentation for TCP packets is already supported in the previous versions.)
* You can now right click on a remote client to add a new rule in the Dashboard.
* Performance improvements.
* Added a few device icons.
* The UI editor of policy group now supports filter and mixed policies.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.4-1399-4f3c53abfe45fce5646d84af11e589c4.zip>

#### Version 4.2.3

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.3-1357-0803594c82248360a95722089650f7f7.zip>

#### Version 4.2.2

* Supports binary mode for http-request and http-response scripts.
* DHCP can detect if a device is private address enabled now.
* Surge won't reload the profile automatically if the new profile is invalid.
* New local and remote notification selections: auto-updating and profile reloading.

<https://dl.nssurge.com/mac/v4/Surge-4.2.2-1351-5dc813192d6e37fdb0895034ebc90b57.zip>

#### Version 4.2.1

**External IP**

* You may now check the external IP address in the interfaces view.

**DDNS**

* Surge Mac can associate its external IP address to .sgddns hostname. You may use the hostname with Surge iOS or Surge Mac on another device. The data is synced via iCloud, and the hostname can't be used publicly.

**Others**

* Surge Mac now can fix the helper installtion issues automatically。

<https://dl.nssurge.com/mac/v4/Surge-4.2.1-1333-14f7cb7cd943be7e4b3cecfb3fcd8ba3.zip>

#### Version 4.2.0

**Web Dashboard**

* The community project YASD is now part of Surge. You can now control Surge via a web browser on local or remote devices. (Licensed by author @geekdada)
* You may now manage the DHCP devices with the Web Dashboard.

**Profile Syntax**

* We have added a profile syntax view to show all the available syntax for the current view if you prefer to edit profile with a text editor. You can find it in Help ▸ Profile Syntax.
* The Diagnostics now can report invalid config lines in the profile.

**Benchmark**

* We have changed the proxy benchmark standard. The result is now similar to a ping test result, which ignores the proxy setup cost.

**Minor Improvements**

* SOCKS proxy service now supports SOCKS4 and SOCKS4a protocol. (Server-side only)
* Cloud Notifications now supports rule notifications.
* The real-time speed is now available on the proxy view.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.0-1321-d4d84696bb58cf8be0189b59ccbe926b.zip>

#### Version 4.1.0

**Scripting**

* You may configure and edit scripts with UI now.

**Profile**

* You may put partial sections into a detached file. See <https://manual.nssurge.com/overview/configuration.html>

**HTTP API**

* Added new profile related HTTP APIs, including GET /profiles, POST /profiles/check
* Added new device management HTTP APIs, including GET /devices, POST /devices, GET /devices/icon
* The HTTP API, proxy services, and external controller now support listening on IPv6 addresses. (No UI supports. Manual profile editing is required.)
* You may now use 'http-api-tls=true' enable TLS for HTTP API access. (aka HTTPS-API)

**Unsupervised Optimizations**

* The external resources downloading now occurs after surge engine started.
* The external resources downloading now automatically starts after if a resource is not ready.

**Other Improvments**

* New rule type: SUBNET, which can match SSID/BSSID/router IP address with a wildcard pattern.
* Significantly optimizes Dashboard performance when handling large numbers of requests.

<https://dl.nssurge.com/mac/v4/Surge-4.1.0-1298-f07b1b8713b2397518f4b252b5786452.zip>

#### Version 4.0.5

**Policy Group**

In this release, we completely refactored the policy group functionality, bringing the following changes:

1. The url-test/fallback/load-balance policy group can no longer be configured with a specific testing URL but with a global testing URL or a policy-configured testing URL. The policy's test results can be used directly in all policy group decisions, eliminating the need to retest each policy group individually.
2. All types of policy groups support mixed nesting. The only requirement is that no circular references can be used.
3. When a group policy is used as a sub-policy of the url-test/fallback/load-balance group.
   * The latency of the select/url-test/fallback/ssid group is the latency of the selected policy.
   * The latency of the load-balance group is the average of the latencies of all available policies.
4. The timeout parameter of a policy group marks policies with latency exceeding this parameter as unavailable when making decisions for the group. But the maximum time taken to test the policy group is controlled by the global test-timeout parameter. (Default is 5s)
5. When testing a group due to decision making, all sub-policies that the group may use are tested, including sub-policies of the sub-policy group.
6. You may use no-alert=true parameter to suppress notifications for particular groups.

**Cloud Notification**

You can receive the notifications on iOS devices. Enable this option first and then configure it on Surge iOS. The two device must use a same iCloud account.

**Minor Changes**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.5-1262-db70f680cd0f15236c8415ec7b804c3a.zip>

#### Version 4.0.4

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.4-1227-9acb8b9e3f39e9048fc82e427184a4af.zip>

#### Version 4.0.3

* You may override the testing URL of a policy for network diagnostics and activity cards.
* The GeoIP database can be updated automatically in the background.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.3-1224-4ef8ae10c8a74c395bb4b6c3f6af6af6.zip>

#### Version 4.0.2

* You may now customize the GeoIP database updating URL.
* tun-excluded-routes and tun-included-routes are now available for Surge Mac.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.2-1219-dbd08724b90aa8b444cd6d0679a245b5.zip>

#### Version 4.0.1

* You may configure the proxy chain with the UI now.
* Fixed some visual inconsistency under reducing transparency mode.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.1-1207-ee7bea1b244950c82a6f90e060fa2d89.zip>

#### Version 4.0.0

* The first version of 4.0.0.

<https://dl.nssurge.com/mac/v4/Surge-4.0.0-1191-d8140b0084223fd3fc4335e4414c0884.zip>

### Surge Mac V3

#### Version 3.5.8

* Bug fixes

<https://dl.nssurge.com/mac/v3/Surge-3.5.8-1130.zip>

#### Version 3.5.7

* Bug fixes

<https://dl.nssurge.com/mac/v3/Surge-3.5.7-1129.zip>

#### Version 3.5.5

**Minor Changes**

* All URL resources now support URLs with a username and password (e.g. <https://user:pass@example.com>), including managed profile, external resources, and importing profile form URL.
* You may switch among the main views with shortcut keys.
* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.5.5-1123.zip>

#### Version 3.5.4

**Changes in Policy Group**

* New parameter: policy-regex-filter. If the parameter is configured, only matched policy line will be used.

**Minor Changes**

* Provides more details for the TLS handshake error.
* Increases the file description limitation alert threshold.

<https://dl.nssurge.com/mac/v3/Surge-3.5.4-1119.zip>

#### Version 3.5.3

**New Parameter: use-local-host-item-for-proxy**

`[General]`

`use-local-host-item-for-proxy = true`

If use-local-host-item-for-proxy is true, Surge sends the proxy request with the IP address defined in the \[Host] section, instead of the original domain.

**Changes in Load Balance Group**

* load-balance group now supports connectivity testing before being used. Add 'url' parameter to enable it.
* Parameters 'timeout', 'interval' and 'evaluate-before-use' are also available.

**Minor Changes**

* Surge will send an ICMP port unreachable message if UDP forwarding fails.
* Eliminate unnecessary local DNS lookup while forwarding UDP traffic to a proxy server.
* Fixed a bug that connecting to Surge iOS via USB is not working in Surge Dashboard.

<https://dl.nssurge.com/mac/v3/Surge-3.5.3-1094.zip>

#### Version 3.5.2

**SSID Suspend**

* Surge Mac supports SSID suspend now. The system proxy and enhanced mode will be temporarily suspended under specified SSIDs.
* The name of WiFi can be an SSID, a BSSID, or a gateway IP address.
* No UI configuration in the current version.

**REJECT-DROP**

* REJECT-DROP policy is now effective to proxy connections. The connections matched with a REJECT-DROP policy will be closed in 60-120s later without any data returned.

**Global Proxy**

* You may now select and view sub-policy for policy groups while using the global proxy mode.

<https://dl.nssurge.com/mac/v3/Surge-3.5.2-1082.zip>

#### Version 3.5.1

**New rule type: DOMAIN-SET**

* DOMAIN-SET is just like RULE-SET. But it is designed a large number of rules and highly efficient.
* Unlike RULE-SET, you can only write hostnames (domain or IP address) in it. One hostname per line.
* You may use "." prefix to include all sub-domains.

**Changes in SRC-IP**

* SRC-IP rule now supports IP-CIDR for both IPv4 and IPv6.

**Changes in DNS over HTTPS**

* From this version, if DNS-over-HTTPS is configured, the traditional DNS will only be used to test the connectivity and resolve the domain in the DOH URL.
* The DNS over HTTPS now has a separate parameter: doh-server. The DOH servers in 'dns-server' will be moved to the new parameter after saving.
* The legacy DNS is always required now.
* DOH can be matched with rule 'PROTOCOL,DOH' now.
* Added a new parameter 'doh-follow-outbound-mode'. In the previous version, the DOH client follows the system proxy settings. From this version, all DOH requests will use DIRECT policy by default. If 'doh-follow-outbound-mode' is set, the DOH requests will follow the outbound mode settings regardless of the system proxy settings.
* We are refactoring the HTTP client for DOH and scripting. Please feedback if you encounter any issue.

**Changes in Scripting**

* Added a simple view to test the script. You may find it in the Window menu.

**Minor Changes**

* Fixed a crash in Dashboard while using search.
* Bug fixes.

**Known Issues**

* You may not configure DOH with UI in this version temporarily.

<https://dl.nssurge.com/mac/v3/Surge-3.5.1-1069.zip>

#### Version 3.5.0

* New feature: Module, which can override the current profile with a set of settings. Highly flexible for diverse purposes. See the post in the community for more information: <https://community.nssurge.com/d/225-module>.
* You may enable modules in the menu now.
* You may view the detail of a module by double clicking.
* Supports pattern filter for Dashboard requests.
* Added a new rule type: PROTOCOL. The possible values are HTTP, HTTPS, SOCKS, SNELL, TCP, UDP.
* You may now use UI to add and edit load-balance group.
  * DNS over HTTP (DoH) now uses DNS wireformat by default. You may configure doh-format=json in \[General] to continue using JSON format.
  * TCP connection setup optimizations.
  * Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.5.0-1039.zip>

#### Version 3.4.0

* Snell protocol now upgrade to version 2, supporting to reuse TCP connections to improve performance. <https://github.com/surge-networks/snell/releases>
* Supports a new proxy protocol: Trojan.
* Remote Dashboard now upgraded to Remote Controller. You may use Surge iOS to select policy group, toggle HTTP capture/MitM, and switch outbound mode remotely.
* The comment lines in the text config won't lost after editing with UI.
* You may open the new connection window of Dashboard by holding the Option key while clicking the Dashboard item in the main menu.
* Supports to use OpenSSL as TLS provider. See the post in the community for more information: <https://community.nssurge.com/d/196-surge-ios-mac-tls-provider>.
* Fixed a bug that Surge may not be able to process DNS answer packets which is longer than 512 bytes.

<https://dl.nssurge.com/mac/v3/Surge-3.4.0-989.zip>

#### Version 3.3.3

* Fixed a bug which causes TFO failed.
* You may use a profile which stores in a subdirectory of the profile directory.
* Added Traditional Chinese localizations.
* Fixed a bug that the menu might be unresponsive.
* Fixed crashs on macOS 10.11.

<https://dl.nssurge.com/mac/v3/Surge-3.3.3-939.zip>

#### Version 3.3.2

* Supports MITM on non-standard port for TCP mode.
* Proxy editing view now supports VMess protocol and all misc options.
* A new option 'persistent' has been added to the load-balance group. (aka PCC, per connection classifier) When 'persistent=true' is set, a same hostname will always get the same policy.
* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.3.2-925.zip>

#### Version 3.3.1

* Supports VMess proxy protocol.
  * vmess-proxy= vmess, example.com, 443, username = 12345678-abcd-1234-1234-47ffca0ce229, ws=true, tls=true, ws-path=/v2, ws-headers=X-Header-1:value|X-Header-2:value
  * All proxy options for TLS proxy are available.
  * Web-socket and TLS options would degrade performance. Only enable when necessary.
  * Surge only supports chacha20-poly1305 encryption algorithm. Please make sure the server supports it. We have no plan to implement other ciphers.

<https://dl.nssurge.com/mac/v3/Surge-3.3.1-906.zip>

#### Version 3.3.0

* The scripting has been rewritten totally. The old scripts are not compatible with this version. See <https://community.nssurge.com/d/33-scripting/3>
* Added support for TLS 1.3. Append 'tls13=true' to the proxy line to enable it. (Requires macOS 10.14 or above)
* Supports to use 'X-Surge-Policy' to force policy for HTTP/HTTPS requests.
* SSID group now supports to use the IP address of default router as an identifier.
* New policy group type: load-balance, which will use a random sub-policy for every request.
* Supports DNS over HTTPS. More information in community: <https://community.nssurge.com/d/48-dns-over-http>
* IN-PORT and DEST-PORT rule now supports port range expression: `DEST-PORT,8000-8999,DIRECT`
* Provides compatibility for Surge iOS 4.
* Surge Mac software package is now notarized by Apple.
* A new standalone view to manage all external resources.

<https://dl.nssurge.com/mac/v3/Surge-3.3.0-893.zip>

#### Version 3.2.1

* Fixed a bug that Handoff doesn't work between Surge iOS and Dashboard.
* Fixed a bug that 'Update All Remote Resources' may not work.

<https://dl.nssurge.com/mac/v3/Surge-3.2.1-863.zip>

#### Version 3.2.0

**Scripting**

* New major feature: scripting. You may use JavaScript to modify the response as you wish. See the manual for more information: <https://manual.nssurge.com/http-processing/scripting.html>
* You can now use a script to modify the response headers and status code.

**Dashboard**

* USB module has been refactored to improve stability. Also, you may choose the device from multiple USB devices now.

**MitM**

* HTTP and MitM engine has been refactored. Please report if you encounter any issues.
* You can now use URL-REGEX rule for MitM connections.
* You may use prefix '-' to exclude domains for MitM. Example:

```
[MITM]
hostname = -*.apple.com, -*.icloud.com, *
```

* MitM hostname list now supports port number. By default only the connections to port 443 will be decrypted. Use suffix :port to enable MitM for other ports. Use suffix :0 to enable MitM for all ports on the hostname.
* URL rewrite type 'header' is now available for MitM connections. You may also use it to rewrite a plain HTTP request to an HTTPS request.

**Misc**

* You can now enable/disable a rule.
* Added a small indicator in the menu icon for Metered Network Mode.
* Added main switches for rewrite and scripting.
* Supports TCP SACKs for Surge VIF.
* New general option: force-http-engine-hosts. You can force Surge to treat a raw TCP connection as an HTTP connection, to enable high-level functions such as URL-REGEX rules, rewrite and scripting. This option uses the same format as \[MITM] hostname option.
* New option for url-test/fallback group: evaluate-before-use. By default, the requests before a connection evaluation will use the first policy in the list and trigger the evaluate. Enable the option to delay the requests until the evaluation completed.

<https://dl.nssurge.com/mac/v3/Surge-3.2.0-860.zip>

#### Version 3.1.1

* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.1.1-811.zip>

#### Version 3.1.0

* Added more feature to the main menu.
* Dashboard now supports to export all requests to an archive file for opening later or sharing.
* Supports a new proxy protocol: Snell. (<https://github.com/surge-networks/snell>)
* Surge Mac can work as a Snell proxy server now. See <https://manual.nssurge.com/others/snell-server.html> for more information.
* A new option to automatically reload if the profile was modified externally/remotely.
* Fixed a compatibility issue with some FTP clients.
* Added a new option to disable automatically notification dismissing.
* The update notification is now shown as a banner instead of an alert window.
* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.1.0-807.zip>

#### Version 3.0.6

* Optimizations for no network error handling.
* Reduces CPU usage on idle.
* Fixed a bug while enabling MitM with a new certificate.
* Fixed crashes on macOS 10.11.

<https://dl.nssurge.com/mac/v3/Surge-3.0.6-781.zip>

#### Version 3.0.5

* CPU usage optimizations (50% reduced for high throughout).
* Enabled Hardened Runtime to get enhanced security protections in macOS Mojave.
* Add more notes for rule evaluating stage.
* WeChat.app may flood ping when network is unstable, which causes a high CPU usage of Surge. We added a mechanism to limit ICMP throughput in this version.

<https://dl.nssurge.com/mac/v3/Surge-3.0.5-773.zip>

#### Version 3.0.4

* Added a new option 'hijack-dns' to hijack DNS queries to other DNS servers with fake IP addresses. See manual for more information: <https://manual.nssurge.com/others/misc-options.html>.
* Bug fixes

<https://dl.nssurge.com/mac/v3/Surge-3.0.4-759.zip>

#### Version 3.0.3

* Supports new iCloud container for Surge iOS migration.
* The MitM feature is now compatible with Android system. Please regenerate an new CA certificate before using with Android.
* Fixed some UI issues in Dashboard.
* Fixed a bug that MitM may refuse to enable after modifying settings.
* Fixed a bug that br decompress may fail.
* Fixed a bug that the menu item may use a wrong color if the accent color of system isn't blue.
* Fixed the JSON viewer color issue in the Dark Mode.
* Minor bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.0.3-754.zip>

#### Version 3.0.2

* Allows import the profile from a URL.
* Fixed an issue that the HTTP capture button may show wrong state in Dashboard.
* Fixed an issue that Dashboard doesn't show User-Agent as the process name while connecting to iOS device.
* Fixed an issue that the bandwidth of processes may be inaccurate.
* Fixed an issue that the DEST-PORT rule may not be parsed.
* Fixed an issue that ruleset can't be used with logical type rule.

<https://dl.nssurge.com/mac/v3/Surge-3.0.2-736.zip>

#### Version 3.0.1

* Fixed an issue that TFO option will not be saved.
* Fixed an issue that UDP relay option shows wrong state.
* Fixed some i18n issues.
* Fixed crashs on macOS 10.11.
* Save proxy declarations with legacy style (custom) if the proxy is written in legacy style in the text file.
* Other minor bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.0.1-711.zip>

#### Version 3.0.0

<https://dl.nssurge.com/mac/v3/Surge-3.0.0-702.zip>

### Surge Mac V2

#### Version 2.6.7

* Fixed a compatibility issue with 304 response.
* Fixed a Dashboard crash.

<https://dl.nssurge.com/mac/Surge-2.6.7-656.zip>

#### Version 2.6.6

* Fixed a compatibility issue with 304 response.
* Fixed an issue that Dashboard may not use the correct encoding to decode text body.

<https://dl.nssurge.com/mac/Surge-2.6.6-654.zip>

#### Version 2.6.5

* Bug fixes.

<https://nssurge.com/mac/Surge-2.6.5-652.zip>

#### Version 2.6.4

* Bug fixes.

<https://nssurge.com/mac/Surge-2.6.4-647.zip>

#### Version 2.6.3

* New Features: External Proxy Provider. See <https://medium.com/@Blankwonder/surge-mac-new-features-external-proxy-provider-375e0e9ea660> for more information.
* Surge will automatically track system proxy settings now. When Surge is no longer the default proxy, the status icon will turn grey and a notification will raise.
* Fixed a compatibility issue with Docker.

<https://nssurge.com/mac/Surge-2.6.3-637.zip>

#### Version 2.6.2

* Fixed an issue that the UDP mode with AEAD ciphers doesn't work.
* Bug fixes.

<https://nssurge.com/mac/Surge-2.6.2-618.zip>

#### Version 2.6.1

* Surge now allows expired DNS answers for performance reasons. See 'Optimistic DNS' section in <https://developer.apple.com/videos/play/wwdc2018/714/> for more information.
* Performance improvements.
* Fixed an issue that UDP traffics are not included in the real-time speed.
* Supports hardware acceleration for AES-GCM encryption.
* Supports NAT64 in a pure IPv6 network. (Previous versions already supported DNS64)

<https://nssurge.com/mac/Surge-2.6.1-612.zip>

#### Version 2.6.0

* Supports using Surge Mac as a gateway.
* A new setup guide view.
* A new config panel for traffic capture options.
* Fixed an issue which Dashboard may disconnect unexpectedly under huge pressure.
* The status bar icon will be red while traffic capture is enabled.
* Improved TUN interface performance.
* Enabling TCP Fast Open in macOS 10.14.

<https://nssurge.com/mac/Surge-2.6.0-596.zip>

#### Version 2.5.3

* Supports UDP relay for shadowsocks protocol. A brief introduction in Chinese: <https://trello.com/c/ugOMxD3u>.
* You may use Dashboard to view UDP conversations.
* Dashboard now can save multiple remote machine profiles.
* Improved the JSON viewer in Dashboard.
* Added an UI switch for the dns-failed option in FINAL rule.
* Bug fixes.

<https://nssurge.com/mac/Surge-2.5.3-563.zip>

#### Version 2.5.2

* You may toggle the hidden state of columns in Dashboard now.
* Supports to export selected rows to csv file.
* Added a connection duration column in Dashboard.
* Supports obfs-uri parameter.
* Improved the benchmark view.
* Fixed a serious bug in the SOCKS5 proxy implementation.
* Bug fixes.

<https://nssurge.com/mac/Surge-2.5.2-544.zip>

#### Version 2.5.1

* The MitM enabling switch has been moved to the main menu and isolated from profile.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.5.1-528.zip>

#### Version 2.5.0

* Added Outbound Mode options: Direct Outbound, Global Proxy and By Rule.
* Added options for all policy to specify outgoing interface: 'interface' and 'allow-other-interface'.
* Added all\_proxy environment variable for 'Copy Shell Export Command'
* Supports client-side SSL/TLS certificate validation for HTTPS and SOCKS5-TLS proxy. A config example is here: <https://gist.github.com/Blankwonder/cd9fa1987e41cf1a1f1df50583ba1d9c> (DO NOT support editing with UI in this version.)
* Refined MitM.
* Concurrently setup connection to host with Round-robin DNS to boost performance.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.5.0-520.zip>

#### Version 2.4.6

* Supports xchacha20-ietf-poly1305.
* Bug fixes.
* HTTP request header and response header can be extracted from TCP connection now. (SOCKS5 and TUN)
* Enhanced mode can handle all connections now, even for connections initialized with IP address directly.
* Surge TUN now supports forwarding ICMP packets.

**From this version, the minimum system version requirement was raised to macOS 10.11. If you are still using macOS 10.10, please use version 2.4.5.**

<http://dl.nssurge.com/mac/Surge-2.4.6-490.zip>

#### Version 2.4.5

* Bug fixes.
* Improved performance for high concurrency.
* TCP fast open has been disabled temporarily since there is a serious problem in macOS/iOS kernel.
* Dashboard will display decoded URL query now.

<http://dl.nssurge.com/mac/Surge-2.4.5-468.zip>

#### Version 2.4.4

* Supports obfs=tls for shadowsocks protocol.
* Refined the proxy edit panel.
* Added Simplified Chinese language.

<http://dl.nssurge.com/mac/Surge-2.4.4-459.zip>

#### Version 2.4.3

* Supports obfs=tls for shadowsocks protocol.
* Refined the proxy edit panel.
* Added Simplified Chinese language.

<http://dl.nssurge.com/mac/Surge-2.4.3-457.zip>

#### Version 2.4.2

* Fixed an issue that enhanced mode may not be closed properly when switching to a profile without dns-server.
* Fixed an issue that managed profile updating and license info are unavailable while enhanced mode enabled.
* When the necessary port is used by another process, the error alert will show which process is using the port.
* Fixed an issue that map local items can't be edited with UI.
* Fixed an issue that system proxy settings may not be reset properly.
* Auto URL test group will execute a retest immediately after the selected policy has failed.

<http://dl.nssurge.com/mac/Surge-2.4.2-445.zip>

#### Version 2.4.1

* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.4.1-439.zip>

#### Version 2.4.0

* Supports enterprise license and profile management.
* Fixed a bug that some fields are unavailable in the configuration panel in some cases.
* Fixed a bug that the FINAL rule can't be edited.
* Fixed a bug that you may not be able to use custom storage path for profiles.
* The interface related options are no longer controlled by profile. Sorry for the repetitive changes.
* You may use $1, $2 to use the matched string in the value while using header rewrite.
* Added an option for HTTP/HTTPS proxy: always-use-connect. When it is true, Surge will use CONNECT method for plain HTTP requests.

<http://dl.nssurge.com/mac/Surge-2.4.0-429.zip>

#### Version 2.3.2

* Added a option to control whether show proxy error notification.
* Fixed a problem that Dashboard show data doesn't exist error.

<http://dl.nssurge.com/mac/Surge-2.3.2-421.zip>

#### Version 2.3.1

* Added a wizard to install CA’s root certificate for iOS simulator.
* Connectivity quality is now an option. (Not show by default)
* Line comments in \[Rule] section in profile file is now presented in UI.
* You may add proxy rule with Dashboard by right-clicking the request or process.
* Dashboard will always open a new window for local machine, instead of asking. You may use "File" menu to connect to a remote machine.
* Added a patch mechanism for adjusting settings for managed config. See manual for more information: <https://manual.nssurge.com/others/managed-configuration.html>

<http://dl.nssurge.com/mac/Surge-2.3.1-420.zip>

#### Version 2.3.0

* Completely redesign the configure interface. You may configure every function with UI now.
* Proxy benchmark is now moved to main application from Dashboard.
* New feature: Header rewrite. See manual for more information: <https://manual.nssurge.com/header-rewrite.html>.
* You may switch profile with command line now: surge-cli switch-profile profilename.

<http://dl.nssurge.com/mac/Surge-2.3.0-416.zip>

#### Version 2.2.4

* Notifications presented by Surge will be removed from Notification Center automatically.
* The interval of attempts to refresh managed config changes to one hour from one minute. (After config expired)
* Supports new encryption methods for shadowsocks-libev 3.0.
* Optimized Dashboard performance.
* Supports TCP Fast Open for shadowsocks proxy. You need add "tfo=true" flag in \[Proxy] section to enable the feature. You may use benchmark to confirm TFO is working.
* You can sort benchmark results now.
* You may choose to reload config after managed config updated.

<http://dl.nssurge.com/mac/Surge-2.2.4-394.zip>

#### Version 2.2.2

* Fixed a bug when using SOCKS5 without authorization.

<http://dl.nssurge.com/mac/Surge-2.2.2-375.zip>

#### Version 2.2.1

* You may use Dashboard to benchmark proxies now.
* Fixed "Too many open files" error by raising limit to 2048.
* Fixed a bug in SOCKS5 with authorization.
* Fixed a bug that managed config may refresh continuously.

<http://dl.nssurge.com/mac/Surge-2.2.1-374.zip>

#### Version 2.2.0

* Map local function is now available.
* Adds notifications when proxy encounters errors.
* Network changed notification will show service name instead of BSD name now.
* Fixed a bug that Dashboard may show the incorrect state of body dump.
* Changes for HTTPS and SOCK5-TLS proxy:
  * Option 'skip-common-name-verify' is deprecated.
  * Add a new option 'skip-cert-verify' to skip certificate verify completely.
  * Add a new option 'sni' to customize SNI field while handshaking. You may use 'sni=off' to disable SNI.
* New rule type: PROCESS-NAME, USER-AGENT and URL-REGEX.
* You can use simple wildcard matching (? and \*) for PROCESS-NAME rule, local DNS mapping and MitM hosts.
* Dashboard supports display POST form data in a table view.
* You may let Surge reload config by sending SIGHUP. You can use command 'killall -HUP Surge' or 'surge-cli reload'.
* Managed configuration is supported now.
* Add a new option 'skip-server-cert-verify' for MitM.

<http://dl.nssurge.com/mac/Surge-2.2.0-368.zip>

#### Version 2.1.4

* Fixed a bug that helper may crash on macOS 10.10.
* Add a option to remove Surge helper for troubleshooting.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.1.4-362.zip>

#### Version 2.1.3

* Fixed a bug that helper may crash on macOS 10.10.
* Add a option to remove Surge helper for troubleshooting.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.1.3-337.zip>

#### Version 2.1.2

* New option: Collapse policy group items in menu
* Fixed a bug that enhanced mode DNS settings may not be reverted.
* Hold option key to click 'Copy Shell Export Command' to get a command with primary interface IP instead of 127.0.0.1.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.1.2-327.zip>

#### Version 2.1.0

* New feature: Enhanced Mode

  Some applications may not obey the system proxy settings. Using enhanced mode can make all applications handled by Surge.
* New rule type: IP-CIDR6

  Example: IP-CIDR6,2005::/16,DIRECT,no-resolve
* The /etc/hosts file will be reloaded automatically if it has changes.

<http://dl.nssurge.com/mac/Surge-2.1.0-318.zip>

#### Version 2.0.13

* Dashboard supports to use ⌘ + 1,2,3,4 to switch panel.
* Dashboard Supports handoff with Surge iOS.
* Fixed a bug that Dashboard may show incorrect process name.

<http://dl.nssurge.com/mac/Surge-2.0.13-304.zip>

#### Version 2.0.12

* Bug fixes.
* Supported SNI while performing MitM.
* The original certificate will be resigned and used while performing MitM, instead of generating a new certificate.

<http://dl.nssurge.com/mac/Surge-2.0.12-295.zip>

#### Version 2.0.11

* Rule test cache will be flushed after network switching now.
* Added a option 'Grey icon if set as system proxy is disabled'.
* Bug fixes and performance improvements.

<http://dl.nssurge.com/mac/Surge-2.0.11-289.zip>

#### Version 2.0.10

* Surge talks to HTTP proxies with a plain HTTP method for non-HTTPS requests now, instead of CONNECT.
* Improved compatibility with some HTTP server.
* Improved compatibility with some DNS server.

<http://dl.nssurge.com/mac/Surge-2.0.10-280.zip>

#### Version 2.0.9

* Dashborad: The height of the detail panel will not change now while switching pages.
* A notification will show when proxy client access from other machine.
* Used SF Mono as monospaced font for header and body data display.
* Supported TCP half-open mechanism.

<http://dl.nssurge.com/mac/Surge-2.0.9-273.zip>

#### Version 2.0.8

* Add a new option 'exclude-simple-hostnames' in the gereral section.
* Dashborad: Selected row will not be lost while the filter or sort column changed.
* Dashborad: Fixes some issues in the active panel.

<http://dl.nssurge.com/mac/Surge-2.0.8-260.zip>

#### Version 2.0.5

* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.0.5-255.zip>

#### Version 2.0.3

* New feature: Show connectivity quality in menu.

  Surge will send a DNS question to all DNS servers concurrently to test physical network connectivity while opening the menu.
* Fixes a problem that Surge may freeze while opening the menu.
* Fixes a problem that if a policy group contains duplicate policies, Surge may crash.

<http://dl.nssurge.com/mac/Surge-2.0.3-250.zip>

#### Version 2.0.2

* Dashboard will no longer display process icon in remote mode.
* Fixes a bug: "Set as System Proxy" option does not work properly if only SOCKS service is enabled.
* Fixes a bug: Dashboard can't add a rule with no-resolve option on and comment not empty.
* Minor bug fixes.

#### Version 2.0.1

* Bug fixes
