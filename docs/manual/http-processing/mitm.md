Title: HTTPS Decryption · GitBook

URL Source: https://manual.nssurge.com/http-processing/mitm.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

HTTPS Decryption (Man-in-the-Middle Attack, MitM)
-------------------------------------------------

Surge may decrypt HTTPS traffic by MitM. Please see [Wikipedia article](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) for more information.

The certificate generator can help you generate a new CA certificate for debugging and make the certificate trusted by the system. It's available in Surge Dashboard (Mac version) and Surge iOS Config Editor. This certificate is generated locally and only saved in your profile file and the system Keychain. The key of the new certificate is generated randomly using OpenSSL.

You can also use an existing CA certificate. Export the certificate to PKCS#12 format (.p12) with a passphrase. Please note that the passphrase cannot be empty due to system limitations. Use the "base64" command to encode in the base64 string and append these settings below to your config file.

```
[MITM]
ca-p12 = MIIJtQ.........
ca-passphrase = password
hostname = *google.com
h2 = true
```

Surge only decrypts traffic to hosts declared here. A general configuration may be like this:

`hostname = -*.apple.com, -*.icloud.com, *`

> Some applications have a strict security policy to use pinned certificates or CA. Enabling decryption to these hosts may cause problems.

This parameter is of the Host List type, for detailed rules see: [Host List Parameter Type](https://manual.nssurge.com/others/host-list.html)

Options
-------

### skip-server-cert-verify (Boolean, Default: false)

Do not verify the certificate of the remote host while performing MITM.

### h2 (Boolean, Default: false)

MITM over HTTP/2: Decrypt HTTPS traffic with MITM over HTTP/2 protocol, which can improve the performance of concurrent requests.

### client-source-address

Use this parameter to enable the MITM function on some devices only.

*   It's a list parameter using commas as the separator.
*   You may specify a single IP address or use a CIDR block. Both IPv4 and IPv6 are supported.
*   You may use the `-` prefix to exclude some clients, e.g., `client-source-address = -192.168.1.2, 0.0.0.0/0`
*   If the parameter is not set, MITM is enabled for all clients. A equivalent to `client-source-address = 0.0.0.0/0, ::/0`
*   `127.0.0.1` should be included if you want to enable MITM for the current device. 
*   Since Surge Mac version 6.1.0, this parameter can use MAC addresses to match specific clients.

### auto-quic-block (Boolean, Default: true) iOS 5.8.0+Mac 5.4.0+

When a QUIC connection (i.e., HTTP/3) hits the MITM hostname list, it automatically blocks that QUIC connection, causing the connection to fall back to HTTP/2 or HTTP/1.1, so that it can be intercepted by MITM.
