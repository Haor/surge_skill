# Surge Mac 6.0 Release Note

<a href="https://dl.nssurge.com/mac/v6/Surge-latest.zip" class="button primary">下载 v6 版本</a>

在 Surge Mac 6.0 中，我们再次带来了多项创造性的独有新功能，同时升级了全新的设计。

### Surge Gateway Mode

在 Surge Mac 6.0 中，原本的 Surge DHCP Server 功能升级为了全新的 Surge Gateway Mode，包含众多新特性：

1. Surge Gateway VM

旧版本中，Surge 依赖系统的 utun 设备和 IP forwarding 机制处理来自其他设备的网络流量，这带来了不必要的开销，也限制了 Surge 的功能。现在，Surge 将使用 macOS 的 VMNET framework，以虚拟机的方式接入网络，直接工作在 Layer 2。（类似于使用虚拟机运行 RouterOS） 这不仅提高了性能，也给 Surge 实现更多的网关功能提供了可能性。

2. IPv6 RA Override

旧版本中使用 Surge DHCP 模式时，遇到的一大问题是与 IPv6 相冲突，因为 IPv6 RA 下发的 DNS 会导致 Surge 的 Fake DNS 机制失效。

现在 Surge 可以发送更高优先级的 RA 消息，覆盖并接管选定设备的 IPv6 网关，不仅解决了原先可能出现的 DNS 问题，也完成了对设备的 IPv6 网络的完全接管。 而且这种接管是定向、非排他性的，不需要对原本网络的 IPv6 进行任何调整即可使用（除非原路由 RA 消息优先级设置为了高，需要手动降低为中），也不会影响其他非选定设备。

{% hint style="info" %}
如果需要上述两个新特性，需要关闭 Gateway Mode 重新开启以打开相应的开关。
{% endhint %}

{% hint style="warning" %}
使用 IPv6 RA Override 功能，需要保证路由器的 IPv6 RA 广播的 DNS 地址，不为 fe80::/10 的 link-local 地址，也不可以为路由器自身的 IPv6 地址。 绝大多数路由可以自定义 IPv6 RA DNS 地址，将其置空或者修改为任意公网 DNS 即可。少数路由不支持修改，已知不兼容的路由为

* ASUS 全系（可通过更换 Merlin/OpenWRT 固件解决）
  {% endhint %}

{% hint style="info" %}
更多利用 Surge Gateway VM 的新功能尚在开发中，如 UDP FastPath，将在后续版本中加入。
{% endhint %}

### Surge VIF Engine

Surge Mac 5.0 时我们推出了 VIF v2 工作模式，利用系统的 Packet Filter 取得了极其强悍的性能表现，在 M3 下测试可达 \~ 37 Gbps，后续又更新了 v3 版本改善了兼容性。

然而由于 macOS Sequoia 系统的新兼容性问题，我们被迫放弃了原本的 utun VIF 方案，转而使用 Apple 目前推荐的 Network Extension 框架实现 Surge VIF，以确保出现问题的可能性最低。NE 下 v2 与 v3 并不能工作，更雪上加霜的是，NE 没有给开发者开放足够的接口去进行调优，使得我们在 v1 中的许多性能优化也失效了。

为此，在 Surge Mac 6.0 中，我们完全重写了 Surge VIF，使用了最新的理论和极致的优化，大幅提高了增强模式下的表现。在 M4 Mac Mini 上进行回环 iperf 测试，上行最大吞吐量可达 \~30Gbps，下行 \~23Gbps，远超其他同类软件。最大吞吐量不仅意味着可以处理更高的流量，也表示在低带宽时开销也更低，对 CPU 占用少且能耗低。

{% hint style="success" %}
从 Surge Mac 6 开始，我们提供**最优性能保证**，如果在购买 Surge 后，发现 Surge 性能指标（包含吞吐量和延迟）在同等条件下劣于其他软件，在购买 30 天内都可以以此申请全额退款。
{% endhint %}

同时本次重写还优化了对于 UDP 流量的处理，特别是大吞吐量下的表现，在 M4 Mac Mini 上进行回环 iperf 测试，可达 10Gbps（此为 iperf3 UDP 测试下的最高限制）。

同时由于 WireGuard 协议栈也依赖于 Surge VIF 的实现，其性能也得到了一定提高。

其他技术细节上，Surge VIF 现在新增了 Active Queue Management （AQM）和 TCP pacing 机制，用于处理大吞吐量时的拥塞和其他兼容性问题。

{% hint style="info" %}
你也可以自行进行 iperf3 测试 TCP 回环吞吐量，首先开启一个终端，执行 `iperf3-darwin -s` 启动测试服务端。 再开启另一个终端，执行 `iperf3-darwin -Rc lvh.me` 即可测试下行吞吐量，执行 `iperf3-darwin -c lvh.me` 测试上行吞吐量。
{% endhint %}

### Surge Ponte 2.0 - Multiple Channels

在 Surge Mac 5.0 中，我们推出了 Surge Ponte 功能用于组建点到点的私人加密网络，得益于创新的工作模式，这可能是使用起来最简单的内网穿透方式。

6.0 中 Surge Ponte 得到了重要强化，Surge Ponte 的服务端不再被限制于只能选择一种工作模式了，你可以同时开启多种穿透模式，甚至选择多条代理线路进行穿透。当 Ponte 客户端进行连接时，将自动选择最快速的通道进行连接。

同时，现在 Surge Ponte 新增了 IPv6 直连通道，仅需在防火墙中开放端口，Surge Ponte 就可以通过 IPv6 直连完成组网。

另外，Surge Ponte 不再依赖公共的 STUN 服务器，开始使用自建的 STUN 服务，由于该服务专门为 Surge Ponte 设计，响应速度得到了明显提升。

{% hint style="info" %}
请注意，Surge iOS 也需要升级到最新测试版本才能使用该特性，使用旧版只会使用第一个通道。
{% endhint %}

### Surge Smart Group

6.0 中 Smart Group 也得到了增强，我们完成了 Smart Group 对 UDP 连接的优化，现在 UDP 流量使用 Smart Group 也会享受到 Smart Group 的智能调优。

同时 Smart Group 本身也得到了强化与改进，以适应更多的情形。Smart Group 与 Snell 协议 reuse 机制的冲突也已经解决。

### Snell v5

Surge 自有的代理协议 Snell 升级到了 v5，带来了两个新特性

{% hint style="success" %}
Snell 协议同样享有**最优性能保证**，如果在购买 Surge 后，发现 Snell 代理协议性能指标（包含吞吐量和延迟）在同等技术条件下劣于其他软件，在购买 30 天内都可以以此申请全额退款。
{% endhint %}

#### Dynamic Record Sizing

该特性将提高在存在丢包的网络环境下延迟表现。技术细节可参考 ：[Cloudflare Blog](https://blog.cloudflare.com/optimizing-tls-over-tcp-to-reduce-latency/)

#### QUIC Proxy Mode

我们之前专门解释过为什么对 QUIC 进行代理转发不是一个好主意，并且加入了 block-quic 参数用于自动屏蔽 QUIC 请求。但是无奈的是，最近发现有些应用开始强依赖 QUIC，若屏蔽 QUIC 流量可能会导致其工作异常。

因此 Snell v5 加入了专为 QUIC 流量设计的 QUIC Proxy 模式，该模式工作属于 UDP over UDP，以避免 TCP over UDP 问题。（服务端需开放 UDP 端口）

* 该工作模式为 QUIC 进行了特殊优化，仅当 Surge 识别到 QUIC 流量时会启用，其他 UDP 流量依然使用 UDP over TCP 模式。
* QUIC Proxy 只会对 QUIC Handshake 数据包进行强加密，以保护 SNI 和目标主机名，同时进行鉴权。后续的所有 QUIC 数据包，由于本身已经被 QUIC 强加密，将直接以裸包进行转发，大幅降低了不必要的加解密开销。同时由于未引入额外字节，不会影响 QUIC 的 PMTU 探测。

服务端下载链接请见：[Snell](https://kb.nssurge.com/surge-knowledge-base/zh/release-notes/snell)

{% hint style="info" %}
Snell v5 的服务端可以向下兼容 v4 客户端，如果不想使用 QUIC Proxy Mode 功能，客户端设置为 v4 版本即可，Dynamic Record Sizing 的优化只和服务端有关。
{% endhint %}

#### 出口控制

* 支持配置 `egress-interface` 参数控制出口 interface（需要 root 权限或者给予`CAP_NET_RAW/CAP_NET_ADMIN` 授权，同时该 interface 上需要有目标地址和 DNS 的路由表）
* 支持 systemd 的 Socket Activation 机制，可用于配置 network namespace，也可用于出口 interface 配置。我们会在之后提供配置样例。

### 流量统计系统

流量统计系统得到了大幅升级，现在能以目标主机名为维度进行统计了，同时统计数据的时间维度扩大到了月度，除了本月外也会保留上月的数据。

同时，越来越多的应用开始使用子进程进行网络请求，这造成了统计和查看上的混乱，新版本中可以将应用包内的所有进程都合并进行统计。

### Fake DNS v6

Surge DNS server 现在同时监听于虚拟 IPv6 地址 fd00:6152::2，可以对 AAAA 查询返回 Fake IPv6 地址，也就是说如果有需要，Surge 现在可以工作在纯 IPv6 环境中。

### Linked Profile

为了解决托管配置的本地修改难题，我们再次优化了 Linked Profile 的设计，现在 #include 语句可以直接使用一个托管配置的 URL 了。

同时，v6 版本在安装托管配置时，将会主动提示用户创建 Linked Profile，如果已经在使用托管配置，现在在尝试修改配置时，也会主动引导创建 Linked Profile。

### 界面更新

新版本带来了全新的设计，Surge Mac 6.0 中着重优化了数据展现，现在你可以在首页看到更多维的数据。

请注意，本次设计更新还没有全面为 macOS 26 进行调整，等待 macOS 26 风格稳定后，我们会再次进行界面更新适配。

同时，几乎每个页面都经过了重新优化，以确保符合最新 macOS 设计标准。

### 其他细节更新

* `IP-CIDR` 规则允许直接使用单 IP，即隐含 `/32`。
* `PROTOCOL,TCP` 规则现在也会对 HTTP 和 HTTPS 连接生效了，保证与 `PROTOCOL,TCP` 规则的语义一致性。
* 优化对特别巨大的配置的处理性能（数百条代理和策略组），现在即使加载巨型配置也不会产生卡顿。
* HTTP request/response 规则新增 `full-header-mode` 参数，开启后 `headers` 字段将以数组格式提供，以保证在处理多个同名字段（如 `Set-Cookie`）时的兼容性。
* 不支持 UDP 的代理的默认回退行为改为 REJECT
* 新增 HTTP 的 zstd 压缩算法支持
* 全局优化 wildcard 匹配性能
* 重做高级设置页面，现在所有高级参数都可以通过 UI 直接编辑了。
