# Surge Mac 网关模式配置指南

Surge 可作为网络网关，用于接管局域网内其他设备的全部网络流量。此功能通常被称为“旁路由”或“透明网关”。

### 工作模式

Surge Mac 提供两种网关模式：

1. **增强模式 (Surge VIF)**: 利用 Surge 的虚拟网络接口作为网关。
2. **Surge VM 网关**: 提供更优的性能和更丰富的功能，但无法与其他虚拟机软件的桥接模式（如 Parallels Desktop, VMware Fusion）同时运行。此模式仅在 Surge Mac 6.0 及以上版本中可用。

{% hint style="info" %}
增强模式可同时用作接管当前设备的网络请求，但 VM 网关仅可用于接管其他设备的网络请求。
{% endhint %}

## 配置方法

1. 在 Surge Mac 中启用“增强模式”或“VM 网关”。
2. 在需要被接管的设备上，进入其网络设置。
3. 将其**网关地址**修改为 Surge Mac 所在设备的 IP 地址（若使用 VM 网关，则修改为 VM 网关的 IP 地址）。
4. 将其 **DNS 服务器**地址修改为 **`198.18.0.2`**。

{% hint style="danger" %}
**注意**：DNS 地址是 **`198.18.0.2`**，而非 `192.168.x.x`。
{% endhint %}

完成以上步骤后，Surge 即开始接管该设备的网络流量。

### 自动化配置 (Surge DHCP)

您可以使用 Surge 的 DHCP 功能来自动为客户端配置网络设置，从而实现自动接管。

**使用前请注意：**

1. **基本知识**: 您需要了解 DHCP 的基本工作原理。
2. **DNS 配置**: 必须在 Surge 的配置文件中至少配置一个有效的上游 DNS 服务器。
3. **禁用现有 DHCP**: 您必须禁用当前网络中的其他 DHCP 服务器（通常由主路由器提供）。
4. **有线连接**: 运行 Surge 的 Mac 设备应使用有线网络连接，强烈不建议使用 Wi-Fi。
5. **静态 IP**: Surge Mac 自身必须使用静态 IP。当启用 Surge DHCP 功能时，Surge 会自动将设备的网络设置为静态 IP。
6. **稳定性**: 开启此功能后，请勿随意移动或关闭运行 Surge 的 Mac 设备，否则可能导致整个网络中断。
7. **紧急恢复**: 如果网络出现问题，请关闭 Surge DHCP 功能，并重新开启主路由器的 DHCP 服务以恢复网络。

默认情况下，新设备加入网络后不会被自动接管。您可以在 Surge 的设备列表中，右键点击目标设备并选择“使用 Surge 作为网关”。如需自动接管所有新设备，可在网关模式配置中勾选“默认使用 Surge 作为网关”选项。

{% hint style="danger" %}
**兼容性提示**: Surge 网关模式的实现机制可能与部分设备存在兼容性问题。建议仅为需要接管的设备开启此功能。
{% endhint %}

### IPv6 RA 覆盖

对于存在 IPv6 的网络环境，仅通过 DHCP 修改 IPv4 设置可能导致流量接管不完整。Surge Mac 6.0 新增了 IPv6 RA (Router Advertisement) 覆盖功能，以确保 IPv6 流量也能被正确接管。

* 此功能不影响客户端的 IPv6 地址分配。
* 如果主路由器的 RA 消息优先级被设为“高”，Surge 可能无法成功覆盖。请将路由器的 RA 优先级调整为“普通”或“低”。

{% hint style="info" %}
如果您不使用 IPv6，也可以直接在路由器设置中禁用整个网络的 IPv6 功能。
{% endhint %}

### 常见问题排查

#### Q: 请求查看器中为何只显示 IP 地址，不显示域名？

**A:** 这是因为客户端的 DNS 未被正确指向 `198.18.0.2` 或 `fd00:6152::2`，导致 Surge 无法通过其 Fake IP 机制将 IP 地址映射回域名。

**解决方案：**

1. **检查配置**: 检查客户端 DNS 设置是否正确。
2. **强制劫持 DNS**: 对于无法手动修改 DNS 的设备，可以在 Surge 网关模式配置中，勾选“劫持所有发送到 53 端口的 UDP DNS 查询”。此选项能解决大部分问题。
3. **处理 IPv6 RA DNS**: 在某些情况下，即使勾选了劫持选项也无效。这可能是因为网络的 IPv6 RA 广播了一个本地链接地址 (link-local) 或路由器自身的 IPv6 地址作为 DNS，导致 DNS 查询绕过了 Surge。请在路由器的 IPv6 设置中，将 RA 的 DNS 地址设置为空，或改为一个公共 DNS 地址（如 Google Public DNS `2001:4860:4860::8888`）。（在配置 Surge IPv6 RA 覆盖时，若检测到此问题会发出警告）

{% hint style="info" %}
部分路由器（如华硕 ASUS 原厂固件）无法自定义 IPv6 RA 的 DNS 设置。可以考虑刷入 Merlin 或 OpenWRT 等第三方固件来解决。
{% endhint %}

4. **处理加密 DNS (DoH/DoT)**: 如果设备或应用内置了加密 DNS 功能，Surge 的 Fake IP 机制将失效。此时，虽然无法显示域名，但仍可通过规则进行流量分流。请为相关规则启用 `extended-matching` 标记，利用 HTTP Host 或 TLS SNI 嗅探结果进行匹配。

{% hint style="info" %}
如果仅仅是少数 Apple 相关域名，如 gateway.icloud.com 和 tether.edge.apple，以 IP 形式进行了请求，这是预期行为，iOS/macOS 对部分域名有特殊的加密 DNS 解析逻辑阻止了 Fake IP 机制。
{% endhint %}

### 已知兼容性问题

#### P2P 客户端

在被接管的设备上运行 P2P 下载软件（如 BT、迅雷）、游戏下载器或直播应用时，可能会因瞬时并发连接数过高而导致 Surge 出现性能问题甚至中断。建议避免在此类设备上使用网关模式。我们将在未来的更新中优化此问题。

{% hint style="info" %}
**技术说明**: 传统路由器在数据包层面工作，处理大量并发连接（如 1000 个）仅涉及 NAT 表的少量开销，压力很低。 而 Surge 工作在应用层，需要对每个连接进行协议嗅探、规则匹配和日志记录。单个大流量连接不成问题，但瞬间产生数千个新连接会带来巨大的处理开销。
{% endhint %}

#### PlayStation Portal™ Remote Player

当 PS Portal 被 Surge 网关模式接管时，异地串流无法正常开启。

这是因为 PS Portal 异地串流的逻辑与 Surge 的工作模式存在冲突，由于 Surge 需要进行 Protocol Sniffing，会对所有 TCP 请求先接受握手再进行处理，而 PS Portal 检查是否是同局域网的方式是直接访问 PS5 的内网 IP，检查是否能完成 TCP 握手，所以导致误判为同局域网。

可以通过增加一条规则的方式解决该问题，如：

`IP-CIDR,192.168.0.100/32,REJECT-DROP,pre-matching,no-resolve`

其中的 IP 地址为 PS5 的内网 IP 地址，规则一定需要带上 `pre-matching` 标记，这样 PS Portal 便不会误判，可以正常启用异地串流流程。

另外，也可以利用该机制，欺骗 PS Portal PS5 处于同一局域网中，这样便可使用自己的私有网络畅玩 PS Portal。如果使用的是 Surge Ponte，只需增加规则将 PS Portal 对 PS5 的访问转至 PS5 所在网络即可。
