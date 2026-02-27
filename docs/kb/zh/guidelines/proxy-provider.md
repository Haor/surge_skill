# 使用来自代理服务商的线路

## 配置模式

### A. 托管配置

大多数服务商会提供一份完整的 Surge 托管配置，以实现“开箱即用”。这是最便捷的接入方式：在该模式下，所有系统设置和分流规则均由服务商预设并负责维护更新。但也正因如此，用户无法在本地直接修改其中的设置与规则。

### B. 关联配置

关联配置以一份托管配置为基础，创建一个可供编辑的本地副本。通过使本地配置中的部分配置段（Section）持续跟踪托管配置的变化，从而在“配置自动更新”与“本地个性化修改”之间取得平衡。

对于大多数用户，推荐配置 `[Proxy]` 和 `[Proxy Group]` 段追踪托管配置，而其他段（如通用设置、规则等）则由本地自行控制。

### C. 外置策略组

这是 Surge 进阶用户最推荐的模式。它允许用户完全自主控制配置文件，利用外部资源实现高度灵活的定制，但要求用户对 Surge 的特性有较深入的了解。

配置示例：

`Proxy-Provider = select, policy-path=https://airport.com/surge.conf`

`policy-path` 对应的 URL 可以是一个纯代理策略列表（每行为一个代理策略声明的文本文件），也可以是一个完整的 Surge 配置文件，Surge 会自动提取其中的 `[Proxy]` 段内容。

## 实践场景

Surge 提供了极高的灵活性以满足各类复杂需求。具体参数说明请参阅官方手册，以下整理了一些推荐的配置方案与常见需求示例。

<details>

<summary><mark style="color:purple;">用例 #1：</mark>按地区划分线路</summary>

如果您的代理服务商提供了多个地区的线路，且您希望能够手动或自动选择特定地区的线路。

首先，建立一个外置策略组以导入服务商的所有线路：

```
Airport-All = select, policy-path=https://airport.com/surge.conf, hidden=true
```

设置 `hidden=true` 是因为该策略组仅作为“资源池”，我们不会在 UI 中直接使用它。

随后建立多个子策略组，利用正则过滤功能筛选出特定地区的线路：

```
Airport-US = smart, include-other-group=Airport-All, policy-regex-filter=美国
Airport-UK = smart, include-other-group=Airport-All, policy-regex-filter=英国
```

由于我们通常不关注具体使用该地区的哪条线路，建议将策略组类型设为 `smart`。这样 Surge 将自动测速并优选最佳线路，且当某条线路故障时，只要组内仍有可用线路，即可实现无感切换。

之后，您便可以在规则 `[Rule]` 中直接使用 `Airport-US` 或 `Airport-UK` 指定地区。

{% hint style="success" %}
若需要可以随时切换线路地区，还可以再建立一个手动选择组：

```
Booster = select, Airport-US, Airport-UK
```

{% endhint %}

</details>

<details>

<summary><mark style="color:purple;">用例 #2：</mark>多供应商资源融合</summary>

假设您同时订阅了 Awesome 和 Fantastic 两家供应商的服务，并希望像“用例 1”那样统一按地区调度，可以进行如下融合配置：

```
Airport-Awesome = select, policy-path=https://awesome.com/surge.conf, hidden=true, external-policy-name-prefix=Awesome-
Airport-Fantastic = select, policy-path=https://fantastic.com/surge.conf, hidden=true, external-policy-name-prefix=Fantastic-

Airport-US = smart, include-other-group="Airport-Awesome, Airport-Fantastic", policy-regex-filter=美国
Airport-UK = smart, include-other-group="Airport-Awesome, Airport-Fantastic", policy-regex-filter=英国
```

`external-policy-name-prefix` 参数的作用是为该组内的子策略名添加前缀。由于各供应商对线路的命名通常仅包含地区（如“美国-01”），添加前缀后（如“Awesome-美国-01”）可以方便在请求列表和日志中辨别当前线路所属的供应商。

{% hint style="warning" %}
在配置 `include-other-group` 参数时，若需包含多个策略组，必须使用引号 `""` 将参数内容包裹。
{% endhint %}

</details>

<details>

<summary><mark style="color:purple;">用例 #3：</mark>跳板代理（链式代理）</summary>

若您需要通过一个跳板代理（Relay）来访问供应商的线路，可以使用 `external-policy-modifier` 参数为导入的策略动态追加 `underlying-proxy` 参数：

```
Airport-Awesome = select, policy-path=https://awesome.com/surge.conf, hidden=true, external-policy-modifier="underlying-proxy=Airport-Fantastic"
```

这将构建出：客户端 -> Airport-Fantastic (跳板) -> Airport-Awesome (出口) -> 目标服务器 的代理链。

{% hint style="info" %}
您可以预先定义一个包含 `DIRECT` 策略的 `select` 组并将其设为 `underlying-proxy`，这样就能在控制面板中随时开启或关闭跳板代理模式。
{% endhint %}

{% hint style="info" %}
也可以使用 `external-policy-modifier` 参数进行其他微调，如打开 TCP Fast Open。
{% endhint %}

</details>
