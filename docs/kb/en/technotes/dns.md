# Local and Proxy DNS Resolution

We often receive requests from users to support the configuration of split DNS resolution by region. This feature is often unnecessary.

Surge only triggers local DNS resolution in these two situations:

1. During rule determination

When determining the rules, Surge tries to match each rule from top to bottom. If it encounters an IP-type rule (including IP-CIDR, IP-CIDR6, GEOIP, ASN, etc.) and the rule is not modified by the no-resolve parameter, Surge will perform DNS resolution before matching.

2. If a proxy policy is used and the proxy server hostname is a domain name.
3. When using the DIRECT policy

If a request uses the DIRECT policy, DNS resolution will be triggered.

That is, if a match has been completed before encountering a rule that requires DNS triggering, and the policy is not DIRECT, local DNS resolution is not necessary.

When using a proxy policy, Surge always sends a request to the proxy server using the domain name, unless the `use-local-host-item-for-proxy` parameter is configured, meaning that DNS resolution always takes place on the proxy server.

This is the most reasonable and efficient workflow, saving unnecessary DNS overhead locally while ensuring that the results of local DNS resolution are not necessarily suitable for use by the proxy server.

To optimize this workflow, the following principles should be followed when writing rules:

1. Place rules that require DNS resolution at the end to avoid triggering unnecessary DNS resolution prematurely.
2. If some domain names cannot be resolved locally, add `DOMAIN` type rules to directly specify the proxy policy, avoiding local DNS triggering.
3. If the FINAL rule uses a proxy policy, configure the `dns-failed` parameter modifier for the `FINAL` rule. This way, when local DNS resolution fails, the request can be forwarded to the proxy server.
