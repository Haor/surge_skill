Title: Encrypted DNS · GitBook

URL Source: https://manual.nssurge.com/dns/doh.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

Encrypted DNS
=============

If encrypted DNS is configured, the traditional DNS will only be used to test the connectivity and resolve the domain in the encrypted DNS URL.

Supported Protocol:

*   DNS over HTTPS: `https://example.com`
*   DNS over HTTP/3: `h3://example.com`
*   DNS over QUIC: `quic://example.com`

### Use Encrypted DNS for All Domains

```
[General]
encrypted-dns-server = https://8.8.8.8/dns-query
```

You may specify multiple encrypted servers here, separated by commas.

### Use Encrypted DNS for Specified Domains

```
[Host]
example.com = server:https://cloudflare-dns.com/dns-query
```

### Use Encrypted DNS with Proxy

If you want to query DoH servers through a proxy, you can set `encrypted-dns-follow-outbound-mode` to true.

```
[General]
encrypted-dns-follow-outbound-mode=true
```

All the encrypted DNS connections will follow the outbound mode settings. Then configure a rule for the DoH hostname to use a proxy.

Or, use `PROTOCOL,DOH`, `PROTOCOL,DOH3` or `PROTOCOL,DOQ` rule to match all encrypted DNS connections.
