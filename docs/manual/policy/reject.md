Title: REJECT Policy · GitBook

URL Source: https://manual.nssurge.com/policy/reject.html

Published Time: Tue, 20 Jan 2026 02:39:13 GMT

To meet different needs, Surge has multiple built-in REJECT policies. In most cases, using REJECT directly is sufficient. If there are special requirements, consider derivative policies.

#### REJECT

Reject the request, if the request is of HTTP type an error page will be returned. This behavior can be controlled by the `show-error-page-for-reject` parameter.

#### REJECT-DROP

Reject the request. Unlike REJECT, this policy will silently discard the connection. Some applications have very aggressive retry logic, where they immediately retry after a connection failure, leading to a request storm. Using this policy can mitigate the issue.

#### REJECT-NO-DROP

If a large number of requests to a hostname trigger the `REJECT/REJECT-TINYGIF` policy within a short period of time (the threshold is 50 times within 30 seconds in the current version), Surge will automatically upgrade the policy to `REJECT-DROP` in order to avoid wasting a lot of resources.

You may use `REJECT-NO-DROP` policy to avoid this behavior.

#### REJECT-TINYGIF

Reject the request, if the request is of HTTP type an 1px transparent gif will be returned, for AD-blocking.

### Pre-matching Reject iOS 5.14.0+Mac 5.9.0+

Due to the extensive range of properties that Surge's rule system can evaluate, rule determination can only occur after receiving the first TCP packet. This results in excessive unnecessary overhead when dealing with storm requests or ad-blocking needs.

In the new version, Surge has added a Pre-matching feature to quickly reject requests with low overhead. For rules using the REJECT policy, this feature can be enabled through `pre-matching` tagging.

```
[Rule]
DOMAIN,ad.com,REJECT,pre-matching
```

Rules marked with `pre-matching` will take effect before the normal rule matching process, thus having the highest priority.

All rules marked with `pre-matching` will be extracted for prioritized matching and executed during the DNS resolution and TCP SYN phases. If a DNS domain is matched, it directly returns No Record; if matched during the TCP SYN phase, an TCP RST response is generated immediately. In case of numerous requests, it escalates to packet loss, and UDP is handled similarly.

Additionally, each rule will only appear once in the recent request list every 5 minutes to avoid flooding due to numerous requests.

The types of rules that can be marked with `pre-matching` include:

*   DOMAIN types: DOMAIN, DOMAIN-SUFFIX, DOMAIN-KEYWORD, DOMAIN-SET, DOMAIN-WILDCARD.
*   IP types: IP-CIDR, IP-CIDR6, GEOIP, IP-ASN.
*   Logical rules: AND, OR, NOT
*   Others: SUBNET, DEST-PORT,SRC-PORT,SRC-IP

RULE-SET can also be used but its content is subject to the above restrictions as well.

### Pre-matching Technical Details

For optimal user experience, rejections are made during the pre-matching phase, and there will be some detailed differences when using different derivative rules.

#### For DNS queries

*   If a REJECT policy is matched, Surge will return a No Record DNS response. If the frequency limit built into the REJECT policy is triggered, the DNS query will be directly discarded without a response.

*   If a REJECT-DROP policy is matched, the DNS query will be directly discarded without a response.

*   If a REJECT-NO-DROP policy is matched, it will return a special IP address 198.18.0.244; Surge will generate TCP RST responses for all TCP connections accessing this address.

#### For TCP requests using IP

*   If a REJECT policy is matched, it will directly generate TCP RST responses; if the frequency limit built into the REJECT policy is triggered, it will discard the corresponding TCP SYN handshake packet.

*   If a REJECT-DROP policy is matched, it will directly discard the TCP SYN handshake packet.

*   If a REJECT-NO-DROP policy is matched, it will directly generate TCP RST responses.

Please note that due to some software potentially having aggressive retry logic, which immediately retries after a request fails and causes abnormal CPU usage, even for the REJECT-NO-DROP policy, when Surge generates a large number of TCP RST packets in a short period of time (the threshold is 100 times within 3 seconds in the current version), it will also trigger a protection mechanism to pause returning TCP RST and directly drop packets instead.

#### For UDP packets

Since UDP packets have no handshake overheads, there isn't any Pre-matching phase; they are directly matched using main rule rule sets:

*   If a REJECT policy is matched, an ICMP Administratively Prohibited response will be generated; if the frequency limit built into the REJECT policy is triggered, packets are directly discarded.

*   If a REJECT-DROP policy is matched, packets are directly discarded.

*   If a REJECT-NO-DROP policy is matched, an ICMP Administratively Prohibited response will be generated.
