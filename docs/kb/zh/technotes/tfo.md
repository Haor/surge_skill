# 关于 TCP Fast Open

## 什么是 TCP Fast Open（TFO）

TCP 连接需要进行三次握手方可开始传输数据。这使得每个 TCP 连接都需要浪费掉一个 RTT 去建立连接。这是因为 TCP 协议被发明时，网络还处于 LAN 局域网时代，RTT 只有毫秒级，所以这个设计并没有问题。

而到了互联网与无线网络时代，RTT 通常可高达几十上百毫秒。这时被浪费掉的这一个 RTT 便成为不可忽略的开销。TCP Fast Open 也因此而生。TFO 的具体实现方式简单来说，就是在三次握手时的第一个 SYN 包里，附带上所需要传输的第一个数据包，如 TLS 协议的 Client Hello。当握手完成时，服务端就已收到了第一个数据包，开始进行后续的传输。这样就挽回了握手导致的延迟损失。（具体实现中还有很多细节，如 cookie，这里不再展开）

### 兼容性问题

但是这项改进遇到了一个问题，由于这是一项对 TCP 协议的扩展，中间网络设备有可能不支持该特性。比方说有些防火墙（NAT）会直接将带有数据段的 SYN 包认为是非法数据包直接抛弃。导致使用了 TFO 的连接完全无法建立。（如中国的移动数据网络）

为此，操作系统不得不引入一个 blackhole 机制，当对某 IP 以 TFO 进行握手时，如果在一定时间内都没有收到回应，那么就重新尝试以非 TFO 方式进行握手，如果成功，则将该 IP 加入黑名单，之后不再以 TFO 进行握手。

但该机制有两个问题：

1. 可能因为网络正常波动丢包而误判，导致 IP 进入黑名单，后续连接全部丧失 TFO 特性。
2. 有的时候是在特定网络下 TFO 无效（如数据网络），但操作系统的黑名单只记录了目标 IP，所以在切换网络后，依然无法使用 TFO。

在我们的测试中，一段时间后代理服务器 IP 几乎一定会被加入黑名单。

{% hint style="info" %}
两个关于 macOS 的 Tips：

1. 可使用 sudo sysctl -w net.inet.tcp.clear\_tfocache=1 命令，强行清空系统的黑名单。
2. 可使用 sudo sysctl -w net.inet.tcp.disable\_tcp\_heuristics=1，强行关闭黑名单功能。（但同时还会影响 ECN 与 MPTCP）
   {% endhint %}

### Surge 中的相关设置

在 Surge 中使用 TFO 时，首先需要为对应的代理策略配置 `tfo=true` 参数。

为了解决操作系统的 blackhole 机制可能带来的问题，Surge 允许通过子网设置手动配置 TFO 可用性，绕过系统的限制。

```
[SSID Setting]
"SSID:My Home" tfo-behaviour=force-enabled
```

`tfo-behaviour` 参数有 3 个选项：

1. `auto`：使用系统的默认黑名单行为。
2. `force-enabled`：在该网络下无视系统黑名单，始终使用 TFO 进行握手。
3. `force-disabled`：在该网络下完全不使用 TFO。

在配置之前，请务必先在该网络下测试 TFO 是否可用，以避免配置为 force-enabled 导致代理完全无法联通。

### 请求日志

在请求的日志中，会显示关于 TFO 的细节信息，一些常见的结果如下：

* `TCP Fast Open was successful (tfo_syn_data_sent, tfo_syn_data_acked)`

  表示 TFO 已成功。
* `Attempted to use TCP Fast Open but failed (tfo_heuristics_disable)`

  表示由于被加入黑名单，TFO 已自动禁用。
* `Attempted to use TCP Fast Open but failed (tfo_cookie_req, tfo_no_cookie_rcv)`

  表示尝试进行了 TFO 握手，但是服务端未开启 TFO 支持。
