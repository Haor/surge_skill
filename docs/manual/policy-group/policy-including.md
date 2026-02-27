Title: Policy Including · GitBook

URL Source: https://manual.nssurge.com/policy-group/policy-including.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

Include External Policies
-------------------------

A policy group may import policies defined in an external file or from a URL.

`egroup = select, policy-path=proxies.txt`

This file contains a list of policies, just like the definition lines in the main profile.

```
Proxy-A = https, example1.com, 443
Proxy-B = https, example2.com, 443
```

#### `update-interval`: Optional, in seconds

The update interval. Only meaningful when the path is a URL.

#### `policy-regex-filter`: Optional

Only use the policies that the regex matches the policy name.

#### `external-policy-modifier`: Optional

You may use this parameter to modify the parameters of external policies.

For example, enabling TFO and changing the testing URL:

```
external-policy-modifier="test-url=http://apple.com/,tfo=true"
```

### `external-policy-name-prefix`: Optional

Add a prefix to the policy names of the sub-policies in this external policy group to facilitate differentiation when multiple different external policy groups are used simultaneously.

Include Existing Policies iOS 4.12.0+Mac 4.5.0+
-----------------------------------------------

You can use `include-all-proxies` and `include-other-group` to include all proxies or reuse existing defines from another group.

#### `include-all-proxies`

The parameter `include-all-proxies=true` includes all proxy policies defined in the [Proxy] section and can be used with the `policy-regex-filter` parameter for filtering.

#### `include-other-group`

Parameter `include-other-group="group1,group2"` includes policies from another policy group, and can include multiple policy groups separated by commas. It also can be used with the `policy-regex-filter` parameter for filtering.

*   `include-all-proxies`, `include-other-group`, and `policy-path` parameters are allowed to be used in a single policy group at the same time. The `policy-regex-filter` parameter applies to all three.
*   There is an order of precedence among the policy groups for the `include-other-group` parameter, but there is no order of precedence among the `include-all-proxies`, `include-other-group`, and `policy-path` parameters. For scenarios where the order of sub-policies makes sense (e.g., fallback groups), use policy groups nesting with `include-other-group`.
