Title: Surge Mac CLI · GitBook

URL Source: https://manual.nssurge.com/others/cli.html

Published Time: Tue, 20 Jan 2026 02:39:16 GMT

Surge Mac CLI
=============

Surge Mac provides a simple CLI program for easy control. You may find it in `/Applications/Surge.app/Contents/Applications/surge-cli`.

Use `--help` to get the latest manual.

```
Available commands:
  reload - Reload the main profile
  switch-profile <profile-name> - Switch to another profile

  stop - Shutdown Surge
  unattended-upgrade - Perform an unattended Surge upgrade if available

  dump active - Show all active connections
  dump request - Show recent connections
  dump rule - Show all effective rules
  dump policy - Show all proxies and policy groups
  dump dns - Show DNS caches
  dump profile [original / effective] - Show the original profile and the effective profile modified by modules
  dump event - Show events

  watch request - Keep tracing the new requests

  environment - Show environment settings
  set <key-path> <value> - Modify environment settings

  test-network - Test the network delay
  test-policy <policy-name> - Test a proxy
  test-all-policies - Test all proxies
  test-group <group-name> - Immediately retest a policy group

  kill <connection-id> - Kill a active connection
  flush dns - Flush DNS cache
  diagnostics - Run network diagnostics
  set-log-level <log-level> - Change log level without writing to the profile

  script evaluate <script-js-path> [mock-script-type] [timeout] - Load a script from a file and evaluate

Available parameters:
  --raw - Output the result in raw JSON format
  --remote/-r - Connect to a remote Surge instance instead of the local. e.g. --remote password@192.168.2.2:6170
```
