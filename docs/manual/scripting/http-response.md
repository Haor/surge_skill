Title: HTTP Response · GitBook

URL Source: https://manual.nssurge.com/scripting/http-response.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

### http-response

Use a script to modify the HTTP response. The value field is a regular expression to match the request URLs.

The incoming parameters are $request and $response:

*   `$request.url<String>`: Request URL.
*   `$request.method<String>`：Request HTTP method.
*   `$request.id<String>`: A unique ID for continuity among scripts.
*   `$request.headers<Object>`：Request HTTP headers.
*   `$response.status<Number>`: Response HTTP status code.
*   `$response.headers<Object>`: Response HTTP headers.
*   `$response.body<String or Uint8Array>`: Response HTTP body, decoded to string with UTF-8 if binary-mode isn't set. Only exists when requires-body = true.

The script must invoke $done() with an object. The object may contain:

*   `body<String or Uint8Array>`: Use the new body to overwrite the old one. Only works when requires-body = true.
*   `headers<Object>`: Use the new headers to overwrite all the old headers. Please note that some fields may not be modified, such as 'Content-Length'.
*   `status<Number>`: Use the new status code to overwrite the old one.

You may use $done(); to abort the request without returning anything. Or use $done({}); to keep the response untouched.

A simple example:

```
let headers = $response.headers;
headers['X-Modified-By'] = 'Surge';

$done({headers});
```
