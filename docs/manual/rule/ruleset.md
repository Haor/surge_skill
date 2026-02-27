Title: Ruleset · GitBook

URL Source: https://manual.nssurge.com/rule/ruleset.html

Published Time: Tue, 20 Jan 2026 02:39:13 GMT

You may use a bundle of rules from a file or a URL. Surge also provides two internal rulesets.

Internal Ruleset
----------------

The internal ruleset contents might change with Surge version updates. Please go to the ruleset settings to check the latest sub-rules.

### SYSTEM

`RULE-SET,SYSTEM,DIRECT`

Includes rules for most requests sent by macOS and iOS itself. The requests sent by App Store, iTunes, and other content services are not included.

```
USER-AGENT,*com.apple.mobileme.fmip1
USER-AGENT,*WeatherFoundation*
USER-AGENT,%E5%9C%B0%E5%9B%BE*
USER-AGENT,%E8%AE%BE%E7%BD%AE*
USER-AGENT,com.apple.geod*
USER-AGENT,com.apple.Maps
USER-AGENT,FindMyFriends*
USER-AGENT,FindMyiPhone*
USER-AGENT,FMDClient*
USER-AGENT,FMFD*
USER-AGENT,fmflocatord*
USER-AGENT,geod*
USER-AGENT,locationd*
USER-AGENT,Maps*
DOMAIN,api.smoot.apple.com
DOMAIN,captive.apple.com
DOMAIN,configuration.apple.com
DOMAIN,guzzoni.apple.com
DOMAIN,smp-device-content.apple.com
DOMAIN,xp.apple.com
DOMAIN-SUFFIX,ess.apple.com
DOMAIN-SUFFIX,push-apple.com.akadns.net
DOMAIN-SUFFIX,push.apple.com
DOMAIN,aod.itunes.apple.com
DOMAIN,mesu.apple.com
DOMAIN,api.smoot.apple.cn
DOMAIN,gs-loc.apple.com
DOMAIN,mvod.itunes.apple.com
DOMAIN,streamingaudio.itunes.apple.com
DOMAIN-SUFFIX,lcdn-locator.apple.com
DOMAIN-SUFFIX,lcdn-registration.apple.com
DOMAIN-SUFFIX,ls.apple.com
PROCESS-NAME,trustd
```

> These rules may be updated with Surge updates. Please refer to the description in the software to get the latest sub-rules.

### LAN

`RULE-SET,LAN,DIRECT`

Includes rules for LAN IP addresses and .local suffix. Please notice this ruleset will trigger a DNS lookup.

```
DOMAIN-SUFFIX,local
IP-CIDR,192.168.0.0/16
IP-CIDR,10.0.0.0/8
IP-CIDR,172.16.0.0/12
IP-CIDR,127.0.0.0/8
IP-CIDR,100.64.0.0/10
IP-CIDR6,fe80::/10
```

External Ruleset
----------------

Ruleset from a URL or a local file. The ruleset file should be a text file. Each line contains a rule declaration without the policy.

Example:

```
DOMAIN,exampleA.com
DOMAIN,exampleB.com
```

The `RULE-SET` line in `[Rule]` accepts optional parameters that apply to every sub-rule:

*   `no-resolve`: Skip DNS resolution when matching the set.
*   `extended-matching`: Allow domain rules inside the set to match both SNI and HTTP Host headers.

Example:

```
RULE-SET,https://example.com/social.list,Proxy,no-resolve,extended-matching
```

Inline Ruleset Mac 5.3.1+
-------------------------

Instead of hosting the list externally, you can embed the rules directly inside the profile.

```
[Ruleset Streaming]
DOMAIN-SUFFIX,netflix.com
DOMAIN-SUFFIX,netflix.net
DOMAIN,netflixdnstest0.com

[Rule]
RULE-SET,Streaming,StreamingProxy
```

Inline rule sets share the same syntax as standalone files and benefit from the same preprocessing/indexing optimizations.
