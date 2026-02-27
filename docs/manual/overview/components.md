Title: Components · GitBook

URL Source: https://manual.nssurge.com/overview/components.html

Published Time: Tue, 20 Jan 2026 02:39:12 GMT

Components
==========

Surge includes several components.

### Surge Proxy Server

This is the core part of Surge. It's a full-function HTTP/SOCKS5 proxy server with high performance and stability, written in Objective-C and optimized for macOS and iOS.

### Surge Virtual Network Interface (Surge VIF)

Some apps do not obey system proxy settings (such as Mail.app), because they need to use a raw TCP socket. This kind of traffic can be handled by Surge VIF.

Surge VIF is enabled by default for Surge iOS. You may enable Surge VIF on Surge Mac by turning on Enhanced Mode.

This is the architecture for Surge iOS: ![Image 2](https://manual.nssurge.com/Surge-Architecture.png)

### Surge Dashboard (Mac Version Only)

Surge Dashboard is a graphical user interface to review and inspect requests and list DNS cache. It can connect to a local Surge instance, or a remote instance when the external-controller-access is set.

[](https://manual.nssurge.com/)[](https://manual.nssurge.com/overview/configuration.html)
