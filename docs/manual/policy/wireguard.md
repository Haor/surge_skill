Title: WireGuard · GitBook

URL Source: https://manual.nssurge.com/policy/wireguard.html

Published Time: Tue, 20 Jan 2026 02:39:13 GMT

You can use Surge as a WireGuard client, converting L3 VPN as an outbound proxy policy.

```
[Proxy]
wireguard-home = wireguard, section-name = HomeServer

[WireGuard HomeServer]
private-key = sDEZLACT3zgNCS0CyClgcBC2eYROqYrwLT4wdtAJj3s=
self-ip = 10.0.2.2
self-ip-v6 = fd00:1111::11
dns-server = 8.8.8.8, 2606:4700:4700::1001
prefer-ipv6 = false
mtu = 1280
peer = (public-key = fWO8XS9/nwUQcqnkfBpKeqIqbzclQ6EKP20Pgvzwclg=, allowed-ips = 0.0.0.0/0, endpoint = 192.168.20.6:51820)
```

Notes for configuration:

1.   All keys can be in base64 or HEX form.
2.   You may configure `self-ip` and `self-ip-v6` simultaneously to utilize the IPv4 & IPv6 dual stack, or just one of them to use the single stack.
3.   Please note that the `self-ip` and `self-ip-v6` must be different for each device, otherwise it may cause IP preemption.
4.   if `prefer-ipv6` is true, prefer the IPv6 if a domain has both A & AAAA records configured when the IPv4 & IPv6 dual stack is enabled.
5.   The peer field can be configured with multiple nodes, separated by commas and indicated by `()` for one node. When configured by the UI, only a single node is allowed to be configured.
6.   The `preshared-key` and `keepalive` are optional parameters for peers.
7.   The endpoint of the peer can use a domain. Please note that the resolution of the endpoint is done by the DNS resolver configured by the [General] section and has nothing to do with the `dns-server` parameter in this paragraph.
8.   The `allowed-ips` of 0.0.0.0/0 means that the policy can be used to access any address, or it can be configured for a specific intranet address.
9.   If you need to access a host using a domain name through this policy, you must configure the `dns-server`, and Surge will perform DNS resolution to that server through WireGuard's VPN tunnel. Multiple DNS addresses can be configured, separated by commas.
10.   The `[WireGuard NAME]` segment can be split into a Detached Profile Section file.
11.   Multiple Wireguard instances can be configured and used simultaneously.

Usage Notes:

1.   WireGuard is an L3 VPN, so the overhead during processing is significantly higher than other general proxy protocols. It is suitable for scenarios with low bandwidth requirements.
2.   The tunnel only supports TCP and UDP protocols. In addition, a very simple ICMP/ICMPv6 response mechanism is provided. When the WireGuard handshake is successful, you can ping the client tunnel IP from the server side to test the connectivity.
3.   Since WireGuard protocol has no error reporting mechanism, in most cases, WireGuard errors are all timeouts (e.g., wrong key, firewall blocking, not configuring server-side NAT, etc.), so please analyze the cause by capturing packets yourself.

Following the WireGuard protocol standard recommendation, WireGuard handshake packets will be tagged with 0x88 (AF41) DSCP to increase the success rate.

#### Customize Reserved Bits iOS 5.3.1+Mac 4.10.3+

Surge supports customizing the reserved bits of WireGuard. It might be used as the client ID or routing ID for some implementations, such as Cloudflare WARP.

Example:

`peer = (public-key = <key>, allowed-ips = "0.0.0.0/0, ::/0", endpoint = example.com:51820, client-id = 83/12/235)`

#### ECN Support iOS 5.8.0+Mac 5.4.0+

When forwarding UDP packets via WireGuard, it supports retaining the TOS(DSCP/ECN) tag of packets inside the tunnel.

Based on the WireGuard protocol standard recommendation, Surge will copy the ECN tag from packets inside the tunnel to packets outside. When receiving packets with an ECN tag, they will be strictly merged according to RFC6040. (`ecn=true` must be set for the WireGuard policy).
