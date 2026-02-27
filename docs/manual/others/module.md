Title: Module · GitBook

URL Source: https://manual.nssurge.com/others/module.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

Module is a set of settings to override the current profile. You may use modules to:

*   Tweak settings in a non-editable profile, such as managed profile and enterprise profile.
*   Change part of settings with one tap. For example, you may use a module to enable MitM for all hostnames and adjust the filter temporarily.
*   Use a module written by others to accomplish a particular task. For example, your co-work may share with you a module that rewrites the API requests to a test server.
*   When you share one profile among devices, some settings might need modifying for different scenarios. The enabling state of modules won't be synced to other devices, so you can use a module to fulfill.

### Basic Concepts

A module is like a patch to the current profile. The settings of modules have a higher priority than the settings of the profile.

There are 3 types of modules:

*   Internal Modules: Provided by Surge itself.
*   Local Modules: .sgmodule files placed in the profile directory.
*   Installed Modules: Modules installed with a URL.

### Write a Module

The syntax of a module is the same as the profile. You are allowed to override these sections:

*   General, MITM

    *   Override: `key = value`
    *   Append to the original value: `key = %APPEND% value`
    *   Insert in the front of the original value: `key = %INSERT% value`

You can manipulate the 'hostname', 'skip-server-cert-verify', and 'tcp-connection' fields only in a MITM section.

> The legacy `[Replica]` section used by the HTTP capture feature was removed in Surge Mac 5.4.0, so modules no longer need to patch it.

*   `[WireGuard *]` sections

WireGuard policies live in sections whose names start with `WireGuard`. Modules can override or append keys inside those sections just like the main profile.

*   `[Ruleset *]` sections

When you define inline rulesets, modules may now patch them as well, which is useful for managed configurations that ship inline lists.

*   Rule, Script, URL Rewrite, Header Rewrite, Host

The new lines will be inserted at the top of the original content.

The rules in a module can only use internal policies: DIRECT, REJECT, and REJECT-TINYGIF.

*   Metadata

You may add metadata in a module file:

```
#!name=Name Here
  #!desc=Description Here
```

You may limit a module to specified platform. (Optional)

```
#!system=mac
```

### Examples:

```
#!name=MitM All Hostnames
#!desc=Perform MitM on all hostnames with port 443, except those to Apple and other common sites which can't be inspected. You still need to configure a CA certificate and enable the main switch of MitM.

[MITM]
hostname = -*.apple.com, -*.icloud.com, -*.mzstatic.com, -*.crashlytics.com, -*.facebook.com, -*.instagram.com, *
```

```
#!name=Game Console SNAT
#!desc=Let Surge handle SNAT conversation properly for PlayStation, Xbox, and Nintendo Switch. Only useful if Surge Mac acts the router for these devices.
#!system=mac
[General]
always-real-ip = %APPEND% *.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com
```

### Parameter Tables Mac 5.5.0+

Use the `#!arguments` metadata to declare parameters that the user can customize when enabling the module. The syntax follows a standard query-string:

```
#!arguments=hostname=example.com&enable_mitm=true
```

Each key becomes available as `%hostname%`, `%enable_mitm%`, etc., and Surge performs a simple text replacement before applying the module. Defaults defined in `#!arguments` are shown in the UI and stored with the module instance.

> Keep placeholders alphanumeric (e.g., `%SERVER_HOST%`) to avoid conflicts with profile syntax. Remove unused placeholders when deleting an argument.

### Requirements iOS 5.10.0+Mac 5.6.0+

The module adds a `#!requirement=` description, allowing for more complex usage condition restrictions. For example, if the module uses the newly added Body Rewrite feature, it needs to restrict the version of the Surge core.

`#!requirement=CORE_VERSION>=20`

It also supports logical expressions, such as CORE_VERSION>=20 && (SYSTEM = 'iOS' || SYSTEM = 'tvOS').

The variables that can be used for judgment are as follows:

*   CORE_VERSION: Number, such as `20`
*   SYSTEM: String, such as `macOS`, `iOS`, `tvOS`
*   SYSTEM_VERSION: String, such as `Version 17.4.1 (Build 21E236)`
*   DEVICE_MODEL: String, such as `Mac15,8`
*   LANGUAGE: String, such as `zh-Hans`
