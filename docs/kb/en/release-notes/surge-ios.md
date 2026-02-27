# Surge iOS Release Notes

### Version 5.14.6

* Added \[General] parameter `block-quic`, which is used to globally override the behavior of blocking QUIC traffic.
* Optimized the text and JSON viewer in the request inspector, now supporting large files and code highlighting.
* Rewrote HTTP script-related implementation; it now performs better and uses less memory when handling large bodies.
* Supports SNI extraction for gQUIC.
* Refactored traffic statistics functionality; now, even if you haven't entered the main program for a long time, you won't have to wait a long time when accessing the traffic statistics page.
* Added export feature to traffic statistics.
* Other detail optimizations and bug fixes.

### Version 5.14.5

* Support DNS over TLS.
* Bug fixes and performance improvements.

### Version 5.14.4

* When enabling the HTTP capture switch, all active connections will now be forcibly interrupted to ensure that no requests are missed due to existing long connections.
* Optimized compatibility with some QUIC clients, such as Lark.
* Fixed an issue where download data bytes in statistics was incorrect after modifying the request HTTP using scripts or other mechanisms.
* Adjusted the priority of processing logic when forwarding QUIC. Now, for a proxy policy that does not support UDP forwarding, it will prioritize considering QUIC Block before falling back to DIRECT or REJECT.
* Bug fixes and other improvements.

### Version 5.14.3

#### New Feature: Port Forwarding

* This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

#### #!REQUIREMENT upgrade

* Now provides three simple notations: #!IOS-ONLY, #!MACOS-ONLY, and #!TVOS-ONLY.
* Content disabled by this end-of-line comment can now be displayed and edited in the UI. It will appear as disabled when conditions are not met, and if enabled, restrictions will be automatically removed.

#### \[Host] Optimization

* \[Host] section supports configuration using DOMAIN-SET and RULE-SET to improve matching efficiency. Use case:

#### Other Improvements

* Added option icmp-forwarding, enabled by default.
* Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized.
* Bug fixes and other improvements.

### Version 5.14.2

* Bug fixes and other improvements.

### Version 5.14.1

* Bug fixes and other improvements.

### Version 5.14.0

#### New Features

* Added pre-matching rules for low-overhead request rejection. Please refer to the documentation for details. <https://manual.nssurge.com/policy/reject.html>
* Body Rewrite supports using JQ expressions to manipulate JSON.
* The shadowsocks protocol adds support for the `2022-blake3-aes-256-gcm` and `2022-blake3-aes-128-gcm` encryption modes
* Adapted icon mode for iOS 18.
* New Control Center control for HTTP capture.
* DNS now supports system search domain settings
* Added parameter proxy-restricted-to-lan to restrict the proxy to only accept devices from the same subnet
* When updating external resources, ETag will be recorded and sent; re-download will not be triggered if the resource has not changed

#### Improvements

* Overall optimization and improvement of UDP forwarding.
* The policy group list view supports configuring custom icons.
* Resolved issues with real-time display on iOS 18
* Optimized the display effect of policy group icons
* Improved HTTP engine compatibility with non-standard requests
* More explicit error prompts when Surge is activated without a network connection
* Enhanced error handling logic for encrypted DNS, retrying immediately upon encountering errors
* Added warning messages for excessive \[Host] entries
* The URL-REGEX rule now supports `extended-matching` tags.
* Allow the use of Ponte policy as an underlying proxy.

#### Bug Fixes

* Fixed an issue where Control Center/home screen widgets would still show as active even when Surge was turned off
* Fixed a memory leak issue in encrypted DNS under certain errors
* Corrected subscription cycle constraint errors for new icons
* Other bug fixes

### Version 5.13.0

* Control Center Widget: On iOS 18, you can now quickly toggle Surge in the Control Center.
* New Icon: Sapphire.
* Added Ponte diagnostic function for quickly locating Ponte-related issues, accessible from the Ponte device page.
* Port Hopping: Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.
* Added `[General]` parameter `show-error-page`, which is used to control whether Surge's HTTP error page is displayed when an error occurs. This parameter is enabled by default, and the behavior is consistent with previous versions.
* Bug fixes.

### Version 5.12.0

* New subscription feature: Custom policy group icons.
* Refactor the Surge tvOS profile deployment process using CloudKit, significantly improving stability. Please note that both Surge iOS and tvOS need to be upgraded to the latest version before you can use the profile deployment feature, and the tvOS version needs to be launched once for registration.
* When using the add rule function in the request list, you can choose to add it to an existing rule set. (Supports local rule files and inline rule sets).
* Optimized behavior when enabling IPv6 VIF under No Default Route mode.
* Other optimizations and bug fixes.

### Version 5.11.3

* Support turning off Surge via widgets/Shortcuts when the always-on switch is turned on
* Support turning on Surge via widgets/Shortcuts when the Surge VPN Profile is not selected (or when other VPNs are running)
* Fix an issue where DOMAIN-SUFFIX rules may become invalid if duplicate DOMAIN and DOMAIN-SUFFIX rules are included in the rule set
* Optimizations related to No Default Route mode, significantly improving usability
* Other issue fixes

### Version 5.11.2

* Now you can see the number of times a rule has been used in the rule list.
* Optimized the implementation method of blocking QUIC traffic to increase the likelihood of clients correctly falling back.
* The Smart group will use the SUBSTITUTE policy (DIRECT) instead of failing directly when there are no sub-policies.
* Fixed an issue where the `server-cert-fingerprint-sha256` parameter was not effective for TLS-like protocols with sni=off settings.
* Added a new rule type `HOSTNAME-TYPE`, used to determine the type of request hostname. Optional values are: `IPv4`, `IPv6`, `DOMAIN`, `SIMPLE`. (`SIMPLE` refers to hostnames without a dot, such as `localhost`)
* Optimized DNS request logs. Now more information is displayed. Additionally, if DIRECT policy connects directly without triggering DNS in the rule system, related DNS logs can still be shown.
* When deleting a policy that is being used by a policy group, it is now allowed to delete it directly and automatically remove it from all policy groups.
* Bug fixes and other Improvements.

### Version 5.11.1

* Optimize the matching performance of small rule sets, especially evident on older model CPUs.
* The external resource update page can display error information generated by rule set processing.
* Automatically ignore invalid empty lines in the rule set.
* Corrected the issue where applying temporary rules and then experiencing a policy change does not disrupt existing connections.
* Corrected crashes that may occur when external policy groups change.
* Fixed an issue where configuration upgrade functionality did not correctly take effect for managed configurations and enterprise configurations.
* During Smart group initialization phase, no longer displays most frequently used tags to avoid misunderstanding.
* Fixed an issue where local script files could not be automatically reloaded after being edited.
* Optimized indexing process for large rule sets.
* Limited maximum number of files for iCloud background auto auto-sync to 200 to avoid memory usage issues.
* Fixed potential UI display issues when adjusting policies through remote controller.

### Version 5.11.0

### Smart Group

This is a new type of policy group, driven by our carefully designed algorithm engine, which can automatically select the appropriate policy from the sub-policies of this policy group. The goal of the Smart policy group is to replace the original automatic testing groups (url/load-balance/fallback), greatly optimizing the experience while minimizing the need for manual intervention in policy groups. Users only need to put the available policies into this group.

For details, see: <https://kb.nssurge.com/surge-knowledge-base/guidelines/smart-group>

### Rule System

* Overall performance optimization of the rule system.
* Significant optimization of the indexing algorithm in large domain rule sets, improving the search efficiency by more than ten times for rule sets with more than 100,000 rules.
* Corrected the issue where sub-rules of logical rules within a rule set could not be covered by the `no-resolve` and `extended-matching` parameters of the rule set.
* Added a new rule type `DOMAIN-WILDCARD`, supporting `?` and `*` domain name matching.
* `DOMAIN-SET` and `RULE-SET` are changed to strict validation. If there are invalid lines in the file, the entire rule set will be invalidated to avoid problems caused by misuse.

### IPv6

* The behavior of the `ipv6-vif` parameter has been modified. When set to always, IPv6 functionality will be enabled even if `ipv6=true` is not set.
* Added a warning for the `ipv6-vif=always` parameter.
* Adjusted the automatic retry mechanism. Accessing IPv6 addresses in a non-IPv6 network will no longer enter the retry process, and the request will fail immediately (solving the problem of some applications stalling when IPv6 VIF is enabled in a non-IPv6 environment, but the application will still continue to send IPv6 requests).

### Other Optimizations

* Enhanced `$notification.post`, adding support for media resources, sound hints, and automatic dismissal.
* Optimized WireGuard failure handling.
* Reduced the power consumption of the TUIC protocol during sleep.
* Improved the precision of time statistics in the request log system, now accurate to µs level.
* Optimized various abnormal retry mechanisms, avoiding high resource usage caused by continuous retry in the face of some specific problems. For operations that need to be retried continuously (such as WireGuard reconnection, Ponte server reporting to iCloud), Surge will now retry after 0.1s, 0.5s, 1s, 5s, 10s, 30s after an error.
* Optimized the caching system for external resources.
* Added the profile line modifier `#!REQUIREMENT`.
* When the current network is found to be managed by Surge Mac Gateway, Surge iOS will now automatically pause. (This can be adjusted via the auto-suspend option, enabled by default.)
* Optimized TUN takeover and specific app performance compatibility issues.
* Optimized memory usage, infrequently used and large scripts will not be cached in memory anymore.
* The network diagnostics page adds SSID/BSSID with copy functionality.
* Now, when uploading logs in the log interface, the engine currently running will automatically generate the most recent verbose logs (the new version has cached 256KB of logs in memory), so when reporting problems, you can upload directly without needing to reproduce in verbose mode.
* For external resources related to policy groups and script types, the maximum size is now limited to 2MB, to avoid memory overflow in case of configuration errors.

### Detail Adjustments

* Raised the memory warning threshold to 45MB, previously 40MB.
* Limited the length of logs that can be written to request notes in debug mode by scripts.
* Changed the default UDP test target to 1.0.0.1.
* If incorrect types of fields are passed when using API in scripts, it will result in script errors.
* After the script is completed or times out, unfinished $httpClient will no longer call the callback function.

### Issue Fixes

* Fixed the issue where changes in iCloud content might not be detected by the main program when both Surge iOS main program and engine are enabled.
* Fixed the problem where Header Rewrite rules could not match URLs based on the Host field.
* Corrected the issue where ip-version and tos parameters could not take effect when testing proxies.
* Fixed the crash issue caused by mistakenly passing null when executing scripts via HTTP-API.

### Version 5.10.0

#### New Features

* New subscription feature: Body Rewrite. Surge now can rewrite the body of HTTP request or response, replacing the original content with regular expressions. If you need to make more flexible modifications, try scripting.

#### Improvements

* Comprehensive enhancement of the Mock (Map Local) function, adding data types such as text, tiny-gif, base64 to facilitate inline data return. Also added the ability to customize status codes.
* Optimized the request list filter, now displaying the filter at the top and allowing quick toggling of filter activation. Long-pressing a filter item displays a menu for deletion or reversing the item to a negative filter.
* Added recognition for STUN packets, which can be matched with PROTOCOL,STUN.
* Optimized the external resource management page.
* Optimized the script editor page.
* Optimized the module management page.
* Added a long-press shortcut menu to the Utilities tab.
* Added a new URL scheme for the iOS version: surge:///install-module?url=…

#### Optimizations

* When configuring Shortcuts to execute Surge scripts, the script list of the current configuration can now be directly accessed.
* Enhanced compatibility when decompressing HTTP Body.
* Optimized the script engine, limiting the number of concurrent JSC engine processes to 2 to avoid memory issues.
* The GeoIP database can now be updated by the main application without needing a restart to take effect.
* Optimized the request log, now displaying the specific rules matched for URL Rewrite and Header Rewrite.
* Adjusted the logic of the DNS engine handling empty results, now not waiting for all servers to respond with empty results when multiple DNS servers are configured, to avoid additional waiting when AAAA records do not exist..
* The module page allows undoing modifications to avoid misoperations that change the order of effectiveness.

#### Fixes

* Fixed the issue where warnings generated by module configurations were not displayed.
* Fixed a crash in Surge caused by passing some incorrect types of parameters in scripts.
* Fixed compatibility issues with non-https WebSockets in proxy mode with the new version of Safari.
* Fixed the issue where deleting an entry in the rule search page would delete all duplicate entries.
* Fixed some missing highlights in the editor.
* Other bug fixes.

### Version 5.9.0

#### Module

* Added several new official modules; official modules can now be dynamically updated.
* Modules have a new classification field for convenient access and categorization in the UI.
* Modules now accept parameter tables, supporting multiple parameters. Parameters will be used to modify module content through text replacement.

#### Script

* New script execution engine. Optimized execution performance and memory usage.
* $httpClient has added several practical parameters. For more details on the updates above, see the documentation.

#### Enhancements

* Added desktop shortcut jumps for remote controllers; see the configuration guide at the bottom of the device page for details.
* New parameter: always-raw-tcp-keywords. For usage, refer to documentation.
* Added SRC-PORT rule to match client port numbers.
* IN-PORT/SRC-PORT/DEST-POT three rules are categorized as port number rule class, supporting more usages.
* The UI can now maintain pure empty lines from original configurations after editing.

#### Fixes

* Corrected a detail issue with QUIC flow control and optimized latency performance for Ponte/TUIC/Hysteria2 protocols.
* After editing a single rule, the notification-related parameters will be retained..
* Corrected an issue where switching outbound modes via widget was not possible in newer iOS versions.
* Fixed potential sudden memory overruns that could occur when when processing huge external resources leading to stops.

### Version 5.8.1

#### Rule Engine Optimizations

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

#### Minor Optimizations

* Now, when performing MITM, the certificate used for signing will be sent to the client together, to support using intermediate certificates for MITM.
* All comments (at the beginning and end of lines) can now use `#`, `//`, `;` three common comment symbols.
* Profile error message prompt optimization, now it can give the exact line number where the error occurred more accurately.
* Fixed an issue that BSSID related matching rules might fail.
* Optimize Surge Ponte error handling process, correct the issue where device information is not automatically updated under certain errors.
* Bug fixes.

### Version 5.8.0

#### New Features

* New Inky icon
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

#### Optimizations

* Reworked HTTP capture functionality
  * The related settings are no longer stored in the configuration, the `[Replica]` section has been deprecated.
  * Added an automatic shut-off setting after turning on the capture switch, which can automatically stop capturing based on time, size, or the number of requests.
  * Added automatic activation of MITM after turning on the capture switch, which can be additionally turned on for specific hostnames. (Even if the main MITM switch is off).
  * Added an option to only save HTTP/HTTPS requests after turning on the capture switch.
* VIF performance optimization, tested to achieve full speed of a 2.5Gbps wired network card on iPhone 15 Pro with VIF taking over a single thread. (Proxy mode performs even better)
* Wi-Fi Assist and Hybrid features will only take effect after the device is unlocked, to avoid unnecessary power and data consumption.
* From this version on, the size of external resources is limited to no more than 10MB to prevent excessive memory usage caused by abnormal external resources. (Except for `domain-set`)
* The parameters `udp-policy-not-supported-behaviour`, `include-apns`, `include-cellular-services` have been added to the UI settings.
* Improved compatibility with some non-standard protocols.
* When testing the Ponte policy, the test URL has been changed from `proxy-test-url` to `internet-test-url`.
* Following the WireGuard protocol standard recommendation, WireGuard handshake packets will now be tagged with 0x88 (AF41) DSCP to increase the success rate.
* When forwarding UDP packets via WireGuard, it supports retaining the TOS(DSCP/ECN) tag of packets inside the tunnel.
* Based on the WireGuard protocol standard recommendation, Surge will copy the ECN tag from packets inside the tunnel to packets outside. When receiving packets with an ECN tag, they will be strictly merged according to RFC6040. (`ecn=true` must be set for the policy).
* UDP NAT can close the UDP session early based on ICMP messages.
* Improved PMTU support for QUIC.

#### Bug Fixes

* Fixed the issue where the external resources of rule sets needed to be reloaded to take effect after updates.
* After a network switch, it will forcefully break the original long connection of DoH/DoQ/DoH3 to avoid obtaining results that are not suitable for the current network environment.
* Fixed the issue where invalid certificates might cause the key store interface to crash.
* Fixed the issue where the Ponte device option in the policy group page might not display text.
* When performing MITM on HTTPS requests that directly connect using an IP address, the IP address should not be sent as SNI, as this might cause compatibility issues.
* Other bug fixes.

### Version 5.7.0

#### New Features

* Surge tvOS is now available. All users who have purchased Surge iOS can use it directly without any additional purchase.
* Supports interactive widgets for iOS 17.
* Added full-text search support for HTTP request's header and body.
* Web Dashboard updated to version 2.0.
* Inline Ruleset, allowing the Ruleset to be written directly in the main profile.

#### Minor Improvments

* Optimized the script logging system, ensuring that script logs in request logs do not display content from other sessions during concurrent execution.
* Separated the open and close shortcut actions for iOS 17. For users of the iOS 17 version, please use actions with the (iOS 17) suffix.
* Removed the Wi-Fi Assist notification.
* When using UI to edit policy groups, you can now select Ponte devices.
* When creating temporary rules for remote devices, Ponte devices can be selected.
* Remote controllers support viewing and updating external resources of remote devices, compatible with Surge Mac and Surge tvOS.
* Icons for Ponte devices now display the device type.
* Improved details related to accessibility.
* Improved some UI details.

#### Bug Fixes

* Fixed some potential issues when editing the MITM Hostname list.
* Fixed an issue where, when creating rules for remote devices, the policy options might be local policies instead of remote policies.
* Fixed an issue where, when using iCloud sync, the local module selection might be deselected if the cache was cleared.
* Fixed an issue where switching to Dropbox sync was not possible.
* Fixed a problem where some card backgrounds were incomplete when expanded.
* Fixed an issue where modules added via Basic Auth URL could not auto-update.
* Fixed a problem in quick switch mode where, after switching from an IPv6 network to a non-IPv6 network, the v6-vif didn't correctly auto-turn off when set to auto.

### Version 5.6.0

#### Enhancements

* Comprehensive optimization of the request list page
* Ponte device sharing can now be initiated and managed directly on iOS
* The name of the source device will be displayed when viewing external requests
* Detached profile supports using as a keyword to refer to content in enterprise profile
* Profile list added Create Linked Profile option for quick creation of detached profile
* Changed the logic of accessing the data protection area, now Surge can be properly activated in the locked screen state. (Except after rebooting)
* Will prompt when a CA certificate expiration is detected
* Single request exported .zip files support import back into Surge iOS, and will be displayed in the favorite requests
* Performance optimization

#### Problem Fixes

* Fixed the issue that in the same round of policy testing, if different test URLs are mixed, the HTTP Header constructed in the secondary test may be incorrect, leading to abnormal test results
* Fixed the issue that the Panel refresh may not be executed correctly after the main program is opened from the background
* Fixed the issue that the policy group title options under the list policy group view may not update in time
* Fixed the issue that using the DIRECT strategy as underlying proxy might cause UDP failure
* Fixed the issue that when using the SSH protocol, if the server side is configured with a banner, it cannot handshake properly
* Fixed some issues that may occur under the Lucid theme on iPad
* Fixed the issue that SSID related functions may not work correctly in some cases
* Fixed some problems that may occur when using TUIC v5 as underlying-proxy
* Fixed the issue that when directly using IPv6 address as vmess hostname, if WebSocket is enabled, the WebSocket request cannot be correctly constructed
* Fixed the issue that the use of certain invalid data in the DOMAIN-SET rule may cause a crash
* Fixed the crash that may be caused by profile errors
* Fixed the issue that the returned data of the replayed request cannot be viewed if there is compression
* Fixed the issue that the device list cannot be loaded when there is only a shared Ponte device
* Fixed some crashes that may occur with DNS over HTTP3
* Fixed the issue that when Surge Ponte is in a subnet CIDR not a multiple of 8, it will judge incorrectly leading to non-use of LAN direct connection
* Fixed some problems that may occur when using Surge Ponte
* Optimized the logic of re-establishing the main connection after network switching in TUIC/Ponte

### Version 5.5.1

#### Remote Controller

* Supports adding and modifying temporary rules remotely.
* The device management now groups devices by active and non-active devices. (whether there is a request)
* Supports directly adding temporary or permanent rules for devices.
* Other detail optimizations.

#### Others

* Added support for TUIC v5 protocol.
* The policy group menu adds the option to display hidden groups.
* In traffic statistics, the subdomains of apple.com will be processed separately, facilitating the observation of the traffic consumption of system services.
* After external resources are updated, now only the update of the policy group will cause the group page to reload, other types will no longer cause the group page to reload.
* Optimized the performance of Surge Ponte/TUIC.
* Optimized the request Note recording when the strategy group is abnormal.
* Fixed the problem that connection reuse was not done correctly under MITM H2 mode.
* Fixed the problem that the request of $httpClient/DoH may sometimes be accidentally cancelled.
* Other bug fixes.

### Version 5.5.0

#### Interface

* New UI theme Lucid, derived from the design language of Surge Mac 5. (Feature Subscription required)
* Remote control device management supports remote modification of device icons. (Surge Mac needs to be updated to version 5.1.0)

#### Surge Ponte

* Surge Ponte supports cross-iCloud account sharing. (Surge Mac needs to be updated to version 5.1.0)
* Fixed issues that might occur when accessing HTTP/1.0 servers via Surge Ponte or TUIC protocol. (e.g. ASUS router management page)

#### Proxy Protocol Related

* Supports ShadowTLS v3. (Feature Subscription required)
* New feature: Adaptive TLS Fingerprint, see the manual for details.
* Fixed an issue that the reuse feature could not work properly under Snell V4.
* SSH protocol now supports server public key fingerprint pinning, see the manual for usage.
* Added UDP forwarding support for VMess protocol.

#### Scripts

* $httpClient supports binary mode.
  * The body of the request supports TypedArray.
  * Passing in binary-mode: true in the request parameters allows the return result to be returned as TypedArray.
* Fixed the problem that `http-request` type scripts could not use binary data directly as response.

#### Others

* Policy group adds parameter `external-policy-modifier`, which can be used to adjust external policies.
* Optimized the request log system
  * Added category marks to the logs.
  * Rule system adds more output for DNS and rulesets.
* Swipe right on temporary rules to write the rules into permanent rules.
* Other bug fixes and optimizations.

### Version 5.4.0

#### Surge Ponte

Surge Ponte is a private network between your devices running Surge Mac & iOS.

* Zero configuration required
* Surge automatically chooses the most appropriate channel to establish connections.
* Always end-to-end encryption.
* The device information and encryption keys are synchronized via your iCloud, and none of your data passes through third-party servers, except the proxy server if you choose.

Surge Ponte needs to be used with Surge Mac 5.

#### WireGuard-related optimizations

* Significantly optimized handshake-related logic.
* WireGuard's Client ID supports UI configuration and adds support for 0xabcdef and 6-character base64 formats.

#### Other updates

* Redesigned the network diagnostics page and optimized the information display.
* Optimized peak bandwidth performance and CPU usage for QUIC.
* Requests matched by the REJECT rule will be marked as Rejected and distinguished by gray, no longer classified as Failed.
* Optimized the switch control logic for various functions to avoid accidentally turning off/on a function in some cases.
* When using MITM, prioritize using the client-reported SNI to generate certificates and use the accessed domain name when SNI is not reported.
* Increased the wake-up speed of executing Surge scripts via shortcuts when Surge is not enabled.
* Changed the display of SOCKS5 proxy request type to TCP. You may confirm in Notes that it was taken over by SOCKS5 proxy.
* Support for configuring DNS over QUIC/H3 for specific domain names in \[Host].
* Introduced the FAILED built-in policy for marking request failures in special cases (e.g., policy group cannot be loaded) instead of using REJECT.
* Fixed an issue where rules would not match if the client accidentally sent a domain name with uppercase letters during rule matching.
* Fixed a problem where policy group decisions would fail if multiple external policy groups used the same name for policies with different actual content.
* DNS Local Mapping allows configuring multiple IPs for a domain name to be used concurrently.
* Other issues fixed.

Please note that starting with iOS 16.4, the system no longer allows reading the MCC/MNC of cellular networks. Related functions may become invalid.

### Version 5.3.1 (Feb 16, 2023)

* The installed modules are now synced between iOS devices via iCloud.
* Support for customizing the reserved bits of WireGuard, also known as the client ID or routing ID.
* Improved WireGuard handshake logic.
* Fixed some UDP forwarding problems.
* Fixed some text editor issues.

### Version 5.3.0 (Feb 3, 2023)

#### New Subscription Feature: Temporary Rules

We have added the temporary rules feature in Surge Mac to the iOS version. Temporary rules will automatically disappear after Surge is stopped and will not be written to the profile for some temporary usage scenarios.

#### New subscription feature: Whois lookup

Quickly perform a Whois lookup to identify the domain or IP owner in the request details menu.

#### New feature: Proxy Detail View

#### Traffic statistics have been enhanced

* In addition to traffic statistics, the number of requests will now be recorded as well.
* In addition to this month's data, last month's data will also be kept.

#### Bug fixes and minor improvements

* JSON and text viewers support search on iOS 16
* Network switching no longer interrupts in-progress $httpClient requests.
* Fixed an issue where scripted requests would sometimes accidentally carry the x-surge header handled internally by Surge
* Fixed an issue that some requests constructed in a special way could not be matched by MITM hostnames.
* Fixed an issue that the LAN proxy and Dashboard may not be accessible if the fast-switch is configured.
* Fixed an issue that could occur when using the expanded card layout on iPad
* Fixed an issue that the Panel button is not showing on iOS 14.

### Version 5.2.2 (Dec 3, 2022)

#### New Feature

* Gaming Optimization. Enabling it will prioritize UDP packets when the system load is very high, and packet processing is delayed.
* SOCKS5 proxy now supports UDP forwarding, as the server side does not consistently support UDP forwarding, the parameter udp-relay=true needs to be explicitly configured.

#### Minor Improvements

* URL regular expressions for Script, Rewrite, Mock, etc. will try to match URLs constructed in many different ways (e.g. Host field in Header) to solve the problem that some apps use custom DNS logic to request directly to IP addresses.
* Removed the silencing mechanism after UDP forwarding errors to avoid extra waiting time after switching networks.
* Added a workaround for suspend and subnet settings that may occur when the SSID is temporarily not available under iOS 16.
* The log view supports freezing now.
* The IPv6 switch no longer prevents direct access to IPv6 addresses when turned off. The switch is now limited to controlling whether the DNS Client requests AAAA records.
* Automatic disabling of AAAA queries due to DNS issues will be prompted in the Event Center instead of just in the logs.
* Fixed handling issue of generating IPv6 fragmentation when forwarding IPv6 UDP packets via WireGuard.
* The external policy group will skip the line and continue processing when it encounters invalid content instead of returning an error directly.
* Adjusted the buffering mechanism of raw TCP forwarding to avoid conflicts with some apps.
* Fixed REJECT requests not being marked as failed under MITM H2.
* Adjusted the output text under diagnostics.
* Other bug fixes.

### Version 5.2.0 (Nov 11, 2022)

#### Support New Proxy Protocol

* Snell V4
* TUIC
* Shadow TLS

See the online manual for more information.

#### Other Improvements

* A new expanded card style for the Policy Group view.
* Refined the Route Table view.
* shadowsocks now supports the none cipher.
* Modified the handshake packet construction logic when forwarding HTTPS requests to proxies, which can slightly optimize latency.
* Surge HTTP requests for proxy testing no longer contain a User-Agent header.

#### Bug fixes

* Fixed an issue that when using Subnet Suspend, the switch in the interface did not display the status correctly.
* Fixed an issue that the module could not configure the MITM h2 parameter.
* Fixed some keyboard-related layout problems.
* Fixed an issue that may not work properly when nesting proxy chains with a specific protocol combination.
* Fixed an issue where UI jumping may occur when starting Surge if iCloud Drive is used.
* Fixed a memory leak that could occur when HTTP capturing is enabled.

### Version 5.1.3 (Sep 29, 2022)

* Added a delayed update mode to the view of the recent request, which will automatically start when too many requests are received, to avoid the Surge main application from getting jammed.
* Optimized the check logic of ICMP traffic limit to avoid the alarm triggered by high concurrency in a very short period.
* Added a lock screen widget that can be used to quickly open Surge.
* Added a view to examine the modified profile after modules are applied.
* Added a new Siri action: enable or disable modules, which can be used with Shortcut.

### Version 5.1.0 (Sep 11, 2022)

#### IPv6 Improvements

* Support UDP forwarding with IPv6 VIF, including local and proxy forwarding.
* Support ICMPv6 local forwarding with IPv6 VIF.
* Fixed an issue that IPv6 address could not be used when using Surge Private DDNS.
* IPv6 handling details refined.

#### WireGuard IPv6 Tunneling

* WireGuard policy now supports IPv6 Tunneling (the previous version already supports connecting to an endpoint with IPv6, this version adds IPv6 support inside the tunnel)
* Read the manual for more information.

#### Text Editor

* A toolbar was added to the text editor.
* Fixed a crash in text editing.
* You can search text in the text editor now.

#### Other updates

* Optimize the proxy failure handling policy. Now when the TCP handshake time to the proxy server is greater than the test-timeout parameter, it is directly determined as failure in order to trigger the policy group to retest faster.
* TabBar shortcut menu added module shortcut opening and closing.
* External resources view allows side-swipe to edit local resources file.
* All types of scripts that use $httpClient to initiate requests are now viewable in the view of the recent request.
* Adjusted script concurrency limit policy to avoid deadlock when multiple scripts refer to each other.
* Other minor bug fixes and improvements.

### Version 5.0.2 (Aug 19, 2022)

* Fixed a bug that the text editor may be unable to save content.

### Version 5.0.1 (Aug 17, 2022)

* You may now flush the DNS cache in the DNS result view.
* Improved the script editor and log viewer.
* Other bug fixes and minor improvements.

### Version 5.0.0 (Aug 10, 2022)

Surge 5.0 comes with a brand new UI design, including a brand new policy group selection view, a new Start tab, and a new icon.

And now, you can try all the features for free for seven days before you purchase.

#### New Features:

* DNS over QUIC and DNS over HTTP3 support
* Real-Time View: Show live speed or request list floating window when using other applications.
* Subnet Setting: Override global settings under specified networks.

#### Minor updates:

* Comprehensive UI improvements.
* New contextual menu in the tab bar items.
* Fixed a bug that encrypted-dns-skip-cert-verification may not work
* MITM hostname and force-http-engine-hosts now support keywords: `<ip-address>`, `<ipv4-address>`, and `<ipv6-address>`.
* Script added function `$utils.ipasn(ipAddress:<String>)` to lookup ASN.
* Script added function `$utils.ipaso(ipAddress:<String>)` to lookup ASO
* Script added function `$utils.ungzip(ipAddres:<Uint8Array>)` for gzip decompression.
* Bug fixes.

### Version 4.15.0 (Jun 30, 2022)

#### MITM over HTTP/2

* Surge now supports performing MITM with HTTP/2 protocol to improve concurrent performance.
* Surge now supports performing MITM on WebSocket connections.

#### Others

* You may use `doh-skip-cert-verification=true` to disable server certificate verification for DNS-over-HTTPS.
* Bug fixes.

### Version 4.14.0 (Jun 1, 2022)

#### SSH Proxy Support

* You can use SSH protocol as a proxy protocol. The feature is equivalent to the `ssh -D` command.
* Both password and public key authentications are supported.
* All the four types of private keys, RSA/ECDSA/ED25519/DSA, are supported.
* Surge only supports `curve25519-sha256` as the kex algorithm and `aes128-gcm` as the encryption algorithm. The SSH server must use OpenSSH v7.3 or above. (It should not be a problem since OpenSSH 7.3 was released in 2016.)

#### Keystore

* You may now save sensitive keystore items to the system keychain.
* You may now configure TLS client certificate authentication with the UI.
* You may use a keystore item as the CA certificate for MITM.

#### Others

* New rule type: `IP-ASN`. You may use the rule to match the autonomous system number of the remote address.
* The request details now include the ASN and ASO information of remote IP addresses.
* You can now enable/disable the rewrite rules and DNS local mapping items.
* The preview of SVG images is removed. You can use the new Web View to see the SVG image.
* Bug fixes.

### Version 4.13.0 (Apr 24, 2022)

#### HTTP Capture

* You can now export HTTP/HTTPS requests to a HAR file, which is a standard format and can be opened by many web analysis tools
* The image viewer now supports SVG format.

#### Proxy

* New parameter `server-cert-fingerprint-sha256` for TLS proxy policies. Use a pinned server certificate instead of the standard X.509 validation.
* `tls-engine` option is now deprecated. OpenSSL is now the only TLS engine.
* You can now use a full profile as the external policy group (policy-path). All proxies in the \[Proxy] section will be used.

#### MITM

* You can export the CA certificate to a P12 or PEM file.
* Fixed an issue that the CA certificate can’t be installed if the default browser isn’t Safari.

#### Header Rewrite

* Header rewrite now supports using the regex to replace the value.
* Header rewrite now supports modifying the response headers. Scripting
* The default timeout of $httpClient is now 5 seconds and you may override it with the timeout parameter.
* You can manage the data of $persistentStore with the UI now.
* You may edit the argument with UI now.

#### Remote Controller

* You may sort and search in the remote device list.

### Version 4.12.0 (Mar 18, 2022)

#### New Feature: Personal Hotspot Proxy Access

* When using an iPhone/iPad as a hotspot, an HTTP or SOCKS5 proxy can be used on the client device to take over the traffic using Surge iOS.
* The proxy IP to be configured on the client is shown in the More Settings and the port number is the same as the WiFi proxy service.

#### New Feature: Hybrid Network

* Instead of setting up connections with cellular data when the Wi-Fi network is poor, always set up connections with Wi-Fi and cellular data simultaneously.
* This feature can improve the network experience significantly on poor Wi-Fi or when the Wi-Fi network is switching.

#### WireGuard

* WireGuard supports multiple peers.
* The allowed-ips now support multiple IP ranges.
* WireGuard supports preshared-key and keepalive.
* WireGuard supports peers with IPv6 endpoints. (But still no IPv6 tunnel support)
* WireGuard now supports underlying-proxy.
* The raw TCP connections are now relayed on the L3 layer if no high-level features are used.

#### Detached Profile

* You can now include multiple detached profiles in one section. But the section will be marked read-only and can't be edited with UI.

`#!include A.dconf, B.dconf`

#### Policy Group

* You can now temporarily override an auto test group or an SSID group's optimal option, until Surge restart or reload.
* The new parameter include-all-proxies=true is added to the policy group, which will include all proxy policies defined in the \[Proxy] section, and can be used with the policy-regex-filter parameter for filtering.
* The new parameter include-other-group="group1,group2" is added to include policies from another policy group, and can include multiple policy groups separated by commas, also can be used with the policy-regex-filter parameter for filtering.
* include-all-proxies, include-other-group, and policy-path parameters are allowed to be used in a single policy group at the same time. The policy-regex-filter parameter applies to all three.
* There is an order of precedence among the policy groups for the include-other-group parameter, but there is no order of precedence among the include-all-proxies, include-other-group, and policy-path parameters. For scenarios where the order of sub-policies makes sense (e.g., fallback groups), use policy groups nesting with include-other-group.

#### Subnet expression

* SSID Group is now upgraded to Subnet Group, which supports subnet expression.
* SSID Setting now supports subnet expression.
* The SUBNET rule now supports subnet expression.
* The \[SSID Setting] can control the TCP Fast Open behavior now. Read the manual for more information.
* The \[SSID Setting] can control the Wi-Fi assist and Hybrid Network behavior now. Read the manual for more information.

#### Proxy Protocol

* The Trojan protocol now supports using WebSocket as the transport layer.
* Shadowsocks protocol now supports underlying-proxy for UDP relay.
* You may configure the UDP testing endpoint for proxies. e.g., proxy-test-udp = google.com\@1.1.1.1
* You may benchmark a single proxy by long press on the proxy cell.

#### Module

* New Official Module: Block HTTP3/QUIC
* Surge will check updates for installed modules automatically.

#### Others

* Performance improvements.
* OpenSSL is now the default TLS engine.
* The managed profile can be opened with the text editor now.
* The default timeout of $httpClient is 5 seconds now.
* Reduced the app package size.
* You need to perform a one-time Dropbox re-authorization if you are using Dropbox syncing.
* Modules allow modifying the skip-server-cert-verify and tcp-connection parameters of \[MITM].
* The client will get an ICMP connection refused message instead of TCP RST if a REJECT policy matches.
* Supports IPv6 addresses with scope ID.
* The Network diagnostics can test proxy UDP relay now.
* Bug fixes.

### Version 4.11.1 (Jan 27, 2022)

* You may edit the profile in the text mode without changing the current profile now.
* The REJECT policy now can evolve to REJECT-DROP policy for UDP traffics.
* Bug fixes.

### Version 4.11.0 (Jan 21, 2022)

#### Proxy Protocol Upgrades:

* WireGuard: Uses Surge as a WireGuard client, converting L3 VPN as an outbound proxy policy.
* Snell V3: Snell protocol now supports UDP relay.
* Trojan protocol now supports UDP relay. (No additional parameter required)
* VMess protocol supports VMessAEAD. (Policy parameter: vmess-aead = true)

#### Improvements:

* The underlying proxy (aka proxy chains) now supports using a policy group.
* New parameter: udp-policy-not-supported-behaviour. To control the fallback behavior when UDP traffic matches a policy that doesn't support UDP relay.
* You may acquire the request's headers within an http-response script via $request.headers.
* Performance optimization.
* Bug fixes.

### Version 4.10.0 (Dec 3, 2021)

* You may extend your Surge iOS Pro license to 6 devices for free. You may find the guidance in the License Management view.

#### New Features

* Sorting option in the request list.
* Supports remote rule editing for the remote controller.
* Added the effective order adjustment view for the module. You can now adjust the effective order of the module.
* Supports custom the policy IP TOS field. Example: test-policy = direct, tos=0xb8.

#### Other Improvements

* UI details refined.
* Performance improvements.
* The network changed notification message will display the data network operator. If network automatic switching is enabled, you can use the notification to confirm the current carrier.
* The URL query part of the HTTP request is no longer displayed in the request list. It is now displayed in the details view.
* Fixed the problem that the JavaScript script timeout mechanism might not work properly.
* Fixed an issue that could occur when a load-balance group contains another group.
* Removed the "All" option from traffic statistics, as it took too long to count all historical traffic when the feature had not been used for a long time.
* You may remove devices in DDNS and Cloud Notification views.

### Version 4.9.4 (Oct 28, 2021)

Bug fixes

### Version 4.9.3 (Sep 30, 2021)

* New feature: Information Panel. Read the manual for more info: <https://manual.nssurge.com/others/panel.html>
* The profile now supports the profile version remark. Read the manual for more info: <https://manual.nssurge.com/release-note/profile-version.html>
* The HTTP scripts now support binary mode to modify the request/response body.
* Other minor improvements and bug fixes.

### Version 4.9.2 (Sep 3, 2021)

Bug fixes

### Version 4.9.1 (Aug 24, 2021)

Bug fixes

### Version 4.9.0 (Aug 20, 2021)

#### New Features: Surge Private DDNS

Surge Mac can associate its external IP address to .sgddns hostname. You may use the hostname with Surge iOS or Surge Mac on another device. The data is synced via iCloud, and the hostname can't be used publicly.

#### New Features: Egress Control (No UI Settings Currently)

* You can use the new internal policy HYBRID to make requests to try Wi-Fi and cellular simultaneously. You can also use the "hybrid=true" parameter to gain a proxy policy for the behavior.
* You can now tell Surge to use IPv4 or IPv6 under a dual-stack environment. Read the manual for more information.

#### New Features: Profile Syntax

You can look up the configuration parameters for the text editing mode within the app. It always displays the syntax for the current version.

#### New Features: Surge VIF IPv6 Stack (No UI Settings Currently)

Surge VIF now supports the IPv6 stack for the raw TCP connections. Use parameter "ipv6-vif=true" to enable.

#### Improvements

* We have changed the proxy benchmark standard. The result is now similar to a ping test result, which ignores the proxy setup cost.
* $request.id is added to the http-request and http-response scripts for continuity among scripts.
* Bug fixes.

### Version 4.8.0 (Jun 14, 2021)

New Features:

* Request Display Filter You may use multiple conditions to filter which requests to show.
* Web Dashboard You may control Surge via a web browser on local or remote devices.

Other bug fixes and improvements.

### Version 4.7.0 (Apr 21, 2021)

#### Rules

* New rule type: SUBNET, which can match SSID/BSSID/router IP address with a wildcard pattern.
* New rule type: CELLULAR-CARRIER, which can match the MCC-MNC code.
* New rule type: CELLULAR-RADIO, which can match the radio access technology of the cellular network.

#### Profile

* You may put partial sections into a detached file. See manual for more information.

#### HTTP API

* Added new profile related HTTP APIs, including GET /profiles, POST /profiles/check
* Added new device management HTTP APIs, including: GET /devices, POST /devices, GET /devices/icon
* The HTTP API, proxy services, and external controller now support listening on IPv6 addresses. (No UI supports. Manual profile editing is required.)
* You may now use 'http-api-tls=true' enable TLS for HTTP API access. (aka HTTPS-API)

Other bug fixes and improvements.

### Version 4.6.0 (Feb 26, 2021)

#### Remote Controller

* You may use this remote controller to view real-time statistics, and events and perform network diagnostics remotely.
* You may use the remote controller to control the DHCP server feature of Surge Mac, including adjusting each device's settings.

#### Cloud Notification

* You can receive Surge Mac's notifications on your iOS device.

#### Scripting

* You may execute a script with Siri or Shortcuts.

#### Policy Group

In this release, we completely refactored the policy group functionality, bringing the following changes:

1. The url-test/fallback/load-balance policy group can no longer be configured with a specific testing URL but with a global testing URL or a policy-configured testing URL. The policy's test results can be used directly in all policy group decisions, eliminating the need to retest each policy group individually.
2. All types of policy groups support mixed nesting. The only requirement is that no circular references can be used.
3. When a group policy is used as a sub-policy of the url-test/fallback/load-balance group.

* The latency of the select/url-test/fallback/ssid group is the latency of the selected policy.
* The latency of the load-balance group is the average of the latencies of all available policies.

4. The timeout parameter of a policy group marks policies with latency exceeding this parameter as unavailable when making decisions for the group. But the maximum time taken to test the policy group is controlled by the global test-timeout parameter. (Default is 5s)
5. When testing a group due to decision making, all sub-policies that the group may use are tested, including sub-policies of the sub-policy group.
6. You may use no-alert=true parameter to suppress notifications for particular groups.

### Version 4.5.1 (Jan 20, 2021)

Bug fixes

### Version 4.5.0 (Jan 19, 2021)

* New Feature: Network Layer Packet Capture: You may now capture the raw TCP/UDP/ICMP packets and inspect them right on the device. Or you can export a standard .pcap file for other tools.
* You can customize the GeoIP database updating URL now.
* The GeoIP database can be updated automatically now.
* Bug fixes and improvements.

### Version 4.4.3 (Oct 28, 2020)

* Optimized for the iPhone 12 series.
* Modified requests are now marked with orange color.
* Bug fixes.

### Version 4.4.2 (Sep 25, 2020)

Bug fixes

### Version 4.4.1 (Sep 23, 2020)

Bug fixes

### Version 4.4.0 (Sep 20, 2020)

New Features:

* HTTP API: Control Surge with HTTP API with another app or from another device.
* Proxy Chain: Connection to a remote host will be performed sequentially from one proxy server to another.

Major Improvements:

* You may mix the external proxies with the proxies of the profile in one policy group now.
* The DNS result view has more information.
* You may use 'policy-regex-filter' to include a part of an external proxy list's content.
* New CELLULAR and CELLULAR-ONLY policy.

Minor Improvements:

* iCloud Drive sync improved.
* You may use $notification.post in a script to post a notification with an action URL.
* The HTTP proxy service now supports basic authentication.
* Surge now enables TCP keepalive for all outgoing connections.
* Surge now supports to use of a URL with a username and password to perform basic authentication for an external resource. (<https://username:password@example.com>)

We recently published official guidance for you to understand Surge. You may find it in the More tab. Version 4.3.2 (Jun 25, 2020) Improvements for the latest iOS system. Version 4.3.1 (Jun 22, 2020) New Feature: Wi-Fi Timeline You may check the connected Wi-Fi network timeline, including entering and leaving time.

Minor Changes

* Optimized the timing system. The DNS time cost is now calculated precisely.
* Bug fixes.

### Version 4.3.0 (Jun 4, 2020)

New Feature: Mock

* You may mock the API server and return a static response. This feature may also be called as Map Local or API Mocking. New Feature: Event Center
* You may now review all historical events.

Minor Changes:

* Optimized the classical start view for Dark Mode.
* The Load-Balance group now supports connectivity testing.
* Add a parameter "use-local-host-item-for-proxy", to use local DNS mapping result even through a proxy protocol.
* The module may adjust contents in \[SSID Setting] now.
* Optimized Wi-Fi Assist feature.
* You may specify the timeout while using the script editor. Version 4.2.2 (May 19, 2020)
* New Feature: Traffic Statistics You may examine the history of traffic usage grouped by the host, by policy, or by the network interface.
* New Feature: DOMAIN-SET We have added a new type of rule: DOMAIN-SET, which may contain millions of sub-rules. No UI configuration in this version. Please configure with the Text Mode

\[Rule] DOMAIN-SET,hostname.txt,REJECT

Each line in the file is a hostname or an IP address. If the hostname starts with a dot, all sub-domains will be matched.

* Other bug fixes and improvements. Version 4.2.1 (Apr 28, 2020) New Feature: Enhanced Wi-Fi Assist
* Surge will try to set up a connection with cellular data when the Wi-Fi network is poor.

Changes in DNS-over-HTTPS

* From this version, if DNS-over-HTTPS is configured, the traditional DNS will only be used to test the connectivity and resolve the domain in the DOH URL.
* The DNS over HTTPS now has a separate parameter: doh-server. The DOH servers in 'dns-server' will be moved to the new parameter after saving.
* The legacy DNS is always required now.
* DOH can be matched with rule 'PROTOCOL,DOH' now.
* Added a new parameter 'doh-follow-outbound-mode'. In the previous version, the DOH client follows the system proxy settings. From this version, all DOH requests will use DIRECT policy by default. If 'doh-follow-outbound-mode' is set, the DOH requests will follow the outbound mode settings regardless of the system proxy settings.

Bug fixes and stability improvements

### Version 4.2.0 (Apr 17, 2020)

New Feature: Module Module is a set of settings to override the current profile. You may use modules to:

* Tweak settings in a non-editable profile, such as managed profile and enterprise profile.
* Change part of settings with one tap. For example, you may use a module to enable MitM for all hostnames and adjust the filter temporarily.
* Use a module written by others to accomplish a particular task. For example, your co-work may share with you a module that rewrites the API requests to a test server.
* When you share one profile among devices, some settings might need modifying for different scenarios. The enabling state of modules won't be synced to other devices, so you can use a module to fulfill.

Minor Improvements:

* Added a new rule type: PROTOCOL.
* Improved the MITM CA certificate install assistant.
* You may now use UI to configure a load-balance policy group.
* You may now use UI to configure SSID suspend.
* Bug fixes.

### Version 4.0.2 (Feb 11, 2020)

* Bug fixes
* Supports choosing profiles in a subdirectory
* A new feature has been added: iperf3 client mode. You may use it to benchmark the bandwidth. Different from the standalone iperf app, you may force the test to use a specified proxy.

A quick guide:

1. Install iperf3 on the proxy server.
2. Run "iperf3 -s" within a screen or tmux session.
3. Start iperf test with Surge. Leave the hostname field empty. 127.0.0.1 will be used and indicates the proxy server itself. Version 4.0.1 (Dec 31, 2019)

* Support VMess proxy protocol
* Bug fixes

### Version 4.0.0 (Sep 18, 2019)

Welcome to Surge 4. We are now introducing the Feature Subscription. As a Pro license owner, you:

* Always have access to all your features for a lifetime.
* Get free enhancement updates for features you already have for a lifetime.
* Get compatibility updates for new systems and new devices for a lifetime.
* Get a one-year free Feature Subscription since your purchasing date.
* Renew the subscription when a new feature impresses you, totally optional.

New features:

* Scripting: Use JavaScript to extend the ability of Surge as your wish.
* Dark Mode: Fully adapted for iOS 13 Dark Mode.
* DNS over HTTPS: Use DNS over HTTPS (DoH, RFC 8484) to perform DNS queries.
* TLS v1.3: TLS v1.3 support for HTTPS/SOCKS5-TLS proxy.
* Dropbox: Use Dropbox to sync your profiles across devices.

### Version 3.8.1 (Jun 4, 2019)

Bug fixes

### Version 3.8.0 (May 21, 2019)

Proxy

* Rules can be enabled/disabled now. Try sliding left on it.
* New option for url-test/fallback group: evaluate-before-use. By default, the requests before a connection evaluation will use the first policy in the list and trigger the evaluation. Enable the option to delay the requests until the evaluation is completed.

MitM

* HTTP and MitM engine has been refactored.
* You can now use the URL-REGEX rule for MitM connections.
* You may use the prefix '-' to exclude domains for MitM.
* MitM hostname list now supports port numbers. By default, only the connections to port 443 will be decrypted.

Minor Improvements

* Move the 'External Resources' item to the profile list view. Managed profile users may utilize the view to update resources now.
* It won't bother you anymore that the Cloud profiles disappear sometimes.
* Touch ID / Face ID now allows passcode as a fallback.
* Refined English localization.
* Refined UI details.
* The notification banner is draggable now.
* All advanced options can be edited with UI now. Please do not touch it before reading the manual.

Bug Fixes

* Fixed a bug that the request detail page doesn't update in real-time
* Fixed a bug that the GEOIP rule doesn't work for IPv6 addresses. Version 3.7.1 (Apr 27, 2019)
* Remote Dashboard: You may connect to another device with Surge iOS/Mac running and inspect the requests.
* An active connection can be killed now.
* Bug fixes Version 3.7.0 (Apr 16, 2019)
* Refined UI, including a fullscreen text editor for complex text fields, new colorful icons, and more detail improvements.
* New feature: Always On. Surge may start automatically even after a device reboot.
* The request detail page now updates in real-time.
* The ruleset can be added or edited with UI now.
* Policy group with an external list can be added or edited with UI now.
* Bug and compatibility fixes.

### Version 3.6.1 (Mar 20, 2019)

* Bug fixes

### Version 3.6.0 (Mar 15, 2019)

* Added support for a new proxy protocol Snell.
* You may export all dumped requests to a .surgearchive file and open with Surge Mac Dashboard.
* Optimizations for the request search view.
* Experimental feature: You can enable Network.framework to utilize user-space network stack, which can improve throughput, reduce latency and enable cutting edge features such as Multipath TCP.
* Minor bug fixes.

### Version 3.5.0 (Jan 3, 2019)

* Performance improvements
* Prompts profile changes via iCloud Drive
* Allows to customize Wi-Fi access ports for HTTP & SOCKS5 proxy services
* Supports to update GeoIP database manually
* Copy cURL is now available for all HTTP methods
* Captured body data may be exported to other apps
* Bug fixes

### Version 3.4.2 (Nov 21, 2018)

Bug fixes
