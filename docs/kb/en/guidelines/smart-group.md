# Smart Group

This is a brand-new type of policy group, driven by our meticulously designed algorithm engine, capable of automatically selecting the appropriate policy from the sub-policies within this group. The goal of the Smart Group is to replace the original automatic test group (`url/load-balance/fallback`), significantly optimizing the experience while minimizing the need for manual intervention by users in the policy group; users simply need to place available policies into this group.

*This feature is a Surge iOS subscription feature, requiring a subscription to unlock. Surge Mac 5 can get this update for free.*

### Smart Group Features

* Real-Time Dynamic Optimization

  Unlike the current automatic test group, which periodically re-tests to determine the policy, the Smart Group dynamically collects the status of each sub-policy, including handshake latency, packet loss rate, connectivity, RTT, and other dimensions of information, and dynamically changes the decision based on this information.
* Adaptive Retry

  In the original architecture of Surge, the decision path of the policy group is resolved during the rule matching phase, which means that even if the connection cannot be established through the proxy, it still needs to trigger the policy group re-test to complete the policy switch.

  We have redesigned the architecture for the Smart Group. Now, when there is a connection establishment fault or slowness, the Smart Group can immediately use an alternative policy to complete the connection, and the upper layer of the connection will not even notice the switch.

  At the same time, the Smart Group will judge whether a route is abnormal based on the historical data of the route, thus enabling an alternative policy in an extremely short time when a policy anomaly occurs. Previously, it usually takes several seconds of timeout to trigger the exception handling process.
* Per-site Tuning

  The current automatic test group's decision is based on the test results for `test-url`. However, the same proxy may have significant differences when accessing different websites, or even completely inaccessible (such as some proxies do not allow SMTP traffic through). The Smart Group will record the connectivity and latency performance to various websites and make targeted policy adjustments the next time a connection is made.
* Test Optimization

  The Smart Group will also periodically re-test to confirm whether some policies that were abnormal before have recovered, but different from the traditional automatic test group, the Smart Group will automatically analyze the usage and select some policies for re-testing, rather than re-testing all policies. This means that even if a large number of policies are configured in the Smart Group, it will not incur a lot of overhead due to re-testing.
* Customizable weights

  You can use expressions to set weight values for sub-policies to fine-tune the decision of the Smart Group.

We have selected a few cases to demonstrate the improvements of the Smart Group compared to the original automatic test group:

<details>

<summary><mark style="color:purple;">Fault Case #1:</mark> When the selected policy of the group experiences a timeout fault</summary>

* url-test group: When the handshake time exceeds the test-timeout value of the policy, it is judged as a policy fault, the corresponding request fails, triggering the policy group re-testing; if there are many policies/long timeout settings, the test may need to wait for tens of seconds. After the re-testing is completed, new connections start using the new policy.

  This process may lead to several seconds to tens of seconds of network interruption.
* Smart group: When the handshake time exceeds 1.5 times the previous average handshake time, the smart group suspects a policy fault, immediately enables the backup policy to complete the connection while imposing a penalty on that policy, reducing the probability of using that policy for subsequent connections. If the same policy is used again and fails, then penalties are applied again, and the effect of the penalties increases exponentially, making the policy almost unusable.

  At the same time, penalties will decay over time, and the probability of using that policy will recover over time. If the route returns to normal, new successful records will significantly erase the effect of penalties.

  So as long as there are still connectable policies in the policy group, users will hardly feel any network interruption.

</details>

<details>

<summary><mark style="color:purple;">Fault Case #2:</mark> A certain proxy is very slow when accessing a specific website, but normal when accessing other websites</summary>

* url-test group: Since the selected policy is only related to test-url, this slowness does not trigger a switch of the policy group.
* Smart group: Smart group can notice that the time to access that website is much higher than the time for that proxy to access other websites. Therefore, in the next connection, it will automatically try policy B, which is not far from the best policy A:
  * If the performance of policy B is far better than that of policy A, then policy B will be used thereafter
  * If the performance of policy B is also poor, it will continue to try policy C. After trying several policies, the Smart group believes this problem belongs to the target website issue and will no longer try to switch policies, stabilizing the policy with the best performance among those tested.

</details>

The above is only part of the logic when the Smart group handles connection problems. The Smart group contains many carefully designed logics and decision systems, and we will continue to optimize it to adapt to more situations.

### How to Use

The Smart group is a brand-new policy group type. To facilitate user migration, you can use the profile upgrade wizard to automatically upgrade all url-test/fallback groups to Smart groups.

* Surge iOS: After the upgrade, opening the app will prompt for an upgrade directly.
* Surge Mac: After the upgrade, you can find the profile upgrade wizard in more settings. (It will pop up automatically in the next version.)

Please note that due to compatibility issues, after upgrading, all versions of Surge iOS using this profile need to be 5.11.0 or above and require a subscription unlock for this feature. Surge Mac needs version 5.7.0. The original profile will be backed up automatically before upgrading.

### Usage Tips

* For the same website, the Smart group will try to use the same policy to connect to avoid problems caused by IP address changes. But for websites that are particularly sensitive to IP address changes (such as online banking), it is recommended to configure rules separately to avoid using the Smart group. (If a website's access speed itself has problems, the Smart Group will gradually stabilize to a single policy after trying multiple policies)
* The Smart Group cannot use other groups as sub-policies, nor can it be used as a sub-policy of `url-test/load-balance` group. But it is possible to use the `include-other-group` parameter to copy sub-policies from other groups.

### Customizable Weights

Weights can be set for sub-policies through the `policy-priority` parameter. The way to implement weight conditions is to multiply the delay of the policy by a coefficient to interfere with the algorithm's decision. (This parameter does not need to be configured if there is no special requirement)

For example, if policy A originally has a delay of 100ms, when configured as 0.9, the policy will be considered as a policy with a delay of 90ms in the algorithm's consideration. Configured as 1.3, it will be considered as 130ms.

That is, <1 increases the priority, >1 decreases the priority, the default is 1.

`policy-priority="Premium:0.9"`

The first parameter is a regular expression for the sub-policy name, the second parameter is the coefficient. You can continuously configure it (but a single policy will only be matched once).

`policy-priority="Premium:0.9;SG:1.3"`

If configured as 0, it means always use this policy first, and then try other policies after failure. (Not recommended)

### FAQ

**Q: What specific algorithm does the Smart Group's algorithm engine use?** A: The algorithm engine of the Smart Group is quite complex. Here the term algorithm does not refer to a specific arithmetic logic, but rather like the BBR algorithm, including a whole set of rules, calculation methods, data structures, and control logic, along with a lot of engineers' years of empirical data adjustments.

**Q: What are the use scenarios for the Smart Group?** A: The goal of the Smart Group is to replace all existing automatic test groups. Users only need to put available policies into this group, and the rest will be completely done by Surge automatically.

**Q: So, is it better to put as many policies as possible into the Smart Group?**

A: Our goal is to fully automate this problem. However, due to the instability of the device's own network, if a large number of low-quality routes are put into the group, when there is an unexpected network fluctuation, the Smart Group may enable some inferior routes, but actually, it is just due to the temporary problem caused by the device's own network. (There is consideration for the current network quality in the Smart Group's algorithm engine, but because there is a time difference in testing the current network quality, it may not be able to get accurate information.) This leads to a certain period after which it can return to the optimized route.

Therefore, it is recommended that the quality of the routes put in the Smart Group should be relatively similar, and then add a few inferior backup routes. It is not recommended to put too many policies that are almost impossible to be used in the group.

**Q: Can the Smart Group be used for automatic switching of routes for sites with regional lock restrictions?**

A: No, Surge cannot determine whether the content accessed has encountered regional lock restrictions, so it cannot make automatic adjustments. The Smart Group can respond to connection errors, timeouts, connection stalls, and other anomalies.

**Q: What if the Smart Group's policies always change?**

A: This is the expected behavior. The Smart Group will always randomly select one of the currently best-performing policies for connection to continuously monitor line quality. The Smart Group will try to use the same policy for the same website, so there is no need to be too concerned about policy changes. Even if there really is a change, except for a few websites (usually financial services, like Paypal), most websites are not sensitive to IP changes, and there is no need to worry about this issue and thus give up the Smart Group or set very high weights.

**Q: Why does the Smart policy group still try different policies for the same domain name?**

A: When accessing a domain name through a proxy, if the response speed of that domain is much lower than the speed at which the proxy accesses other websites, it is inferred that the proxy is not friendly to this target website. Therefore, other routes will be tried in subsequent connections. After a period of data collection, it will eventually converge and stabilize on one policy.

**Q: Why is a certain proxy clearly already malfunctioning, but still marked as "Most Used" on the interface?**

A: The "Most Used" displayed on the Smart policy group interface refers to the policy that has been used most frequently in recent times. When a certain policy suddenly malfunctions, although it is no longer the preferred policy, it may still be the most frequently used policy recently.

### Known Issues

* When using the Snell protocol in the Smart Group, the reuse mechanism will not take effect
* The Smart Group currently focuses on latency and does not consider the bandwidth of the route. Please ensure that the maximum bandwidth of the policies put into this group basically meets the needs, to avoid choosing low-bandwidth policies affecting the experience of large data volume transmission.
