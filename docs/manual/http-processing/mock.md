Title: Mock (Map Local) · GitBook

URL Source: https://manual.nssurge.com/http-processing/mock.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

You may mock the HTTP server and return a static response. This feature may also be called Map Local or API Mocking. If you want to return a response dynamically, try scripting.

Example:

```
[Map Local]
^http://surgetest\.com/json data-type=text data="{}" status-code=500
^http://surgetest\.com/gif data-type=tiny-gif status-code=200
^http://surgetest\.com/file data-type=file data="data/map-local.json" header="a:b|foo:bar"
^http://surgetest\.com/base64 data="dGVzdA==" data-type=base64
```

### Parameters

#### URL Pattern

Each line is defined by multiple parameters, separated by space, the first of which is a regular expression for the URL. If an HTTP request (or a decrypted HTTPS request) matches this expression, then this rule is applied.

#### `data-type`

Surge currently supports four types of data

*   `file`: Returns the content of a specific file or URL.
*   `text`: Returns the text of the data field, encoded in UTF-8. iOS 5.9.1+Mac 5.5.1+
*   `tiny-gif`: Returns a 1px GIF. iOS 5.9.1+Mac 5.5.1+
*   `base64`: Returns binary data encoded in base64. iOS 5.9.1+Mac 5.5.1+

#### `data`

*   For `file` type, this field should be the path to the data file, with relative paths being relative to the configuration file's directory. In macOS, absolute paths can also be used.

*   For `text` type, this field is the content itself.

*   For `tiny-gif` type, this field is meaningless.

*   For `base64` type, this field should contain valid base64 data.

You can use `data-type=text data=""` to return an empty result.

This parameter allows you to customize the HTTP Header of the return result. Use `|` to separate multiple key-value pairs.

### About Content-Type

You can use the `header` field to control the Content-Type of the return result. If not provided, Surge will try to complete it as much as possible.

*   For `file` type, it will try to convert the file extension to MIME type. If it fails, `application/octet-stream` will be used.

*   For `text` type, `plain\text` is used by default.

*   For `tiny-gif` type, `image/gif` is used by default.

*   For `base64` type, `application/octet-stream` is used by default.
