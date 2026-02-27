# Snell

Snell is a lean encrypted proxy protocol developed by our team. Here are some highlights:

* Extreme performance.
* Support UDP over TCP relay.
* Single binary with zero dependencies. (except glibc)
* A wizard to help you start.
* Proxy server will report remote errors to the client if an error encounters. Clients may choose countermeasures for different scenarios.

> The Snell protocol is intended for Surge users only. Please do not reverse-analyze the protocol and make a compatible client of it. We want to keep the user base as small as possible; thanks for your understanding.

{% code overflow="wrap" %}

```markdown
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-armv7l.zip
```

{% endcode %}

## Release Notes

### v5.0.1

* 修正了一处因断言低概率出现的崩溃问题

### v5.0.0

#### Dynamic Record Sizing

该特性将提高在存在丢包的网络环境下延迟表现。技术细节可参考 ：[Cloudflare Blog](https://blog.cloudflare.com/optimizing-tls-over-tcp-to-reduce-latency/)

#### QUIC Proxy Mode

Snell v5 加入了专为 QUIC 流量设计的 QUIC Proxy 模式，该模式工作属于 UDP over UDP，以避免 TCP over UDP 问题。（服务端需开放 UDP 端口）

* 该工作模式为 QUIC 进行了特殊优化，仅当 Surge 识别到 QUIC 流量时会启用，其他 UDP 流量依然使用 UDP over TCP 模式。
* QUIC Proxy 只会对 QUIC Handshake 数据包进行强加密，以保护 SNI 和目标主机名，同时进行鉴权。后续的所有 QUIC 数据包，由于本身已经被 QUIC 强加密，将直接以裸包进行转发，大幅降低了不必要的加解密开销。同时由于未引入额外字节，不会影响 QUIC 的 PMTU 探测。

#### 出口控制

* 支持配置 `egress-interface` 参数控制出口 interface（需要 root 权限或者给予`CAP_NET_RAW/CAP_NET_ADMIN` 授权，同时该 interface 上需要有目标地址和 DNS 的路由表）
* 支持 systemd 的 Socket Activation 机制，可用于配置 network namespace，也可用于出口 interface 配置。我们会在之后提供配置样例。

{% hint style="info" %}
Snell v5 的服务端可以向下兼容 v4 客户端，如果不想使用 QUIC Proxy Mode 功能，客户端设置为 v4 版本即可，Dynamic Record Sizing 的优化只和服务端有关。
{% endhint %}

### v4.1.1

* Fix a potential crash that may occur during UDP forwarding.

{% code overflow="wrap" %}

```markdown
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-armv7l.zip
```

{% endcode %}

### v4.1.0

* Add a dns parameter for customizing DNS server addresses, supporting multiple address configurations.
* Update the DNS library c-ares to the latest version to resolve compatibility issues with specific DNS records.
* Add output of the currently used DNS server at startup.
* Adjust log output to lower broken pipe error messages to verbose level.
* Update libuv to v1.48.0 to fix potential crashes when accessing IPv6 addresses on certain systems.
* Improve log information for DNS errors.
* Fix an issue where certain invalid DNS records could cause a crash.

### v4.0.1

Fixed a bug that UDP packets can't be forwarded to IPv6 addresses.

## Surge Mac as Snell Proxy Server

You may also use Surge Mac as a Snell proxy server (Starting from version 3.1.0). Add the following lines to your profile.

```
[Snell Server]
interface = 0.0.0.0
port = 6160
psk = RANDOM_KEY_HERE
```

The embedded Snell server in Surge uses the Snell V1 protocol.
