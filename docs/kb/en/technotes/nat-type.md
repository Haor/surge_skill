# NAT Types

When performing UDP forwarding, different forwarding mapping policies can lead to variations in UDP penetration capabilities. This variation is commonly referred to as **NAT Type**.

The naming of NAT types may vary across different software and documents, but they are generally categorized into the following types:

* **Type A**: Full Cone NAT (also known as Type 1 or Open)
* **Type B**: Address Restricted Cone NAT (also known as Type 2 or Moderate)
* **Type C**: Port Restricted Cone NAT
* **Type D**: Symmetric NAT

The NAT type is primarily determined by your **router**, but it may also be restricted by your **Internet Service Provider (ISP)**.

***

### Impact of Surge on NAT Types

When Surge is enabled and takes over the network through its VIF, an additional layer of conversion affects the NAT type. Specifically:

* If the original network is a **Type A Full Cone NAT**, Surge will downgrade it to a **Type B Address Restricted Cone NAT**.
* If the original network is at or below Type B, then the NAT type remains unchanged.

This change not only affects all processes on this machine but also applies to other devices taken over through gateway mode.

To avoid downgrading the level of your NAT (e.g., ensuring online gaming connectivity), you can resolve this issue by configuring the **`always-real-ip`** parameter. When configuring, ensure that this parameter covers relevant STUN domain names (you can confirm specific domain names via Surge's request list).

Surge Mac's built-in **Game Console STUN** module has pre-configured settings for common game console STUN domains:

```
always-real-ip = *.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com
```

For a more aggressive approach, you can use this configuration to cover most SUN servers without noticeable side effects:

```
always-real-ip = *stun*
```

### Using Proxies with Different NAT Types

When requests are processed through a proxy policy, their corresponding level of NAT depends on the proxy server's own type rather than that of your local network. You can test a proxy server’s level using Surge Mac’s Proxy Diagnosis feature (located in Window Menu › Proxy Diagnosis).

### Requirements for Surge Ponte Regarding Network Address Translation

If you wish to use Surge Ponte without relying on proxy servers, your local network needs to be Type A Full Cone Nat; both your router and ISP must support this configuration.

If penetrating via a proxy server instead relies solely upon said server’s own translation characteristics—if self-maintained typically setting firewall rules allowing all port-bound UDP traffic suffices.

### Is Surge's NAT Type Test Accurate?

All NAT type testing tools rely on sending different STUN requests and observing whether responses are received to make a judgment. If the network packet loss is severe, or the STUN server is abnormal, the test results may be lower than expected. Surge sends multiple requests during testing to ensure the test results are as accurate as possible.
