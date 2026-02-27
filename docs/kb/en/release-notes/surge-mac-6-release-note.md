# Surge Mac 6.0 Release Note

<a href="https://dl.nssurge.com/mac/v6/Surge-latest.zip" class="button primary">Download v6 Version</a>

In Surge Mac 6.0, we once again bring a number of creative and unique new features, along with a brand new upgraded design.

### Surge Gateway Mode

In Surge Mac 6.0, the original Surge DHCP Server feature has been upgraded to the all-new Surge Gateway Mode, which includes many new features:

1. Surge Gateway VM

In previous versions, Surge relied on the system's utun device and IP forwarding mechanism to handle network traffic from other devices, which introduced unnecessary overhead and also limited Surge's capabilities. Now, Surge uses macOS’s VMNET framework to connect to networks as a virtual machine, operating directly at Layer 2 (similar to running RouterOS in a VM). This not only improves performance, but also makes it possible for Surge to implement more gateway features.

2. IPv6 RA Override

A major issue encountered in previous versions when using Surge DHCP mode was conflicts with IPv6, as DNS issued by IPv6 RA would render Surge’s Fake DNS mechanism ineffective.

Now, Surge can send higher-priority RA messages to override and take over the IPv6 gateway of selected devices, which not only solves possible DNS issues, but also fully takes over the device’s IPv6 network. Moreover, this takeover is targeted and non-exclusive; it can be used without any adjustments to the original network’s IPv6 (unless the original router RA message priority is set to high, in which case it needs to be manually lowered to medium), and does not affect other non-selected devices.

{% hint style="info" %}
To use the above two new features, you need to disable and then re-enable Gateway Mode to turn on the corresponding switches.
{% endhint %}

{% hint style="warning" %}
To use the IPv6 RA Override feature, you need to ensure that the DNS address broadcasted by the router's IPv6 RA is neither a link-local address in the fe80::/10 range nor the router's own IPv6 address.

Most routers allow customization of the IPv6 RA DNS address; you can simply leave it blank or change it to any public DNS. A few routers do not support modification. Known incompatible routers include:

* All ASUS models (this can be resolved by switching to Merlin/OpenWRT firmware)
  {% endhint %}

{% hint style="info" %}
More new features making use of the Surge Gateway VM are under development, such as UDP FastPath, and will be added in future versions.
{% endhint %}

### Surge VIF Engine

In Surge Mac 5.0, we introduced the VIF v2 operation mode, utilizing the system's Packet Filter to achieve extremely strong performance—testing up to \~37Gbps on M3, followed by the v3 version for improved compatibility.

However, due to new compatibility issues in macOS Sequoia, we had to abandon the original utun VIF solution and switch to Apple’s currently recommended Network Extension framework for Surge VIF, to ensure minimal risk of issues. Under NE, v2 and v3 cannot work, and even worse, NE does not expose enough interfaces for developers to optimize, rendering many of our v1 performance optimizations ineffective.

Therefore, in Surge Mac 6.0, we have completely rewritten Surge VIF using the latest theory and extreme optimizations, dramatically improving performance in enhanced mode. Loopback iperf testing on M4 Mac Mini shows max upstream throughput of \~30Gbps and downstream \~23Gbps, far surpassing other similar software. Higher max throughput means Surge can handle more traffic, and at low bandwidth the overhead is also lower, with less CPU usage and lower power consumption.

{% hint style="success" %}
Starting with Surge Mac 6, we offer an **Optimal Performance Guarantee**: if, after purchasing Surge, you find that Surge’s performance metrics (including throughput and latency) under the same conditions are inferior to other software, you can apply for a full refund within 30 days of purchase.
{% endhint %}

This rewrite also optimizes handling of UDP traffic, especially under high throughput. On M4 Mac Mini, loopback iperf testing can reach 10Gbps (the upper limit for iperf3 UDP mode).

As the WireGuard protocol stack also relies on Surge VIF, its performance has also improved.

On other technical details, Surge VIF now features Active Queue Management (AQM) and TCP pacing mechanisms to handle congestion and compatibility issues at high throughput.

{% hint style="info" %}
You can run your own iperf3 test for TCP loopback throughput: first, open a terminal and run `iperf3-darwin -s` to start the server. Then open another terminal and run `iperf3-darwin -Rc lvh.me` to test downstream throughput, or `iperf3-darwin -c lvh.me` for upstream throughput.
{% endhint %}

### Surge Ponte 2.0 - Multiple Channels

In Surge Mac 5.0, we launched the Surge Ponte feature for building point-to-point encrypted private networks. Thanks to its innovative mode, this may be the simplest private NAT traversal solution to use.

In 6.0, Surge Ponte is significantly enhanced: the Ponte server is no longer limited to a single operation mode. You can enable multiple traversal modes at the same time and even choose multiple proxy lines for traversal. When a Ponte client connects, it will automatically select the fastest channel.

Additionally, Surge Ponte now supports IPv6 direct channels: simply open the port in the firewall and Surge Ponte can form a network over IPv6 direct connections.

Also, Surge Ponte no longer relies on public STUN servers. It now uses a self-hosted STUN service, specifically designed for Surge Ponte, delivering significantly improved response times.

{% hint style="info" %}
Please note: Surge iOS must also be updated to the latest beta version to use this feature—older versions will only use the first channel.
{% endhint %}

### Surge Smart Group

Smart Group is also upgraded in 6.0—we’ve completed optimization for UDP connections, so now UDP traffic will also benefit from Smart Group’s intelligent optimizations.

At the same time, Smart Group itself has been enhanced and improved to handle more scenarios. Conflicts between Smart Group and the Snell protocol reuse mechanism have also been resolved.

### Snell v5

Surge's proprietary proxy protocol, Snell, has been upgraded to v5, with two major new features.

{% hint style="success" %}
The Snell protocol also enjoys the **Optimal Performance Guarantee**: if, after purchasing Surge, you find Snell proxy protocol’s performance metrics (including throughput and latency) are inferior to other software under the same technical conditions, you may apply for a full refund within 30 days of purchase.
{% endhint %}

#### Dynamic Record Sizing

This feature will improve latency performance in lossy network environments. Technical details can be referenced here: [Cloudflare Blog](https://blog.cloudflare.com/optimizing-tls-over-tcp-to-reduce-latency/)

#### QUIC Proxy Mode

We previously detailed why proxy forwarding for QUIC is not a good idea, and added the block-quic parameter to automatically block QUIC requests. However, some apps have recently become highly dependent on QUIC, and blocking QUIC traffic may cause malfunction.

Therefore, Snell v5 introduces a QUIC Proxy mode designed specifically for QUIC traffic, working as UDP over UDP to avoid TCP over UDP issues (server must open a UDP port).

* This mode is specially optimized for QUIC and is enabled only when Surge detects QUIC traffic; other UDP traffic still uses UDP over TCP mode.
* QUIC Proxy only strongly encrypts QUIC Handshake packets to protect the SNI and destination hostname, as well as for authentication. All subsequent QUIC packets, already strongly encrypted by QUIC, are directly forwarded as raw packets, greatly reducing unnecessary encryption/decryption overhead. As no extra bytes are introduced, PMTU probing for QUIC is not impacted.

Server-side:

{% content-ref url="snell" %}
[snell](https://kb.nssurge.com/surge-knowledge-base/release-notes/snell)
{% endcontent-ref %}

{% hint style="info" %}
The Snell v5 server is backward compatible with v4 clients. If you do not want to use QUIC Proxy Mode, simply set the client to v4. Dynamic Record Sizing optimization is server-side only.
{% endhint %}

#### Egress Control

* Supports configuration of the `egress-interface` parameter to control the egress interface (requires root privilege or granting `CAP_NET_RAW/CAP_NET_ADMIN` license, and the interface must have routes to the destination and DNS).
* Supports systemd’s Socket Activation mechanism for configuring network namespaces and egress interfaces. We will provide sample profiles in the future.

### Traffic Statistics System

The traffic statistics system has received a major upgrade. You can now view traffic stats by target hostname, and the time dimension is extended to the whole month—with statistics for last month also retained.

As more and more apps use child processes for network requests (making statistics and monitoring confusing), the new version can aggregate all processes within an app bundle for statistics.

### Fake DNS v6

The Surge DNS server now also listens on the virtual IPv6 address fd00:6152::2 and can return fake IPv6 addresses for AAAA queries. This means Surge can now operate in pure IPv6 environments if needed.

### Linked Profile

To solve the problem of locally modifying managed configurations, we have further improved the Linked Profile design. Now the #include statement can directly use a managed profile URL.

Also, when installing a managed profile in v6, Surge will actively prompt users to create a Linked Profile. For users already using managed profiles, the app now guides you to create a Linked Profile when attempting to modify it.

### UI Updates

The new version brings a completely redesigned interface. Surge Mac 6.0 features enhanced data presentation, so you can see more dimensions of data on the home page.

Please note: this update is not yet fully adapted for macOS 26. Once macOS 26’s style stabilizes, we will further update the UI for compatibility.

Meanwhile, nearly every page has been re-optimized to comply with the latest macOS design standards.

### Other Detail Updates

* `IP-CIDR` rules now allow direct use of a single IP (i.e., `/32` is implied).
* `PROTOCOL,TCP` rules now also affect HTTP and HTTPS connections, guaranteeing semantic consistency with `PROTOCOL,TCP` rules.
* Performance for handling especially large profiles (hundreds of proxies and policy groups) has been optimized; even giant profiles now load smoothly.
* HTTP request/response rules now include a `full-header-mode` parameter; when enabled, the `headers` field will be provided as an array to better handle multiple fields with the same name (such as `Set-Cookie`).
* The default fallback behavior for proxies not supporting UDP is now REJECT.
* Added support for the HTTP zstd compression algorithm.
* Globally optimized wildcard match performance.
* The advanced settings page has been completely redone; now all advanced parameters can be edited directly through the UI.
