# Testing Strategy for Automatic Policy Groups

Auto-group policies include: url-test, fallback, and load-balance.

### First-time Use

When using a policy group for the first time, Surge's default behavior is to use the first sub-policy in the group while triggering a policy group test. Before the test is complete, if the policy group is used again, the first sub-policy will still be used.

If the policy group is configured with the `evaluate-before-use=true` parameter, then when the policy group test is not completed, the corresponding request will be blocked, waiting for the test result to continue.

### Regular Retesting

Automatic policy groups support configuring the interval parameter. When the time of the last test exceeds this interval, the previous test result is marked as expired.

When the policy group is used again, the sub-policy with the expired result will be used first, and a new test will be triggered simultaneously. In other words, if the policy group is not used, even if the result has expired, the retest will not be triggered immediately.

### Tolerance Parameter

The `url-test` policy group has a special parameter: `tolerance`, which defaults to 100 ms. A sub-policy will only be selected if its test result is more than the tolerance value higher than the original selected sub-policy's result.

For example, the policy group contains sub-policies A and B, with A currently selected and a tolerance of 100 ms.

When the new test results are A: 50ms B: 10 ms, A is still used. When the new test results are A: 150ms B: 10 ms, B is switched to.

This feature is used to avoid repeatedly switching the selected policy between several strategies with small differences in results, causing the exit IP to change frequently and causing abnormalities.

### Retesting in Exceptional Situations

When the selected proxy policy of a policy group fails, it should be retested immediately and switched to another policy. However, since the actual situation is often not simple, Surge has more complex logic for this.

When accessing a target website through a proxy, there are three main types of errors:

1. Network problems with the device itself, such as poor signal or network interruption.
2. Proxy server failure or network problems.
3. Target website server failure or network problems.

Obviously, we only want to trigger policy group retesting when encountering error 2. The problem is that Surge cannot accurately determine the source of the problem. As a result, Surge reclassifies the errors:

* Category A: Definitely error 1. (e.g., No route to host error)
* Category B: Possibly error 1 or 2. (e.g., TCP handshake timeout error)
* Category C: Definitely error 2. (e.g., Connection refused error)
* Category D: Possibly error 2 or 3. (e.g., Socket closed by remote error)
* Category E: Definitely error 3.

The current version of Surge's policy is: when the selected sub-policy encounters a Category C error, a retest will be triggered immediately. If there are 3 Category B or D errors within 60 seconds, a retest will also be triggered. Categories A and E do not trigger retesting.

For different proxy protocols, the classification of errors will be different. For example, shadowsocks, Trojan, and VMess protocols do not return status codes when the target website is in error, so there is no difference between entering the wrong proxy server key and the target server being unreachable from Surge's perspective. Both are just the proxy server actively closing the TCP connection. (Snell protocol has complete error codes and error information reporting)
