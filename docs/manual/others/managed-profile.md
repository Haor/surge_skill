Title: Managed Profile · GitBook

URL Source: https://manual.nssurge.com/others/managed-profile.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

Surge can update a profile from a URL automatically. If the profile text starts with

`#!MANAGED-CONFIG http://test.com/surge.conf interval=60 strict=true`

The profile can only be updated when Surge main app is running.

Ensure the new remote profile also includes the #!MANAGED-CONFIG line. Without it, the profile will revert to a standard one.

### Parameters

#### interval: Optional, in seconds (Default: 86400s).

Set the update interval for the profile. Please note that this is the shortest time to trigger an update; Surge does not necessarily trigger an update immediately after this time.

#### strict: true or false (Default: false).

If strict is true, Surge will require a force update after the interval arrives. Otherwise if the update fails the user may still use the outdated config.

> Note: Even when strict is true, the user still can start Surge by widget or VPN switch in Settings.

### REQUIREMENT Statement

The `!REQUIREMENT` statement can be used at the beginning or end of a configuration line to limit the line's effect to specific environments, such as

`#!REQUIREMENT CORE_VERSION>=22 Group = smart, policyA, policyB`

or

`Group = url, policyA, policyB //!REQUIREMENT CORE_VERSION<22`

Variables that can be used for conditions include `CORE_VERSION, SYSTEM, SYSTEM_VERSION, DEVICE_MODEL, LANGUAGE`

Available operators are `=,==,>=,=>,<=,=<,>,<,!,<>,AND,&&,OR,||,NOT,!,BEGINSWITH,CONTAINS,ENDSWITH,LIKE,MATCHES`

A typical example of a variable value:

```
CORE_VERSION: 22
SYSTEM: iOS
SYSTEM_VERSION: System Version 17.4.1 (Build 21E236)
DEVICE_MODEL: iPhone16,1
LANGUAGE: en-US
```

#### Core Version

When Surge releases new features, it often introduces new syntax to the configuration, and the corresponding Core Version increases. This version can be used to determine whether a feature is available, with the version number and main changes as follows:

*   22: Surge Mac 5.7.0, Surge iOS 5.11.0, Smart Group
*   20: Surge Mac 5.6.0, Surge iOS 5.10.0, Body Rewrite, Inline Map Local

When using strings in expressions, the strings should be wrapped with '. When an expression contains spaces, it should be wrapped in "".

`#!REQUIREMENT "CORE_VERSION>=22 AND SYSTEM=='iOS'" Group = smart, policyA, policyB`

Expressions will be lost when modifying profile in the UI, so this feature is mainly used for managed and enterprise profiles.

Since earlier versions than Surge iOS 5.11.0 and Mac 5.7.0 do not support this expression, both line beginning and line end notation methods are provided, allowing for flexible support of older versions. For example, if you want to use Smart Group for clients that support it, you can write:

```
#!REQUIREMENT CORE_VERSION>=22 Group = smart, policyA, policyB 
Group = url-test, policyA, policyB //!REQUIREMENT CORE_VERSION<22
```

Since the first line is treated as a pure comment in older versions, it will not take effect, and the line-end comment in the second line will also be treated as a general comment. Only the second line takes effect.

### FORBIDDEN-AUTO-UPGRADE Statement

Starting with Surge iOS 5.11.0 and Mac 5.7.0 versions, Surge can automatically optimize the profile for upgrades to avoid the inability to use the latest features due to managed profile not being adjusted in time.

If for some special reasons, you do not wish the profile to apply certain automatic optimizations, you can use the `FORBIDDEN-AUTO-UPGRADE` expression, such as

`#!FORBIDDEN-AUTO-UPGRADE smart-group`

Currently available optimization keywords include

*   `smart-group`: automatically upgrades `url-test/load-balance` groups to `smart` groups.
