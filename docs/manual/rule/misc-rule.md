Title: Misc Rule · GitBook

URL Source: https://manual.nssurge.com/rule/misc-rule.html

Published Time: Tue, 20 Jan 2026 02:39:13 GMT

Miscellaneous Rule
------------------

### Port Number Rules

Port number rules support three kinds of expressions:

*   Directly writing the port number, such as IN-PORT,6153
*   Port number closed interval: such as DEST-PORT,10000-20000
*   Using >, <, <=, >= operators, such as SRC-PORT,>=50000 iOS 5.8.4+Mac 5.4.4+

#### DEST-PORT

Rule matches if the target port of the request matches.

```
DEST-PORT,80-81,DIRECT
```

#### IN-PORT

Rule matches if the incoming port of the request matches. Useful while Surge listening on multiple ports.

```
IN-PORT,6152,DIRECT
```

#### SRC-PORT iOS 5.8.4+Mac 5.4.4+

Rule matches if the client port number of the request matches.

```
SRC-PORT,>=50000,DIRECT
```

### Others

#### SRC-IP

Rule matches if the client IP address of the request matches. Only for remote machines.

```
SRC-IP,192.168.20.100,DIRECT
```

The SRC-IP rule also supports CIDR notation.

```
SRC-IP,192.168.20.0、24,DIRECT
```

#### PROTOCOL

Rule matches if the protocol of the request matches. The possible values are HTTP, HTTPS, TCP, UDP, DOH, DOH3, DOQ, QUIC, STUN.

```
PROTOCOL,HTTP,DIRECT
```

1.   Due to the existence of multiple draft versions of QUIC, not all QUIC traffic can be recognized by Surge.
2.   For compatibility reasons, `PROTOCOL,UDP` can also match QUIC traffic.
3.   `PROTOCOL,TCP` now covers HTTP and HTTPS connections so you can write a single rule for TCP-based web traffic.
4.   The protocol keywords `DOH`, `DOH3`, and `DOQ` are only used to match encrypted DNS requests sent by Surge itself. This feature needs to be used in conjunction with `encrypted-dns-follow-outbound-mode=true`.
5.   STUN detection is available for filtering P2P traffic; `PROTOCOL,STUN` will block or forward STUN packets specifically.

#### SCRIPT

Use a Javascript script to determine whether it matches.

```
SCRIPT,ScriptName,DIRECT
```

#### CELLULAR-RADIO iOS Only

Rule matches if the cellular radio technology of the current network matches. The possible values are GPRS, Edge, WCDMA, HSDPA, HSUPA, CDMA1x, CDMAEVDORev0, CDMAEVDORevA, CDMAEVDORevB, eHRPD, HRPD, LTE, NRNSA, NR

```
CELLULAR-RADIO,LTE,DIRECT
```

#### DEVICE-NAME

Rule matches if the client's device name matches.

*   For Surge Ponte access, the device name is the device name in the client device system settings.

*   If Surge DHCP is enabled, for local area network device access, you can use the custom device name found on the device view.

#### MAC-ADDRESS Mac 6.1.0+

The MAC address of the accessing device can be matched. Please note that this is only effective for devices on the same local area network; if the request is forwarded by a gateway, the MAC address cannot be obtained.

#### HOSTNAME-TYPE Mac 5.7.3+

Rule matches the form of the hostname in a request. The supported keywords are:

*   `IPv4`: hostname is an IPv4 literal.
*   `IPv6`: hostname is an IPv6 literal.
*   `DOMAIN`: hostname contains dots and is a regular domain name.
*   `SIMPLE`: hostnames without a dot, such as `localhost`.

Example:

```
HOSTNAME-TYPE,IPv6,REJECT
HOSTNAME-TYPE,SIMPLE,DIRECT
```
