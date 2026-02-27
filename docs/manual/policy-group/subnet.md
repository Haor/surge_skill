Title: Subnet Group · GitBook

URL Source: https://manual.nssurge.com/policy-group/subnet.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

Subnet Group
============

Using a Subnet policy group, you can automatically select a policy based on the current network environment. You can use [subnet expression](https://manual.nssurge.com/rule/subnet.html) as a condition.

`Subnet Group = subnet, default = ProxyHTTP, TYPE:WIFI = ProxyHTTP, SSID:MyHome = ProxySOCKS5`

Starting from Surge iOS 4.12.0 & Surge Mac 4.5.0, the SSID group is now renamed to Subnet Group. The legacy syntax of SSID Group is still supported. You may use the group type keyword `subnet` or `ssid` for compatibility.

### Parameters

#### `default`: Required

The policy when no subnet expression is matched.

#### `cellular`: Optional (Deprecated, use `TYPE:CELLULAR` instead)

The policy for cellular networks. If not provided, the default policy will be used.
