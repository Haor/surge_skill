# 不同 REJECT 策略的区别

Surge 内置了多个不同的 REJECT 策略，不同策略间有一些细微的差别：

* `REJECT`：拒绝该请求，当连接类型为 HTTP 时，会返回一个错误页面。（该行为可被 `show-error-page-for-reject` 参数控制）
* `REJECT-TINYGIF`：拒绝该请求，当连接类型为 HTTP 时，返回一个 1px 的 GIF 图片响应。若为其他类型连接则直接断开。该策略主要用于 Web 广告屏蔽。
* `REJECT-DROP`：拒绝该请求，与 `REJECT` 不同的是，该策略将静默抛弃请求。因为部分程序有着十分暴力的重试逻辑，在连接失败后会立刻进行重试，导致请求风暴，这将严重浪费系统资源。

{% hint style="info" %}
如果发往某主机名的请求短时间内大量触发 REJECT/REJECT-TINYGIF 策略（当前版本的阈值为 30 秒内 10 次），Surge 将自动升级 REJECT 策略为 REJECT-DROP 策略。
{% endhint %}

* `REJECT-NO-DROP`：一般情况下与 `REJECT` 策略相同，区别在于使用该规则时将不会触发上述自动升级的行为。
