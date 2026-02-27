# Surge Gateway Mode Configuration Guide

Surge can function as a network gateway to take over all network traffic from other devices within the local area network. This feature is commonly referred to as a "bypass router" or "transparent gateway."

### Operating Modes

Surge Mac provides two gateway modes:

1. **Enhanced Mode (Surge VIF)**: Utilizes Surge's virtual network interface as the gateway.
2. **Surge VM Gateway**: Offers better performance and more features, but cannot run concurrently with bridge modes of other virtual machine software (such as Parallels Desktop, VMware Fusion). This mode is only available on Surge Mac 6.0 and above.

{% hint style="info" %}
Enhanced Mode can also be used to take over network requests of the current device, while the VM Gateway can only be used to take over requests from other devices.
{% endhint %}

## Configuration Steps

1. Enable "Enhanced Mode" or "VM Gateway" in Surge Mac.
2. On the device to be taken over, go to its network settings.
3. Change its **gateway address** to the IP address of the device running Surge Mac (if using VM Gateway, set it to the IP address of the VM Gateway).
4. Change its **DNS server** address to **`198.18.0.2`**.

{% hint style="danger" %}
**Note**: The DNS address should be **`198.18.0.2`**, not `192.168.x.x`.
{% endhint %}

Once these steps are completed, Surge will start taking over network traffic of the device.

### Automated Configuration (Surge DHCP)

You can use Surge's DHCP feature to automatically configure network settings for clients and achieve automatic takeover.

**Before using this feature, please note:**

1. **Basic Knowledge**: You need to have a basic understanding of how DHCP works.
2. **DNS Configuration**: At least one valid upstream DNS server must be set in Surge's profile.
3. **Disable Existing DHCP**: You must disable other DHCP servers in your current network (usually provided by the main router).
4. **Wired Connection**: The Mac running Surge should use a wired network connection—using Wi-Fi is strongly discouraged.
5. **Static IP**: The Surge Mac itself must use a static IP. When DHCP is enabled, Surge will automatically set the network to use a static IP.
6. **Stability**: After enabling this feature, do not move or turn off the Mac running Surge at will, or you may disrupt the entire network.
7. **Emergency Recovery**: If you experience network issues, turn off Surge DHCP and re-enable the main router's DHCP service to restore the network.

By default, new devices joining the network will not be automatically taken over. You can right-click the target device in Surge's device list and select "Use Surge as Gateway." To automatically take over all new devices, check the "Use Surge as Gateway by default" option in the gateway mode settings.

{% hint style="danger" %}
**Compatibility Tip**: Due to the implementation of Surge Gateway Mode, there may be compatibility issues with certain devices. It is recommended to only enable this feature for devices that need to be taken over.
{% endhint %}

### IPv6 RA Override

In networks with IPv6 present, only modifying IPv4 settings via DHCP may result in incomplete traffic takeover. Surge Mac 6.0 introduces IPv6 RA (Router Advertisement) override functionality to ensure IPv6 traffic is also properly taken over.

* This feature does not affect the IPv6 address assignment of clients.
* If the main router's RA message priority is set to "High," Surge may not be able to successfully override it. Please adjust the router's RA priority to "Normal" or "Low."

{% hint style="info" %}
If you are not using IPv6, you can also disable IPv6 for the entire network directly in your router's settings.
{% endhint %}

### FAQ & Troubleshooting

#### Q: Why does the request viewer only display IP addresses instead of domain names?

**A:** This is because the client's DNS is not properly set to `198.18.0.2` or `fd00:6152::2`, causing Surge to be unable to map IP addresses back to domains through its Fake IP mechanism.

**Solutions:**

1. **Check Settings**: Verify if the client DNS settings are correct.
2. **Force DNS Hijack**: For devices that cannot manually change DNS, check the "Hijack all UDP DNS queries sent to port 53" option in Surge Gateway Mode settings. This option resolves most issues.
3. **Handle IPv6 RA DNS**: In some cases, even the hijack option is ineffective. This may be due to the network's IPv6 RA broadcasting a link-local address or the router's own IPv6 address as DNS, causing DNS queries to bypass Surge. In your router's IPv6 settings, set the RA's DNS address to empty, or change it to a public DNS address (such as Google Public DNS `2001:4860:4860::8888`). (When configuring Surge IPv6 RA override, a warning will be triggered if this issue is detected)

{% hint style="info" %}
Some routers (such as original ASUS firmware) cannot customize the DNS setting for IPv6 RA. You can consider flashing third-party firmware like Merlin or OpenWRT to solve this.
{% endhint %}

4. **Handle Encrypted DNS (DoH/DoT)**: If the device or application has built-in encrypted DNS, Surge's Fake IP mechanism becomes invalid. In this case, domain names cannot be displayed but traffic can still be routed via rules. Enable the `extended-matching` flag for related rules—this allows matching based on HTTP Host or TLS SNI sniffing results.

{% hint style="info" %}
If only a small number of Apple-related domains such as gateway.icloud.com and tether.edge.apple are accessed by IP, this is expected behavior. iOS/macOS has special encrypted DNS logic for certain domains, preventing the Fake IP mechanism from working.
{% endhint %}

### Known Compatibility Issues

#### P2P Clients

Running P2P download software (such as BT, Xunlei), game downloaders, or live streaming apps on taken-over devices may cause performance issues or interruption in Surge due to a surge in concurrent connections. It is recommended to avoid using Gateway Mode for such devices. Future updates will optimize this.

{% hint style="info" %}
**Technical Note**: Traditional routers operate on the packet layer, so handling a large number of concurrent connections (like 1000) only involves minor NAT table overhead and minimal load. Surge, however, operates at the application layer and needs to perform protocol sniffing, rule matching, and log recording for every connection. A single large traffic connection poses no problem, but thousands of new concurrent connections cause significant overhead.
{% endhint %}

#### PlayStation Portal™ Remote Player

When the PS Portal is taken over by Surge Gateway Mode, remote streaming cannot start normally.

This is because the logic for PS Portal's remote streaming conflicts with Surge's operating mode: Surge must first accept the TCP handshake to perform protocol sniffing, but PS Portal checks for local network status by accessing the PS5's intranet IP and seeing if a TCP handshake can be completed. This causes a false positive as if both are on the same LAN.

You can resolve this by adding a rule:

`IP-CIDR,192.168.0.100/32,REJECT-DROP,pre-matching,no-resolve`

Replace the IP address above with your PS5's intranet IP, and make sure to include the `pre-matching` flag. This will allow PS Portal to correctly recognize the network and enable remote streaming.

Alternatively, you can leverage this mechanism to trick PS Portal into thinking the PS5 is on the same LAN—enabling you to play PS Portal via your own private network. If using Surge Ponte, simply add a rule to forward PS Portal's access to the PS5's network accordingly.
