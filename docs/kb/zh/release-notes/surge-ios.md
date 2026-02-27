# Surge iOS 更新日志

### 版本 5.14.6

* 新增 \[General] 参数 `block-quic`，该参数用于全局覆盖是否阻止 QUIC 流量的行为
* 优化请求查看器中的文本与 JSON 浏览器，支持大文件与代码高亮
* 重写 HTTP 脚本相关实现，现在在处理大型 Body 时性能更好且内存占用更低
* 支持 gQUIC 的 SNI 提取
* 重构流量统计功能，现在即使长期未进主程序，也不会在进入流量统计页面时需要长时间等待了
* 流量统计新增导出功能
* 其他细节优化与问题修正

### 版本 5.14.5

* 支持 DNS over TLS。
* 修复错误和性能改进。

### 版本 5.14.4

* 启用 HTTP 捕获开关时，所有活动连接现在将被强制中断，以确保不会由于现有长连接而漏请求。
* 优化了与某些 QUIC 客户端（如 Lark）的兼容性。
* 修复了在使用脚本或其他机制修改请求 HTTP 后，统计中的下载数据字节数不正确的问题。
* 调整了转发 QUIC 时的处理逻辑优先级。现在，对于不支持 UDP 转发的代理策略，将优先考虑 QUIC Block，然后才会回退到 DIRECT 或 REJECT。
* 修复错误和其他改进。

### 版本 5.14.3

#### 新功能：端口转发

* 该功能常用于开发和调试场景，例如使用 SSH 连接到 MariaDB 等服务器。

#### #!需求 升级

* 现在提供了三个简单的表示法：#!IOS-ONLY、#!MACOS-ONLY 和 #!TVOS-ONLY。
* 由该行尾注释禁用的内容现在可以在 UI 中显示和编辑。当条件不满足时，将显示为禁用状态，并且如果启用了，将自动移除限制。

#### \[Host] 优化

* \[Host] 部分支持使用 DOMAIN-SET 和 RULE-SET 进行配置，以提高匹配效率。使用实例：

#### 其他改进

* 添加了 icmp-forwarding 选项，默认启用。
* 优化使用智能策略组作为基础代理。现在在这种使用场景中，可以充分利用智能策略组的特性。
* 修复错误和其他改进。

### 版本 5.14.2

* 修复错误和其他改进。

### 版本 5.14.1

* 修复错误和其他改进。

### 版本 5.14.0

#### 新功能

* 添加了低开销请求拒绝的预匹配规则。详情请参阅文档。<https://manual.nssurge.com/policy/reject.html>
* Body Rewrite 支持使用 JQ 表达式操作 JSON。
* shadowsocks 协议新增支持 `2022-blake3-aes-256-gcm` 和 `2022-blake3-aes-128-gcm` 加密模式。
* 针对 iOS 18 的图标模式进行了适配。
* 新增用于 HTTP 捕获的控制中心控件。
* DNS 现在支持系统搜索域设置。
* 增加参数 proxy-restricted-to-lan，以限制代理仅接受来自同一子网的设备。
* 在更新外部资源时，将记录并发送 ETag；如果资源未更改，则不会触发重新下载。

#### 改进

* 全面优化和改进 UDP 转发性能。
* 策略组列表视图支持配置自定义图标。
* 解决了 iOS 18 上实时显示的问题。
* 优化策略组图标的显示效果。
* 提高 HTTP 引擎对非标准请求的兼容性。
* 当 Surge 无网络连接激活时，提供更明确的错误提示信息。
* 优化加密 DNS 的错误处理逻辑，在遇到错误时立即重试。
* 对于过多 \[Host] 条目添加警告消息。
* URL 正则表达式规则现在支持 `extended-matching` 标签。
* 允许使用 Ponte 策略作为底层代理。

#### Bug 修复

* 修复了即使 Surge 已关闭，控制中心/主屏幕小组件仍会显示为活动状态的问题。
* 修复了在某些错误情况下，加密 DNS 出现内存泄漏的问题。
* 更正新图标订阅周期约束错误。
* 其他 bug 修复。

### 版本 5.13.0

* 控制中心小组件：在 iOS 18 上，您现在可以在控制中心快速开关 Surge
* 新图标：Sapphire（蓝宝石）
* 添加 Ponte 诊断功能，用于快速定位与 Ponte 相关的问题，可从 Ponte 设备页面访问。
* 端口跳跃：Hysteria2 和 TUIC 协议现在支持端口跳跃，以改善 ISP 的 UDP QoS 问题。详情请参阅服务器文档
* 添加 `[General]` 参数 `show-error-page`，用于控制是否在发生错误时显示 Surge 的 HTTP 错误页面。此参数默认启用，其行为与以前的版本一致
* 其他问题修正

### 版本 5.12.0

* 新的订阅功能：自定义策略组图标
* 使用 CloudKit 重构 Surge tvOS 配置部署流程，稳定性得到大幅提升。请注意需要将 iOS 和 tvOS 都升级至最新版本后才可以使用配置部署功能，且 tvOS 版本需要先启动一次完成注册
* 在请求列表里使用增加规则功能时，可以选择加入已存在的规则集。（支持本地规则文件和 inline 规则集）
* 模块支持配置 client-source-address 参数
* 修正导出 HAR 时的一些问题
* UI 恢复兼容模式（接管模式）设置并增加详细描述
* 优化 No Default Route 模式下开启 IPv6 VIF 时的行为
* 修正 UI 编辑规则时的一些细节问题，如开启状态和注释
* 优化在外部资源页面查看巨型资源时的表现
* 其他细节优化与问题修正

### 版本 5.11.3

* 支持在始终开启开关打开的情况下，通过小组件/控制中心/捷径关闭 Surge
* 支持在 Surge VPN Profile 未被选中的情况下（其他 VPN 运行时），通过小组件/控制中心/捷径开启 Surge
* 修正规则集中包含重复的 DOMAIN 与 DOMAIN-SUFFIX 规则时，可能导致 DOMAIN-SUFFIX 失效的问题
* No Default Route 模式相关优化，大幅提高可用性
* 其他问题修正

### 版本 5.11.2

* 新的订阅功能：规则分析，目前包含两个子功能：
  1. 规则使用计数，会记录规则的匹配次数。（只统计主规则集中的条目，各类规则集和逻辑规则的子规则不会被统计，统计时会忽略规则参数）
  2. 当前规则集性能测试
* 优化了阻拦 QUIC 流量的实现方法，以提高让客户端正确回退的可能性
* Smart 组当不存在子策略时，也会使用 SUBSTITUTE 策略(DIRECT)而非直接失败。
* 修正 TLS 类协议，在 sni=off 的设置下，server-cert-fingerprint-sha256 参数未能生效的问题
* 新增规则类型 HOSTNAME-TYPE，用于判断请求的主机名的类型，可选值有：IPv4, IPv6, DOMAIN, SIMPLE。（SIMPLE 指的是不包含 . 的主机名，如 localhost）
* 优化了 DNS 的请求日志，现在会显示更多的信息，且在规则系统未触发 DNS 时，如果是 DIRECT 策略直连也可以显示 DNS 的相关日志了
* 在删除策略时，如果该策略被策略组所使用，现在允许直接删除并将自动从所有策略组移除
* 建立 Subnet 策略组时，现在可以使用 Subnet 表达式的编辑向导
* 修正规则集索引建立过程可能是会阻塞 UI 的问题
* 优化了请求详情页的 IP 地址展示
* 编辑策略组时不再可以将自身作为子策略加入

### 版本 5.11.1

* 优化小型规则集的匹配性能，在旧型号 CPU 上效果尤为明显
* 外置资源更新页面可以显示规则集处理产生的错误信息
* 自动忽略规则集中的无效空行
* 修正应用临时规则后，如果产生了策略变化，不会打断原有连接的问题
* 修正当外部策略组产生变化时，可能导致的崩溃
* 修正配置升级功能未能对托管配置和企业配置正确生效的问题
* 在 Smart 组初始化阶段，不再显示最常使用标签，以避免产生误解
* 修正本地脚本文件被编辑后无法被自动重载的问题
* 优化大型规则集的索引流程
* 限制 iCloud 后台自动同步的最大文件数量为 200，避免产生内存占用问题
* 修正通过远程控制器调整策略时，UI 可能显示不正确的问题

### 版本 5.11.0

#### Smart Group

这是一种全新的策略组类型，由我们精心设计的算法引擎所驱动，可以自动从该策略组的子策略中选择合适的策略。Smart 策略组的目标是取代原有的自动测试组（url/load-balance/fallback），大幅优化体验的同时，尽可能减少用户需要手动干预策略组的情况，用户只需将可用策略放入该组即可。

详情请见：<https://kb.nssurge.com/surge-knowledge-base/v/zh/guidelines/smart-group>

#### 规则系统

* 规则系统整体性能优化。
* 大幅优化大型域名规则集中的索引算法，对于十万条以上的规则集，检索效率提高了十倍以上。
* 修正规则集内的逻辑规则的子规则无法被规则集的 no-resolve 和 extended-matching 参数覆盖的问题
* 新增规则类型 DOMAIN-WILDCARD，支持 ? 与 \* 匹配域名
* DOMAIN-SET 与 RULE-SET 改为强校验，当文件中包含无效行时将导致整个规则集无效，以避免误用产生问题

#### IPv6

* ipv6-vif 参数行为修改，当设置为 always 时，即使未设置 ipv6=true，也会开启 IPv6 功能。
* 为 ipv6-vif=always 参数增加了警告
* 调整了自动重试机制，在非 IPv6 网络下访问 IPv6 地址不再会进入重试流程，请求会立刻失败（以此解决在非 IPv6 环境下开启 IPv6 VIF 造成部分应用卡顿的问题，如微信和淘宝，但是应用仍然会持续发出 IPv6 请求）

#### 其他优化

* $notification.post 增强，新增媒体资源支持、声音提示和自动消除。
* 优化 WireGuard 失败处理
* 降低 TUIC 协议在休眠时对电量的消耗
* 请求日志系统时间统计精度提高，现在可精确到 µs 级
* 优化各种异常的重试机制，避免在出现一些特定问题时持续重试导致高资源占用。对于需要持续重试的操作（如 WireGuard 重连、Ponte 服务端上报 iCloud），现在 Surge 会在出错后的 0.1s, 0.5s, 1s, 5s, 10s, 30s 后重试。
* 优化外部资源的缓存系统
* 新增配置文件行命令 #!REQUIREMENT
* 在发现当前网络由 Surge Mac Gateway 所接管时，现在将自动暂停 Surge iOS。（可通过 auto-suspend 选项调整行为，默认开启）
* 优化 TUN 接管和特定 app 的性能兼容性问题
* 优化了内存占用，不常用和巨大的脚本现在将不会被缓存至内存
* 网络诊断页新增 SSID/BSSID，增加复制功能
* 现在在日志界面执行日志上传时，将自动为当前运行的引擎生成最近的 verbose 日志（新版本在内存缓存了 256KB 的日志），这样在汇报问题时，直接执行上传即可，无需再使用 verbose 模式复现。
* 对于策略组与脚本类型的外部资源，现在限制最大大小为 2MB，避免当错误配置时，导致的内存超限。

#### 细节调整

* 提高内存警告的阈值到 45MB，原为 40MB。
* 限制了脚本在 debug 模式下，可以往请求 notes 中写入的日志的长度
* 默认 UDP 测试目标改为 1.0.0.1
* 在脚本中使用 API 时如果传入了错误类型的字段，将产生脚本异常
* 当脚本已完成或超时后，未完成的 $httpClient 不再会调用回调函数

#### 问题修正

* 修正在 Surge iOS 主程序和引擎都开启时，iCloud 内容发生变化可能无法被主程序所检测的问题
* 修正 Header Rewrite 规则无法根据 Host 字段进行 URL 匹配的问题
* 修正了在测试代理时，ip-version 和 tos 参数无法生效的问题
* 修正通过 HTTP-API 执行脚本时，若果错误的传入 null 会导致崩溃的问题

### 版本 5.10.0

#### 新功能

* 新的订阅功能：Body Rewrite。Surge 现在可以重写 HTTP 请求或响应的 Body，用正则表达式替换原始内容。如果你需要进行更灵活的修改，请使用脚本。

#### 改进

* Mock (Map Local) 功能全面强化，- 新增 text, tiny-gif, base64 等数据类型，以便于 inline 直接返回数据。同时增加了 status code 自定义。
* 请求列表过滤器优化，现在将把过滤器显示于顶部，并快速切换过滤器是否启用，长按过滤器项目可以显示菜单，可删除或反转该项目为负过滤器。
* 新增对 STUN 数据包的识别，可用 PROTOCOL,STUN 进行匹配。
* 优化外置资源管理页面
* 优化脚本编辑器页面
* 优化模块管理页面
* 新增 Utilites 标签页的长按快捷菜单
* iOS 版本新增 URL scheme: surge:///install-module?url=…

#### 优化

* 配置 Shortcuts 执行 Surge 脚本时可直接读取当前配置的脚本列表
* 增强了 HTTP Body 解压时的兼容性
* 优化脚本引擎，限制 JSC 引擎并发处理数为 2 以避免内存问题
* GeoIP 数据库由主应用更新后不再需要重启即可生效
* 优化了请求记录，现在将显示匹配到的 URL Rewrite 和 Header Rewrite 的具体规则
* 调整了 DNS 引擎处理空结果的逻辑，现在在配置了多个 DNS 服务器的时候，也不再等待所有服务器响应空结果，以避免在 AAAA 记录不存在时产生额外等待。
* 模块页面允许撤销修改以避免误操作导致生效顺序修改

#### 修正

* 修正了在使用覆盖策略组后，显示策略组的延迟依然是覆盖前的选项的结果
* 修正在 iPad 上长按过滤器会导致崩溃的问题
* 修正因模块配置而产生的警告信息不会显示的问题
* 修正在脚本中传入一些错误类型的参数会导致 Surge 崩溃的问题
* 修正与新版 Safari 的非 https WebSocket 在代理模式下的兼容性问题
* 修正在规则搜索页删除条目时，会将重复条目全部删除的问题
* 修正编辑器高亮的一些缺失

### 版本 5.9.0

#### 模块系统

* 新增数个官方模块，现在官方模块可以动态更新了。
* 模块新增分类字段，用于在 UI 上便捷访问与归类。
* 模块新增参数表传入，支持传入多个参数，参数将用以文本替换的形式对模块内容进行修改。

#### 脚本系统

* 全新的脚本执行引擎。优化了执行性能和内存占用。
* $httpClient 新增了多个实用参数。 以上更新详见文档。

#### 增强

* 新增远程控制器的桌面快捷跳转，详见设备页面底部的配置向导。
* 新参数：always-raw-tcp-keywords，使用方式详见文档。
* 新增规则 SRC-PORT 用于匹配客户端端口号。
* IN-PORT/SRC-PORT/DEST-PORT 三个规则统归为端口号规则类，支持更多用法。
* 现在 UI 编辑后可以保持原配置中的纯空行了。

#### 修正

* 修正 QUIC 流控的一个细节问题，优化了 Ponte/TUIC/Hysteria2 协议的延迟表现。
* 编辑单条规则后，notification 相关参数将会保留。
* 修正新版 iOS 下无法通过小组件切换出站模式的问题。
* 修正在处理巨型的外部资源时，有可能会出现突发的内存超限导致停止。

### 版本 5.8.1

#### 规则引擎优化

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

#### Minor Optimizations

* MITM 时发送签名所使用的证书（证书链），以支持使用 intermediate 证书作为签发证书。
* 行首与行末注释，现在可以随意使用 `#` `//` `;` 等三种常见写法
* 配置文件错误消息提示优化，现在它可以更准确地给出发生错误的确切行号。
* 修复了 BSSID 相关匹配规则可能会失败的问题。
* 优化 Surge Ponte 错误处理流程，修正某些错误下不会自动更新设备信息的问题
* Bug 修正。

### 版本 5.8.0

#### 新功能

* 新的 Inky 图标
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

#### 优化

* HTTP 捕获功能重做
  * 相关设置不再存放于配置中，`[Replica]` 段已废弃。
  * 新增开启捕获开关后的自动关闭设置，可根据时间、大小、请求数自动停止抓取。
  * 新增 MITM 自动开启，开启捕获开关后可对特定主机名额外开启 MITM。（即使 MITM 主开关未开启）。
  * 新增在开启捕获开关后，只保存 HTTP/HTTPS 请求的选项。
* VIF 性能优化，经测试可在 iPhone 15 Pro 下以 VIF 接管单线程达到 2.5Gbps 有线网卡满速。（代理模式性能更佳）
* Wi-Fi Assist 和 Hybrid 功能将只在设备解锁后生效，避免造成不必要的电量与流量消耗。
* 该版本中开始限制外部资源大小为不超过 10MB，避免异常的外部资源导致内存超限。（domain-set 除外）
* `udp-policy-not-supported-behaviour`、`include-apns`、`include-cellular-services` 参数加入了 UI 设置。
* 优化了对一些非标准协议的兼容性。
* 对 Ponte 策略进行测试时，测试 URL 由 proxy-test-url 改为 internet-test-url。
* 根据 WireGuard 协议标准推荐，现在 WireGuard 的握手数据包将打上 0x88 (AF41) 的 DSCP 标记以增加成功率。
* 通过 WireGuard 转发 UDP 数据包时，支持 tunnel 内数据包保留 TOS(DSCP/ECN) 标记了。
* 根据 WireGuard 协议标准推荐，Surge 将复制 tunnel 内数据包的 ECN 标记到 tunnel 外数据包上。收到含有 ECN 标记的数据包时，将严格按照 RFC6040 进行合并处理。（需要为策略配置 `ecn=true`）
* UDP NAT 支持根据 ICMP 消息提前关闭 UDP 会话。
* 完善了 QUIC 的 PMTU 支持。

#### 问题修正

* 修正规则集的外部资源更新后需要重新才能生效的问题。
* 在网络切换后将强制打断原有的 DoH/DoQ/DoH3 长连接，避免获取到不适合当前网络环境的结果。
* 修正无效的证书可能导致密钥库界面崩溃的问题。
* 修正策略组页面的 Ponte 设备选项可能不显示文字的问题。
* 在对使用 IP 地址直连的 HTTPS 请求进行 MITM 时，不应将 IP 地址作为 SNI 发送，这可能导致出现兼容性问题。
* 其他问题修正。

### 版本 5.7.0

#### 新功能

* Surge tvOS 现已可以使用，所有 Surge iOS 已购用户均可直接使用，无需额外付费
* 支持 iOS 17 的可交互小组件
* 新增请求的 Header 与 Body 全文搜索支持
* Web Dashboard 更新至 2.0 版本
* 新增功能 Inline Ruleset，可将 Ruleset 直接写于主配置中

#### 细节优化

* 优化脚本日志系统，确保并发执行时请求日志中的脚本日志不会显示其他会话的内容
* 拆分开启与关闭的 iOS 17 的捷径动作，iOS 17 版本用户请使用使用 (iOS 17) 后缀的动作
* 取消了 Wi-Fi Assist 的提示通知
* 使用 UI 编辑策略组时可以选择 Ponte 设备了
* 为远程设备创建临时规则时，可以选择 Ponte 设备了
* 远程控制器支持查看与更新远程设备的外部资源，支持 Surge Mac 与 Surge tvOS
* Ponte 设备的图标可以显示设备类型了
* 优化了无障碍访问相关的细节
* 优化了一些 UI 细节

#### 问题修正

* 修正 MITM Hostname 列表编辑时可能出现的一些问题
* 修正为远程设备创建规则时，策略选项有可能是本地的策略而非远端策略的问题
* 修正了当使用 iCloud 同步时，当缓存被清除时可能导致本地模块的勾选被取消的问题
* 修正了无法切换到 Dropbox 同步的问题
* 修正了部分卡片背景在展开时背景不完整的问题
* 修正了使用 Basic Auth URL 添加的模块，无法自动更新的问题
* 修正快速切换模式下，从 IPv6 网络切换至非 IPv6 网络后，v6-vif 为 auto 时未能正确自动关闭 v6 vif 的问题

### 版本 5.6.0

#### 细节增强

* 请求列表页面全面优化
* 可以在 iOS 端直接发起和管理 Ponte 设备共享了
* 查看外部请求时将显示来源设备名
* 分离配置支持使用 作为关键字引用企业配置中的内容
* 配置列表新增 Create Linked Profile 选项，用于快速创建分离配置
* 性能优化
* 修改了访问数据保护区的逻辑，现在 Surge 在锁屏状态下也可以正常被开启。（重启手机后除外）
* 当检查到 CA 证书过期时给予提示
* 单个请求导出的 .zip 文件支持导入回 Surge iOS，将显示在收藏请求中

#### 问题修正

* 修正在同一轮策略测试中，如果混用不同的测试 URL，在二次测试时构造的 HTTP Header 可能不正确导致测试结果异常的问题
* 修正从后台打开主程序后，Panel 刷新可能无法正确被执行的问题。
* 修正列表策略组视图下，策略组标题选项有可能更新不及时的问题。
* 修正使用 DIRECT 策略作为 underlying\* proxy 时，有可能导致 UDP 失败的问题
* 修正使用 SSH 协议时，如果服务端配置了 banner 无法正确握手的问题。
* 修正 iPad 下 Lucid 主题可能出现的一些问题。
* 修正部分情况下 SSID 相关功能无法正确工作的问题。
* 修正当使用 TUIC v5 作为 underlying-proxy 时可能出现的一些问题。
* 修正当直接使用 IPv6 地址作为 vmess 主机名时，如果开启 WebSocket 会无法正确构造 WebSocket 请求的问题。
* 修正当 DOMAIN-SET 规则使用了特定的无效数据会导致崩溃的问题
* 修正配置错误可能导致的崩溃
* 修正了重放的请求返回数据如果存在压缩则无法查看的问题
* 修正云通知界面提示错误的问题
* 修正只有共享的 Ponte 设备时无法载入设备列表的问题
* 修正 DNS over HTTP3 可能出现的一些崩溃
* 修正 Surge Ponte 在子网 CIDR 不为 8 的整数倍时，会错误判断导致不使用局域网直连的问题
* 修正使用 Surge Ponte 时可能出现的一些问题
* 优化 TUIC/Ponte 在网络切换后重建主连接的逻辑

### 版本 5.5.1

#### 远程控制器全面优化

* 支持远程增加与修改临时规则
* 设备管理器默认分组为活跃和非活跃设备（是否有请求）
* 支持为设备直接增加临时或永久规则
* 其他细节优化

#### 其他

* 新增 TUIC v5 协议支持。
* 策略组菜单新增显示隐藏的策略组选项。
* 流量统计中，apple.com 的子域名将拆分处理，便于观察系统服务的流量消耗。
* 外部资源更新后，现在仅策略组更新会导致策略组页面重载，其他类型不再会导致策略组页面重载。
* 优化了 Surge Ponte/TUIC 的性能表现。
* 优化了策略组异常时的请求 Note 记录。
* 修正 MITM H2 模式下未能正确进行连接复用的问题
* 修正了有时 $httpClient/DoH 的请求可能被意外取消的问题。
* 其他问题修正。

### 版本 5.5.0

#### 界面

* 新 UI 主题 Lucid，源自 Surge Mac 5 的设计语言的主题风格。（需要订阅功能）
* 远程控制的设备管理支持远程修改设备图标。（Surge Mac 需更新至 5.1.0 版本）

#### Surge Ponte

* Surge Ponte 支持跨 iCloud 账号分享。（Surge Mac 需更新至 5.1.0 版本）
* 修正通过 Surge Ponte 或 TUIC 协议，访问 HTTP/1.0 的服务端时可能出现的问题。（如 ASUS 路由器管理页面）

#### 代理协议相关

* 支持 ShadowTLS v3。（需要订阅功能）
* 新功能：Adaptive TLS Fingerprint，详见手册。
* 修正了 Snell V4 下 reuse 功能不能正常生效的问题。
* SSH 协议新增服务器公钥指纹指定，使用方式详见手册。
* 为 VMess 协议增加了 UDP 转发支持。

#### 脚本

* 脚本的 $httpClient 支持 binary 模式。
  * 请求时的 body 支持传入 TypedArray。
  * 请求时的参数传入 `binary-mode: true` 可使返回结果以 TypedArray 返回。
* 修正 `http-request` 类型脚本无法使用 binary 数据直接作为 response 的问题。

#### 其他

* 策略组新增参数 `external-policy-modifier`，可用于对外部策略进行调整。
* 优化了请求的日志系统
  * 增加了日志的分类标识。
  * 规则判断系统增加 DNS 和规则集的更多输出。
* 临时规则上侧滑可将规则写入永久规则。
* 其他问题修正和优化。

### 版本 5.4.0

#### Surge Ponte

Surge Ponte 是一种在运行 Surge Mac 和 iOS 设备之间的私有网络。

* 无需繁琐配置。
* Surge 会自动选择最合适的通道建立连接。
* 始终端到端加密。
* 设备信息和加密密钥通过您的 iCloud 同步，除了您选择的代理服务器外，您的数据不会经过任何第三方服务器。

需要配合 Surge Mac 5 使用 Surge Ponte。

#### WireGuard 相关优化

* 大幅优化了握手相关逻辑。
* WireGuard 的 Client ID 支持由 UI 配置，且新增 0xabcdef 和 6 字符 base64 格式支持

#### 其他更新

* 重做了网络诊断页面，优化了信息展示。。
* 优化 QUIC 的峰值带宽性能和 CPU 占用。
* 被 REJECT 规则匹配的请求将被标记为 Rejected 并使用灰色区分，不再归为 Failed。
* 优化了各功能的开关控制逻辑，避免在一些情况下意外关闭/开启某项功能。
* MITM 时优先使用客户端上报的 SNI 生成证书，未上报 SNI 时使用访问域名。
* 加快了在未开启 Surge 下通过捷径执行 Surge 脚本的唤醒速度。
* SOCKS5 代理请求类型显示时修改为 TCP，可在 Notes 中确认是由 SOCKS5 代理接管。
* 支持在 \[Host] 中为特定域名配置 DNS over QUIC/H3。
* 引入了 FAILED 内置策略用于在特殊情况下标记请求失败（如策略组无法加载），而不是使用 REJECT。
* 修正当规则匹配时，如果客户端意外发送大写字母的域名会无法匹配的问题。
* 修正当多个外置策略组使用了相同名字当实际内容不同的策略时，会导致策略组决策失败的问题。
* DNS Local Mapping 允许为域名配置多个 IP 作为并发使用结果。
* 优化了有线网络适配器的判断，避免误判。
* 其他问题修正。

请注意，从 iOS 16.4 版本开始，系统不再允许读取数据网络的 MCC/MNC，相关功能可能会失效。

### Version 5.3.1 (Feb 16, 2023)

* The installed modules are now synced between iOS devices via iCloud.
* Support for customizing the reserved bits of WireGuard, also known as the client ID or routing ID.
* Improved WireGuard handshake logic.
* Fixed some UDP forwarding problems.
* Fixed some text editor issues.

### Version 5.3.0 (Feb 3, 2023)

#### New Subscription Feature: Temporary Rules

We have added the temporary rules feature in Surge Mac to the iOS version. Temporary rules will automatically disappear after Surge is stopped and will not be written to the profile for some temporary usage scenarios.

#### New subscription feature: Whois lookup

Quickly perform a Whois lookup to identify the domain or IP owner in the request details menu.

#### New feature: Proxy Detail View

#### Traffic statistics have been enhanced

* In addition to traffic statistics, the number of requests will now be recorded as well.
* In addition to this month's data, last month's data will also be kept.

#### Bug fixes and minor improvements

* JSON and text viewers support search on iOS 16
* Network switching no longer interrupts in-progress $httpClient requests.
* Fixed an issue where scripted requests would sometimes accidentally carry the x-surge header handled internally by Surge
* Fixed an issue that some requests constructed in a special way could not be matched by MITM hostnames.
* Fixed an issue that the LAN proxy and Dashboard may not be accessible if the fast-switch is configured.
* Fixed an issue that could occur when using the expanded card layout on iPad
* Fixed an issue that the Panel button is not showing on iOS 14.

### Version 5.2.2 (Dec 3, 2022)

#### New Feature

* Gaming Optimization. Enabling it will prioritize UDP packets when the system load is very high, and packet processing is delayed.
* SOCKS5 proxy now supports UDP forwarding, as the server side does not consistently support UDP forwarding, the parameter udp-relay=true needs to be explicitly configured.

#### Minor Improvements

* URL regular expressions for Script, Rewrite, Mock, etc. will try to match URLs constructed in many different ways (e.g. Host field in Header) to solve the problem that some apps use custom DNS logic to request directly to IP addresses.
* Removed the silencing mechanism after UDP forwarding errors to avoid extra waiting time after switching networks.
* Added a workaround for suspend and subnet settings that may occur when the SSID is temporarily not available under iOS 16.
* The log view supports freezing now.
* The IPv6 switch no longer prevents direct access to IPv6 addresses when turned off. The switch is now limited to controlling whether the DNS Client requests AAAA records.
* Automatic disabling of AAAA queries due to DNS issues will be prompted in the Event Center instead of just in the logs.
* Fixed handling issue of generating IPv6 fragmentation when forwarding IPv6 UDP packets via WireGuard.
* The external policy group will skip the line and continue processing when it encounters invalid content instead of returning an error directly.
* Adjusted the buffering mechanism of raw TCP forwarding to avoid conflicts with some apps.
* Fixed REJECT requests not being marked as failed under MITM H2.
* Adjusted the output text under diagnostics.
* Other bug fixes.

### Version 5.2.0 (Nov 11, 2022)

#### Support New Proxy Protocol

* Snell V4
* TUIC
* Shadow TLS

See the online manual for more information.

#### Other Improvements

* A new expanded card style for the Policy Group view.
* Refined the Route Table view.
* shadowsocks now supports the none cipher.
* Modified the handshake packet construction logic when forwarding HTTPS requests to proxies, which can slightly optimize latency.
* Surge HTTP requests for proxy testing no longer contain a User-Agent header.

#### Bug fixes

* Fixed an issue that when using Subnet Suspend, the switch in the interface did not display the status correctly.
* Fixed an issue that the module could not configure the MITM h2 parameter.
* Fixed some keyboard-related layout problems.
* Fixed an issue that may not work properly when nesting proxy chains with a specific protocol combination.
* Fixed an issue where UI jumping may occur when starting Surge if iCloud Drive is used.
* Fixed a memory leak that could occur when HTTP capturing is enabled.

### Version 5.1.3 (Sep 29, 2022)

* Added a delayed update mode to the view of the recent request, which will automatically start when too many requests are received, to avoid the Surge main application from getting jammed.
* Optimized the check logic of ICMP traffic limit to avoid the alarm triggered by high concurrency in a very short period.
* Added a lock screen widget that can be used to quickly open Surge.
* Added a view to examine the modified profile after modules are applied.
* Added a new Siri action: enable or disable modules, which can be used with Shortcut.

### Version 5.1.0 (Sep 11, 2022)

#### IPv6 Improvements

* Support UDP forwarding with IPv6 VIF, including local and proxy forwarding.
* Support ICMPv6 local forwarding with IPv6 VIF.
* Fixed an issue that IPv6 address could not be used when using Surge Private DDNS.
* IPv6 handling details refined.

#### WireGuard IPv6 Tunneling

* WireGuard policy now supports IPv6 Tunneling (the previous version already supports connecting to an endpoint with IPv6, this version adds IPv6 support inside the tunnel)
* Read the manual for more information.

#### Text Editor

* A toolbar was added to the text editor.
* Fixed a crash in text editing.
* You can search text in the text editor now.

#### Other updates

* Optimize the proxy failure handling policy. Now when the TCP handshake time to the proxy server is greater than the test-timeout parameter, it is directly determined as failure in order to trigger the policy group to retest faster.
* TabBar shortcut menu added module shortcut opening and closing.
* External resources view allows side-swipe to edit local resources file.
* All types of scripts that use $httpClient to initiate requests are now viewable in the view of the recent request.
* Adjusted script concurrency limit policy to avoid deadlock when multiple scripts refer to each other.
* Other minor bug fixes and improvements.

### Version 5.0.2 (Aug 19, 2022)

* Fixed a bug that the text editor may be unable to save content.

### Version 5.0.1 (Aug 17, 2022)

* You may now flush the DNS cache in the DNS result view.
* Improved the script editor and log viewer.
* Other bug fixes and minor improvements.

### Version 5.0.0 (Aug 10, 2022)

Surge 5.0 comes with a brand new UI design, including a brand new policy group selection view, a new Start tab, and a new icon.

And now, you can try all the features for free for seven days before you purchase.

#### New Features:

* DNS over QUIC and DNS over HTTP3 support
* Real-Time View: Show live speed or request list floating window when using other applications.
* Subnet Setting: Override global settings under specified networks.

#### Minor updates:

* Comprehensive UI improvements.
* New contextual menu in the tab bar items.
* Fixed a bug that encrypted-dns-skip-cert-verification may not work
* MITM hostname and force-http-engine-hosts now support keywords: `<ip-address>`, `<ipv4-address>`, and `<ipv6-address>`.
* Script added function `$utils.ipasn(ipAddress:<String>)` to lookup ASN.
* Script added function `$utils.ipaso(ipAddress:<String>)` to lookup ASO
* Script added function `$utils.ungzip(ipAddres:<Uint8Array>)` for gzip decompression.
* Bug fixes.

### Version 4.15.0 (Jun 30, 2022)

#### MITM over HTTP/2

* Surge now supports performing MITM with HTTP/2 protocol to improve concurrent performance.
* Surge now supports performing MITM on WebSocket connections.

#### Others

* You may use `doh-skip-cert-verification=true` to disable server certificate verification for DNS-over-HTTPS.
* Bug fixes.

### Version 4.14.0 (Jun 1, 2022)

#### SSH Proxy Support

* You can use SSH protocol as a proxy protocol. The feature is equivalent to the `ssh -D` command.
* Both password and public key authentications are supported.
* All the four types of private keys, RSA/ECDSA/ED25519/DSA, are supported.
* Surge only supports `curve25519-sha256` as the kex algorithm and `aes128-gcm` as the encryption algorithm. The SSH server must use OpenSSH v7.3 or above. (It should not be a problem since OpenSSH 7.3 was released in 2016.)

#### Keystore

* You may now save sensitive keystore items to the system keychain.
* You may now configure TLS client certificate authentication with the UI.
* You may use a keystore item as the CA certificate for MITM.

#### Others

* New rule type: `IP-ASN`. You may use the rule to match the autonomous system number of the remote address.
* The request details now include the ASN and ASO information of remote IP addresses.
* You can now enable/disable the rewrite rules and DNS local mapping items.
* The preview of SVG images is removed. You can use the new Web View to see the SVG image.
* Bug fixes.

### Version 4.13.0 (Apr 24, 2022)

#### HTTP Capture

* You can now export HTTP/HTTPS requests to a HAR file, which is a standard format and can be opened by many web analysis tools
* The image viewer now supports SVG format.

#### Proxy

* New parameter `server-cert-fingerprint-sha256` for TLS proxy policies. Use a pinned server certificate instead of the standard X.509 validation.
* `tls-engine` option is now deprecated. OpenSSL is now the only TLS engine.
* You can now use a full profile as the external policy group (policy-path). All proxies in the \[Proxy] section will be used.

#### MITM

* You can export the CA certificate to a P12 or PEM file.
* Fixed an issue that the CA certificate can’t be installed if the default browser isn’t Safari.

#### Header Rewrite

* Header rewrite now supports using the regex to replace the value.
* Header rewrite now supports modifying the response headers. Scripting
* The default timeout of $httpClient is now 5 seconds and you may override it with the timeout parameter.
* You can manage the data of $persistentStore with the UI now.
* You may edit the argument with UI now.

#### Remote Controller

* You may sort and search in the remote device list.

### Version 4.12.0 (Mar 18, 2022)

#### New Feature: Personal Hotspot Proxy Access

* When using an iPhone/iPad as a hotspot, an HTTP or SOCKS5 proxy can be used on the client device to take over the traffic using Surge iOS.
* The proxy IP to be configured on the client is shown in the More Settings and the port number is the same as the WiFi proxy service.

#### New Feature: Hybrid Network

* Instead of setting up connections with cellular data when the Wi-Fi network is poor, always set up connections with Wi-Fi and cellular data simultaneously.
* This feature can improve the network experience significantly on poor Wi-Fi or when the Wi-Fi network is switching.

#### WireGuard

* WireGuard supports multiple peers.
* The allowed-ips now support multiple IP ranges.
* WireGuard supports preshared-key and keepalive.
* WireGuard supports peers with IPv6 endpoints. (But still no IPv6 tunnel support)
* WireGuard now supports underlying-proxy.
* The raw TCP connections are now relayed on the L3 layer if no high-level features are used.

#### Detached Profile

* You can now include multiple detached profiles in one section. But the section will be marked read-only and can't be edited with UI.

`#!include A.dconf, B.dconf`

#### Policy Group

* You can now temporarily override an auto test group or an SSID group's optimal option, until Surge restart or reload.
* The new parameter include-all-proxies=true is added to the policy group, which will include all proxy policies defined in the \[Proxy] section, and can be used with the policy-regex-filter parameter for filtering.
* The new parameter include-other-group="group1,group2" is added to include policies from another policy group, and can include multiple policy groups separated by commas, also can be used with the policy-regex-filter parameter for filtering.
* include-all-proxies, include-other-group, and policy-path parameters are allowed to be used in a single policy group at the same time. The policy-regex-filter parameter applies to all three.
* There is an order of precedence among the policy groups for the include-other-group parameter, but there is no order of precedence among the include-all-proxies, include-other-group, and policy-path parameters. For scenarios where the order of sub-policies makes sense (e.g., fallback groups), use policy groups nesting with include-other-group.

#### Subnet expression

* SSID Group is now upgraded to Subnet Group, which supports subnet expression.
* SSID Setting now supports subnet expression.
* The SUBNET rule now supports subnet expression.
* The \[SSID Setting] can control the TCP Fast Open behavior now. Read the manual for more information.
* The \[SSID Setting] can control the Wi-Fi assist and Hybrid Network behavior now. Read the manual for more information.

#### Proxy Protocol

* The Trojan protocol now supports using WebSocket as the transport layer.
* Shadowsocks protocol now supports underlying-proxy for UDP relay.
* You may configure the UDP testing endpoint for proxies. e.g., proxy-test-udp = google.com\@1.1.1.1
* You may benchmark a single proxy by long press on the proxy cell.

#### Module

* New Official Module: Block HTTP3/QUIC
* Surge will check updates for installed modules automatically.

#### Others

* Performance improvements.
* OpenSSL is now the default TLS engine.
* The managed profile can be opened with the text editor now.
* The default timeout of $httpClient is 5 seconds now.
* Reduced the app package size.
* You need to perform a one-time Dropbox re-authorization if you are using Dropbox syncing.
* Modules allow modifying the skip-server-cert-verify and tcp-connection parameters of \[MITM].
* The client will get an ICMP connection refused message instead of TCP RST if a REJECT policy matches.
* Supports IPv6 addresses with scope ID.
* The Network diagnostics can test proxy UDP relay now.
* Bug fixes.

### Version 4.11.1 (Jan 27, 2022)

* You may edit the profile in the text mode without changing the current profile now.
* The REJECT policy now can evolve to REJECT-DROP policy for UDP traffics.
* Bug fixes.

### Version 4.11.0 (Jan 21, 2022)

#### Proxy Protocol Upgrades:

* WireGuard: Uses Surge as a WireGuard client, converting L3 VPN as an outbound proxy policy.
* Snell V3: Snell protocol now supports UDP relay.
* Trojan protocol now supports UDP relay. (No additional parameter required)
* VMess protocol supports VMessAEAD. (Policy parameter: vmess-aead = true)

#### Improvements:

* The underlying proxy (aka proxy chains) now supports using a policy group.
* New parameter: udp-policy-not-supported-behaviour. To control the fallback behavior when UDP traffic matches a policy that doesn't support UDP relay.
* You may acquire the request's headers within an http-response script via $request.headers.
* Performance optimization.
* Bug fixes.

### Version 4.10.0 (Dec 3, 2021)

* You may extend your Surge iOS Pro license to 6 devices for free. You may find the guidance in the License Management view.

#### New Features

* Sorting option in the request list.
* Supports remote rule editing for the remote controller.
* Added the effective order adjustment view for the module. You can now adjust the effective order of the module.
* Supports custom the policy IP TOS field. Example: test-policy = direct, tos=0xb8.

#### Other Improvements

* UI details refined.
* Performance improvements.
* The network changed notification message will display the data network operator. If network automatic switching is enabled, you can use the notification to confirm the current carrier.
* The URL query part of the HTTP request is no longer displayed in the request list. It is now displayed in the details view.
* Fixed the problem that the JavaScript script timeout mechanism might not work properly.
* Fixed an issue that could occur when a load-balance group contains another group.
* Removed the "All" option from traffic statistics, as it took too long to count all historical traffic when the feature had not been used for a long time.
* You may remove devices in DDNS and Cloud Notification views.

### Version 4.9.4 (Oct 28, 2021)

Bug fixes

### Version 4.9.3 (Sep 30, 2021)

* New feature: Information Panel. Read the manual for more info: <https://manual.nssurge.com/others/panel.html>
* The profile now supports the profile version remark. Read the manual for more info: <https://manual.nssurge.com/release-note/profile-version.html>
* The HTTP scripts now support binary mode to modify the request/response body.
* Other minor improvements and bug fixes.

### Version 4.9.2 (Sep 3, 2021)

Bug fixes

### Version 4.9.1 (Aug 24, 2021)

Bug fixes

### Version 4.9.0 (Aug 20, 2021)

#### New Features: Surge Private DDNS

Surge Mac can associate its external IP address to .sgddns hostname. You may use the hostname with Surge iOS or Surge Mac on another device. The data is synced via iCloud, and the hostname can't be used publicly.

#### New Features: Egress Control (No UI Settings Currently)

* You can use the new internal policy HYBRID to make requests to try Wi-Fi and cellular simultaneously. You can also use the "hybrid=true" parameter to gain a proxy policy for the behavior.
* You can now tell Surge to use IPv4 or IPv6 under a dual-stack environment. Read the manual for more information.

#### New Features: Profile Syntax

You can look up the configuration parameters for the text editing mode within the app. It always displays the syntax for the current version.

#### New Features: Surge VIF IPv6 Stack (No UI Settings Currently)

Surge VIF now supports the IPv6 stack for the raw TCP connections. Use parameter "ipv6-vif=true" to enable.

#### Improvements

* We have changed the proxy benchmark standard. The result is now similar to a ping test result, which ignores the proxy setup cost.
* $request.id is added to the http-request and http-response scripts for continuity among scripts.
* Bug fixes.

### Version 4.8.0 (Jun 14, 2021)

New Features:

* Request Display Filter You may use multiple conditions to filter which requests to show.
* Web Dashboard You may control Surge via a web browser on local or remote devices.

Other bug fixes and improvements.

### Version 4.7.0 (Apr 21, 2021)

#### Rules

* New rule type: SUBNET, which can match SSID/BSSID/router IP address with a wildcard pattern.
* New rule type: CELLULAR-CARRIER, which can match the MCC-MNC code.
* New rule type: CELLULAR-RADIO, which can match the radio access technology of the cellular network.

#### Profile

* You may put partial sections into a detached file. See manual for more information.

#### HTTP API

* Added new profile related HTTP APIs, including GET /profiles, POST /profiles/check
* Added new device management HTTP APIs, including: GET /devices, POST /devices, GET /devices/icon
* The HTTP API, proxy services, and external controller now support listening on IPv6 addresses. (No UI supports. Manual profile editing is required.)
* You may now use 'http-api-tls=true' enable TLS for HTTP API access. (aka HTTPS-API)

Other bug fixes and improvements.

### Version 4.6.0 (Feb 26, 2021)

#### Remote Controller

* You may use this remote controller to view real-time statistics, and events and perform network diagnostics remotely.
* You may use the remote controller to control the DHCP server feature of Surge Mac, including adjusting each device's settings.

#### Cloud Notification

* You can receive Surge Mac's notifications on your iOS device.

#### Scripting

* You may execute a script with Siri or Shortcuts.

#### Policy Group

In this release, we completely refactored the policy group functionality, bringing the following changes:

1. The url-test/fallback/load-balance policy group can no longer be configured with a specific testing URL but with a global testing URL or a policy-configured testing URL. The policy's test results can be used directly in all policy group decisions, eliminating the need to retest each policy group individually.
2. All types of policy groups support mixed nesting. The only requirement is that no circular references can be used.
3. When a group policy is used as a sub-policy of the url-test/fallback/load-balance group.

* The latency of the select/url-test/fallback/ssid group is the latency of the selected policy.
* The latency of the load-balance group is the average of the latencies of all available policies.

4. The timeout parameter of a policy group marks policies with latency exceeding this parameter as unavailable when making decisions for the group. But the maximum time taken to test the policy group is controlled by the global test-timeout parameter. (Default is 5s)
5. When testing a group due to decision making, all sub-policies that the group may use are tested, including sub-policies of the sub-policy group.
6. You may use no-alert=true parameter to suppress notifications for particular groups.

### Version 4.5.1 (Jan 20, 2021)

Bug fixes

### Version 4.5.0 (Jan 19, 2021)

* New Feature: Network Layer Packet Capture: You may now capture the raw TCP/UDP/ICMP packets and inspect them right on the device. Or you can export a standard .pcap file for other tools.
* You can customize the GeoIP database updating URL now.
* The GeoIP database can be updated automatically now.
* Bug fixes and improvements.

### Version 4.4.3 (Oct 28, 2020)

* Optimized for the iPhone 12 series.
* Modified requests are now marked with orange color.
* Bug fixes.

### Version 4.4.2 (Sep 25, 2020)

Bug fixes

### Version 4.4.1 (Sep 23, 2020)

Bug fixes

### Version 4.4.0 (Sep 20, 2020)

New Features:

* HTTP API: Control Surge with HTTP API with another app or from another device.
* Proxy Chain: Connection to a remote host will be performed sequentially from one proxy server to another.

Major Improvements:

* You may mix the external proxies with the proxies of the profile in one policy group now.
* The DNS result view has more information.
* You may use 'policy-regex-filter' to include a part of an external proxy list's content.
* New CELLULAR and CELLULAR-ONLY policy.

Minor Improvements:

* iCloud Drive sync improved.
* You may use $notification.post in a script to post a notification with an action URL.
* The HTTP proxy service now supports basic authentication.
* Surge now enables TCP keepalive for all outgoing connections.
* Surge now supports to use of a URL with a username and password to perform basic authentication for an external resource. (<https://username:password@example.com>)

We recently published official guidance for you to understand Surge. You may find it in the More tab. Version 4.3.2 (Jun 25, 2020) Improvements for the latest iOS system. Version 4.3.1 (Jun 22, 2020) New Feature: Wi-Fi Timeline You may check the connected Wi-Fi network timeline, including entering and leaving time.

Minor Changes

* Optimized the timing system. The DNS time cost is now calculated precisely.
* Bug fixes.

### Version 4.3.0 (Jun 4, 2020)

New Feature: Mock

* You may mock the API server and return a static response. This feature may also be called as Map Local or API Mocking. New Feature: Event Center
* You may now review all historical events.

Minor Changes:

* Optimized the classical start view for Dark Mode.
* The Load-Balance group now supports connectivity testing.
* Add a parameter "use-local-host-item-for-proxy", to use local DNS mapping result even through a proxy protocol.
* The module may adjust contents in \[SSID Setting] now.
* Optimized Wi-Fi Assist feature.
* You may specify the timeout while using the script editor. Version 4.2.2 (May 19, 2020)
* New Feature: Traffic Statistics You may examine the history of traffic usage grouped by the host, by policy, or by the network interface.
* New Feature: DOMAIN-SET We have added a new type of rule: DOMAIN-SET, which may contain millions of sub-rules. No UI configuration in this version. Please configure with the Text Mode

\[Rule] DOMAIN-SET,hostname.txt,REJECT

Each line in the file is a hostname or an IP address. If the hostname starts with a dot, all sub-domains will be matched.

* Other bug fixes and improvements. Version 4.2.1 (Apr 28, 2020) New Feature: Enhanced Wi-Fi Assist
* Surge will try to set up a connection with cellular data when the Wi-Fi network is poor.

Changes in DNS-over-HTTPS

* From this version, if DNS-over-HTTPS is configured, the traditional DNS will only be used to test the connectivity and resolve the domain in the DOH URL.
* The DNS over HTTPS now has a separate parameter: doh-server. The DOH servers in 'dns-server' will be moved to the new parameter after saving.
* The legacy DNS is always required now.
* DOH can be matched with rule 'PROTOCOL,DOH' now.
* Added a new parameter 'doh-follow-outbound-mode'. In the previous version, the DOH client follows the system proxy settings. From this version, all DOH requests will use DIRECT policy by default. If 'doh-follow-outbound-mode' is set, the DOH requests will follow the outbound mode settings regardless of the system proxy settings.

Bug fixes and stability improvements

### Version 4.2.0 (Apr 17, 2020)

New Feature: Module Module is a set of settings to override the current profile. You may use modules to:

* Tweak settings in a non-editable profile, such as managed profile and enterprise profile.
* Change part of settings with one tap. For example, you may use a module to enable MitM for all hostnames and adjust the filter temporarily.
* Use a module written by others to accomplish a particular task. For example, your co-work may share with you a module that rewrites the API requests to a test server.
* When you share one profile among devices, some settings might need modifying for different scenarios. The enabling state of modules won't be synced to other devices, so you can use a module to fulfill.

Minor Improvements:

* Added a new rule type: PROTOCOL.
* Improved the MITM CA certificate install assistant.
* You may now use UI to configure a load-balance policy group.
* You may now use UI to configure SSID suspend.
* Bug fixes.

### Version 4.0.2 (Feb 11, 2020)

* Bug fixes
* Supports choosing profiles in a subdirectory
* A new feature has been added: iperf3 client mode. You may use it to benchmark the bandwidth. Different from the standalone iperf app, you may force the test to use a specified proxy.

A quick guide:

1. Install iperf3 on the proxy server.
2. Run "iperf3 -s" within a screen or tmux session.
3. Start iperf test with Surge. Leave the hostname field empty. 127.0.0.1 will be used and indicates the proxy server itself. Version 4.0.1 (Dec 31, 2019)

* Support VMess proxy protocol
* Bug fixes

### Version 4.0.0 (Sep 18, 2019)

Welcome to Surge 4. We are now introducing the Feature Subscription. As a Pro license owner, you: · Always have access to all your features for a lifetime. · Get free enhancement updates for features you already have for a lifetime. · Get compatibility updates for new systems and new devices for a lifetime. · Get a one-year free Feature Subscription since your purchasing date. · Renew the subscription when a new feature impresses you, totally optional.

New features: · Scripting: Use JavaScript to extend the ability of Surge as your wish. · Dark Mode: Fully adapted for iOS 13 Dark Mode. · DNS over HTTPS: Use DNS over HTTPS (DoH, RFC 8484) to perform DNS queries. · TLS v1.3: TLS v1.3 support for HTTPS/SOCKS5-TLS proxy. · Dropbox: Use Dropbox to sync your profiles across devices.

### Version 3.8.1 (Jun 4, 2019)

Bug fixes

### Version 3.8.0 (May 21, 2019)

Proxy

* Rules can be enabled/disabled now. Try sliding left on it.
* New option for url-test/fallback group: evaluate-before-use. By default, the requests before a connection evaluation will use the first policy in the list and trigger the evaluation. Enable the option to delay the requests until the evaluation is completed.

MitM

* HTTP and MitM engine has been refactored.
* You can now use the URL-REGEX rule for MitM connections.
* You may use the prefix '-' to exclude domains for MitM.
* MitM hostname list now supports port numbers. By default, only the connections to port 443 will be decrypted.

Minor Improvements

* Move the 'External Resources' item to the profile list view. Managed profile users may utilize the view to update resources now.
* It won't bother you anymore that the Cloud profiles disappear sometimes.
* Touch ID / Face ID now allows passcode as a fallback.
* Refined English localization.
* Refined UI details.
* The notification banner is draggable now.
* All advanced options can be edited with UI now. Please do not touch it before reading the manual.

Bug Fixes

* Fixed a bug that the request detail page doesn't update in real-time
* Fixed a bug that the GEOIP rule doesn't work for IPv6 addresses. Version 3.7.1 (Apr 27, 2019)
* Remote Dashboard: You may connect to another device with Surge iOS/Mac running and inspect the requests.
* An active connection can be killed now.
* Bug fixes Version 3.7.0 (Apr 16, 2019)
* Refined UI, including a fullscreen text editor for complex text fields, new colorful icons, and more detail improvements.
* New feature: Always On. Surge may start automatically even after a device reboot.
* The request detail page now updates in real-time.
* The ruleset can be added or edited with UI now.
* Policy group with an external list can be added or edited with UI now.
* Bug and compatibility fixes.

### Version 3.6.1 (Mar 20, 2019)

* Bug fixes

### Version 3.6.0 (Mar 15, 2019)

* Added support for a new proxy protocol Snell.
* You may export all dumped requests to a .surgearchive file and open with Surge Mac Dashboard.
* Optimizations for the request search view.
* Experimental feature: You can enable Network.framework to utilize user-space network stack, which can improve throughput, reduce latency and enable cutting edge features such as Multipath TCP.
* Minor bug fixes.

### Version 3.5.0 (Jan 3, 2019)

* Performance improvements
* Prompts profile changes via iCloud Drive
* Allows to customize Wi-Fi access ports for HTTP & SOCKS5 proxy services
* Supports to update GeoIP database manually
* Copy cURL is now available for all HTTP methods
* Captured body data may be exported to other apps
* Bug fixes

### Version 3.4.2 (Nov 21, 2018)

Bug fixes
