Title: Port Forwarding · GitBook

URL Source: https://manual.nssurge.com/others/port-forwarding.html

Published Time: Tue, 20 Jan 2026 02:39:16 GMT

Port Forwarding iOS 5.14.3+Mac 5.10.0+
======================================

Surge can listen on a specific local port and forward TCP requests from that port to a specific host. This feature can be used independently when Surge request handling (system proxy or enhanced mode) is not enabled.

Profile example:

```
[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy
```

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.
