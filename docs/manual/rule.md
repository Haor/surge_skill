Title: Proxy Rule · GitBook

URL Source: https://manual.nssurge.com/rule.html

Published Time: Tue, 20 Jan 2026 02:39:13 GMT

Rule
====

Surge can forward requests to another proxy server or connect to the host directly, depending on customized rules.

### Priority

Rules are matched from the first one to the last one, in the order they appear in the config file. In other words, rules at the top of the list have higher priority than the latter ones.

### Composition

Each rule consists of 3 parts: rule type, a matcher (except for the FINAL rule), and a proxy policy:

```
TYPE,         VALUE,         POLICY
Example:   DOMAIN-SUFFIX,apple.com,     DIRECT
           IP-CIDR,      192.168.0.0/16,ProxyA
```

Surge supports several types of rules, see the specific rule introductions under this category. A policy can be a built-in policy, or a proxy policy, or a policy group. See the description in the policy section for details. Rules must end with a FINAL rule to define the default behavior.

Example:

```
[Rule]
DOMAIN-SUFFIX,company.com,ProxyA
DOMAIN-KEYWORD,google,DIRECT
GEOIP,US,DIRECT
IP-CIDR,192.168.0.0/16,DIRECT
FINAL,ProxyB
```

DOMAIN, DOMAIN-SUFFIX and DOMAIN-KEYWORD are [domain based rules](https://manual.nssurge.com/rule/domain-based.html). IP-CIDR and GEOIP are [IP based rules](https://manual.nssurge.com/rule/ip-based.html).
