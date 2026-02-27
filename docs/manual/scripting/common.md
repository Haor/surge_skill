Title: Basic · GitBook

URL Source: https://manual.nssurge.com/scripting/common.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

_Scripting requires Surge iOS 4 or Surge Mac 3.3.0_

Scripting
---------

You may use JavaScript to extend the ability of Surge as you wish.

Script Section
--------------

```
[Script]
script1 = type=http-response,pattern=^http://www.example.com/test,script-path=test.js,max-size=16384,debug=true
script2 = type=cron,cronexp="* * * * *",script-path=fired.js
script3 = type=http-request,pattern=^http://httpbin.org,script-path=http-request.js,max-size=16384,debug=true,requires-body=true
script4 = type=dns,script-path=dns.js,debug=true
```

Each line has two components: script name and parameters. Common parameters:

*   `type`: The type of script: `http-request`, `http-response`, `cron`, `event`, `dns`, `rule`, `generic`.
*   `script-path`: The path of the script, can be a relative path to the profile, an absolute path, or a URL.
*   `script-update-interval`: The update interval while using an URL for script-path, in seconds. 
*   `debug`: Enabling the debug mode, which has several effects:
    1.   The script is loaded from the filesystem every time before evaluating it. (Surge Mac only)
    2.   For `http-request` and `http-response` scripts, when you use `console.log()` to log messages, the messages also appear in the request's notes.

*   `timeout`: The longest-running time for the script. The default value is 5s.
*   `argument`: The script may fetch the value with `$argument`.
*   `engine`: Refer to the latter half of this article.

Parameters for `http-request` and `http-response`:

*   `pattern`: The regex pattern to match the URL.

*   `requires-body`: This allows the script to modify the request/response body. The default value is false. This behavior is expensive. Only enable when necessary.

*   `max-size`: The maximum allowed size for the request/response body. The default value is 131072 (128KB).

*   `binary-body-mode`: Only available in iOS 15 and macOS. The raw binary body data will be passed to the script in Uint8Array instead of a string value.

Scripting requires Surge to load the entire response body data to memory. A huge response body may cause Surge iOS to crash since the iOS system limits the maximum amount of memory the Network Extension can occupy.

Please only enable scripting for necessary URLs.

If the response body size exceeds the `max-size` value, Surge fallbacks to passthrough mode and skips scripting for this request.

Basic Constraints
-----------------

Scripts allow asynchronous operations. $done(value

Performances
------------

You don't need to worry about the performance of scripting. The JavaScript core is notably effective.

Public API
----------

### Basic Information

*   **`$network`**

The object contains the detail of the network environment.

*   **`$script`**

    *   `$script.name<String>`: The script name which is being evaluated.
    *   `$script.startTime<Date>`: The time when the current script starts.
    *   `$script.type<String>`: The type of the current script.

*   **`$environment`**

    *   `$environment.system<String>`: iOS or macOS.
    *   `$environment.surge-build<String>`: The build number of Surge.
    *   `$environment.surge-version<String>`: The short version number of Surge.
    *   `$environment.language<String>`: The current UI language of Surge.
    *   `$environment.device-model<String>`: The current device model. iOS 5.9.0+Mac 5.5.0+

### Persistent Store

*   **`$persistentStore.write(data<String>, [key<String>])`**

Save data permanently. Only a string is allowed. Return true if successes.

*   **`$persistentStore.read([key<String>])`**

Get the saved data. Return a string or Null.

If the key is undefined, the script with the same script-path shares the storage pool. Data can be shared among different scripts when using a key.

Tips: Surge Mac writes the $persistentStore data to the directory `~/Library/Application Support/com.nssurge.surge-mac/SGJSVMPersistentStore/`. You may edit the files here directly for debugging.

### Control Surge

*   **`$httpAPI(method<String>, path<String>, body<Object>, callback<Function>(result<Object>))`**

You may use $httpAPI to call all HTTP APIs to control Surge's functions. No authentication parameters are required. See the HTTP API section for the available abilities.

### $httpClient

*   **`$httpClient.post(URL<String> or options<Object>, callback<Function>)`**

Start an HTTP POST request. The first parameter can be a URL or object. An example object may look like that.

```
{
  url: "http://www.example.com/",
  headers: {
    Content-Type: "application/json"
    },
  body: "{}",
  timeout: 5
}
```

When using an object as an option list. The `url` is required. If the `headers` field exists, it overwrites all existing header fields. `body` can be a string or object. When presenting an object, it is encoded to JSON string, and the 'Content-Type' is set to `application/json`.

#### callback

callback: callback(error, response

When successful, the error is null, and the response object contains `status` and `headers` properties.

Similar function: **$httpClient.get**, **$httpClient.put**, **$httpClient.delete**, **$httpClient.head**, **$httpClient.options**, **$httpClient.patch**.

#### Options

*   `timeout`: The default timeout is 5 seconds. You may override it with this option.
*   `insecure`: If this option is set to true, https requests will not verify the server certificate. iOS 5.9.0+Mac 5.5.0+
*   `auto-cookie`: Control whether to automatically process Cookie-related fields and store them, enabled by default. If turned off, the Cookie header is passed as a normal field. iOS 5.9.0+Mac 5.5.0+
*   `auto-redirect`: Control whether to automatically redirect requests when encountering 30x HTTP status codes, enabled by default. iOS 5.9.0+Mac 5.5.0+

##### Policy

You may specify a policy to perform the request:

*   `policy`: Use an existing policy with its name.
*   `policy-descriptor`: Use a temporary policy with a full descriptor.

#### Binary Data iOS 5.4.1+Mac 5.0.1+

You may pass a TypedArray object as a body.

Also, you may use the `binary-mode` parameter to let Surge return response data in TypedArray instead of String.

```
{
  url: "http://www.example.com/",
  binary-mode: true
}
```

### Utilities

*   **`console.log(message<String>)`**

Log to Surge logfile.

*   **`setTimeout(function[, delay])`**

Same as the setTimeout in browsers.

*   **`$utils.geoip(ip<String>)`**

Perform a GeoIP lookup. The results are in the ISO 3166 code.

*   **`$utils.ipasn(ip<String>)`**

Look up the ASN of the IP address.

*   **`$utils.ipaso(ip<String>)`**

Look up the ASO of the IP address.

*   **`$utils.ungzip(binary<Uint8Array>)`**

Decompress gzip data. The result is also a Uint8Array.

*   **`$notification.post(title<String>, subtitle<String>, body<String>[, options<Object>])`**

Post a notification.

Available options: iOS 5.11.0+Mac 5.7.0+

*   `action`: The operation after opening Surge through clicking the notification.

    *   `open-url`: Opens a URL, the specific URL is provided by the `url` parameter.

    *   `clipboard`: Copies content to the clipboard (will be confirmed by user), content is given through the `text` parameter.

*   `media-url`: Provides media content for the notification, such as an image. The content should be a valid URL.

*   `media-base64`: Same function as above, but the content is directly provided by base64. It requires providing the MIME type of the content with the `media-base64-mime` parameter.

*   `auto-dismiss`: Automatically dismisses this notification after a specified period of time, in seconds, defaulting to 0, meaning it persists indefinitely.

*   `sound`: Uses default push message sound when popping up notifications.

### Manually Trigger

You can manually trigger a script on Surge iOS by long pressing on the script or using the system Shortcuts app.

If you use Shortcuts to trigger a script, you may optionally pass a parameter to the script and use the `$intent.parameter` to retrieve it.

Script Engine iOS 5.9.0+Mac 5.5.0+
----------------------------------

Surge currently contains two JavaScript script evaluating engines.

### JavaScriptCore (`engine=jsc`)

*   Advantages:
    1.   The engine initializes quickly, and the overhead when calling is low (low latency).

*   Disadvantages:
    1.   Since JSC runs inside the NE process, it will cause the memory usage of the Surge NE process to increase significantly, possibly leading to system termination due to exceeding memory limits.

### WebView (`engine=webview`)

*   Advantages:

    1.   Since the actual running environment of WebView is another independent process, the execution of the script has almost no impact on the memory usage of the NE process, and it will not cause the Surge NE process to be terminated due to memory usage issues.
    2.   The JS execution environment of WebView can use JIT, which greatly improves the execution efficiency for complex or CPU-intensive scripts.
    3.   WebAPI can be used.

*   Disadvantages:

    1.   The engine's initialization time overhead is slightly higher
    2.   When it is necessary to transfer a large amount of data between the script and Surge, due to cross-process communication, the efficiency is lower, which is more apparent when using binary-body-mode to process larger requests.

### Usage Recommendations

1.   For small, frequently called, simple scripts, such as Rule, DNS type scripts, it is recommended to use JSC.
2.   For complex, high-memory scripts (such as parsing JSON of MB-level HTTP body), it is recommended to use WebView.

### Configuration Method

Add the parameter: `engine` to the script configuration line, which can be configured as `auto`, `jsc`, `webview`.

*   The default is `auto`, always using WebView where available.
*   If the WebAPI is used in the script, it should be explicitly configured as `webview` so that when the script is executed in an environment that does not support WebView, users will be prompted.

### Engine Availability

*   iOS: JSC and WebView
*   macOS
    *   macOS 10.15 and below: only JSC
    *   macOS 11.0 and above: JSC and WebView

*   tvOS: only JSC
