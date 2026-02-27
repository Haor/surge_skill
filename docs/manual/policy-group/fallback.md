Title: Fallback Group · GitBook

URL Source: https://manual.nssurge.com/policy-group/fallback.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

Fallback Group
==============

Select an available policy by priority and availability. The availability is tested by accessing a URL, just like an automatic testing group. The difference is that the fallback group only cares about availability and not the specific latency. The policy defined in the front has a high priority.

`FallbackGroup = fallback, ProxySOCKS5, ProxySOCKS5TLS`

### Temporary Override

You can temporarily override the result of automatic testing by manually selecting a policy.

*   In Surge Mac, you can find the override option in the corresponding group in the main menu.

*   In Surge iOS, you can find the override option by long-pressing on the corresponding policy's menu in the policy group view.

### Parameters

#### `interval`: Optional, in seconds, default: 600(s)

Determine how long the benchmark result will be discarded.

#### `timeout`: Optional, in seconds, default: 5(s)

Abandon a policy if it is not finished until timeout.
