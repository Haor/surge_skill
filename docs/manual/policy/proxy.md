Title: Proxy Policy · GitBook

URL Source: https://manual.nssurge.com/policy/proxy.html

Published Time: Tue, 20 Jan 2026 02:39:13 GMT

A proxy policy indicates forwarding the request to another proxy server. Surge supports HTTP/HTTPS/SOCKS5/SOCKS5-TLS and more proxy protocols.

Section `[Proxy]` declares proxy policies. You can create multiple proxies for different rules.

The configuration lines example:

```
[Proxy]
ProxyHTTP = http, 1.2.3.4, 443, username, password
ProxyHTTPS = https, 1.2.3.4, 443, username, password
ProxySOCKS5 = socks5, 1.2.3.4, 443, username, password
ProxySOCKS5TLS = socks5-tls, 1.2.3.4, 443, username, password, skip-common-name-verify=true
```

Proxy Type
----------

Surge supports the most common standard proxy protocols.

*   HTTP Proxy: `ProxyHTTP = http, 1.2.3.4, 443, username, password`
*   HTTPS Proxy (HTTP Proxy via TLS): `ProxyHTTPS = https, 1.2.3.4, 443, username, password`
*   SOCKS5: `ProxySOCKS5 = socks5, 1.2.3.4, 443, username, password`
*   SOCKS5 via TLS: `ProxySOCKS5TLS = socks5-tls, 1.2.3.4, 443, username, password`
*   SSH
*   WireGuard (L3 layer VPN as proxy)

Surge also supports several popular community proxy protocols.

*   Snell: `Proxy-Snell = snell, 1.2.3.4, 8000, psk=password, version=4`
*   Shadowsocks: `Proxy-SS = ss, 1.2.3.4, 8000, encrypt-method=chacha20-ietf-poly1305, password=abcd1234`
*   VMess: `Proxy-VMess = vmess, 1.2.3.4, 8000, username=0233d11c-15a4-47d3-ade3-48ffca0ce119`
*   Trojan: `Proxy-Trojan = trojan, 192.168.20.6, 443, password=password1`
*   TUIC: `Proxy-TUIC = tuic, 192.168.20.6, 443, token=pwd, alpn=h3`
*   Hysteria 2: `Proxy-Hysteria = hysteria2, 192.168.20.6, 443, password=pwd, download-bandwidth=100`iOS 5.8.0+Mac 5.4.0+
*   AnyTLS: `Proxy-AnyTLS = anytls, 192.168.20.6, 443, password=pwd`iOS 5.17.0+Mac 6.4.3+

### UDP Relay

Surge supports UDP relay of SOCKS5, Snell v4/v5, Shadowsocks, Trojan, WireGuard, Hysteria 2, and TUIC protocols. The UDP relay support for shadowsocks and SOCKS5 proxies should be turned on manually by appending the parameter `udp-relay=true` since the server may not always support the UDP relay.

Parameters
----------

#### Proxy Chain

*   `underlying-proxy`

Use a proxy to connect another proxy, aka proxy chain. It can be another proxy policy's or policy group's name.

#### Common Parameter for Proxy via TLS (HTTP, SOCKS5-TLS, VMess, Trojan, TUIC, Hysteria 2, AnyTLS)

*   `skip-cert-verify`: Optional, "true" or "false" (Default: false).

If this option is enabled, Surge will not verify the server's certificate.

*   `sni`: The default value is the proxy hostname

You may customize the Server Name Indication (SNI) during the TLS handshake. Use sni=off to turn off SNI completely. By default, Surge sends the SNI using the hostname like most browsers.

*   `server-cert-fingerprint-sha256`: Optional.

Use a pinned server certificate instead of the standard X.509 validation.

#### Parameter for HTTP/HTTPS protocol

*   `always-use-connect`: Optional.

Always use the HTTP CONNECT method to relay the request, even for plain HTTP requests.

#### Parameter for SOCKS5 Protocol

*   `udp-relay`: Optional. Since the UDP relay is optional for the SOCKS5 server, you must enable the UDP relay explicitly.

#### Parameter for Snell Protocol

See knowledge base [Snell](https://kb.nssurge.com/surge-knowledge-base/release-notes/snell) for more information.

*   `psk`: Required.
*   `version`: Required.
*   `reuse`: Optional. Connection reuse is an optional feature for Snell V4.
*   `obfs`: Optional. `http` is the only option supported by Snell V4.
*   `obfs-host`: Optional.
*   `obfs-uri`: Optional.

#### Parameter for Shadowsocks Protocol

*   `udp-relay`: Optional. Since the UDP relay is optional for the shadowsocks server, you must enable the UDP relay explicitly.
*   `obfs`: Optional. `http` or `tls`
*   `obfs-host`: Optional.
*   `obfs-uri`: Optional.
*   `udp-port`: Optional. When performing UDP forwarding, use another server port number. This can be used when the server's TCP and UDP services do not listen on the same port (e.g., if ShadowTLS is configured). iOS 5.14.0+Mac 5.9.0+

#### Parameter for VMess Protocol

*   `ws`: Optional. Use the Web Socket transport layer.
*   `ws-path`: Optional.
*   `ws-headers`: Optional.
*   `encrypt-method`: Optional. Possible values: `chacha20-ietf-poly1305` or `aes-128-gcm`.
*   `vmess-aead`: Optional.

#### Parameter for Trojan Protocol

*   `ws`: Optional. Use the Web Socket transport layer.
*   `ws-path`: Optional.
*   `ws-headers`: Optional.

#### Parameter for TUIC

*   `token`: Required.
*   `alpn`: Optional. It must match the server's ALPN setting.
*   `port-hopping`: Optional. Configure a list of ports or ranges (for example `1234;5000-6000`). Surge will periodically rotate among them instead of using the main port.
*   `port-hopping-interval`: Optional. Interval in seconds for hopping, defaults to 30. When this field is set, the primary port in the declaration is ignored.

#### Parameter for Hysteria 2 iOS 5.8.0+Mac 5.4.0+

*   `download-bandwidth`: Optional, in Mbps.
*   `port-hopping`: Optional. Semicolon-separated list of explicit ports or ranges. Enables the port hopping mode described in the release notes.
*   `port-hopping-interval`: Optional. Interval in seconds, default 30. After enabling port hopping, the leading port argument is no longer used.

#### Parameter for AnyTLS v2 iOS 5.17.0+Mac 6.4.3+

*   `reuse`: Optional. According to the AnyTLS specification, connection reuse is enabled by default. You may disable it by setting `reuse` to false.

Client Certificate for TLS Proxy
--------------------------------

Surge supports client certificate verification for TLS-based proxies.

Example:

```
[Proxy]
Proxy = https, example.com, 443, client-cert=cert1

[Keystore]
cert1 = base64=<P12 base64 string here>, password=123456
```

Shadow TLS
----------

Shadow TLS is a proxy obfuscator and can be used with any TCP-based proxy. ([https://github.com/ihciah/shadow-tls](https://github.com/ihciah/shadow-tls))

Starting from Surge iOS 5.2.0 & Surge Mac 4.10.0, Surge supports Shadow TLS v2 protocol. Append `shadow-tls-password` to any proxy declaration to utilize it.

Example:

```
[Proxy]
STLS-SNELL = snell, 1.2.3.4, 443, psk=pwd1, version=4, reuse=true, shadow-tls-password=pwd2
```

Starting from Surge iOS 5.5.0 & Surge Mac 5.0.3, Surge supports Shadow TLS v3 protocol.

Example:

```
STLS-SNELL = snell, 1.2.3.4, 443, psk=pwd1, version=4, reuse=true, shadow-tls-password=pwd2, shadow-tls-version=3
```

#### Parameters

*   `shadow-tls-password`: Required. It must match the server's setting.
*   `shadow-tls-sni`: Optional. The SNI will be sent to the server during the TLS handshake in plain. If not set, no SNI will be sent.
*   `shadow-tls-version`: Optional. Possible values: 2 or 3. Default value: 2.
