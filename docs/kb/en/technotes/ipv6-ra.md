# IPv6 RA Override

In Surge Mac v6, the IPv6 RA Override feature has been introduced to take over the IPv6 network of other devices. This feature is pioneered by Surge, so there is almost no technical information about this solution on the Internet. Therefore, this document is created to explain the feature details and facilitate troubleshooting for users.

### Core Principle

In an IPv6 network, RA broadcasts are one of the cornerstones of the network. Typically, routers accomplish three things by sending RA broadcasts:

1. Provide an IPv6 address prefix, allowing other devices to generate their own public IPv6 address (GUA address).
2. Announce its link-local address as the default route.
3. Configure the IPv6 DNS for clients.

The RA message design features a priority mechanism, which allows high-priority RA messages to override medium and low-priority messages. This is the core principle behind Surge IPv6 RA Override. One notable difference is that, while RA messages are usually broadcast, Surge's RA is unicast, only affecting the device that needs to be taken over.

At the same time, Surge's RA does not contain address prefix information, so address allocation still depends on the original router's RA broadcast. Surge's high-priority broadcast only performs route and DNS override. Therefore, the original router's RA broadcast must not be disabled; otherwise, IPv6 address allocation will not be possible. You only need to ensure that its priority is not set to high.

### IPv6 RA DNS

If the original router’s RA configures IPv6 DNS, and that address is a link-local address or the router's own IPv6 address, the DNS packets may not be intercepted by Surge due to route priority issues, causing the fake IP mechanism to fail.

Surge's RA packet will broadcast its own v6 DNS address `fd00:6152::2`, but different operating systems handle high-priority RA DNS in different ways. Some systems override the original setting, while others simply append it. Therefore, Surge recommends modifying the original broadcast DNS address to be empty or any public address to avoid situations where coverage cannot be achieved.

However, even if DNS override fails, only the fake IP mechanism will be ineffective. Requests can still be taken over, and domain name-based rules can still be applied via SNI sniffing.

### Stability

In v4 DHCP mode, since Surge completely replaces the original DHCP service, it can guarantee successful takeover; otherwise, clients cannot connect to the network at all.

However, in v6 RA override mode, since the override operates independently of the original RA, if there is network fluctuation causing Surge's RA override packets to be lost, there may be cases where client devices are not overridden. At this point, client devices' IPv6 will be directly connected.

Even so, such situations usually only appear when initially connecting to the network. Once connected, Surge will continuously and periodically send RA override messages, at a frequency much higher than the RA message validity period, so it is rare for the override to fail.

### Compatibility Issues

In our tests, the vast majority of devices responded well to Surge's RA override, but in a few cases, there may be compatibility issues:

#### Sony PS5

The PS5’s IPv6 stack is incomplete and cannot correctly handle high-priority IPv6 RA messages, so it cannot be taken over.

#### Windows

Some Windows devices may experience takeover failure after a period of time, with a warning appearing in the Event Viewer: `TCPIP - Event 4205 - Autoconfigured route limit has been reached. No further autoconfigured routes will be added until the interface is reconnected.`

We found that only some devices experience this issue with low probability. We are still analyzing and testing the real cause. Since Windows is closed source and does not provide related documentation, it is relatively difficult, and it may simply be a Windows bug.

All of the problems above can be solved by manually modifying the device’s IPv6 profile, bypassing RA and directly configuring the IPv6 address, gateway, and DNS.

* IPv6 address: Make sure it is consistent with the originally auto-assigned address. However, if your IPv6 prefix may change, you’ll need to reconfigure it after changes.
* Gateway address: You can find the Surge VM’s IPv6 address on the Surge overview page and input this address.
* DNS: `fd00:6152::2`

Manual configuration ensures stable and complete takeover.
