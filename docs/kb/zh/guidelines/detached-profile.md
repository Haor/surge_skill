# 配置分离

为了满足各种使用场景的复杂性，Surge 支持将配置的一个段分离至另一个或多个文件中。该功能在 UI 层面又被叫做关联配置。

样例：

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

其中所引用的另一个文件，必须包含对应段的 \[] 声明。因此，该文件既可以是一个只包含部分段的文件（一个或多个），也可以是一个完整的配置。

使用该功能，你可以：

1. 只引用服务商托管配置的 \[Proxy] 和 \[Proxy Group] 段，自行编写其他段。
2. 在多个配置间共享某几个段的内容。

请注意：

* 在通过 UI 修改配置后，会按照 include 的声明将配置写入对应的分离配置段文件。但是如果一个段中引用了多个分离配置段文件，那么该段的相关内容无法在 UI 中进行编辑。
* 如果引用的是一个托管配置，则和该段相关的配置不可被编辑，但是不影响其他段的调整。
* 文件名的后缀并没有要求，如果是一个完整配置可继续使用 conf 后缀，如果并非一个完整配置建议使用 dconf，dconf 文件在 Surge iOS 里可在列表中显示，并可以使用文本编辑。
* 引用的文件不可以再次去引用另一个文件。

<details>

<summary><mark style="color:purple;">用例 #1：</mark>代理服务商提供了托管配置，仅需要其代理策略，并不想使用托管配置中的其他内容</summary>

1. 新建空白配置。
2. 在配置中增加以下内容：

```
[Proxy]
#!include ManagedProfile.conf

[Proxy Group]
#!include ManagedProfile.conf
```

其中 ManagedProfile.conf 为托管配置文件名。

3. 重载该配置，此时可以使用来自 ManagedProfile.conf 的策略和策略组，但是其他内容均可自由编辑。

</details>

<details>

<summary><mark style="color:purple;">用例 #2：</mark>多个客户端间配置不同的 WireGuard Peer IP 和 Private Key</summary>

1. 假设原配置名为 Common.conf，新建 iPhone.conf 供 iPhone 使用，新建 Mac.conf 供 MacBook 使用。
2. iPhone.conf 和 Mac.conf 文件里，共同使用的内容放在 Common.conf 中并引用，WireGuard 段的内容和其他需要分开对待的内容单独撰写：

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

由于 Surge iOS 和 Mac 的 \[General] 段内容区别较大，一般建议分开单独撰写。

</details>
