# Surge Mac 重置

如果你在使用中遇到了问题，希望重置 Surge 的所有状态（或者希望完全的卸载 Surge）。请注意在 macOS 中删除应用并重新安装并不影响应用数据，请在关闭 Surge 后删除以下文件和目录，无需删除 App 重新安装。

```
~/Library/Preferences/com.nssurge.surge-mac.plist
~/Library/Preferences/com.nssurge.surge-dashboard.plist
~/Library/Application Support/com.nssurge.surge-mac
~/Library/Application Support/com.nssurge.surge-dashboard
~/Library/Application Support/Surge
~/Library/Caches/com.nssurge.surge-mac
```

也可以直接使用以下脚本

```bash
#!/bin/bash

defaults delete com.nssurge.surge-mac
defaults delete com.nssurge.surge-dashboard

rm -Rf ~/Library/Application\ Support/com.nssurge.surge-mac
rm -Rf ~/Library/Application\ Support/com.nssurge.surge-dashboard
rm -Rf ~/Library/Application\ Support/Surge
rm -Rf ~/Library/Caches/com.nssurge.surge-mac

```
