Title: Policy Group · GitBook

URL Source: https://manual.nssurge.com/policy-group/group.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

Policy Group
============

A policy group may contain multiple policies. It can be a proxy policy, another policy group, or a built-in policy.

The existence of policy groups is to allow for flexible adjustment of the specific policies being used when proxy rules are applied, without the need to modify the rules themselves.

There are several group types: `select`, `url-test`, `fallback`, `load-balance`, and `subnet`. Policy groups should be declared in section [Proxy Group].
