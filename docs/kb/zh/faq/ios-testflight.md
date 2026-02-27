# Surge iOS TestFlight

加入 Surge iOS TestFlight 后可以使用 Surge iOS 和 Surge tvOS 的 Beta 版本，Beta 版本包含实验性的功能且可能不稳定，仅推荐喜欢尝鲜且有经验的用户参与，所有已购买用户都可以自行加入。

1. 如果是从网站购买的授权或者已经绑定了邮箱

直接访问 <https://nssurge.com/account> 登录后操作。

2. 如果通过 App Store IAP 购买

请先在 App 的授权管理页面绑定邮箱，然后再访问 <https://nssurge.com/account> 登录后操作。

详情请参考 [ios-faq](https://kb.nssurge.com/surge-knowledge-base/zh/license/ios-faq "mention")

技术支持不会回答关于 TestFlight 自身的询问邮件，请查阅 Apple 的相关说明。

## 常见问题

### 为什么提示：「无法接受此邀请，因为你的 Apple 账户 <joe@icloud.com> 已与此 App关联。」

受限于 TestFlight 系统限制，如果已经加入过 Surge 的 TestFlight，希望通过 Opt-out 操作修改绑定账号，重绑定操作必须要等待 90 天后方可进行。

### TestFlight 版本可否绑定在 Surge iOS 未上架的 App Store 区域账号？

不可以，Apple 于 2021 年 2 月修改了 TestFlight 的行为，必须使用一个 Surge 上架区域的 Apple ID 方可安装 TestFlight 版本。（即不可以使用中国区 ID）

如果在非上架区域尝试安装，会收到「所请求的 App 不可用或者不存在」错误。

### TestFlight 的 Apple ID 和授权邮箱有关系吗？

最终关联的 Apple ID 由点击邀请邮件的 iOS 设备的当前登录的 App Store 账号决定，和授权邮箱（即收取 TestFlight 邀请的邮箱）并没有关系。

但是我们强烈推荐使用与授权邮箱一致的 Apple ID 进行绑定，使用不一致的 Apple ID 接受邀请，可能导致后续解除绑定时出现异常（此为 Apple 服务端的一个问题）。可以在加入 TestFlight 前先自助修改授权邮箱。

请注意一旦出现异常，需要在执行 Opt-out 后等待 90 天方可绑定至其他账号。

### TestFlight 版本是否稳定？

TestFlight 版本的目标是测试新功能，更新频率高但是可能不太稳定，如遇到问题请及时反馈，一般严重问题会在一到两天内修复。另外 TestFlight 中允许随时会退到先前的版本，如果遇到严重问题也可以自行进行版本回退。

### 收不到 TestFlight 邀请邮件怎么办？

邀请邮件由 Apple 服务器发出，部分邮箱可能接收困难，请先检查垃圾邮件箱，也可 Opt-out 后重新加入以重发，或者修改授权邮箱到另一个邮箱地址接收。

### 怎样修改绑定的 Apple ID？（或者操作错误导致邀请码失效）

可在上述管理页面执行 Opt-out 操作，然后重新进行加入。请注意退出后需要等待 90 天方可重新加入。

### 怎样取消 TestFlight 的邮件通知和推送

所有 TestFlight 相关的推送和邮件均由 Apple 发送，如需取消邮件或推送需在 TestFlight 的 App 内进行操作。
