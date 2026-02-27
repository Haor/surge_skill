# TCP Fast Open

## What is TCP Fast Open (TFO)

TCP connections require a three-way handshake before data transmission can begin. This means that every TCP connection wastes an RTT to establish the connection. This design was not a problem when the TCP protocol was invented, as networks were in the LAN era, with RTTs only in the milliseconds.

However, in the era of the internet and wireless networks, RTTs can be as high as tens or even hundreds of milliseconds. This wasted RTT has become a significant overhead. Thus, TCP Fast Open was born. In simple terms, TFO's specific implementation is to attach the first data packet to be transmitted, such as the TLS protocol's Client Hello, in the first SYN packet of the three-way handshake. When the handshake is complete, the server has received the first data packet and can start subsequent transmissions. This recovers the latency loss caused by the handshake. (There are many details in the actual implementation, such as cookies, which are not discussed here)

### Compatibility issues

However, this improvement encountered a problem: as an extension to the TCP protocol, intermediate network devices may not support this feature. For example, some firewalls (NATs) may treat SYN packets with data segments as illegal packets and discard them directly. As a result, connections using TFO cannot be established at all (e.g., China's mobile data network).

To address this, operating systems had to introduce a blackhole mechanism. When attempting a TFO handshake with a specific IP, if no response is received within a certain time, the system retries the handshake without TFO. If successful, the IP is added to a blacklist, and future handshakes will not use TFO.

This mechanism has two issues:

1. It may misjudge due to normal network fluctuations and packet loss, causing the IP to enter the blacklist and lose the TFO feature for all subsequent connections.
2. Sometimes, TFO is only ineffective under specific networks (e.g., data networks), but the operating system's blacklist only records the target IP. So, even after switching networks, TFO cannot be used.

In our tests, the proxy server IP would almost certainly be added to the blacklist after some time.

{% hint style="info" %}
Two tips for macOS:

1. You can use the command sudo sysctl -w net.inet.tcp.clear\_tfocache=1 to forcibly clear the system's blacklist.
2. You can use sudo sysctl -w net.inet.tcp.disable\_tcp\_heuristics=1 to forcibly disable the blacklist function. (However, this will also affect ECN and MPTCP)
   {% endhint %}

### Surge's related settings

To use TFO in Surge, first, configure the `tfo=true` parameter for the corresponding proxy policy.

To address potential issues with the operating system's blackhole mechanism, Surge allows manual configuration of TFO availability through subnet settings, bypassing system restrictions.

```
[SSID Setting]
"SSID:My Home" tfo-behaviour=force-enabled
```

The `tfo-behaviour` parameter has three options:

1. `auto`: Use the system's default blacklist behavior.
2. `force-enabled`: Ignore the system blacklist and always use TFO for handshakes in this network.
3. `force-disabled`: Do not use TFO in this network.

Before configuring, please test whether TFO is available in the network to avoid setting it to force-enabled, which may cause the proxy to be completely unreachable.

### Request logs

In the request logs, details about TFO will be displayed. Some common results are as follows:

* `TCP Fast Open was successful (tfo_syn_data_sent, tfo_syn_data_acked)`

  This indicates that TFO was successful.
* `Attempted to use TCP Fast Open but failed (tfo_heuristics_disable)`

  This indicates that TFO was automatically disabled due to being added to the blacklist.
* `Attempted to use TCP Fast Open but failed (tfo_cookie_req, tfo_no_cookie_rcv)`

  This indicates that a TFO handshake was attempted, but the server did not support TFO.
