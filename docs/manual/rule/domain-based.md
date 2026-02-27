Title: Domain-based Rule · GitBook

URL Source: https://manual.nssurge.com/rule/domain-based.html

Published Time: Tue, 20 Jan 2026 02:39:13 GMT

Domain-based Rule
=================

There are three domain-based rule types.

#### DOMAIN

`DOMAIN,www.apple.com,Proxy`

Rule matches if the domain of the request matches exactly.

#### DOMAIN-SUFFIX

`DOMAIN-SUFFIX,apple.com,Proxy`

Rule matches if the domain of the request matches the suffix. For example: 'google.com' matches 'www.google.com', 'mail.google.com' and 'google.com', but does **not** match 'content-google.com'.

#### DOMAIN-KEYWORD

`DOMAIN-KEYWORD,google,Proxy`

Rule matches if the domain of the request contains the keyword.

#### DOMAIN-SET

Designed for a large number of domain names, supports fast search for thousands of records. Each line in the file is a domain name if a line begins with . matches all sub-domains and the domain name itself. This can be used for ad filtering.

### Domain-based Rule Parameters

#### extended-matching iOS 5.8.0+Mac 5.4.0+

When this parameter is enabled, the rule will try to match both the SNI and the HTTP Host Header (or :authority).

The parameter is only available for `DOMAIN`, `DOMAIN-SUFFIX`, `DOMAIN-KEYWORD` rules, and you can propagate it to `DOMAIN-SET` entries by appending the parameter to the corresponding `RULE-SET`/`DOMAIN-SET` line.
