Title: Host List Parameter Type · GitBook

URL Source: https://manual.nssurge.com/others/host-list.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

In Surge, many parameters utilize the Host List type to accommodate various complex needs, such as `force-http-engine-hosts`, `always-raw-tcp-hosts`, `[MITM]`'s `hostname`, and more.

The Host List type parameter is a list separated by `,` and follows these rules:

*   Use prefix `-` to exclude a hostname.
*   Wildcard characters `*` and `?` are supported.
*   Items in the list will be matched in order, and once a match is successful, it will end the matching process. Therefore, items at the front have higher priority. Especially when using the `-` prefix, you should write the hostnames that need to be excluded at the front.
*   If a port number is not provided, then Surge will automatically append the standard port number for that parameter, like for the `force-http-engine-hosts` parameter, if only the hostname is configured, then it will only be effective for port 80. For the MITM feature, it will only be effective for port 443.
*   Use suffix :port to match other ports.
*   Use suffix :0 to match all ports.
*   Use `<ip-address>` to match all hostnames using an IPv4/IPv6 address directly instead of a domain.
*   Use `<ipv4-address>` to match all hostnames using an IPv4 address directly instead of a domain.
*   Use `<ipv6-address>` to match all hostnames using an IPv6 address directly instead of a domain.

Taking the `force-http-engine-hosts` parameter as an example:

*   `-*.apple.com`: Excludes all requests sent to *.apple.com on port 80.
*   `www.google.com`: Uses forced HTTP processing for www.google.com on port 80.
*   `www.google.com:8080`: Uses forced HTTP processing for www.google.com on port 8080.
*   `www.google.com:0`: Uses forced HTTP processing for www.google.com on all ports.
*   `*:0`: Uses forced HTTP processing for all hostnames on all ports.
*   `-<ip-address>`: Excludes all requests using an IPv4/IPv6 address directly.

### Example

When configuring the hostname for MITM, if you want to decrypt all HTTPS connections but exclude those well-known hostnames that cannot be decrypted due to certificate pinning, you can write it like this:

```
[MITM]
hostname = -*icloud*, -*.mzstatic.com, -*.facebook.com, -*.instagram.com, -*.twitter.com, -*dropbox*, -*apple*, -*.amazonaws.com, -<ip-address>, *
```
