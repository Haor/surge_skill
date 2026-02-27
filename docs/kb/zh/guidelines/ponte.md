# Surge Ponte 指引

Surge Ponte 是一种在运行 Surge Mac 和 iOS 设备之间的私有网络。

* 无需繁琐配置。
* Surge 会自动选择最合适的通道建立连接。
* 始终端到端加密。
* 设备信息和加密密钥通过您的 iCloud 同步，除了您选择的代理服务器外，您的数据不会经过任何第三方服务器。

该文章将协助您开始使用 Surge Ponte。

### 了解 Ponte 类型

Surge Mac 可以用作 Surge Ponte 服务端和客户端，而 Surge iOS 只能用作 Surge Ponte 客户端。

当配置 Surge Mac 作为 Surge Ponte 服务端时，有 3 种不同的配置方式。

1. 直接 NAT 穿透

仅当当前网络处于 Full Cone NAT 时可用，当前网络的 NAT 类型和路由器的具体型号、ISP 有关，一般很难改变。

2. 通过代理 NAT 穿透

可在任何网络情况下使用，需借助一支持 UDP 转发的代理实现。（请注意，如果你使用的是付费代理服务，使用 Surge Ponte 时同样会消耗你的流量。）

3. 静态端口转发（高级用户）

如果您有公网 IP 地址并且知道如何配置路由器，则可以选择配置静态端口转发。

### 在 Surge Mac 上配置 Surge Ponte

1. 在侧边栏中选择“概览”，然后打开 Surge Ponte 开关。
2. 点击下一步。
3. 等待 Surge 测试当前网络的 NAT 类型。
4. 如果测试结果是：
   * Full Cone NAT（A）：您可以选择任意方法来设置 Surge Ponte。
   * 其他（B/C/D）：您可以选择通过代理的 NAT 穿透，或者如果您有公网 IP 地址并且知道如何配置路由器，则可以选择静态端口转发。
5. 如果您选择了通过代理的 NAT 穿透，请选择一个支持 UDP 中继的代理（Snell/shadowsocks/Trojan/SOCKS5/WireGuard）。
6. Surge 将测试代理是否合格。代理服务器不能位于 NAT 或防火墙后面，除非它们已经适当配置以允许 Full Cone NAT。
7. 为当前设备选择一个名称，例如 MyMacMini。名称不区分大小写，只能包含字母、数字、下划线和连字符。
8. 在其他设备上打开 Surge Ponte。Surge iOS 配置起来会非常简单，因为它只能用作客户端。

### 使用 Surge Ponte

你现在可以从任何一个运行 Surge 且登录了相同 iCloud 的设备上访问这个设备了。有两种使用方式：

1. 你可以使用域名 `ponte-name.sgponte`（如 mymacmini.sgponte）访问这个设备上的服务，如你在该设备上的 8080 端口上运行了一个 HTTP 服务器，那在其他设备上可以直接访问 <http://mymacmini.sgponte:8080/>
2. 你也可以使用策略 `DEVICE:PONTE-NAME` 使用该设备作为跳板使用其访问其他网络，如内网中的 NAS。规则示例：

```
IP-CIDR,192.168.30.0/24,DEVICE:MyMacMini
```

<details>

<summary><mark style="color:purple;">用例 #1：</mark>配合 Surge Ponte 和系统文件共享服务，你可以随时从 iOS 设备上访问 Mac 中的文件。</summary>

1. 在 Surge Mac 上开启 Surge Ponte，这里取名为 macbook。
2. 在 macOS 的系统设置中，找到通用›共享›文件共享，打开开关。
3. 在 iOS 设备上开启 Surge iOS，确认 Surge Ponte 界面中可以看见 Mac 设备。
4. 打开系统自带的「文件」app，切换到「浏览」页，点击右上角的更多按钮，选择连接服务器。
5. 输入 macbook.sgponte，点击下一步。
6. 选择注册用户，输入 Mac 的用户名和登录密码。

</details>

<details>

<summary><mark style="color:purple;">用例 #2：</mark>可以配合 Surge 的 DNS 映射功能访问家庭网络中的设备，而无需配置全网段规则。</summary>

1. 在 Surge Mac 上开启 Surge Ponte，这里取名为 `macbook`。
2. 在 Surge Mac 上配置 DNS 映射：nas.myhome = 192.168.1.20，具体 IP 与名字为需要访问的设备。
3. 在客户端设备上配置规则，`DOMAIN-SUFFIX,myhome,DEVICE:macbook`，请注意由于该域名无法在客户端设备上被解析，所以该规则必须放置于会触发解析的 IP 类规则之前。
4. 通过浏览器访问 nas.myhome 即可。

</details>

### 客户端侧代理

在客户端同样可以配置代理以访问 Ponte 服务端，这不是必须的。即使服务端配置了代理 NAT 穿透，客户端也不需要配置代理，但配置代理可以帮助突破某些网络环境下的 UDP 流量封锁。

比如由于中国大陆的出境网络通常于网络高峰期会出现 UDP 流量严重丢包的现象，若使用了一个境外的代理作为 NAT 穿透，客户端最好也配置使用相同的代理访问 Ponte 设备。

<figure><img src="https://3176820532-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FnRjbzkErvUl5IX5jdskH%2Fuploads%2Fgit-blob-b602c8debd4fe5f5d4c37a15876c60d111ce0000%2Fponte-nat.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Vector 为 Surge Ponte 服务所使用的底层代理协议。
{% endhint %}

### 提示

1. 你可以将内网网段设置为一个不常见的子网地址，如 192.168.150.0/24，已确保不会在其他网络下访问内网时产生地址冲突。
2. 当 Ponte 客户端与服务端处于同一个 LAN 时，将自动通过 LAN 建立连接，不会使用 NAT 穿透或代理服务器。
3. 当访问的 Ponte 设备名就是当前设备时，该策略将被转换为 DIRECT 策略。
4. 当使用 `ponte-name.sgponte` 进行访问时，实际上是动态创建了 `DEVICE:ponte-name` 策略并使用，且在远端会将 `ponte-name.sgponte` 解析为 127.0.0.1。所以即使是监听于 127.0.0.1 上的服务也可以被访问。
5. `DEVICE:NAME` 策略可以不需要在 `[Proxy]` 处声明就直接使用，且也可以用在 `[Proxy Group]` 中作为子策略，如与 Subnet Group 联用。
6. 目前 Surge Ponte 仅支持通过 IPv4 建立连接，但是可以转发 IPv6 请求。
