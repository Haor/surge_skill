Title: Enhanced Mode · GitBook

URL Source: https://manual.nssurge.com/others/enhanced-mode.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

Enhanced Mode (Surge Virtual Network Interface, VIF)
====================================================

Some applications may not follow the system proxy settings. Using the enhanced mode in Surge can ensure all applications are handled.

To accomplish this, Surge creates a virtual network interface (VIF) and registers it as the default route. All DNS queries are answered with a virtual IP in the 198.18.0.0/15 block.

It is important to note that the Surge VIF can only process TCP, UDP, and ICMP traffic. Therefore, only enable this feature when necessary. Additionally, it is not possible to proxy ICMP traffic, so the Surge VIF will return a response directly.

The enhanced mode is enabled by default on Surge for iOS, while on Surge for Mac, it must be manually started.

Starting from Surge Mac 5.8.0, enhanced mode is powered by Apple's Network Extension framework instead of the legacy utun driver. Existing configuration parameters such as `vif-mode` stay in the profile for backward compatibility but no longer affect the runtime behavior.

Surge VM Gateway
================

### UDP Fast Path Mac 6.4.0+

When Surge Mac operates in Gateway VM mode, devices that create thousands of short-lived UDP flows (such as P2P downloaders or online games) can exhaust the standard layer-4 proxy engine. The UDP Fast Path feature automatically downgrades those high-connection clients to a lightweight L3 forwarding mode whenever they exceed the threshold (10 connections within 1 second or 30 within 10 seconds).

*   Packets forwarded via the fast path bypass the proxy engine entirely and therefore cannot be matched by rules or MITM.
*   Destination ports below 1024 stay in normal mode to preserve compatibility with common services.
*   You can toggle the fast path for each client device from the Dashboard/Device list if you need to pin a client to either behavior.
