# NAT 类型详解

在进行 UDP 转发时，不同的转发映射策略会导致 UDP 穿透功能的差异，这种差异通常被称为 **NAT 类型**。

NAT 类型的命名在不同软件和文档中可能有所不同，但一般可分为以下几类：

* **A 类**：Full Cone NAT（也称 1 类或开放型）
* **B 类**：Address Restricted Cone NAT（也称 2 类或中等型）
* **C 类**：Port Restricted Cone NAT
* **D 类**：Symmetric NAT

NAT 类型主要由你的**路由器**决定，但也可能受到互联网服务提供商（ISP）的限制。

***

### Surge 对 NAT 类型的影响

当启用 Surge 并通过其 VIF 接管网络后，由于增加了一层转换，会对 NAT 类型产生影响。具体表现为：

* 如果原始网络为 **A 类 Full Cone NAT**，Surge 会将其降级为 **B 类 Address Restricted Cone NAT**。
* 如果原始网络为 **B 类及以下**，则 NAT 类型保持不变。

这种变化不仅影响本机所有进程，还会作用于通过网关模式接管的其他设备。

若想避免 NAT 级别降低（例如，确保在线游戏联机），可以通过配置 **`always-real-ip`** 参数解决问题。配置时，需确保该参数覆盖相关的 **STUN 域名**（可通过 Surge 的请求列表确认具体域名）。

Surge Mac 内置的 **Game Console STUN** 模块即为常见游戏主机的 STUN 域名预设了配置：

```
always-real-ip = *.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com
```

暴力一点，可以使用该配置覆盖绝大多数 SUN 服务器，通常不会有明显的副作用：

```
always-real-ip = *stun*
```

### 使用代理时的 NAT 类型

当请求通过**代理策略**处理时，其对应的 NAT 级别由**代理服务器的 NAT 类型**决定，与本地网络的 NAT 类型无关。你可以通过 Surge Mac 的**代理诊断功能**（位于窗口菜单 › 代理诊断）测试代理服务器的 NAT 级别。

### Surge Ponte 对 NAT 类型的要求

若希望在不借助代理服务器的情况下使用 Surge Ponte，则本地网络需要为 A 类 Full Cone NAT，这需要你的路由器与 ISP 共同支持。

若通过代理服务器进行穿透，则与本地 NAT 类型无关，仅需要关注代理服务器的 NAT 类型。如果该服务器由您自己所维护，通常情况下设置防火墙放行所有端口的 UDP 流量即可。

### Surge 的 NAT 类型测试准确吗？

所有的 NAT 类型测试工具，都是靠发出不同的 STUN 请求，观察是否能收到响应以进行判断的，如果网络丢包情况严重，或者 STUN 服务器异常，则可能导致测试结果偏低。Surge 在测试时或多次发包以保证测试结果尽量准确。
