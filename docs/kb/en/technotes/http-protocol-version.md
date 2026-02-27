# HTTP Protocol Version

### Possible HTTP Versions

1. HTTP/1.0: Almost extinct now, with only a few websites still using it. But it is essentially not much different from HTTP/1.1.
2. HTTP/1.1: The most widely used HTTP protocol version. When accessing non-https\:// websites, the HTTP/1.x protocol is definitely used.
3. HTTP/2: Gradually becoming the mainstream HTTP protocol version. Must be used with https, i.e., TLS. The biggest improvement over HTTP/1.x is the support for multiplexing requests.
4. HTTP/3: The latest HTTP specification, officially finalized on June 9, 2022, but many websites based on previous draft versions already exist on the Internet. The biggest difference from previous versions is that HTTP/3 is based on UDP rather than TCP.

### How browsers and servers generally negotiate HTTP versions (i.e., without Surge intervention)

1. When accessing non-https\:// websites, HTTP/1.1 is definitely used.
2. When accessing https\:// websites, during the TLS handshake phase, the browser will inform the server of its preference for the `h2` protocol through the ALPN (Application-Layer Protocol Negotiation) extension of TLS. If the server supports HTTP/2, it will notify the client in the TLS handshake response. Afterward, the browser and server start using HTTP/2 on the TLS layer. If the server does not indicate support for `h2`, it will fall back to HTTP/1.1.
3. The HTTP Response Header returned by the server may contain the `Alt-Svc` field, indicating that the website supports other protocols, such as `Alt-Svc: h3=":443"`, which means that the service also supports the HTTP/3 protocol on port 443. The browser will use the HTTP/3 protocol for the next request (specific strategies are determined by the browser's logic, and different browsers may have different strategies).
4. Therefore, even if a website supports HTTP/3, it must first connect using HTTP/2 or 1.1 when accessed for the first time, and then upgrade to HTTP/3 after reading the Alt-Svc field.
5. To solve this problem, the SVCB/HTTPS RRs DNS record was added. The browser prefers to query this record rather than the A/AAAA record when accessing. The record will indicate the specific protocol versions supported by the server and the access points for each version. Thus, it can connect directly using HTTP/3.

### Differences in strategies of different browsers

Different browser implementations have inconsistencies in HTTP version negotiation. For example, Chrome always prioritizes using the HTTP/3 protocol when it is available and falls back to HTTP/2 when it fails. Safari, on the other hand, tries to use HTTP/2 and HTTP/3 concurrently and prefers the connection that completes the connection establishment process first. This may cause Safari to often or never use HTTP/3 during testing.

### The impact of Surge activation on HTTP protocol version negotiation

1. When MITM is in effect

If MITM is effective for a connection, Surge will completely take over the HTTP protocol stack. Surge supports communicating with the client using HTTP/1.1 or HTTP/2.

When the MITM via HTTP/2 switch is turned on in the configuration (`h2=true`), Surge will accept the client's h2 ALPN, otherwise, it will fall back to HTTP/1.1.

* If HTTP/1.1 is used for takeover, the handshake with the real server will not send h2 ALPN, forcing the use of HTTP/1.1.
* If HTTP/2 is used for takeover
