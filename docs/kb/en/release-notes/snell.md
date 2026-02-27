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

* Fixed a low-probability crash caused by an assertion.

### v5.0.0

#### Dynamic Record Sizing

This feature will improve latency performance under network environments with packet loss. For technical details, refer to: [Cloudflare Blog](https://blog.cloudflare.com/optimizing-tls-over-tcp-to-reduce-latency/)

#### QUIC Proxy Mode

Snell v5 introduces a special QUIC Proxy mode designed for QUIC traffic. This mode works as UDP over UDP to avoid TCP over UDP issues. (The server needs to open a UDP port.)

* This working mode is specially optimized for QUIC. It is only enabled when Surge detects QUIC traffic; other UDP traffic still uses the UDP over TCP mode.
* QUIC Proxy will only strongly encrypt the QUIC Handshake packets to protect SNI and target hostnames, while also performing authentication. All subsequent QUIC packets, already strongly encrypted by QUIC itself, will be forwarded as raw packets, greatly reducing unnecessary encryption and decryption overhead. Additionally, since no extra bytes are introduced, QUIC's PMTU probing will not be affected.

#### Egress Control

* Supports configuration of the `egress-interface` parameter to control the egress interface (requires root privileges or `CAP_NET_RAW/CAP_NET_ADMIN` license, and the interface must have routing tables for the target address and DNS).
* Supports systemd's Socket Activation mechanism, which can be used to configure network namespaces as well as for egress interface profile. We will provide configuration examples later.

{% hint style="info" %}
The Snell v5 server is backward compatible with v4 clients. If you do not wish to use the QUIC Proxy Mode feature, set the client to v4. The Dynamic Record Sizing optimization only relates to the server.
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
