Title: Process Rule · GitBook

URL Source: https://manual.nssurge.com/rule/process.html

Published Time: Tue, 20 Jan 2026 02:39:13 GMT

Process Rule
============

You may assign a policy for a specified process. Process rule is available for Surge Mac only, Surge iOS ignores these rules.

#### PROCESS-NAME Mac Only

```
PROCESS-NAME,Telegram,Proxy
```

Rule matches if the process name of the request matches. Wildcard characters * and ? are supported.

> You may specify the filename or the full path of the executable file. For the macOS application package, it is in the path .app/Contents/MacOS.
