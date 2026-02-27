Title: External Proxy Program · GitBook

URL Source: https://manual.nssurge.com/policy/external-proxy.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

External Proxy Program Mac Only
-------------------------------

Surge Mac supports the External Proxy Program policy, which allows Surge to work more easily with other proxy software.

The following is an example of ssh.

First, the policy keyword type is `external`.

```
[Proxy]
external = external, exec = "/usr/bin/ssh", args = "11.22.33.44", args = "-D", args = "127.0.0.1:1080", local-port = 1080, addresses = 11.22.33.44
```

The `args` and `addresses` parameters are optional, `exec` and `local-port` are required. `args` and `addresses` fields can be repeatedly used for appending.

Surge will do the following:

1.   When the policy is used, Surge starts the external process with the exec and args parameters, and later forwards the request to SOCKS5 127.0.0.1:[local-port].
2.   If the external process is terminated, it will be restarted automatically when the policy is used.
3.   Surge automatically excludes the addresses in the addresses parameter from the VIF routes when Enhanced Mode is on. (so please fill in the proxy server IP address in this field. Hostname and domain are not supported.)
4.   Surge always uses the DIRECT policy for requests from external processes. (In order to deal with plug-in programs like obfs-local, children of external processes are handled similarly)
5.   Automatically shut down all external processes when Surge exits, and automatically clean up the route table items when the Enhanced Mode shuts down.

Some notes:

1.   The functions of 3 and 4 above are overlapping, please use the addresses declaration to exclude VIF processing, which can reduce processing overhead, the function of 4 is for additional protection.
2.   stdout and stderr of external processes are redirected to /tmp/Surge-External-xxxxxx.log for troubleshooting.
3.   Since external processes may take a little time to start. If a connection refused error is encountered when forwarding to 127.0.0.1:[local-port], Surge will automatically retry after 500ms, up to 6 times per request.
4.   Surge iOS will be treated as the external policy as REJECT since it's not supported.
