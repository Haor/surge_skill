Title: Header Rewrite · GitBook

URL Source: https://manual.nssurge.com/http-processing/header-rewrite.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

Surge can rewrite the request or response header sent by the clients before they are forwarded to the server.

Example:

```
[Header Rewrite]
http-request ^http://example.com header-add DNT 1
http-request ^http://example.com header-del Cookie
http-request ^http://example.com header-replace User-Agent Unknown
http-response ^http://example.com header-replace-regex Date 2022 2023
```

The rewrite rule consists of several parts:

1.   HTTP direction: `http-request` or `http-response`. The old versions only support modifying the request and this part can be omitted, like this:

```
[Header Rewrite]
 ^http://example.com header-add DNT 1
```
2.   URL regular expression

3.   Action type
4.   Header field
5.   Value (not available for header-del)
6.   Replace template (only for header-replace-regex)

Append a new header line to the header, even if the header field already exists.

Example:

```
[Header Rewrite]
http-request ^http://example.com header-add DNT 1

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1
```

Delete a header line from the header.

Example:

```
[Header Rewrite]
http-request ^http://example.com header-del DNT

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
```

Replace a header value in the header. If the header field doesn't exist, nothing happens.

Example:

```
[Header Rewrite]
http-request ^http://example.com header-replace DNT 1

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 0

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1
```

If you would like to add or replace a header line whenever the field exists. You may use header-add and header-del together.

```
[Header Rewrite]
^http://example.com header-del DNT
^http://example.com header-add DNT 1
```

Replace a header value in the header with a regex expression and template. If the header field doesn't exist, nothing happens.

```
[Header Rewrite]
http-request ^http://example.com header-replace-regex User-Agent Safari Chrome

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 0

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Chrome/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 0
```
