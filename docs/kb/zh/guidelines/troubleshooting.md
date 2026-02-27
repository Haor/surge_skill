# Surge 故障排除指南

如果你在使用 Surge 时遇到了问题，请参照该文进行故障排除。

{% hint style="success" %}
在开始前，可以先阅读 [《Surge 官方中文指引：理解 Surge 原理》](https://manual.nssurge.com/book/understanding-surge/cn/) 了解 Surge 的具体工作原理。
{% endhint %}

{% hint style="warning" %}
在进行仔细排错前，请先尝试重启 Mac 或者 iPhone 试一下是否可以解决问题。如果问题在重启后消失且不再出现，一般属于系统级偶发 Bug，可以忽略。

如果该指南未能成功协助解决问题，请联系 <support@nssurge.com>，请记得附带本指南中所提供的测试命令的输出结果。
{% endhint %}

{% stepper %}
{% step %}

#### 托管配置问题

请注意，Surge 是一款网络工具，其工作行为取决于配置的设置，如果你的配置来源于服务商或者其他人，如果在安装或更新配置时出现错误，请与配置提供者联系，我们无法提供协助。
{% endstep %}

{% step %}

#### 分析问题来源

Surge 作为一款本地网络转发工具，常见的问题分为两大类：未能成功接管网络请求，和未能成功发出网络。这两类问题的处理方式上有本质的区别。

首先，请打开 Surge Mac 的请求查看器（Dashboard），如果是 Surge iOS 请打开最近请求页面。然后打开浏览器访问任意常见网站，如 <https://bing.com。然后观察请求列表中是否出现了该请求。>

{% hint style="info" %}
如果你曾经修改过 Surge 的捕获过滤器设置，可能导致请求被隐藏，请务必确认捕获过滤器中没有隐藏测试的请求。
{% endhint %}

如果请求列表中没有该请求，则说明是接管问题。如果出现了请求，则说明是转发问题。
{% endstep %}

{% step %}

#### 如果未能看见请求 - 接管类问题

{% tabs %}
{% tab title="Surge Mac" %}
Surge Mac 存在系统代理与增强模式（NE VIF）两大接管模式，请先前往总览页面确认这两项是否开启，状态是否正常。其中任意一个开启即可接管浏览器请求。

**确认系统代理**

如果这里显示正常，则可以通过命令行进一步确认，在终端执行 `scutil --proxy` 可以打印当前系统中生效的系统代理设置，如果 Surge 正确设定了系统代理，那么结果应该为：

```
<dictionary> {
  ExcludeSimpleHostnames : 1
  HTTPEnable : 1
  HTTPPort : 6152
  HTTPProxy : 127.0.0.1
  HTTPSEnable : 1
  HTTPSPort : 6152
  HTTPSProxy : 127.0.0.1
}
```

其中 ExcludeSimpleHostnames 字段的值无所谓，如果其他字段的值不一样，则说明 Surge 未能成功设置系统代理，请检查是否有其他同类软件抢占了系统代理设置。

**确认增强模式**

可在系统设置›网络›VPN 设置中，查看 Surge 是否处于开启状态。如果没有，则说明增强模式启动失败，通常你应该在 Surge 的界面上看到明确的错误提示。同时如果有其他 VPN 项目处于开启状态，说明是该程序抢占了系统 VPN 使用权。

也可以通过命令行进行测试，执行 `ping apple.com`，如果成功，且目标 IP 为 `198.18.x.x`，则说明 Surge 增强模式工作正常，可进一步通过 `curl -vvv https://apple.com` 确认。

如果增强模式不正常，在尝试重启无效后，可尝试在 Surge Mac 的更多›设置›系统权限总览中，将网络扩展和 VPN 配置移除。然后重启电脑后重新尝试打开增强模式。
{% endtab %}

{% tab title="Surge iOS" %}
通常来讲，Surge iOS 正常开启的情况下，几乎不会出现接管问题。请尝试重启系统，如果无效的话，请尝试在系统设置中，重置网络设置。如果依然无法出现请求，请联系 <support@nssurge.com>。
{% endtab %}
{% endtabs %}

{% hint style="info" %}
如果你仅在访问某些域名时，出现接管问题，这通常是配置导致的：

* Surge 配置中的 `skip-proxy` 参数，会使得该参数中的请求，不使用系统代理进行接管，所以如果访问域名出现于该参数中，请删除。
* 在 Surge iOS 或 Surge Mac 增强模式下，如果是访问某个内网 IP 无法被接管，这是正常情况，因为当前网络可能存在范围更小、优先级更高的路由表，系统将直接访问而不会经由 Surge VIF 处理。请务必为该 IP 配置一个域名（本地 DNS 映射）进行访问，以保证请求一定会被 Surge 接管。
  {% endhint %}
  {% endstep %}

{% step %}

#### 如果能看见请求 - 转发类问题

请点击到具体的请求，切换到日志（Notes）标签页，这里记录了该请求失败的具体原因。通常来将一般都是代理服务器故障导致的，一些常见错误如下：

* Connection refused: 代理配置错误或代理服务器故障
* Connection timeout: 代理配置错误或代理服务器故障
* No upstream DNS server: Surge 配置中不存在有效的 DNS 服务器，请调整配置
* No route to host: 代理配置错误或者当前设备没有网络
  {% endstep %}
  {% endstepper %}
