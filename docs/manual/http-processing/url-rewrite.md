Title: URL Rewrite · GitBook

URL Source: https://manual.nssurge.com/http-processing/url-rewrite.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

URL Rewrite
===========

Surge can rewrite the request's URL with 2 different methods or reject certain requests by URL.

Example:

```
[URL Rewrite]
^http://www\.google\.cn http://www.google.com header
^http://yachen\.com https://yach.me 302
^http://ad\.com/ad\.png _ reject
```

The rewrite rule consists of three parts: regular expression, replacement, and type.

### Header Mode

Surge will modify the request header and redirect the request to another host if necessary. The client will not notice this rewrite action.

The "Host" field in the request header will be modified to match the new URL.

```
[URL Rewrite]
^http://www\.google\.cn http://www.google.com header
```

### 302 Mode

Surge will simply return a 302 redirect response. HTTPS requests can be redirected if MitM for the hostname is enabled.

```
[URL Rewrite]
^http://yachen\.com https://yach.me 302
```

### Reject Mode

Reject the request if the pattern is matched. The replacement parameter will be ignored. HTTPS requests will be rejected if MitM for the hostname is enabled.

```
[URL Rewrite]
^http://ad\.com/ad\.png _ reject
```
