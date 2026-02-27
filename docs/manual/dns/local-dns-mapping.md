Title: Local DNS Mapping · GitBook

URL Source: https://manual.nssurge.com/dns/local-dns-mapping.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

Surge supports local-customized DNS mapping. It's equivalent to /etc/hosts, but with more powerful features, including wildcard, alias, and assigning DNS server.

```
[Host]
abc.com = 1.2.3.4
*.dev = 6.7.8.9
foo.com = bar.com
bar.com = server:8.8.8.8
```

Wildcard
--------

You can use * prefix to wildcard all sub-domains. Please note that Surge uses a simple string match. For example, *google.com will match google.com, foo.google.com, and bargoogle.com. And *.google.com will **not** match google.com.

```
[Host]
*.dev = 6.7.8.9
```

Alias
-----

It's just like a CNAME record.

```
[Host]
foo.com = bar.com
```

Assigning DNS Server
--------------------

You can assign a specified DNS server to one or more domains.

```
[Host]
bar.com = server:8.8.8.8
```

Since Surge has its own DNS client implementation, some hostnames may fail to resolve. You can use 'server:system' to let the system handle the lookup.

```
[Host]
Macbook = server:system
```

`server:syslib` works similarly but keeps the query inside Surge while forwarding it to whatever DNS servers macOS is currently using. It is particularly useful in enhanced mode where the traditional system resolver might be bypassed.

By default, all hostnames with the suffix '.local' will be resolved by the system.

Referencing Rule Sets Mac 5.10.0+
---------------------------------

When you already maintain large rule sets or domain sets, reproducing the same list in `[Host]` is tedious. Surge allows binding an entire `DOMAIN-SET` or `RULE-SET` to a DNS mapping entry so that the upstream or IP mapping is shared automatically.

```
[Host]
DOMAIN-SET:https://example.com/domains.txt = server:https://doh.example.com/dns-query
RULE-SET:https://example.com/rules.txt = 10.0.0.10
```

`DOMAIN-SET:` expects a domain list, while `RULE-SET:` can include mixed rule types (DOMAIN, DOMAIN-SUFFIX, IP ranges, etc.). This syntax follows the same remote file format described in [Ruleset](https://manual.nssurge.com/rule/ruleset.html) and is especially helpful for DOH/DOQ assignments that need to stay aligned with a managed list.

Use Local DNS Item Even For Proxies
-----------------------------------

```
[General]
use-local-host-item-for-proxy=true
```

By default, the DNS resolve always happens on the remote proxy server since Surge always sends proxy requests with domains.

After enabling this option, for the requests that match a local DNS mapping record, Surge sends proxy requests with the local IP addresses instead of the original domains.

It only works for local DNS mapping records using an IP address.
