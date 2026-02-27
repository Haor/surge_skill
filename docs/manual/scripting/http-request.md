Title: HTTP Request · GitBook

URL Source: https://manual.nssurge.com/scripting/http-request.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

### http-request

Uses a script to modify the HTTP request. The value field is a regular expression to match the request URLs.

The incoming parameters are $request:

*   `$request.url<String>`: Request URL.
*   `$request.method<String>`：Request HTTP method.
*   `$request.headers<Object>`：Request HTTP Headers.
*   `$request.body<String or Uint8Array>`：Request body. Only works when requires-body = true.
*   `$request.id<String>`: A unique ID for continuity among scripts.

The script must invoke $done() with an object. The object may contain:

*   `url<String>`: Use the new URL to overwrite the old one. Please note that it won't update the 'Host' field in the header as URL Rewrite does. You need to change it manually by returning a modified header object if necessary.
*   `headers<Object>`: Use the new headers to overwrite all the old headers. Please note that some fields may not be modified, such as 'Content-Length'.
*   `body<String or Uint8Array>`: Use the new body to overwrite the old one. Only works when requires-body = true.

*   `response<Object>`：If this object exists, Surge returns an HTTP response directly without making a real network operation. The object may contain:

    *   `status<Number>`: Response HTTP status code. (Optional. Default: 200)
    *   `headers<Object>`: Response HTTP Headers. (Optional)
    *   `body<String or Uint8Array>`: Response HTTP Body. (Optional)

You may use $done(); to abort the request without returning anything. Or use $done({}); to keep the request untouched.

Some limitations in the current version:

*   The request body may not be overwritten when using chunked encoding.
*   The request body may not be overwritten when 'Expect: 100-continue' exists in the header.

A simple example:

```
let headers = $request.headers;
headers['X-Modified-By'] = 'Surge';

$done({headers});
```
