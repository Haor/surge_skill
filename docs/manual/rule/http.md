Title: HTTP Rule · GitBook

URL Source: https://manual.nssurge.com/rule/http.html

Published Time: Tue, 20 Jan 2026 02:39:13 GMT

HTTP Rule
=========

There are two HTTP rule types. HTTP rule is for HTTP requests or HTTPS requests. It won't affect TCP connections.

#### USER-AGENT

```
USER-AGENT,Instagram*,DIRECT
```

Rule matches if the user agent of the request matches. Wildcard characters * and ? are supported.

#### URL-REGEX

`URL-REGEX,^http://google\.com,DIRECT`

Rule matches if the URL matches the regular expression.

You can append the `extended-matching` parameter to also test the HTTP Host header (or `:authority`) and SNI, which helps when TLS handshake information is needed:

```
URL-REGEX,^https://example\.com,Proxy,extended-matching
```
