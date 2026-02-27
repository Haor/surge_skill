Title: Automatic Testing Group · GitBook

URL Source: https://manual.nssurge.com/policy-group/url-test.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

Automatic Testing Group
=======================

Automatically select which policy will be used by benchmarking the latency to the testing URL. You change the testing URL in the general settings or override the testing URL for a policy.

`AutoTestGroup = url-test, ProxySOCKS5, ProxySOCKS5TLS`

### Temporary Override

You can temporarily override the result of automatic testing by manually selecting a policy.

*   In Surge Mac, you can find the override option in the corresponding group in the main menu.

*   In Surge iOS, you can find the override option by long-pressing on the corresponding policy's menu in the policy group view.

### Parameters

#### interval: Optional, in seconds, default: 600(s)

The benchmark result will be discarded after the interval time. A retest will happen if the policy group is used.

#### tolerance: Optional, in milliseconds, default: 100(ms)

The policy will be changed only when the new winner has a higher score than the old winner's score plus the tolerance.

This option prevents policies with similar scores from constantly alternating.

#### timeout: Optional, in seconds, default: 5(s)

Abandon a policy if not finished in timeout.

#### evaluate-before-use: Optional, Boolean, Default: false

By default, when the Automatic Testing policy group is used for the first time, in order not to affect the request, it will first access using the first policy in the policy group while triggering a test of the policy group.

If this option is enabled, then when using the Automatic Testing policy group for the first time, it will trigger a test of the policy group and wait until testing is finished before making requests with selected results.
