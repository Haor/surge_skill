# Detached Profile

To meet the complexity of various usage scenarios, Surge supports separating a section of the configuration file into one or more separate files. This feature is also called linked profile at the UI level.

Example:

```
[General]
loglevel = notify

[Proxy]
#!include Proxy1.dconf, Proxy2.dconf

[Proxy Group]
#!include Group.dconf

[Rule]
#!include Rule.dconf
```

The referenced file must contain the corresponding section declaration with \[]. Therefore, the file can be either a partial configuration file containing only some sections (one or more) or a complete configuration.

With this feature, you can:

1. Only reference the \[Proxy] and \[Proxy Group] sections from the proxy service provider's managed configuration and write the other sections yourself.
2. Share the content of a few sections between multiple configurations.

Please note:

* After modifying the configuration through the UI, the configuration will be written to the corresponding separate configuration section files according to the include declaration. However, if a section refers to multiple separate configuration section files, the related content of that section cannot be edited in the UI.
* If a managed configuration is referenced, the related configuration cannot be edited, but it does not affect the adjustment of other sections.
* There is no requirement for the file extension. If it is a complete configuration, you can continue to use the conf extension. If it is not a complete configuration, it is recommended to use the dconf extension. Dconf files can be displayed in the list in Surge iOS and can be edited with a text editor.
* The referenced file cannot refer to another file.

<details>

<summary><mark style="color:purple;">Use Case #1:</mark> The proxy service provider provides a managed configuration, and you only need its proxy policies and don't want to use the other contents in the managed configuration</summary>

1. Create a new blank configuration.
2. Add the following content to the configuration:

```
[Proxy]
#!include ManagedProfile.conf

[Proxy Group]
#!include ManagedProfile.conf
```

Where ManagedProfile.conf is the managed configuration file name.

3. Reload the configuration, and now you can use the policies and policy groups from ManagedProfile.conf, but other content can be freely edited.

</details>

<details>

<summary><mark style="color:purple;">Use Case #2:</mark> Different WireGuard Peer IPs and Private Keys for multiple clients in the configuration</summary>

1. Suppose the original configuration name is Common.conf, create a new iPhone.conf for iPhone use and a Mac.conf for MacBook use.
2. In the iPhone.conf and Mac.conf files, share the common content in the Common.conf file and reference it. Write the content of the WireGuard section and other content that needs to be treated separately:

```
[General]
loglevel = notify

[Proxy]
#!include Common.conf

[Proxy Group]
#!include Common.conf

[Rule]
#!include Common.conf

[WireGuard HomeServer]
private-key = …
```

Since the content of the \[General] section in Surge iOS and Mac is quite different, it is generally recommended to write them separately.

</details>
