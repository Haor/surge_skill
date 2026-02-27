Title: SSH · GitBook

URL Source: https://manual.nssurge.com/policy/ssh.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

You may use SSH protocol as a proxy policy, an equivalent to `ssh -D`.

Profile syntax:

*   Password authentication

```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw
```

*   Public key authentication

```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, private-key=key1

[Keystore]
key1 = type=openssh-private-key, base64=[The base64 encoded content of the private key file]
```

*   Please note you must use base64 to encode the entire private key file again, even though the private key file uses the base64 encoding itself.

*   All four types of private keys, RSA/ECDSA/ED25519/DSA, are supported.

*   Surge only supports `curve25519-sha256` as the kex algorithm and `aes128-gcm` as the encryption algorithm. It means that the SSH server must use OpenSSH v7.3 or above. (It should not be a problem since OpenSSH 7.3 was released on 2016-08-01.)

*   You may specify the idle timeout parameter now. The default value is 180s.

```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw, idle-timeout=180
```

Server Fingerprint
------------------

To cope with MITM attacks, you can specify the server's public key fingerprint with `server-fingerprint`, which ensures that only legitimate servers are connected.

```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw, idle-timeout=180, server-fingerprint = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBk2No6KBq2m9VTCcHXXJBX4/A3RNr+L+yDBl5+TF9qz"
```

As there may be multiple public keys for a server, the `server-fingerprint` parameter supports configuring multiple fingerprints.

```
server-fingerprint = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBk2No6KBq2m9VTCcHXXJBX4/A3RNr+L+yDBl5+TF9qz,ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD7aoFCymj8NJL+xMqYzRLGpIfVd2sebgtnD3cplG7/lrvPGYIpRAOkKqdUBOkRd2x68JFe0u+gBHQxFkv8o81Saqr6qxcrq4mPiyqxOTRkvDMtYrjJ4AJZE26nCzHRCC7Ji6Mq2OtepTJcC9uk2LLcRrF3G05qu6ToeK1LgXgqc+b2RLOQJ1AXEeNgn0NIXWlBv4AhQRJ6fFQi4HO/jkxpFNfzKY+dPDx6P3VAazYa2nl8wpLbXt+tq6SBv8RctwDuYszAbjSCPPJq7ToX/Svqqbl82qtOLOofcQ8/f8809i4RQ0yuEpVLnVVWd7cZx5h45vt+/I1Ifr2pS7BqhLL/,ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLdhR3D2BvyD7FTXfx0CrjZF2tVgoVRFi1poGKoX0eXc9OlpiaqNos4niiN0GWyoT4mL724cgvaL+vHW8sTZE5A="
```

If the server's sshd supports ed25519, only the fingerprint of ssh-ed25519 is needed.

You may obtain the server fingerprint from `~/.ssh/known_hosts` file. Or you may use the command `ssh-keyscan example.com` in a trusted network environment to fetch. Please remove the hostname in the front of the line before copying it to Surge.
