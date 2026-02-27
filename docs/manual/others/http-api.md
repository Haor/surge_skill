Title: HTTP API · GitBook

URL Source: https://manual.nssurge.com/others/http-api.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

HTTP API iOS 4.4.0+Mac 4.0.0+
-----------------------------

You may use HTTP API to control Surge.

Configuration
-------------

```
[General]
http-api = examplekey@0.0.0.0:6171
http-api-tls = false
```

Authentication
--------------

The API key must be filled in the 'X-Key' header for all requests.

```
GET /v1/events
X-Key: examplekey
Accept: */*
```

In some specific situations, if it is not convenient to set the header, you can also pass it through the URL query. For example, directly downloading the CA certificate through a browser.

```
http://127.0.0.1:6171/v1/mitm/ca?x-key=examplekey
```

HTTPS(TLS)
----------

Setting `http-api-tls = true` can enable HTTPS support for the HTTP API service. Surge will use the CA certificate of MITM to generate the server certificate for the corresponding access address.

Basic Constraints
-----------------

Only HTTP without TLS is currently supported. Surge only uses GET and POST methods.

*   For GET method, you should use URL queries to send parameters.
*   For POST method, you should use JSON body to send parameters.

Surge will always return a JSON body as a response.

Paths
-----

### Toggle capabilities

*   GET /v1/features/mitm
*   POST /v1/features/mitm
*   GET /v1/features/capture
*   POST /v1/features/capture
*   GET /v1/features/rewrite
*   POST /v1/features/rewrite
*   GET /v1/features/scripting
*   POST /v1/features/scripting
*   GET /v1/features/system_proxy (Surge Mac Only)
*   POST /v1/features/system_proxy (Surge Mac Only)
*   GET /v1/features/enhanced_mode (Surge Mac Only)
*   POST /v1/features/enhanced_mode (Surge Mac Only)

Use GET method to obtain the state of a capability.

GET Response example:

```
{"enabled":true}
```

Use POST method to adjust the state of a capability.

POST Request example:

```
{"enabled":true}
```

### Outbound Mode

*   GET /v1/outbound
*   POST /v1/outbound

Use GET to obtain the outbound mode, and use POST to change it.

GET Response example:

```
{"mode":"rule"}
```

POST Request example:

```
{"mode":"rule"}
```

Possible modes: direct, proxy, rule

*   GET /v1/outbound/global
*   POST /v1/outbound/global

Obtain or change the default policy for global outbound mode.

GET Response example:

```
{"policy":"ProxyA"}
```

POST Request example:

```
{"policy":"ProxyB"}
```

### Proxy Policy

*   GET /v1/policies

List all policies.

*   GET /v1/policies/detail?policy_name=ProxyNameHere

Obtain the detail of policy.

*   POST /v1/policies/test

Test policies with a URL.

Request example:

```
{"policy_names": ["ProxyA", "ProxyB"], "url": "http://bing.com"}
```

*   GET /v1/policy_groups

List all policy groups and their options.

*   GET /v1/policy_groups/test_results

Obtain the test result of a url-test/fallback/load-balance group.

*   GET /v1/policy_groups/select?group_name=GroupNameHere

Obtain the option of a select group.

Response example:

```
{"policy": "ProxyA"}
```

*   POST /v1/policy_groups/select

Change the option of a select group.

Request example:

```
{"group_name": "GroupA", "policy": "ProxyA"}
```

*   POST /v1/policy_groups/test

Test a group immediately.

Request example:

```
{"group_name": "GroupA"}
```

Response example:

```
{
    "available": [
        "ProxyA",
        "ProxyB"
    ],
}
```

### Requests

*   GET /v1/requests/recent

List recent requests.

*   GET /v1/requests/active

List all active requests.

*   POST /v1/requests/kill

Kill an active request.

Request example:

```
{"id": 100}
```

### Profiles

*   GET /v1/profiles/current?sensitive=0

Obtain the text content of the current profile. If 'sensitive' is false, all passwords field will be masked.

*   POST /v1/profiles/reload

Execute profile reloading immediately.

*   POST /v1/profiles/switch (Surge Mac Only)

Request example:

```
{"name": "Profile2"}
```

Switch to another profile.

*   GET /v1/profiles Mac Only 4.0.6+

Get all available profile names.

*   POST /v1/profiles/check Mac Only 4.0.6+

Request example:

```
{"name": "Profile2"}
```

Check the profile. If the profile is invalid an error will be returned. Otherwise the "error" field will be null.

### DNS

*   POST /v1/dns/flush

Flush the DNS cache.

*   GET /v1/dns

Obtain the current DNS cache content.

*   POST /v1/test/dns_delay

Test the DNS delay.

Modules
-------

*   GET /v1/modules

List the available and enabled modules.

Response example:

```
{
    "enabled": [
        "router.com"
    ],
    "available": [
        "Game Console SNAT",
        "Google Home Devices",
        "router.com",
        "MitM All Hostnames"
    ]
}
```

*   POST /v1/modules

Enable or disable modules.

Request example:

```
{
    "router.com": false,
    "Google Home Devices": true
}
```

### Scripting

*   GET /v1/scripting

List all the scripts.

*   POST /v1/scripting/evaluate

Evaluate a script with a mock environment.

Request example:

```
{
    "script_text": "The content of JS script",
    "mock_type": "cron",
    "timeout": 5
}
```

*   POST /v1/scripting/cron/evaluate

Evaluate a cron script immediately.

Request example:

```
{
    "script_name": "script1",
}
```

### Device Management Mac Only 4.0.6+

*   GET /v1/devices

Obtain the list of the current active and saved devices.

*   GET /v1/devices/icon?id={iconID}

Obtain the icon of a device. You may get the iconID from device.dhcpDevice.icon.

*   POST /v1/devices

Change the device properties. `physicalAddress` field is required. And you may adjust multiple or one property from `name`, `address`, and `shouldHandledBySurge`.

Request example:

```
{
    "physicalAddress":"F0:9F:C2:00:00:00",
    "name": "Computer",
    "address": "192.168.1.200",
    "shouldHandledBySurge": true
}
```

### Misc

*   POST /v1/stop

Shutdown Surge engine. If Always On is enabled on Surge iOS, the Surge engine will restart.

*   GET /v1/events

Obtain the content of the event center.

*   GET /v1/rules

Obtain the list of rules.

*   GET /v1/traffic

Obtain traffic information.

*   POST /v1/log/level

Change the log level for the current session.

Request example:

```
{"level": "verbose"}
```

*   GET /v1/mitm/ca

Obtain the CA certificate for MITM, in DER binary format. (Certificate only, no private key included)
