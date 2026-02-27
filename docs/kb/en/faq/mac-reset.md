# Surge Mac Reset

If you encounter issues while using Surge and want to reset all states (or wish to completely uninstall Surge), please note that deleting the application and reinstalling it on macOS does not affect application data. After closing Surge, please delete the following files and directories without needing to delete and reinstall the App.

```
~/Library/Preferences/com.nssurge.surge-mac.plist
~/Library/Preferences/com.nssurge.surge-dashboard.plist
~/Library/Application Support/com.nssurge.surge-mac
~/Library/Application Support/com.nssurge.surge-dashboard
~/Library/Application Support/Surge
~/Library/Caches/com.nssurge.surge-mac
```

You can also use the following script directly

```bash
#!/bin/bash

defaults delete com.nssurge.surge-mac
defaults delete com.nssurge.surge-dashboard

rm -Rf ~/Library/Application\ Support/com.nssurge.surge-mac
rm -Rf ~/Library/Application\ Support/com.nssurge.surge-dashboard
rm -Rf ~/Library/Application\ Support/Surge
rm -Rf ~/Library/Caches/com.nssurge.surge-mac
```
