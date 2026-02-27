# Surge Ponte Guide

Surge Ponte is a private network between Surge Mac and iOS devices.

* No complicated configuration required.
* Surge automatically selects the most suitable channel for establishing a connection.
* Always end-to-end encrypted.
* Device information and encryption keys are synced through your iCloud, and your data will not pass through any third-party servers except for the proxy server you choose.

This article will help you get started with Surge Ponte.

### Understanding Ponte Types

Surge Mac can be used as both a Surge Ponte server and client, while Surge iOS can only be used as a Surge Ponte client.

When configuring Surge Mac as a Surge Ponte server, there are 3 different configuration methods.

1. Direct NAT traversal

Only available when the current network is in Full Cone NAT, the NAT type of the current network and the specific model of the router, ISP are related, and it is generally difficult to change.

2. NAT traversal via proxy

Can be used in any network situation, and needs the help of a proxy that supports UDP forwarding. (Please note that if you are using a paid proxy service, using Surge Ponte will also consume your traffic.)

3. Static port forwarding (advanced users)

If you have a public IP address and know how to configure the router, you can choose to configure static port forwarding.

### Configuring Surge Ponte on Surge Mac

1. Select "Overview" in the sidebar, and then turn on the Surge Ponte switch.
2. Click Next.
3. Wait for Surge to test the NAT type of the current network.
4. If the test result is:
   * Full Cone NAT (A): You can choose any method to set up Surge Ponte.
   * Other (B/C/D): You can choose NAT traversal via proxy, or if you have a public IP address and know how to configure the router, you can choose static port forwarding.
5. If you choose NAT traversal via proxy, please select a proxy that supports UDP relay (Snell/shadowsocks/Trojan/SOCKS5/WireGuard).
6. Surge will test if the proxy is qualified. The proxy server cannot be behind a NAT or firewall unless they have been properly configured to allow Full Cone NAT.
7. Choose a name for the current device, such as MyMacMini. The name is case insensitive and can only contain letters, numbers, underscores, and hyphens.
8. Turn on Surge Ponte on other devices. Configuring Surge iOS is very simple because it can only be used as a client.

### Using Surge Ponte

You can now access this device from any other device running Surge and logged into the same iCloud account. There are two ways to use it:

1. You can use the domain name `ponte-name.sgponte` (e.g. mymacmini.sgponte) to access services on this device, such as an HTTP server running on port 8080 of the device, which can be accessed directly on other devices at <http://mymacmini.sgponte:8080/>
2. You can also use the policy `DEVICE:PONTE-NAME` to use the device as a springboard to access other networks, such as a NAS in the intranet. Rule example:

```
IP-CIDR,192.168.30.0/24,DEVICE:MyMacMini
```

<details>

<summary><mark style="color:purple;">Use Case #1:</mark> With Surge Ponte and system file sharing services, you can access files on your Mac from your iOS device at any time.</summary>

1. Turn on Surge Ponte on Surge Mac, and name it macbook.
2. In macOS system settings, find General > Sharing > File Sharing, and turn on the switch.
3. Turn on Surge iOS on your iOS device, and make sure you can see the Mac device in the Surge Ponte interface.
4. Open the built-in "Files" app on your iOS device, switch to the "Browse" page, click the More button in the top right corner, and select Connect to Server.
5. Enter macbook.sgponte, and click Next.
6. Choose Registered User, and enter your Mac username and login password.

</details>

<details>

<summary><mark style="color:purple;">Use Case #2:</mark> Access devices in home network with Surge's DNS mapping feature without configuring rules for the entire subnet.</summary>

1. Enable Surge Ponte on Surge Mac, named `macbook` here.
2. Configure DNS mapping on Surge Mac: `nas.myhome = 192.168.1.20`, where the IP address and name are for the device to be accessed.
3. Configure rules on the client device: `DOMAIN-SUFFIX,myhome,DEVICE:macbook`. Note that since this domain name cannot be resolved on the client device, this rule must be placed before any IP-related rules that trigger resolution.
4. Access `nas.myhome` through a browser.

</details>

### Client-side Proxy

A proxy can also be configured on the client side to access the Ponte server. This is not necessary even if the server is configured with a proxy NAT traversal, but configuring a proxy can help overcome UDP traffic blocking in certain network environments.

For example, due to severe UDP packet loss during network peak hours for outbound traffic from mainland China, it is best for the client to also configure the use of the same proxy to access Ponte devices if a foreign proxy is used for NAT traversal.

<figure><img src="https://856006905-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FqrBG3qqNVELxHgiBGHTv%2Fuploads%2FenUga9dUTT4v9RWWLmqj%2Fponte-nat.png?alt=media&#x26;token=d6dae434-7680-4395-9247-c3d4b0e79388" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Vector is the underlying proxy protocol used by Surge Ponte services.
{% endhint %}

### Tips

1. You can set the internal network segment to an uncommon subnet address, such as 192.168.150.0/24, to ensure that there are no address conflicts when accessing the internal network from other networks.
2. When the Ponte client and server are on the same LAN, the connection will be automatically established through the LAN and will not use NAT traversal or proxy servers.
3. When the Ponte device name being accessed is the current device, the strategy will be converted to the DIRECT strategy.
4. When accessing through `ponte-name.sgponte`, a `DEVICE:ponte-name` strategy is dynamically created and used, and `ponte-name.sgponte` is resolved to 127.0.0.1 on the remote end. Therefore, even services listening on 127.0.0.1 can be accessed.
5. The `DEVICE:NAME` strategy can be used directly without being declared in `[Proxy]`, and can also be used as a sub-strategy in `[Proxy Group]`, such as in conjunction with Subnet Group.
6. Currently, Surge Ponte only supports establishing connections through IPv4, but can forward IPv6 requests.
