Title: DNS · GitBook

URL Source: https://manual.nssurge.com/scripting/dns.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

### dns

Uses a script as a DNS resolver. The value field will be used as a name.

`dns dnspod script-path=dnspod.js`

Then add a line in [Host] section:

```
[Host]
example.com = script:dnspod
*.example.com = script:dnspod
```

The incoming parameter is $domain.

The script should return **one** of the followings:

*   `address<String>`: Use this IP address as a result. It must be a valid IPv4/IPv6 address in string.
*   `addresses<Array>`: Use multiple IP addresses as a result.
*   `server<String>`: Ask Surge to lookup the domain via a specified upstream DNS server. It must be a valid IPv4/IPv6 address in string.
*   `servers<Array>`: Ask Surge to lookup the domain via multiple specified upstream DNS servers.

When returning `address<String>` or `addresses<Array>`, an additional 'ttl' can also be returned, to add the result to cache and avoid repeated lookup. The unit is second.

Here is example, which uses the public HTTP DNS API of DNSPod as a resolver for Surge:

```
$httpClient.get('http://119.29.29.29/d?dn=' + $domain, function(error, response, data){
  if (error) {
    $done({}); // Fallback to standard DND query
  } else {
    $done({addresses: data.split(';'), ttl: 600});
  }
});
```
