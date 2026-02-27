# Surge tvOS

Apple 于 tvOS 17 中加入了 Network Extension 支持，Surge 终于可以直接运行于 tvOS 中。所有已购买 Surge iOS 的用户均可直接使用，无需额外购买与功能订阅。

在将 tvOS 升级至 17.0 后，可直接从 App Store 安装 Surge tvOS，也可以在加入 TestFlight 后使用测试版本，详见：[ios-testflight](https://kb.nssurge.com/surge-knowledge-base/zh/faq/ios-testflight "mention")

### 功能

Surge tvOS 版本与 Surge iOS 版本使用完全一致的核心，即所有 Surge iOS 的功能均可以在 Surge tvOS 版本中使用，包括脚本、WireGuard 等复杂功能。但是部分依赖于 UI 的功能无法使用，如流量统计等。

同时，Surge tvOS 允许作为 Surge Ponte 服务端或客户端使用，正确配置后可以 Apple TV 作为跳板访问内部网络，也可以用于远程控制 Surge tvOS。关于 Surge Ponte 的详情请参考 [ponte](https://kb.nssurge.com/surge-knowledge-base/zh/guidelines/ponte "mention")。

### 开始使用

请将 Surge iOS 升级到 5.7.0 或以上版本，在更多页面中找到 Surge tvOS 项目，然后按照向导操作。

请注意，Apple TV 所登录的**主账号**必须与 Surge iOS 设备的 **iCloud 账号**一致。

### 配置

由于 Surge tvOS 无法访问 iCloud Drive（tvOS 系统未提供该机制），所有的配置相关操作需由 Surge iOS 进行部署操作进行修改。

请注意由于 Surge iOS 版本无法评估 Apple TV 所在的网络情况，所有在配置 Surge Ponte 服务端时无法像 Surge Mac 那样，对选项的可用性进行检测，请先自行确认所处网络或者所选择的代理是否为 Full Cone NAT。

#### 关于外部资源

与 Surge iOS 不相同的是，Surge tvOS 将在第一次启动时进行外部资源更新，这时部分外置策略组、外置规则可能能为空，并回退至 DIRECT，请查看日志以确认是否有外置资源持续加载失败，如有必要请调整规则与策略保证外置资源可以完成初始化。

也可以通过远程控制器查看当前的远程资源更新情况，并手动进行更新。

### 控制

Surge tvOS 不提供直接的 UI 控制功能，所有控制操作均应通过 Surge iOS 完成，在完成配置部署并开启 Surge tvOS 后，在工具列表的远程控制器设备列表中会自动出现 Apple TV 的项目，可通过 Surge iOS 进行各项控制操作与查看请求和统计结果。

远程控制器通过 Surge Ponte 进行访问，可在任何网络下进行控制，若无需使用 Surge Ponte 穿透功能，可将 Surge Ponte 配置为 LAN-Only，仅供同局域网下远程控制使用。

### 调试

若在使用中出现了问题，可在主界面下按 3 次播放按钮，调出调试菜单，可在菜单中查看日志以分析错误。
