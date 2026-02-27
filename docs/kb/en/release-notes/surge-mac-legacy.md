# Surge Mac Legacy Versions

## Surge Mac Legacy Versions

{% hint style="success" %}
Starting from version 6, please check the changelog here: <https://nssurge.com/support/mac/release-notes>
{% endhint %}

* Since Surge Mac v5.8.0, the minimum macOS requirement for Surge has been raised to macOS 12.0. If your operating system is 10.13/10.14/10.15/11, please download version 5.7.5: <https://dl.nssurge.com/mac/v5/Surge-5.7.5-2826-4f19761fb2275ebbe2acf43907bd9371.zip>
* The last version of Surge Mac v5 download link: <https://dl.nssurge.com/mac/v5/Surge-latest.zip>
* The last version of Surge Mac v4 download link: <https://dl.nssurge.com/mac/v4/Surge-latest.zip>
* The last version of Surge Mac v3 download link: <https://dl.nssurge.com/mac/v3/Surge-latest.zip>
* The last version of Surge Mac v2 download link: <https://dl.nssurge.com/mac/v2/Surge-latest.zip>

## Surge Mac v5 Release Notes

#### Version 5.10.3

* Added `[General]` parameter `block-quic`, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
  * `per-policy`: Determined by the policy's `block-quic` parameter, default value, i.e., current version behavior.
  * `all-proxy`: Overrides the proxy policy's `block-quic` parameter, blocks all
  * `all`: Overrides all policies' `block-quic` parameters, blocks all including DIRECT policy
  * `always-allow`: Overrides the proxy policy's `block-quic` parameter, allows all
* The adding new rule view can now remember previous options.
* Added dark mode support to the error page.
* Add integration support for the Dia browser.
* Bug fixes and other improvements.

<https://dl.nssurge.com/mac/v5/Surge-5.10.3-3272-5cf851de0c9af2bf96ab410244010f9a.zip>

#### Version 5.10.2

* Accessing the remote Dashboard of Ponte devices no longer requires Enhanced Mode to be enabled.
* Added DNS over TLS support, e.g., `tls://8.8.8.8`
* Optimize the process of adding rules through the Dashboard.
* Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
* Bug fixes and other improvements.

<https://dl.nssurge.com/mac/v5/Surge-5.10.2-3235-9255a55c4af59cbf0ed01b245ef86dcc.zip>

#### Version 5.10.1

* When enabling the HTTP capture switch, all active connections will now be forcibly interrupted to ensure that no requests are missed due to existing long connections.
* Optimized compatibility with some QUIC clients, such as Lark.
* Fixed an issue where download data bytes in statistics was incorrect after modifying the request HTTP using scripts or other mechanisms.
* Adjusted the priority of processing logic when forwarding QUIC. Now, for a proxy policy that does not support UDP forwarding, it will prioritize considering QUIC Block before falling back to DIRECT or REJECT.
* Fixed an issue where utun devices could not be used when binding the outbound interface.
* Fixed an issue where repeated notifications might continuously occur during Ponte Server retry failures.
* Resolved an issue where a specific request forwarded by Surge Ponte might get stuck under certain networks.
* Bug fixes and other improvements.

<https://dl.nssurge.com/mac/v5/Surge-5.10.1-3207-1e925800c695a40e8a34ceca6d856b0d.zip>

#### Version 5.10.0

**New Feature: Port Forwarding**

Example

```
[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy
```

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

**#!REQUIREMENT upgrade**

* Now provides three simple notations: #!IOS-ONLY, #!MACOS-ONLY, and #!TVOS-ONLY.
* Content disabled by this end-of-line comment can now be displayed and edited in the UI. It will appear as disabled when conditions are not met, and if enabled, restrictions will be automatically removed.

Example

```
DOMAIN,reject.com,REJECT #!MACOS-ONLY
```

**\[Host] Optimization**

\[Host] section supports configuration using DOMAIN-SET and RULE-SET to improve matching efficiency. Use case:

```
[Host]
DOMAIN-SET:https://example.com/domains.txt = server:https://doh.com/dns-query
RULE-SET:https://example.com/rules.txt = server:https://doh.com/dns-query
```

**Other Improvements**

* Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized.
* Surge Ponte can now automatically retry to recover after an abnormal NAT type appears.
* Bug fixes and other improvements.

<https://dl.nssurge.com/mac/v5/Surge-5.10.0-3195-d468f4e99b54bcde0432f2b5a0e38296.zip>

#### Version 5.9.3

* Bug fixes and other improvements.

<https://dl.nssurge.com/mac/v5/Surge-5.9.3-3122-0244efc5738b3cebde7c87c556cfddb8.zip>

#### Version 5.9.2

* The menu bar icon can now display the outbound mode.
* Fixed some issues related to Ponte.
* Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
* Fixed an issue where the \[Host] entry configured for .local domain names might be invalid.
* Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
* Other bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.9.2-3098-643c195efc1153b6d4993af6bba73a59.zip>

#### Version 5.9.0

#### New Features

* Added pre-matching rules for low-overhead request rejection. Please refer to the documentation for details. <https://manual.nssurge.com/policy/reject.html>
* Body Rewrite supports using JQ expressions to manipulate JSON.
* The shadowsocks protocol adds support for the `2022-blake3-aes-256-gcm` and `2022-blake3-aes-128-gcm` encryption modes

#### Improvements

* The URL-REGEX rule now supports `extended-matching` tags.
* Allow the use of Ponte policy as an underlying proxy.
* Modify the termination logic of HTTP scripts. If a request needs to be interrupted, use $done({abort: true}). Other failures will not modify or terminate the request.
* Overall optimization and improvement of UDP forwarding.

#### Bug Fixes

* Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.
* Fix the issue of not being able to obtain system routes on macOS 12.
* Fix the issue where determining the existence of IPv6 might be incorrect in some cases.
* Fix the issue where an incorrect message might sometimes indicate that the proxy settings have been modified by another program.
* Other bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.9.0-3025-f8d045da66079150d4a281ed3770b3f6.zip>

#### Version 5.8.2

* Fix the issue where IPv6 VIF cannot take over requests when the `gateway-restricted-to-lan` parameter is enabled.
* DNS lookup of `use-application-dns.net` will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
* Bug fixes and minor improvements.

<https://dl.nssurge.com/mac/v5/Surge-5.8.2-2946-b739968f1d90da3b755d3bf82941e8c2.zip>

#### Version 5.8.1

* New parameters: proxy-restricted-to-lan/gateway-restricted-to-lan It has been found that some users, due to a lack of understanding of network security knowledge, accidentally expose proxy and gateway services to the Internet (e.g., configured DMZ). Therefore, these two parameters have been added to restrict proxy and gateway services to only accept devices from the current subnet. These two parameters are enabled by default.
* Fix the compatibility between enhanced mode and PPPoE direct dialing.
* Support using ETag to avoid downloading duplicate data when requesting external resources.
* Surge now supports handling the system's DNS search domain settings.
* Other bug fixes and compatibility improvements.

<https://dl.nssurge.com/mac/v5/Surge-5.8.1-2929-5220af95366dfacec7ca84cb8ddd122c.zip>

#### Version 5.8.0

**Network Extension**

* Due to numerous issues arising from the traditional utun takeover solution in newer system versions, starting from Surge Mac 5.8.0, Surge Mac will use Network Extension as the enhanced mode to take over the system network.
* The minimum system version requirement for Surge Mac is raised to macOS 12.
* Due to different required permissions, manual authorization operations is needed after updating.
* The `vif-mode` parameter will no longer be effective.
* Enhanced mode can now be used in conjunction with network sharing functionality, meaning you can directly create a Wi-Fi managed by Surge (requires wired network)

**Port Hopping**

Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.

`Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234;5000-6000;7044;8000-9000", port-hopping-interval=30`

After configuring the `port-hopping` parameter, the primary port number configured in the front will no longer be effective.

Parameters:

* `port-hopping`: Used to configure the range of ports. Separated by commas and supports ranges configured with a hyphen.
* `port-hopping-interval`: The interval for changing port numbers. Defaults to 30 seconds

**Other Improvments**

* Due to the large amount of features requiring permissions in the new macOS system, a dedicated page has been added for managing system permissions.
* The `syslib` keyword for local DNS mapping can now be used in enhanced mode. However, in non-enhanced mode, the resolution is entirely handled by the system. In enhanced mode, Surge resolves it using the system's DNS address.
* Added `[General]` parameter `show-error-page`, which is used to control whether Surge's HTTP error page is displayed when an error occurs. This parameter is enabled by default, and the behavior is consistent with previous versions.

<https://dl.nssurge.com/mac/v5/Surge-5.8.0-2900-6379c9d5240ae1555772aed2eb977e69.zip>

#### Version 5.7.5

* The panel is now available in Surge Mac.
* DNS Forwarding Subsystem Optimization
  * When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
  * Surge can now correctly respond to PTR requests for fake IPs, meaning that using the `dig -x 198.18.23.87` command can be used to determine the original domain name corresponding to a fake IP.
  * The DNS forwarder will now forward DNS requests to specific upstream servers based on `[Host]` section configuration.
  * Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
* When adding a rule for the current webpage, you can choose to add to an existing ruleset.
* Bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.7.5-2826-4f19761fb2275ebbe2acf43907bd9371.zip>

#### Version 5.7.4

* Due to the sudden shutdown of a public STUN server that Surge Ponte relies on, resulting in the unavailability of Surge Ponte, we have carried out an emergency replacement. Additionally, we will build our own STUN server in the future to avoid such issues.
* Enhance compatibility with VPN and multiple network cards

  In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

  However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

  This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.
* Fix an issue where DOMAIN-SUFFIX rules may become invalid if duplicate DOMAIN and DOMAIN-SUFFIX rules are included in the rule set.
* Other bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.7.4-2806-afe67661ef616b7bbab189dec1473b68.zip>

#### Version 5.7.3

* Now you can see the number of times a rule has been used in the rule list.
* Optimized the implementation method of blocking QUIC traffic to increase the likelihood of clients correctly falling back.
* The Smart group will use the SUBSTITUTE policy (DIRECT) instead of failing directly when there are no sub-policies.
* Fixed an issue where the `server-cert-fingerprint-sha256` parameter was not effective for TLS-like protocols with sni=off settings.
* Added a new rule type `HOSTNAME-TYPE`, used to determine the type of request hostname. Optional values are: `IPv4`, `IPv6`, `DOMAIN`, `SIMPLE`. (`SIMPLE` refers to hostnames without a dot, such as `localhost`)
* Optimized DNS request logs. Now more information is displayed. Additionally, if DIRECT policy connects directly without triggering DNS in the rule system, related DNS logs can still be shown.
* When deleting a policy that is being used by a policy group, it is now allowed to delete it directly and automatically remove it from all policy groups.
* Bug fixes and other Improvements.

<https://dl.nssurge.com/mac/v5/Surge-5.7.3-2785-048c0bdc5ee2b05dab39852d51a19ff4.zip>

#### Version 5.7.2

* Optimize the matching performance of ASN rules in the rule set.
* Fix the issue where FINAL rules cannot be edited through UI.
* Fix the problem that invalid cron expressions would cause scripts to be executed repeatedly.
* Optimized the management mechanism of the script engine.
* Other minor issues fixed.

<https://dl.nssurge.com/mac/v5/Surge-5.7.2-2762-9a963758f386b5da00e7744b2a7f254d.zip>

#### Version 5.7.1

* Optimize the matching performance of small rule sets, especially evident on older model CPUs.
* The external resource update page can display error information generated by rule set processing.
* Automatically ignore invalid empty lines in the rule set.
* Corrected the issue where applying temporary rules and then experiencing a policy change does not disrupt existing connections.
* Corrected the issue when using Ponte policy within Smart group, if the target device is itself, it failed to automatically switch to DIRECT policy.
* Corrected the problem of incorrect time displayed in request logs for Ponte device requests.
* Corrected crashes that may occur when external policy groups change.
* Fixed an issue where configuration upgrade functionality did not correctly take effect for managed configurations and enterprise configurations.
* During Smart group initialization phase, no longer displays most frequently used tags to avoid misunderstanding.

<https://dl.nssurge.com/mac/v5/Surge-5.7.1-2757-e7b680d5dc23e1258188adc4d81116d7.zip>

#### Version 5.7.0

#### Smart Group

This is a new type of policy group, driven by our carefully designed algorithm engine, which can automatically select the appropriate policy from the sub-policies of this policy group. The goal of the Smart policy group is to replace the original automatic testing groups (url/load-balance/fallback), greatly optimizing the experience while minimizing the need for manual intervention in policy groups. Users only need to put the available policies into this group.

For details, see: <https://kb.nssurge.com/surge-knowledge-base/guidelines/smart-group>

#### Rule System

* Overall performance optimization of the rule system.
* Significant optimization of the indexing algorithm in large domain rule sets, improving the search efficiency by more than ten times for rule sets with more than 100,000 rules.
* Corrected the issue where sub-rules of logical rules within a rule set could not be covered by the `no-resolve` and `extended-matching` parameters of the rule set.
* Added a new rule type `DOMAIN-WILDCARD`, supporting `?` and `*` domain name matching.
* `DOMAIN-SET` and `RULE-SET` are changed to strict validation. If there are invalid lines in the file, the entire rule set will be invalidated to avoid problems caused by misuse.

#### IPv6

* The behavior of the `ipv6-vif` parameter has been modified. When set to always, IPv6 functionality will be enabled even if `ipv6=true` is not set.
* Added a warning for the `ipv6-vif=always` parameter.
* Adjusted the automatic retry mechanism. Accessing IPv6 addresses in a non-IPv6 network will no longer enter the retry process, and the request will fail immediately (solving the problem of some applications stalling when IPv6 VIF is enabled in a non-IPv6 environment, but the application will still continue to send IPv6 requests).

#### Other Optimizations

* Enhanced `$notification.post`, adding support for media resources, sound hints, and automatic dismissal.
* Optimized WireGuard failure handling.
* Reduced the power consumption of the TUIC protocol during sleep.
* Improved the precision of time statistics in the request log system, now accurate to µs level.
* Optimized various abnormal retry mechanisms, avoiding high resource usage caused by continuous retry in the face of some specific problems. For operations that need to be retried continuously (such as WireGuard reconnection, Ponte server reporting to iCloud), Surge will now retry after 0.1s, 0.5s, 1s, 5s, 10s, 30s after an error.
* Optimized the caching system for external resources.
* Added the profile line modifier `#!REQUIREMENT`.

#### Detail Adjustments

* Limited the length of logs that can be written to request notes in debug mode by scripts.
* Changed the default UDP test target to 1.0.0.1.
* If incorrect types of fields are passed when using API in scripts, it will result in script errors.
* After the script is completed or times out, unfinished $httpClient will no longer call the callback function.

#### Issue Fixes

* Fixed the issue where the HTTP Body captured from remote devices could not be read in the Dashboard.
* Fixed the problem where Header Rewrite rules could not match URLs based on the Host field.
* Corrected the issue where ip-version and tos parameters could not take effect when testing proxies.
* Fixed the crash issue caused by mistakenly passing null when executing scripts via HTTP-API.

<https://dl.nssurge.com/mac/v5/Surge-5.7.0-2724-acaafccea020f6afdc758c83057ffcbb.zip>

#### Version 5.6.0

**New Feature**

* Mock (Map Local) feature fully enhanced.
  * Added data types such as `text`, `tiny-gif`, `base64` for inline direct data return.
  * Added `status-code` parameter
  * UI related configurations have not been updated yet. For usage methods, see the documentation: <https://manual.nssurge.com/http-processing/mock.html>
* When the parameter `encrypted-dns-follow-outbound-mode=true` is configured, if a DoH/DoQ/DoH3 connection matches a proxy server using a domain name, and if there is a DNS Local Mapping record for that proxy server's domain name containing an IP address or traditional DNS server, then it is permissible to query through that proxy server. (Querying DNS through a proxy server will break CDN optimization, leading to severe slowness when loading images and videos. Unless there are very special requirements and it is not necessary to configure in this way, domain rules should be used to ensure requests are directly queried by the proxy server.)
* Added feature Body Rewrite, see documentation for details: <https://manual.nssurge.com/http-processing/body-rewrite.html-> Added recognition for STUN packets, which can be matched using PROTOCOL,STUN. Similar to QUIC, to ensure compatibility, PROTOCOL,UDP can also continue to match STUN traffic.

**Enhancements**

* Optimized request logging. Now the specific rules matched for URL Rewrite and Header Rewrite will be displayed.
* Adjusted the logic of how the DNS engine handles empty results. Now when multiple DNS servers are configured, it no longer waits for all servers to respond with empty results in order to avoid additional waiting when AAAA records do not exist. (However, since the behavior of DNS servers may vary in different environments, observe whether this change causes side effects; please provide feedback if issues arise causing abnormal results.)
* Canceled warning notifications when ICMP exceeds limits

#### Fixes

* Enhanced compatibility when decompressing HTTP Body.
* Fixed a crash in Surge caused by passing some incorrect types of parameters in scripts.
* Adapted to new system restrictions, fixed the issue where selecting to display the main window is ineffective in some cases
* Fixed compatibility issues with non-https WebSocket in proxy mode and the new version of Safari

<https://dl.nssurge.com/mac/v5/Surge-5.6.0-2611-efc3b7ebb3872061e9a6a4917742e203.zip>

#### Version 5.5.0

**Module**

* Added several new official modules; official modules can now be dynamically updated.
* Modules have a new classification field for convenient access and categorization in the UI.
* Modules now accept parameter tables, supporting multiple parameters. Parameters will be used to modify module content through text replacement.

**Script**

* New script execution engine. Optimized execution performance and memory usage.
* $httpClient has added several practical parameters. For more details on the updates above, see the documentation.

**Enhancements**

* New parameter: always-raw-tcp-keywords. For usage, refer to documentation.
* Added SRC-PORT rule for matching client port numbers.
* IN-PORT/SRC-PORT/DEST-PORT three rules are categorized as port number rule types, supporting three kinds of expressions:
  * Directly writing the port number, such as IN-PORT,6153
  * Port number closed interval: such as DEST-PORT,10000-20000
  * Using >, <, <=, >= operators, such as SRC-PORT,>=50000
* The UI can now maintain pure empty lines from original configurations after editing.

**Fixes**

* Corrected a detail issue with QUIC flow control and optimized latency performance for Ponte/TUIC/Hysteria2 protocols.
* After editing a single rule, the notification-related parameters will be retained.

<https://dl.nssurge.com/mac/v5/Surge-5.5.0-2586-ed7ce88d6b2a286537ff5402324cb7fe.zip>

#### Version 5.4.3

* Rewrote the virtual IP database, now the database can automatically clean up data based on the last time of use.
* Fixed some issues that may occur when using Snell v4 with WireGuard and enabling reuse.
* For DNS requests with illegal domain names, an empty result response will be generated instead of being directly ignored.
* `tun-included-routes` and `tun-excluded-routes` parameters now supports IPv6 CIDR block when IPv6 VIF is enabled.
* Support configuring no-resolve for built-in rule sets/Inline rule sets.
* Surge Ponte connections no longer validate peer addresses to ensure normal operation in certain special scenarios.
* Bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.4.3-2540-511d4692c27626166bbcbb61fdd56bc8.zip>

#### Version 5.4.2

* Fixed an issue that the built-in rule set LAN failed to correctly trigger DNS resolution.
* Fixed an issue that could cause a crash when handling some malformed UDP packets.
* Fixed an issue that the system that could potentially misjudge has been restarted, causing the Fake IP table to be cleared.
* Fixed a compatibility issue with a specific HTTP server.
* Compatible with some non-standard SOCKS5 UDP server implementations, adjusted errors to warnings.
* Other bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.4.2-2502-001dc6b9672b7e79f92ca5cd3be6baf2.zip>

#### Version 5.4.1

**Rule Engine Optimizations**

* The implementation of RULE-SET and DOMAIN-SET has been completely rewritten. Now, Surge automatically preprocesses and indexes rule sets during resource updates, significantly increasing the matching speed.
  1. There is no longer any difference in performance and memory usage between RULE-SET and DOMAIN-SET types of rule sets, allowing flexible usage.
  2. There is no longer a restriction in DOMAIN-SET rule sets that prevents the use of eTLDs.
  3. The matching speed for DOMAIN, DOMAIN-SUFFIX, IP-CIDR, and IP-CIDR6 rules in RULE-SET has been greatly improved.
  4. A DOMAIN/DOMAIN-SUFFIX rule set with approximately 100,000 entries used to take 100ms for a single match in the old version; now, it only takes single-digit ms.
  5. An IP-CIDR rule set with approximately 10,000 entries used to take about 0.1ms for a single match in the old version. The new version only needs 0.0002ms, an improvement of about 500 times. The performance improvement for IP-CIDR6 rules is even greater.
  6. In the new version, building a regional IP address collection using the IP-CIDR rule set offers the same performance as directly using the internal GEOIP rule.
  7. The Inline Ruleset added in the previous version does not benefit from this optimization, but there is virtually no difference at the scale of hundreds of entries.
  8. In previous versions, rules within a Ruleset were matched one by one from top to bottom. If rules requiring DNS resolution were included, DNS would only be triggered when starting to match that sub-rule. In the new version, if any rule requiring DNS resolution is included in the rule set, DNS resolution will occur before testing that rule set. (In most cases, there is no difference)
* Main ruleset matching efficiency has been slightly optimized.
* The efficiency of IP-CIDR6 rules has been significantly improved even in non-indexed situations.
* RULE-SET rules can now be configured directly with parameters no-resolve and extended-matching, which are equivalent to configuring all sub-rules with these parameters.
* DOMAIN-SET rule sets also support configuration with extended-matching.

**Minor Optimizations**

* Now, when performing MITM, the certificate used for signing will be sent to the client together, to support using intermediate certificates for MITM.
* All comments (at the beginning and end of lines) can now use `#`, `//`, `;` three common comment symbols.
* Profile error message prompt optimization, now it can give the exact line number where the error occurred more accurately.
* Optimize Surge Ponte error handling process, correct the issue where device information is not automatically updated under certain errors.
* Bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.4.1-2495-041f47425e9ecf56580562ce01560448.zip>

#### Version 5.4.0

**New Features**

* Protocol sniffing

  Requests to port 80 and 443 will wait for the client to send the first packet, then extract the SNI and other information for the rule system to judge.

  * `DOMAIN`, `DOMAIN-SUFFIX`, `DOMAIN-KEYWORD` rules add an optional parameter called `extended-matching`. When this parameter is enabled, the rule will try to match both the SNI and the HTTP Host Header (or :authority).
  * Added a parameter called `always-raw-tcp-hosts`, used to forcibly turn off active protocol detection for specific hostnames.
* New proxy protocol support: Hysteria 2

  Hysteria 2 is a proxy protocol optimized for unstable and packet-loss-prone network environments, based on UDP/QUIC.
* Automatic QUIC blocking

  Since most proxy protocols are not suitable for forwarding QUIC traffic, Surge will now automatically block QUIC traffic to make it fallback to HTTPS/TCP protocol, ensuring performance. For QUIC traffic that hits the MITM hostname, it will also be automatically rejected.
* ECN (Explicit Congestion Notification) support for QUIC-based protocols

  Significantly improved the performance of the Vector(Surge Ponte)/TUIC/Hysteria 2 protocol.

**Optimizations**

* Reworked HTTP capture functionality
  * The related settings are no longer stored in the configuration, the `[Replica]` section has been deprecated.
  * Added an automatic shut-off setting after turning on the capture switch, which can automatically stop capturing based on time, size, or the number of requests.
  * Added automatic activation of MITM after turning on the capture switch, which can be additionally turned on for specific hostnames. (Even if the main MITM switch is off).
  * Added an option to only save HTTP/HTTPS requests after turning on the capture switch.
* Improved compatibility with some non-standard protocols.
* When testing the Ponte policy, the test URL has been changed from `proxy-test-url` to `internet-test-url`.
* Following the WireGuard protocol standard recommendation, WireGuard handshake packets will now be tagged with 0x88 (AF41) DSCP to increase the success rate.
* When forwarding UDP packets via WireGuard, it supports retaining the TOS(DSCP/ECN) tag of packets inside the tunnel.
* Based on the WireGuard protocol standard recommendation, Surge will copy the ECN tag from packets inside the tunnel to packets outside. When receiving packets with an ECN tag, they will be strictly merged according to RFC6040. (`ecn=true` must be set for the policy).
* UDP NAT can close the UDP session early based on ICMP messages.
* Improved PMTU support for QUIC.

**Bug Fixes**

* Fixed the issue where the external resources of rule sets needed to be reloaded to take effect after updates.
* After a network switch, it will forcefully break the original long connection of DoH/DoQ/DoH3 to avoid obtaining results that are not suitable for the current network environment.
* Fixed the issue where invalid certificates might cause the key store interface to crash.
* When performing MITM on HTTPS requests that directly connect using an IP address, the IP address should not be sent as SNI, as this might cause compatibility issues.
* Other bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.4.0-2470-d6f513ab6e647abc29490f1f3506667f.zip>

#### Version 5.3.2

* Surge Mac is now ready for macOS Sonoma.
* External resources can now be remotely managed and updated by Surge iOS.
* Fixed the issue where the location permission request could not be correctly triggered.
* Surge Web Dashboard upgraded to version 2.0.4.
* Other improvements.

<https://dl.nssurge.com/mac/v5/Surge-5.3.2-2393-f4b3e5e9a7bc5b73106ace7b0776eefe.zip>

#### Version 5.3.1

* Surge Dashboard now can directly create temporary rules for local and remote Surge instances.
* Surge Web Dashboard now upgraded to version 2.0.
* Added Inline Ruleset, which allows the Ruleset to be written directly in the main profile
* Module enhanced. Modules can now operate \[WireGuard \*] and \[Ruleset \*] sections.
* Added an HTTP API for obtaining CA certificates (DER format): GET /v1/mitm/ca.
* Fixed that MITM failed records could not be correctly generated.

<https://dl.nssurge.com/mac/v5/Surge-5.3.1-2383-066f883d96a472655c9ea7be50475b8b.zip>

#### Version 5.3.0

* You can now directly access the Remote Dashboard of registered devices through Surge Ponte.
* The Surge Dashboard can now operate the policy group and outbound options of remote devices.
* macOS Sonoma now requires location permissions to obtain the SSID. If related rules and subnet settings are used, Surge will prompt for location permissions.
* Fixed a bug that the override of a policy group cannot be canceled remotely.
* Corrected the compatibility issue between VIF and specific devices.
* Surge Ponte improvments.
* Minor bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.3.0-2375-bc1b4791973df9aba493c3190a7b0050.zip>

#### Version 5.2.3

* You can now create a new modifiable profile based on an existing profile. In this new profile, the selected sections will reference the corresponding content in the original profile and will automatically synchronize with the original profile. At the same time, unselected sections in the new profile can be modified freely without being affected by the original profile. (The UI for the detached profile feature.)
* The detached profile now can include the Enterprise profile.
* Fixed the issue that it was impossible to connect when the SSH server configured a banner.
* You can now use the UI to edit ShadowTLS parameters.
* Optimize performance in VIF v1 mode for ARM64 architecture. When the VIF mode is set to automatic, the new version will automatically use the v1 engine under M1/M2 processors, with a maximum performance of \~8Gbps, thereby avoiding compatibility and stability issues.
* Correct the issue where the opening position of the Dashboard main window may be incorrect.

<https://dl.nssurge.com/mac/v5/Surge-5.2.3-2354-ce8606235be8df196c0e9619a9c8cbbd.zip>

#### Version 5.2.2

* Fixed the problem where there might be incorrect prompts about system proxy settings being modified by other applications when there is no valid network.
* Fixed some issues that may occur when using TUIC v5 as the underlying-proxy.
* Fixed the issue where if WebSocket is enabled, it cannot correctly construct a WebSocket request when directly using an IPv6 address as the vmess hostname.
* Provide clearer error prompts when the SOCKS5 server does not support UDP relay.
* Bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.2.2-2340-74b1e55a52888040394976468a61d973.zip>

#### Version 5.2.1

* Surge Ponte now can work in LAN-only mode when NAT type doesn't meet the requirement. Devices on same LAN can still access.
* The connection limiter mechanism added in the previous version has been temporarily removed.
* Optimize the logic of setting as system proxy function.
* Fixed a memory leak issue.
* Bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.2.1-2333-ef97cd79e935d838387dc99712fb38b3.zip>

#### Version 5.2.0

* Due to the fixed size of macOS network stack memory, when the network stack buffer is exhausted, the kernel will automatically close the program with the highest occupancy to release resources. This problem may occur when using Surge to take over P2P downloaders. This version will automatically check for this issue and enter safe mode automatically.
* Surge VIF engine has been upgraded to v3, no longer relying on Packet Filter (pf), solving compatibility issues with virtual machines and network sharing functions. At the same time, connection number limits have been added to avoid system resource exhaustion caused by excessive concurrent requests.
* Add a connection limiter for single processes and single devices to avoid consuming large amounts of resources for individual devices.
* Support for QUIC's PMTU discovery, which improves the performance of Surge Ponte and TUIC protocols.
* Optimize error handling logic of QUIC-based protocols.
* When forwarding UDP packets using TUIC v5, follow the DF flag of the IP packet. Avoid the issue that can occur when visiting the QUIC website with TUIC v5.
* Other bug fixes and optimizations.

<https://dl.nssurge.com/mac/v5/Surge-5.2.0-2302-721d7db5429609c5a54af922f045a509.zip>

#### Version 5.1.1

* Added support for TUIC v5 protocol.
* Optimized the performance of Surge Ponte/TUIC.
* Optimized the request Note recording when the strategy group is abnormal.
* Fixed the problem that connection reuse was not done correctly under MITM H2 mode.
* Fixed the problem that the request of $httpClient/DoH may sometimes be accidentally cancelled.
* Adjusted the traffic characteristics of Snell v4 protocol.
* Other bug fixes and optimizations.

<https://dl.nssurge.com/mac/v5/Surge-5.1.1-2264-6f04d8ac1bbf1c91178a09124e45e37e.zip>

#### Version 5.1.0

**Surge Ponte**

* Surge Ponte supports cross-iCloud account sharing.
* Fixed issues that might occur when accessing HTTP/1.0 servers via Surge Ponte or TUIC protocol. (e.g. ASUS router management page)

**Interface**

* Icon Library: You can now select icons for your device from a library of about 7000 icons.

**Proxy Protocol Related**

* Fixed an issue that the reuse feature could not work properly under Snell V4.
* SSH protocol now supports server public key fingerprint pinning, see the manual for usage.

**Scripts**

* $httpClient supports binary mode.
  * The body of the request supports TypedArray.
  * Passing in binary-mode: true in the request parameters allows the return result to be returned as TypedArray.
* Fixed the problem that `http-request` type scripts could not use binary data directly as response.

**Others**

* Policy group adds parameter `external-policy-modifier`, which can be used to adjust external policies.
* Optimized the request log system
  * Added category marks to the logs.
  * Rule system adds more output for DNS and rulesets.
* Other bug fixes and optimizations.

<https://dl.nssurge.com/mac/v5/Surge-5.1.0-2216-82115a08df678cfa87137a506f7df061.zip>

#### Version 5.0.3

* Added UDP relay support for the VMess protocol
  * Since the VMess server-side supports UDP forwarding by default, there's no need to add extra parameters to use it.
  * Due to design flaws in the VMess protocol, when using VMess to forward UDP traffic, P2P scenarios may not work, such as voice calls, online gaming, etc. Therefore, it is not recommended to use the VMess protocol.
* SSH protocol now supports specifying the server's public key fingerprint. Check the manual for more information.
* The external IP address is now obtained through the STUN protocol and no longer relies on api.my-ip.io.
* The DDNS now uses the secured IPv6 address instead if a temporary one, when IPv6 is selected.
* Bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.0.3-2199-c241935acf37b3ec7f7fa4f5120e8690.zip>

#### Version 5.0.2

* Due to the new privacy restrictions on macOS, if the Wi-Fi BSSID-related features are used, Surge will request location service permissions to read the Wi-Fi BSSID.
* Shadow TLS v3 is now supported. Append `shadow-tls-version=3` to enable it.
* Surge Mac now supports Adaptive TLS Fingerprint. For more information, please check the community thread.
* Supports a new parameter `external-policy-modifier` for groups to modify the parameters of external policies.
* The new proxy client notification will only be prompted when a real request is received and will no longer be displayed when being port scanned.
* Bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.0.2-2186-2ab1aba0dc49688683b2e4d43200e468.zip>

#### Version 5.0.1

* The registered Ponte device view is now available when the Ponte switch in off.
* Fixed a crash while using Surge Dashboard via USB.
* $httpClient now supports binary mode.
* Bug fixes.

<https://dl.nssurge.com/mac/v5/Surge-5.0.1-2162-22743a4d2f1e0aeb0b872e8f544c2e69.zip>

### Surge Mac V4

#### Version 4.11.2 (May 6, 2023)

* Replace the API service provider for obtaining external IP.

<https://dl.nssurge.com/mac/v4/Surge-4.11.2-2016-b4c9dad3472594b01ef3d8ac9b05c78e.zip>

#### Version 4.11.1 (Apr 15, 2023)

* Fixed a bug that Surge VIF v6 may not be enabled automatically when set to auto.
* Fixed a bug that requests sent by $httpClient may not obey the ip-version parameter of the selected policy.
* Fixed a bug that DDNS can’t be enabled if the user deleted the iCloud data of Surge.
* Fixed a bug that domain rules can’t match if the requests’ domain is in uppercase.
* Fixed a bug that the UI can’t add listeners in the advanced proxy service settings.
* Fixed a bug that the UI can’t add new items in the metered network SSID view.
* Fixed a WireGuard related crash.
* Other bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.11.1-2013-eac717436d753b5ea2b82a206d5851e7.zip>

#### Version 4.10.3 (Feb 16, 2023)

* The installed modules are now synced between Mac devices via iCloud.
* Performance optimization.
* Fixed an issue that the DHCP service might not be able to start after auto-upgrading.
* Fixed an issue that the remove helper script can't be executed on macOS Ventura.
* Fixed menu bar icon issues when using multiple displays.
* WireGuard related optimizations.
* Support for customizing the reserved bits of WireGuard, also known as the client ID or routing ID.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.10.3-2004-d730cb305e3cbb949f82d01771624b4e.zip>

#### Version 4.10.2 (Feb 3, 2023)

* UDP performance optimization.
* Change the way connections are rejected from ICMP to TCP RST. This ensures that the Windows operating system can correctly detect the rejection.
* Fixed the proxy editing view layout issue.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.10.2-1981-d99d487bbd9f9109a00dd5a5b7915be4.zip>

#### Version 4.10.1 (Dec 3, 2022)

**New Feature**

* Gaming Optimization Mode: `udp-priority = true`. Enabling it will prioritize UDP packets when the system load is very high, and packet processing is delayed.
* SOCKS5 proxy now supports UDP forwarding, as the server side does not consistently support UDP forwarding, the parameter udp-relay=true needs to be explicitly configured.
* The `ipv6-vif` parameter now supports `always` and `auto` like Surge iOS. If set to `auto`, IPv6 VIF will only be enabled if a valid Internet IPv6 address (2000::/3) exists.

**Minor Improvements**

* URL regular expressions for Script, Rewrite, Mock, etc. will try to match URLs constructed in many different ways (e.g. Host field in Header) to solve the problem that some apps use custom DNS logic to request directly to IP addresses.
* Removed the silencing mechanism after UDP forwarding errors to avoid extra waiting time after switching networks.
* The IPv6 switch no longer prevents direct access to IPv6 addresses when turned off. The switch is now limited to controlling whether the DNS Client requests AAAA records.
* Automatic disabling of AAAA queries due to DNS issues will be prompted in the Event Center instead of just in the logs.
* Fixed handling issue of generating IPv6 fragmentation when forwarding IPv6 UDP packets via WireGuard.
* The external policy group will skip the line and continue processing when it encounters invalid content instead of returning an error directly.
* Adjusted the buffering mechanism of raw TCP forwarding to avoid conflicts with some apps.
* Fixed REJECT requests not being marked as failed under MITM H2.
* Adjusted the output text under diagnostics.
* Other bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.10.1-1964-34ee4f3efbd20065ad808cf0cab6d380.zip>

#### Version 4.10.0 (Nov 10, 2022)

**Support New Proxy Protocol**

* New proxy protocol supported: TUIC. (<https://github.com/EAimTY/tuic>).
* New proxy protocol supported: Snell V4. (<https://manual.nssurge.com/others/snell.html>)
* New proxy transport layer protocol supported: Shadow TLS. (<https://github.com/ihciah/shadow-tls>). You may append `shadow-tls-password=pwd` to any proxy to utilize it.

**Other Improvements**

* shadowsocks now supports the none cipher.
* Modified the handshake packet construction logic when forwarding HTTPS requests to proxies, which can slightly optimize latency.
* Surge HTTP requests for proxy testing no longer contain a User-Agent header.
* A new option to allow to disable system processes combining in the process view.
* Fixes an issue on M1 processors where the system would move Surge to the efficiency core when using an application in full screen causing a significant drop in performance.

**Bug fixes**

* Fixed a memory leak that could occur when HTTP capturing is enabled.
* Fixed an issue that may not work properly when nesting proxy chains with a specific protocol combination.
* Fixed an issue that the module could not configure the MITM h2 parameter.

<https://dl.nssurge.com/mac/v4/Surge-4.10.0-1927-f009d35c5da9df00cccf818edd74b20d.zip>

#### Version 4.9.1 (Sep 29, 2022)

* Overall performance optimization.
* Added an alert when using router mode in an IPv6 network.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.9.1-1866-e90f4c1609827e5669c21803ac8e90a3.zip>

#### Version 4.9.0 (Sep 11, 2022)

**Router Mode**

* Overall performance optimization.
* Fixed a performance issue with PS5.

**Surge VIF IPv6**

* You may use the parameter `ipv6-vif = always` to let Surge configure IPv6 address and the default route for Surge VIF.
* Surge VIF now supports handling raw TCP and UDP traffic with IPv6.
* ICMPv6 relay is now supported.

**MITM**

* New parameter `client-source-address`. Use this parameter to enable the MITM function on some devices only.
  * It's a list parameter, using commas as the separator.
  * You may specify a single IP address or use a CIDR block, both IPv4 and IPv6 are supported.
  * You may use the `-` prefix to exclude some clients, e.g., `client-source-address = -192.168.1.2, 0.0.0.0/0`
  * If the parameter is not set, MITM is enabled for all clients. A equivalent to `client-source-address = 0.0.0.0/0, ::/0`
  * `127.0.0.1` should be included if you want to enable MITM for the current device.

**WireGuard**

* WireGuard now supports IPv6 tunneling.
  * Use parameter `self-ip-v6` to assign an IPv6 address for Surge.
  * You may configure `self-ip` and `self-ip-v6` to utilize the IPv4 & IPv6 dual stack, or just one of them to use the single stack.
  * Make sure to use the correct `dns-server` address for the enabled IP protocol version.
  * The `allowed-ips` parameter supports IPv6 CIDR now, e.g., `allowed-ips = 0.0.0.0/0, ::0/0`

**Others**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.9.0-1850-c52ab2531bb82ff6f8d72df65f65c76a.zip>

#### Version 4.8.0 (Aug 9, 2022)

**Experimental function: DNS over QUIC and DNS over HTTP/3**

* Surge now supports DNS over QUIC. (e.g.: `encrypted-dns-server = quic://example.com`)
* Surge now supports DNS over HTTP/3. (e.g.: `encrypted-dns-server = h3://example.com/dns-query`)
* Parameter `doh-server` renames to `encrypted-dns-server`.
* Parameter `doh-follow-outbound-mode` renames to `encrypted-dns-follow-outbound-mode`.
* Parameter `doh-skip-cert-verification` renames to `encrypted-dns-skip-cert-verification`.
* The DNS relay (`always-real-ip` and non-A/AAAA record lookup) in the Enhanced Mode now uses the encrypted DNS servers.
* You may use `encrypted-dns-skip-cert-verification=true` to disable server certificate verification for DNS-over-HTTPS.

**Scripting**

* New helper functions: `$utils.ipasn(ipAddress<String>)`, `$utils.ipaso(ipAddress<String>)` and `$utils.ungzip(binary<Uint8Array>)`.
* New subtype of the event script: `notification`. You may use a script to forward Surge notifications to a third-party message service.

**Others**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.8.0-1788-3b96ac4d92f39b6a4a8e195708aae8d8.zip>

#### Version 4.7.0 (Jun 30, 2022)

**MITM over HTTP/2**

* Surge now supports performing MITM with HTTP/2 protocol to improve concurrent performance.
* Surge now supports performing MITM on WebSocket connections.

**Others**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.7.0-1757-0b3d1ec3c3f7067386361dd582ad964a.zip>

#### Version 4.6.1 (Jun 10, 2022)

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.6.1-1718-a39555f74c3f6d43fdcaa8501d55d26a.zip>

#### Version 4.6.0 (Jun 8, 2022)

**SSH Proxy Support**

* You can use SSH protocol as a proxy protocol. The feature is equivalent to the `ssh -D` command.
* Both password and public key authentications are supported.
* All the four types of private keys, RSA/ECDSA/ED25519/DSA, are supported.
* Surge only supports `curve25519-sha256` as the kex algorithm and `aes128-gcm` as the encryption algorithm. The SSH server must use OpenSSH v7.3 or above. (It should not be a problem since OpenSSH 7.3 was released on 2016-08-01.)

**Keystore**

* You may now save sensitive keystore items to the system keychain. (More, Profile, Manage Keystore)

**Others**

* New rule type: IP-ASN. You may use the rule to match the autonomous system number of the remote address.
* Dashboard now shows more details about the remote address, including the ASN.
* Surge will try to fix the system proxy settings after applying fails.
* You can now enable/disable the rewrite rules and DNS local mapping items.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.6.0-1708-9ef4eecae3a0cc5dfebd74e5e850cb2f.zip>

#### Version 4.5.2

**Dashboard**

* You can now export HTTP/HTTPS requests to a HAR file, which is a standard format and can be opened by many web analysis tools

**Proxy**

* New parameter `server-cert-fingerprint-sha256` for TLS proxy policies. Use a pinned server certificate instead of the standard X.509 validation.
* `tls-engine` option is now deprecated. OpenSSL is now the only TLS engine.
* You may use `%PROFILE_DIR%` in the external proxy arguments, which will be replaced to the path of the profile directory.
* You can now use a full profile as the external policy group (policy-path). All proxies in the \[Proxy] section will be used.

**DHCP Server**

* Surge DNS is now integrated with the DHCP device management. You can use a device name to get the IP address directly. Reverse IP lookup is also supported.
* The helper upgrade is now optional to prevent the interrupt after an auto-upgrade.
* Surge now can relaunch itself after a crash.

**CLI**

* surge-cli just got a refresh. Use `surge-cli --help` to know what you can do with it.

**Others**

* Header rewrite now supports using the regex to replace the value.
* Header rewrite now supports modifying the response headers.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.5.2-1663-d480512b326806e7e850f98efe875bec.zip>

#### Version 4.5.1

* There is a kernel bug in macOS 12.3, which significantly degrades performance of the Enhanced Mode and Router Mode. A workaround is deployed in this version.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.5.1-1621-c2a973ddb992df5c34757daacc632598.zip>

#### Version 4.5.0

**WireGuard**

* WireGuard supports multiple peers.
* The allowed-ips now support multiple IP ranges.
* WireGuard supports preshared-key and keepalive.
* WireGuard supports peers with IPv6 endpoints. (But still no IPv6 tunnel support)
* WireGuard and shadowsocks policy now support underlying-proxy.
* The raw TCP connections are now relayed on the L3 layer if no high-level features are used.

**Detached Profile**

* You can now include multiple detached profiles into one section. But the section will be marked read-only and can't be edited with UI.

`#!include A.dconf, B.dconf`

**Policy Group**

* You can now temporarily override an auto test group or an SSID group's optimal option, until Surge restart or reload.
* The new parameter include-all-proxies=true is added to the policy group, which will include all proxy policies defined in the \[Proxy] section, and can be used with the policy-regex-filter parameter for filtering.
* The new parameter include-other-group="group1,group2" is added to include policies from another policy group, and can include multiple policy groups separated by commas, also can be used with the policy-regex-filter parameter for filtering.
* include-all-proxies, include-other-group, and policy-path parameters are allowed to be used in a single policy group at the same time. The policy-regex-filter parameter applies to all three.
* There is an order of precedence among the policy groups for the include-other-group parameter, but there is no order of precedence among the include-all-proxies, include-other-group, and policy-path parameters. For scenarios where the order of sub-policies makes sense (e.g., fallback groups), use policy groups nesting with include-other-group.

**Subnet expression**

* SSID Group is now upgraded to Subnet Group, which supports subnet expression.
* SSID Setting now supports subnet expression.
* The SUBNET rule now supports subnet expression.
* A subnet expression can be one of these:
  * Use SSID:value to match the Wi-Fi SSID, wildcard character is allowed.
  * Use BSSID:value to match the Wi-Fi BSSID, wildcard character is allowed.
  * Use ROUTER:value to match the router IP address.
  * Use TYPE:WIFI to match all Wi-Fi networks.
  * Use TYPE:WIRED to match all wired networks.
  * Use TYPE:CELLULAR to match all cellular networks. (iOS Only)
  * Use MCCMNC:100-200 to match a cellular network. (iOS Only)
* The \[SSID Setting] can control the TCP Fast Open behavior now. Read the manual for more information.

**Others**

* Performance improvements.
* The default timeout of $httpClient is 5 seconds now.
* New Official Module: Block HTTP3/QUIC
* You can now adjust the effective order among modules.
* Modules allow to modify the skip-server-cert-verify and tcp-connection parameters of \[MITM].
* The client will get an ICMP connection refused message instead of TCP RST if a REJECT policy matches.
* Supports IPv6 addresses with scope ID.
* The Network diagnostics can test proxy UDP relay now.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.5.0-1618-5d2042223762269c5322520810dd7e0c.zip>

#### Version 4.4.1

* You may click a proxy of a select group in the main menu with holding the Option key, to test the proxy alone.
* Fixed a bug that UDP NAT can't be released if a REJECT policy is matched.
* Other bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.4.1-1532-abe4b5471dcb3eaeec51fcda768cc635.zip>

#### Version 4.4.0

* Uses Surge as a WireGuard client, converting L3 VPN as an outbound proxy policy. More information: <https://manual.nssurge.com/policy/wireguard.html>
* Supports VmessAEAD. (Policy parameter: vmess-aead = true)
* Trojan protocol now supports UDP relay. (No additional parameter required)
* The underlying proxy now supports using a policy group.
* Performance optimization.
* Added a release note window to show update history.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.4.0-1521-a0024e9fbe33f5ccaa41316d63cdefee.zip>

#### Version 4.3.1

* Snell Protocol v3, which brings UDP over TCP relay support
  * Optimized for high throughput.
  * Port Restricted Cone NAT support. (aka NAT type 2)
* The http-response scripts can read request headers via $request.headers now.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.3.1-1461-829471a307259fe1729cf06a7cd13d06.zip>

#### Version 4.3.0

* Surge Dashboard now supports managing DHCP devices. All of the properties (name, icon, static IP address, gateway mode) can be edited locally and remotely.
* The traffic statistics data is now persistent between sessions. And you may use Dashboard to view all the detailed statistical data.
* The statistics data range is extended to 24 hours.
* Performance improvements.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.3.0-1430-bde27671bfdadfab143338a7cd5b2fa3.zip>

#### Version 4.2.5

* Performance improvements.
* Supports remote rule editing for Surge iOS remote controller.
* Kill other processes that take over port 53 when starting DHCP service.
* Surge now only executes reloading if the profile is valid.
* Supports custom the policy IP TOS field. Example: test-policy = direct, tos=0xb8.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.5-1414-764146258a319c307056593a1309cf89.zip>

#### Version 4.2.4

* New option: Menubar icon display mode. You can now hide the icon and display the real-time speed only, to save the precious menubar space.
* New HTTP API: GET /policies/benchmark\_results
* Supports IP Fragmentation for UDP and ICMP packets. (IP Fragmentation for TCP packets is already supported in the previous versions.)
* You can now right click on a remote client to add a new rule in the Dashboard.
* Performance improvements.
* Added a few device icons.
* The UI editor of policy group now supports filter and mixed policies.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.4-1399-4f3c53abfe45fce5646d84af11e589c4.zip>

#### Version 4.2.3

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.3-1357-0803594c82248360a95722089650f7f7.zip>

#### Version 4.2.2

* Supports binary mode for http-request and http-response scripts.
* DHCP can detect if a device is private address enabled now.
* Surge won't reload the profile automatically if the new profile is invalid.
* New local and remote notification selections: auto-updating and profile reloading.

<https://dl.nssurge.com/mac/v4/Surge-4.2.2-1351-5dc813192d6e37fdb0895034ebc90b57.zip>

#### Version 4.2.1

**External IP**

* You may now check the external IP address in the interfaces view.

**DDNS**

* Surge Mac can associate its external IP address to .sgddns hostname. You may use the hostname with Surge iOS or Surge Mac on another device. The data is synced via iCloud, and the hostname can't be used publicly.

**Others**

* Surge Mac now can fix the helper installtion issues automatically。

<https://dl.nssurge.com/mac/v4/Surge-4.2.1-1333-14f7cb7cd943be7e4b3cecfb3fcd8ba3.zip>

#### Version 4.2.0

**Web Dashboard**

* The community project YASD is now part of Surge. You can now control Surge via a web browser on local or remote devices. (Licensed by author @geekdada)
* You may now manage the DHCP devices with the Web Dashboard.

**Profile Syntax**

* We have added a profile syntax view to show all the available syntax for the current view if you prefer to edit profile with a text editor. You can find it in Help ▸ Profile Syntax.
* The Diagnostics now can report invalid config lines in the profile.

**Benchmark**

* We have changed the proxy benchmark standard. The result is now similar to a ping test result, which ignores the proxy setup cost.

**Minor Improvements**

* SOCKS proxy service now supports SOCKS4 and SOCKS4a protocol. (Server-side only)
* Cloud Notifications now supports rule notifications.
* The real-time speed is now available on the proxy view.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.0-1321-d4d84696bb58cf8be0189b59ccbe926b.zip>

#### Version 4.1.0

**Scripting**

* You may configure and edit scripts with UI now.

**Profile**

* You may put partial sections into a detached file. See <https://manual.nssurge.com/overview/configuration.html>

**HTTP API**

* Added new profile related HTTP APIs, including GET /profiles, POST /profiles/check
* Added new device management HTTP APIs, including GET /devices, POST /devices, GET /devices/icon
* The HTTP API, proxy services, and external controller now support listening on IPv6 addresses. (No UI supports. Manual profile editing is required.)
* You may now use 'http-api-tls=true' enable TLS for HTTP API access. (aka HTTPS-API)

**Unsupervised Optimizations**

* The external resources downloading now occurs after surge engine started.
* The external resources downloading now automatically starts after if a resource is not ready.

**Other Improvments**

* New rule type: SUBNET, which can match SSID/BSSID/router IP address with a wildcard pattern.
* Significantly optimizes Dashboard performance when handling large numbers of requests.

<https://dl.nssurge.com/mac/v4/Surge-4.1.0-1298-f07b1b8713b2397518f4b252b5786452.zip>

#### Version 4.0.5

**Policy Group**

In this release, we completely refactored the policy group functionality, bringing the following changes:

1. The url-test/fallback/load-balance policy group can no longer be configured with a specific testing URL but with a global testing URL or a policy-configured testing URL. The policy's test results can be used directly in all policy group decisions, eliminating the need to retest each policy group individually.
2. All types of policy groups support mixed nesting. The only requirement is that no circular references can be used.
3. When a group policy is used as a sub-policy of the url-test/fallback/load-balance group.
   * The latency of the select/url-test/fallback/ssid group is the latency of the selected policy.
   * The latency of the load-balance group is the average of the latencies of all available policies.
4. The timeout parameter of a policy group marks policies with latency exceeding this parameter as unavailable when making decisions for the group. But the maximum time taken to test the policy group is controlled by the global test-timeout parameter. (Default is 5s)
5. When testing a group due to decision making, all sub-policies that the group may use are tested, including sub-policies of the sub-policy group.
6. You may use no-alert=true parameter to suppress notifications for particular groups.

**Cloud Notification**

You can receive the notifications on iOS devices. Enable this option first and then configure it on Surge iOS. The two device must use a same iCloud account.

**Minor Changes**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.5-1262-db70f680cd0f15236c8415ec7b804c3a.zip>

#### Version 4.0.4

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.4-1227-9acb8b9e3f39e9048fc82e427184a4af.zip>

#### Version 4.0.3

* You may override the testing URL of a policy for network diagnostics and activity cards.
* The GeoIP database can be updated automatically in the background.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.3-1224-4ef8ae10c8a74c395bb4b6c3f6af6af6.zip>

#### Version 4.0.2

* You may now customize the GeoIP database updating URL.
* tun-excluded-routes and tun-included-routes are now available for Surge Mac.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.2-1219-dbd08724b90aa8b444cd6d0679a245b5.zip>

#### Version 4.0.1

* You may configure the proxy chain with the UI now.
* Fixed some visual inconsistency under reducing transparency mode.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.1-1207-ee7bea1b244950c82a6f90e060fa2d89.zip>

#### Version 4.0.0

* The first version of 4.0.0.

<https://dl.nssurge.com/mac/v4/Surge-4.0.0-1191-d8140b0084223fd3fc4335e4414c0884.zip>

### Surge Mac V3

#### Version 3.5.8

* Bug fixes

<https://dl.nssurge.com/mac/v3/Surge-3.5.8-1130.zip>

#### Version 3.5.7

* Bug fixes

<https://dl.nssurge.com/mac/v3/Surge-3.5.7-1129.zip>

#### Version 3.5.5

**Minor Changes**

* All URL resources now support URLs with a username and password (e.g. <https://user:pass@example.com>), including managed profile, external resources, and importing profile form URL.
* You may switch among the main views with shortcut keys.
* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.5.5-1123.zip>

#### Version 3.5.4

**Changes in Policy Group**

* New parameter: policy-regex-filter. If the parameter is configured, only matched policy line will be used.

**Minor Changes**

* Provides more details for the TLS handshake error.
* Increases the file description limitation alert threshold.

<https://dl.nssurge.com/mac/v3/Surge-3.5.4-1119.zip>

#### Version 3.5.3

**New Parameter: use-local-host-item-for-proxy**

`[General]`

`use-local-host-item-for-proxy = true`

If use-local-host-item-for-proxy is true, Surge sends the proxy request with the IP address defined in the \[Host] section, instead of the original domain.

**Changes in Load Balance Group**

* load-balance group now supports connectivity testing before being used. Add 'url' parameter to enable it.
* Parameters 'timeout', 'interval' and 'evaluate-before-use' are also available.

**Minor Changes**

* Surge will send an ICMP port unreachable message if UDP forwarding fails.
* Eliminate unnecessary local DNS lookup while forwarding UDP traffic to a proxy server.
* Fixed a bug that connecting to Surge iOS via USB is not working in Surge Dashboard.

<https://dl.nssurge.com/mac/v3/Surge-3.5.3-1094.zip>

#### Version 3.5.2

**SSID Suspend**

* Surge Mac supports SSID suspend now. The system proxy and enhanced mode will be temporarily suspended under specified SSIDs.
* The name of WiFi can be an SSID, a BSSID, or a gateway IP address.
* No UI configuration in the current version.

**REJECT-DROP**

* REJECT-DROP policy is now effective to proxy connections. The connections matched with a REJECT-DROP policy will be closed in 60-120s later without any data returned.

**Global Proxy**

* You may now select and view sub-policy for policy groups while using the global proxy mode.

<https://dl.nssurge.com/mac/v3/Surge-3.5.2-1082.zip>

#### Version 3.5.1

**New rule type: DOMAIN-SET**

* DOMAIN-SET is just like RULE-SET. But it is designed a large number of rules and highly efficient.
* Unlike RULE-SET, you can only write hostnames (domain or IP address) in it. One hostname per line.
* You may use "." prefix to include all sub-domains.

**Changes in SRC-IP**

* SRC-IP rule now supports IP-CIDR for both IPv4 and IPv6.

**Changes in DNS over HTTPS**

* From this version, if DNS-over-HTTPS is configured, the traditional DNS will only be used to test the connectivity and resolve the domain in the DOH URL.
* The DNS over HTTPS now has a separate parameter: doh-server. The DOH servers in 'dns-server' will be moved to the new parameter after saving.
* The legacy DNS is always required now.
* DOH can be matched with rule 'PROTOCOL,DOH' now.
* Added a new parameter 'doh-follow-outbound-mode'. In the previous version, the DOH client follows the system proxy settings. From this version, all DOH requests will use DIRECT policy by default. If 'doh-follow-outbound-mode' is set, the DOH requests will follow the outbound mode settings regardless of the system proxy settings.
* We are refactoring the HTTP client for DOH and scripting. Please feedback if you encounter any issue.

**Changes in Scripting**

* Added a simple view to test the script. You may find it in the Window menu.

**Minor Changes**

* Fixed a crash in Dashboard while using search.
* Bug fixes.

**Known Issues**

* You may not configure DOH with UI in this version temporarily.

<https://dl.nssurge.com/mac/v3/Surge-3.5.1-1069.zip>

#### Version 3.5.0

* New feature: Module, which can override the current profile with a set of settings. Highly flexible for diverse purposes. See the post in the community for more information: <https://community.nssurge.com/d/225-module>.
* You may enable modules in the menu now.
* You may view the detail of a module by double clicking.
* Supports pattern filter for Dashboard requests.
* Added a new rule type: PROTOCOL. The possible values are HTTP, HTTPS, SOCKS, SNELL, TCP, UDP.
* You may now use UI to add and edit load-balance group.
  * DNS over HTTP (DoH) now uses DNS wireformat by default. You may configure doh-format=json in \[General] to continue using JSON format.
  * TCP connection setup optimizations.
  * Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.5.0-1039.zip>

#### Version 3.4.0

* Snell protocol now upgrade to version 2, supporting to reuse TCP connections to improve performance. <https://github.com/surge-networks/snell/releases>
* Supports a new proxy protocol: Trojan.
* Remote Dashboard now upgraded to Remote Controller. You may use Surge iOS to select policy group, toggle HTTP capture/MitM, and switch outbound mode remotely.
* The comment lines in the text config won't lost after editing with UI.
* You may open the new connection window of Dashboard by holding the Option key while clicking the Dashboard item in the main menu.
* Supports to use OpenSSL as TLS provider. See the post in the community for more information: <https://community.nssurge.com/d/196-surge-ios-mac-tls-provider>.
* Fixed a bug that Surge may not be able to process DNS answer packets which is longer than 512 bytes.

<https://dl.nssurge.com/mac/v3/Surge-3.4.0-989.zip>

#### Version 3.3.3

* Fixed a bug which causes TFO failed.
* You may use a profile which stores in a subdirectory of the profile directory.
* Added Traditional Chinese localizations.
* Fixed a bug that the menu might be unresponsive.
* Fixed crashs on macOS 10.11.

<https://dl.nssurge.com/mac/v3/Surge-3.3.3-939.zip>

#### Version 3.3.2

* Supports MITM on non-standard port for TCP mode.
* Proxy editing view now supports VMess protocol and all misc options.
* A new option 'persistent' has been added to the load-balance group. (aka PCC, per connection classifier) When 'persistent=true' is set, a same hostname will always get the same policy.
* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.3.2-925.zip>

#### Version 3.3.1

* Supports VMess proxy protocol.
  * vmess-proxy= vmess, example.com, 443, username = 12345678-abcd-1234-1234-47ffca0ce229, ws=true, tls=true, ws-path=/v2, ws-headers=X-Header-1:value|X-Header-2:value
  * All proxy options for TLS proxy are available.
  * Web-socket and TLS options would degrade performance. Only enable when necessary.
  * Surge only supports chacha20-poly1305 encryption algorithm. Please make sure the server supports it. We have no plan to implement other ciphers.

<https://dl.nssurge.com/mac/v3/Surge-3.3.1-906.zip>

#### Version 3.3.0

* The scripting has been rewritten totally. The old scripts are not compatible with this version. See <https://community.nssurge.com/d/33-scripting/3>
* Added support for TLS 1.3. Append 'tls13=true' to the proxy line to enable it. (Requires macOS 10.14 or above)
* Supports to use 'X-Surge-Policy' to force policy for HTTP/HTTPS requests.
* SSID group now supports to use the IP address of default router as an identifier.
* New policy group type: load-balance, which will use a random sub-policy for every request.
* Supports DNS over HTTPS. More information in community: <https://community.nssurge.com/d/48-dns-over-http>
* IN-PORT and DEST-PORT rule now supports port range expression: `DEST-PORT,8000-8999,DIRECT`
* Provides compatibility for Surge iOS 4.
* Surge Mac software package is now notarized by Apple.
* A new standalone view to manage all external resources.

<https://dl.nssurge.com/mac/v3/Surge-3.3.0-893.zip>

#### Version 3.2.1

* Fixed a bug that Handoff doesn't work between Surge iOS and Dashboard.
* Fixed a bug that 'Update All Remote Resources' may not work.

<https://dl.nssurge.com/mac/v3/Surge-3.2.1-863.zip>

#### Version 3.2.0

**Scripting**

* New major feature: scripting. You may use JavaScript to modify the response as you wish. See the manual for more information: <https://manual.nssurge.com/http-processing/scripting.html>
* You can now use a script to modify the response headers and status code.

**Dashboard**

* USB module has been refactored to improve stability. Also, you may choose the device from multiple USB devices now.

**MitM**

* HTTP and MitM engine has been refactored. Please report if you encounter any issues.
* You can now use URL-REGEX rule for MitM connections.
* You may use prefix '-' to exclude domains for MitM. Example:

```
[MITM]
hostname = -*.apple.com, -*.icloud.com, *
```

* MitM hostname list now supports port number. By default only the connections to port 443 will be decrypted. Use suffix :port to enable MitM for other ports. Use suffix :0 to enable MitM for all ports on the hostname.
* URL rewrite type 'header' is now available for MitM connections. You may also use it to rewrite a plain HTTP request to an HTTPS request.

**Misc**

* You can now enable/disable a rule.
* Added a small indicator in the menu icon for Metered Network Mode.
* Added main switches for rewrite and scripting.
* Supports TCP SACKs for Surge VIF.
* New general option: force-http-engine-hosts. You can force Surge to treat a raw TCP connection as an HTTP connection, to enable high-level functions such as URL-REGEX rules, rewrite and scripting. This option uses the same format as \[MITM] hostname option.
* New option for url-test/fallback group: evaluate-before-use. By default, the requests before a connection evaluation will use the first policy in the list and trigger the evaluate. Enable the option to delay the requests until the evaluation completed.

<https://dl.nssurge.com/mac/v3/Surge-3.2.0-860.zip>

#### Version 3.1.1

* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.1.1-811.zip>

#### Version 3.1.0

* Added more feature to the main menu.
* Dashboard now supports to export all requests to an archive file for opening later or sharing.
* Supports a new proxy protocol: Snell. (<https://github.com/surge-networks/snell>)
* Surge Mac can work as a Snell proxy server now. See <https://manual.nssurge.com/others/snell-server.html> for more information.
* A new option to automatically reload if the profile was modified externally/remotely.
* Fixed a compatibility issue with some FTP clients.
* Added a new option to disable automatically notification dismissing.
* The update notification is now shown as a banner instead of an alert window.
* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.1.0-807.zip>

#### Version 3.0.6

* Optimizations for no network error handling.
* Reduces CPU usage on idle.
* Fixed a bug while enabling MitM with a new certificate.
* Fixed crashes on macOS 10.11.

<https://dl.nssurge.com/mac/v3/Surge-3.0.6-781.zip>

#### Version 3.0.5

* CPU usage optimizations (50% reduced for high throughout).
* Enabled Hardened Runtime to get enhanced security protections in macOS Mojave.
* Add more notes for rule evaluating stage.
* WeChat.app may flood ping when network is unstable, which causes a high CPU usage of Surge. We added a mechanism to limit ICMP throughput in this version.

<https://dl.nssurge.com/mac/v3/Surge-3.0.5-773.zip>

#### Version 3.0.4

* Added a new option 'hijack-dns' to hijack DNS queries to other DNS servers with fake IP addresses. See manual for more information: <https://manual.nssurge.com/others/misc-options.html>.
* Bug fixes

<https://dl.nssurge.com/mac/v3/Surge-3.0.4-759.zip>

#### Version 3.0.3

* Supports new iCloud container for Surge iOS migration.
* The MitM feature is now compatible with Android system. Please regenerate an new CA certificate before using with Android.
* Fixed some UI issues in Dashboard.
* Fixed a bug that MitM may refuse to enable after modifying settings.
* Fixed a bug that br decompress may fail.
* Fixed a bug that the menu item may use a wrong color if the accent color of system isn't blue.
* Fixed the JSON viewer color issue in the Dark Mode.
* Minor bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.0.3-754.zip>

#### Version 3.0.2

* Allows import the profile from a URL.
* Fixed an issue that the HTTP capture button may show wrong state in Dashboard.
* Fixed an issue that Dashboard doesn't show User-Agent as the process name while connecting to iOS device.
* Fixed an issue that the bandwidth of processes may be inaccurate.
* Fixed an issue that the DEST-PORT rule may not be parsed.
* Fixed an issue that ruleset can't be used with logical type rule.

<https://dl.nssurge.com/mac/v3/Surge-3.0.2-736.zip>

#### Version 3.0.1

* Fixed an issue that TFO option will not be saved.
* Fixed an issue that UDP relay option shows wrong state.
* Fixed some i18n issues.
* Fixed crashs on macOS 10.11.
* Save proxy declarations with legacy style (custom) if the proxy is written in legacy style in the text file.
* Other minor bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.0.1-711.zip>

#### Version 3.0.0

<https://dl.nssurge.com/mac/v3/Surge-3.0.0-702.zip>

### Surge Mac V2

#### Version 2.6.7

* Fixed a compatibility issue with 304 response.
* Fixed a Dashboard crash.

<https://dl.nssurge.com/mac/Surge-2.6.7-656.zip>

#### Version 2.6.6

* Fixed a compatibility issue with 304 response.
* Fixed an issue that Dashboard may not use the correct encoding to decode text body.

<https://dl.nssurge.com/mac/Surge-2.6.6-654.zip>

#### Version 2.6.5

* Bug fixes.

<https://nssurge.com/mac/Surge-2.6.5-652.zip>

#### Version 2.6.4

* Bug fixes.

<https://nssurge.com/mac/Surge-2.6.4-647.zip>

#### Version 2.6.3

* New Features: External Proxy Provider. See <https://medium.com/@Blankwonder/surge-mac-new-features-external-proxy-provider-375e0e9ea660> for more information.
* Surge will automatically track system proxy settings now. When Surge is no longer the default proxy, the status icon will turn grey and a notification will raise.
* Fixed a compatibility issue with Docker.

<https://nssurge.com/mac/Surge-2.6.3-637.zip>

#### Version 2.6.2

* Fixed an issue that the UDP mode with AEAD ciphers doesn't work.
* Bug fixes.

<https://nssurge.com/mac/Surge-2.6.2-618.zip>

#### Version 2.6.1

* Surge now allows expired DNS answers for performance reasons. See 'Optimistic DNS' section in <https://developer.apple.com/videos/play/wwdc2018/714/> for more information.
* Performance improvements.
* Fixed an issue that UDP traffics are not included in the real-time speed.
* Supports hardware acceleration for AES-GCM encryption.
* Supports NAT64 in a pure IPv6 network. (Previous versions already supported DNS64)

<https://nssurge.com/mac/Surge-2.6.1-612.zip>

#### Version 2.6.0

* Supports using Surge Mac as a gateway.
* A new setup guide view.
* A new config panel for traffic capture options.
* Fixed an issue which Dashboard may disconnect unexpectedly under huge pressure.
* The status bar icon will be red while traffic capture is enabled.
* Improved TUN interface performance.
* Enabling TCP Fast Open in macOS 10.14.

<https://nssurge.com/mac/Surge-2.6.0-596.zip>

#### Version 2.5.3

* Supports UDP relay for shadowsocks protocol. A brief introduction in Chinese: <https://trello.com/c/ugOMxD3u>.
* You may use Dashboard to view UDP conversations.
* Dashboard now can save multiple remote machine profiles.
* Improved the JSON viewer in Dashboard.
* Added an UI switch for the dns-failed option in FINAL rule.
* Bug fixes.

<https://nssurge.com/mac/Surge-2.5.3-563.zip>

#### Version 2.5.2

* You may toggle the hidden state of columns in Dashboard now.
* Supports to export selected rows to csv file.
* Added a connection duration column in Dashboard.
* Supports obfs-uri parameter.
* Improved the benchmark view.
* Fixed a serious bug in the SOCKS5 proxy implementation.
* Bug fixes.

<https://nssurge.com/mac/Surge-2.5.2-544.zip>

#### Version 2.5.1

* The MitM enabling switch has been moved to the main menu and isolated from profile.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.5.1-528.zip>

#### Version 2.5.0

* Added Outbound Mode options: Direct Outbound, Global Proxy and By Rule.
* Added options for all policy to specify outgoing interface: 'interface' and 'allow-other-interface'.
* Added all\_proxy environment variable for 'Copy Shell Export Command'
* Supports client-side SSL/TLS certificate validation for HTTPS and SOCKS5-TLS proxy. A config example is here: <https://gist.github.com/Blankwonder/cd9fa1987e41cf1a1f1df50583ba1d9c> (DO NOT support editing with UI in this version.)
* Refined MitM.
* Concurrently setup connection to host with Round-robin DNS to boost performance.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.5.0-520.zip>

#### Version 2.4.6

* Supports xchacha20-ietf-poly1305.
* Bug fixes.
* HTTP request header and response header can be extracted from TCP connection now. (SOCKS5 and TUN)
* Enhanced mode can handle all connections now, even for connections initialized with IP address directly.
* Surge TUN now supports forwarding ICMP packets.

**From this version, the minimum system version requirement was raised to macOS 10.11. If you are still using macOS 10.10, please use version 2.4.5.**

<http://dl.nssurge.com/mac/Surge-2.4.6-490.zip>

#### Version 2.4.5

* Bug fixes.
* Improved performance for high concurrency.
* TCP fast open has been disabled temporarily since there is a serious problem in macOS/iOS kernel.
* Dashboard will display decoded URL query now.

<http://dl.nssurge.com/mac/Surge-2.4.5-468.zip>

#### Version 2.4.4

* Supports obfs=tls for shadowsocks protocol.
* Refined the proxy edit panel.
* Added Simplified Chinese language.

<http://dl.nssurge.com/mac/Surge-2.4.4-459.zip>

#### Version 2.4.3

* Supports obfs=tls for shadowsocks protocol.
* Refined the proxy edit panel.
* Added Simplified Chinese language.

<http://dl.nssurge.com/mac/Surge-2.4.3-457.zip>

#### Version 2.4.2

* Fixed an issue that enhanced mode may not be closed properly when switching to a profile without dns-server.
* Fixed an issue that managed profile updating and license info are unavailable while enhanced mode enabled.
* When the necessary port is used by another process, the error alert will show which process is using the port.
* Fixed an issue that map local items can't be edited with UI.
* Fixed an issue that system proxy settings may not be reset properly.
* Auto URL test group will execute a retest immediately after the selected policy has failed.

<http://dl.nssurge.com/mac/Surge-2.4.2-445.zip>

#### Version 2.4.1

* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.4.1-439.zip>

#### Version 2.4.0

* Supports enterprise license and profile management.
* Fixed a bug that some fields are unavailable in the configuration panel in some cases.
* Fixed a bug that the FINAL rule can't be edited.
* Fixed a bug that you may not be able to use custom storage path for profiles.
* The interface related options are no longer controlled by profile. Sorry for the repetitive changes.
* You may use $1, $2 to use the matched string in the value while using header rewrite.
* Added an option for HTTP/HTTPS proxy: always-use-connect. When it is true, Surge will use CONNECT method for plain HTTP requests.

<http://dl.nssurge.com/mac/Surge-2.4.0-429.zip>

#### Version 2.3.2

* Added a option to control whether show proxy error notification.
* Fixed a problem that Dashboard show data doesn't exist error.

<http://dl.nssurge.com/mac/Surge-2.3.2-421.zip>

#### Version 2.3.1

* Added a wizard to install CA’s root certificate for iOS simulator.
* Connectivity quality is now an option. (Not show by default)
* Line comments in \[Rule] section in profile file is now presented in UI.
* You may add proxy rule with Dashboard by right-clicking the request or process.
* Dashboard will always open a new window for local machine, instead of asking. You may use "File" menu to connect to a remote machine.
* Added a patch mechanism for adjusting settings for managed config. See manual for more information: <https://manual.nssurge.com/others/managed-configuration.html>

<http://dl.nssurge.com/mac/Surge-2.3.1-420.zip>

#### Version 2.3.0

* Completely redesign the configure interface. You may configure every function with UI now.
* Proxy benchmark is now moved to main application from Dashboard.
* New feature: Header rewrite. See manual for more information: <https://manual.nssurge.com/header-rewrite.html>.
* You may switch profile with command line now: surge-cli switch-profile profilename.

<http://dl.nssurge.com/mac/Surge-2.3.0-416.zip>

#### Version 2.2.4

* Notifications presented by Surge will be removed from Notification Center automatically.
* The interval of attempts to refresh managed config changes to one hour from one minute. (After config expired)
* Supports new encryption methods for shadowsocks-libev 3.0.
* Optimized Dashboard performance.
* Supports TCP Fast Open for shadowsocks proxy. You need add "tfo=true" flag in \[Proxy] section to enable the feature. You may use benchmark to confirm TFO is working.
* You can sort benchmark results now.
* You may choose to reload config after managed config updated.

<http://dl.nssurge.com/mac/Surge-2.2.4-394.zip>

#### Version 2.2.2

* Fixed a bug when using SOCKS5 without authorization.

<http://dl.nssurge.com/mac/Surge-2.2.2-375.zip>

#### Version 2.2.1

* You may use Dashboard to benchmark proxies now.
* Fixed "Too many open files" error by raising limit to 2048.
* Fixed a bug in SOCKS5 with authorization.
* Fixed a bug that managed config may refresh continuously.

<http://dl.nssurge.com/mac/Surge-2.2.1-374.zip>

#### Version 2.2.0

* Map local function is now available.
* Adds notifications when proxy encounters errors.
* Network changed notification will show service name instead of BSD name now.
* Fixed a bug that Dashboard may show the incorrect state of body dump.
* Changes for HTTPS and SOCK5-TLS proxy:
  * Option 'skip-common-name-verify' is deprecated.
  * Add a new option 'skip-cert-verify' to skip certificate verify completely.
  * Add a new option 'sni' to customize SNI field while handshaking. You may use 'sni=off' to disable SNI.
* New rule type: PROCESS-NAME, USER-AGENT and URL-REGEX.
* You can use simple wildcard matching (? and \*) for PROCESS-NAME rule, local DNS mapping and MitM hosts.
* Dashboard supports display POST form data in a table view.
* You may let Surge reload config by sending SIGHUP. You can use command 'killall -HUP Surge' or 'surge-cli reload'.
* Managed configuration is supported now.
* Add a new option 'skip-server-cert-verify' for MitM.

<http://dl.nssurge.com/mac/Surge-2.2.0-368.zip>

#### Version 2.1.4

* Fixed a bug that helper may crash on macOS 10.10.
* Add a option to remove Surge helper for troubleshooting.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.1.4-362.zip>

#### Version 2.1.3

* Fixed a bug that helper may crash on macOS 10.10.
* Add a option to remove Surge helper for troubleshooting.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.1.3-337.zip>

#### Version 2.1.2

* New option: Collapse policy group items in menu
* Fixed a bug that enhanced mode DNS settings may not be reverted.
* Hold option key to click 'Copy Shell Export Command' to get a command with primary interface IP instead of 127.0.0.1.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.1.2-327.zip>

#### Version 2.1.0

* New feature: Enhanced Mode

  Some applications may not obey the system proxy settings. Using enhanced mode can make all applications handled by Surge.
* New rule type: IP-CIDR6

  Example: IP-CIDR6,2005::/16,DIRECT,no-resolve
* The /etc/hosts file will be reloaded automatically if it has changes.

<http://dl.nssurge.com/mac/Surge-2.1.0-318.zip>

#### Version 2.0.13

* Dashboard supports to use ⌘ + 1,2,3,4 to switch panel.
* Dashboard Supports handoff with Surge iOS.
* Fixed a bug that Dashboard may show incorrect process name.

<http://dl.nssurge.com/mac/Surge-2.0.13-304.zip>

#### Version 2.0.12

* Bug fixes.
* Supported SNI while performing MitM.
* The original certificate will be resigned and used while performing MitM, instead of generating a new certificate.

<http://dl.nssurge.com/mac/Surge-2.0.12-295.zip>

#### Version 2.0.11

* Rule test cache will be flushed after network switching now.
* Added a option 'Grey icon if set as system proxy is disabled'.
* Bug fixes and performance improvements.

<http://dl.nssurge.com/mac/Surge-2.0.11-289.zip>

#### Version 2.0.10

* Surge talks to HTTP proxies with a plain HTTP method for non-HTTPS requests now, instead of CONNECT.
* Improved compatibility with some HTTP server.
* Improved compatibility with some DNS server.

<http://dl.nssurge.com/mac/Surge-2.0.10-280.zip>

#### Version 2.0.9

* Dashborad: The height of the detail panel will not change now while switching pages.
* A notification will show when proxy client access from other machine.
* Used SF Mono as monospaced font for header and body data display.
* Supported TCP half-open mechanism.

<http://dl.nssurge.com/mac/Surge-2.0.9-273.zip>

#### Version 2.0.8

* Add a new option 'exclude-simple-hostnames' in the gereral section.
* Dashborad: Selected row will not be lost while the filter or sort column changed.
* Dashborad: Fixes some issues in the active panel.

<http://dl.nssurge.com/mac/Surge-2.0.8-260.zip>

#### Version 2.0.5

* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.0.5-255.zip>

#### Version 2.0.3

* New feature: Show connectivity quality in menu.

  Surge will send a DNS question to all DNS servers concurrently to test physical network connectivity while opening the menu.
* Fixes a problem that Surge may freeze while opening the menu.
* Fixes a problem that if a policy group contains duplicate policies, Surge may crash.

<http://dl.nssurge.com/mac/Surge-2.0.3-250.zip>

#### Version 2.0.2

* Dashboard will no longer display process icon in remote mode.
* Fixes a bug: "Set as System Proxy" option does not work properly if only SOCKS service is enabled.
* Fixes a bug: Dashboard can't add a rule with no-resolve option on and comment not empty.
* Minor bug fixes.

#### Version 2.0.1

* Bug fixes
