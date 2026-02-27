Title: Rule · GitBook

URL Source: https://manual.nssurge.com/scripting/rule.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

### rule

Uses a script as a rule. The value field will be used as a name.

`rule ssid-rule script-path=ssid-rule.js`

Then add a line in [Rule] section:

`SCRIPT,ssid-rule,DIRECT`

The script should return an object with property 'matched' to indicate if matched.

The incoming parameters are：

*   `$request.hostname<String>`
*   `$request.destPort<Number>`
*   `$request.processPath<String>`
*   `$request.userAgent<String>`
*   `$request.url<String>`
*   `$request.sourceIP<String>`
*   `$request.listenPort<Number>`
*   `$request.dnsResult<Object>`
*   `$request.srcPort<Number>`iOS 5.8.4+Mac 5.4.4+
*   `$request.protocol<Number>`iOS 5.8.4+Mac 5.4.4+

By default, the SCRIPT rule doesn't trigger a DNS lookup. You may use the 'requires-resolve' option to change it.

`SCRIPT,ssid-rule,DIRECT,requires-resolve`

The DNS result presents in $request.dnsResult.

A simple example:

```
var hostnameMatched = ($request.hostname === 'home.com');
var ssidMatched = ($network.wifi.ssid === 'My Home');

$done({matched: (hostnameMatched && ssidMatched)});
```
