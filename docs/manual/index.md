Title: Overview · GitBook

URL Source: https://manual.nssurge.com/

Published Time: Tue, 20 Jan 2026 02:39:12 GMT

Surge Overview
--------------

Surge is a web development and proxy utility designed for developers, thus requiring professional knowledge to use.

The core workflow of Surge consists of four main capabilities:

*   Takeover: Surge allows the user to take over the network connection sent by the device. Both proxy service and virtual NIC takeover are supported.

*   Processing: The software enables users to modify network requests and responses which have been taken over. This includes URL redirection, local file mapping, custom modification using JavaScript, and many other methods.

*   Forwarding: The network requests, once taken over, can be forwarded by the user to other proxy servers. The forwarding can be either global or using a flexible rule system to determine an outbound policy.

*   Intercept: Specific data from network requests and responses can be intercepted and saved by the user. Additionally, the user can also decrypt HTTPS traffic with MITM.

Features
--------

*   High Performance, Stability, and Efficiency: Surge can smoothly handle all network traffic with industrial-grade stability using minimum system resources.
*   Flexible Rule System: You can write forwarding rules based on a domain name, IP CIDR, GeoIP, etc. Surge can automatically proxy requests to other servers using HTTP/HTTPS/SOCKS5/SOCKS5-TLS/Shadowosocks protocols.
*   HTTPS Decryption: Decrypt HTTPS traffic by a man-in-the-middle attack. The certificate generator will help you generate a CA certificate trusted by your operating system for debugging purposes.
*   Local DNS Mapping: Surge supports local-customized DNS mapping. Its multiple functional modules, including wildcard, alias, and custom DNS server, will be able to satisfy various needs.
*   Proxy Group: You may categorize several proxies as a group, and a policy will be employed in accordance with the grouping. Proxy group can be configured as Auto Speed Test (select policy based on benchmarking URL access speed), SSID (select policy based on Wi-Fi SSID), and manual-select.
*   HTTP Rewrite: You can rewrite HTTP/HTTPS requests to another URL using customized rules or block the requests;
*   Remote Dashboard: Surge Dashboard may connect to remote Surge iOS or Surge Mac instances via USB or network.
*   Full IPv6 Support: All functions work in the IPv6 environment.

### Surge Mac Exclusive Features

*   Enhanced Mode: Surge can set up a virtual network interface to handle all network traffic for applications that do not explicitly support web proxy.
*   Metered Network Mode: You can control which applications/processes are allowed to access the Internet, which is useful when on metered connections (e.g., cellular networks).
*   Gateway Mode: Surge Mac can be configured as a layer three gateway to handle network traffic for other devices in the same network.

### Surge iOS Exclusive Features

*   All functions work on cellular networks.
*   Capture all HTTP/HTTPS/TCP traffic from any apps on your device, and redirect to HTTP/HTTPS/SOCKS5/Shadowosocks proxy servers following highly configurable rules, even if the app does not follow system proxy settings.
*   Override system DNS settings even on a cellular network and boost performance by querying all DNS servers simultaneously.
*   Monitor and analyze network requests on iOS devices by connecting Surge Dashboard to Surge iOS via Wi-Fi or USB cables. You can even examine cellular network requests when connecting via USB cables.

### Understanding Surge

We have published an official guidebook to help you understand Surge.

*   English version: [https://manual.nssurge.com/book/understanding-surge/en/](https://manual.nssurge.com/book/understanding-surge/en/)

*   Chinese version: [https://manual.nssurge.com/book/understanding-surge/cn/](https://manual.nssurge.com/book/understanding-surge/cn/)
