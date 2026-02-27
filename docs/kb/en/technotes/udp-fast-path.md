# VM UDP Fast Path

When using Surge in Gateway mode to take over downstream devices, some devices may run P2P-style applications that heavily use UDP (such as BitTorrent clients, game launchers, live streaming apps, etc.). These can cause a sudden surge of connections in the Dashboard. This not only slows down Surge’s overall processing speed, but in extreme cases may even exhaust macOS system resources and cause Surge to be forcibly terminated by the system.

## Root Cause

Surge works as a Layer-4 proxy. For every UDP flow with a distinct 4-tuple (source address / source port / destination address / destination port), Surge treats it as an independent connection and manages it accordingly.\
For typical applications, even those using UDP, the number of logical connections is usually small, so the overhead is acceptable. However, for P2P applications, thousands of logical connections can be created within just a few seconds, which dramatically amplifies the cost of connection management.

## UDP Fast Path Mechanism

To mitigate this, we introduced the **UDP Fast Path** protection mechanism. When Surge detects that a client is creating a large number of UDP connections in a short period of time (**≥ 10** new connections within **1 second**, or **≥ 30** within **10 seconds**), Surge will enable UDP Fast Path for that specific client and downgrade its UDP traffic to pure Layer-3 forwarding.

In UDP Fast Path mode:

* Each packet only goes through minimal Layer-3 forwarding logic, without establishing a separate connection for each 4-tuple.
* The processing performance is extremely high and can easily exceed the physical NIC’s bandwidth limit in theory.
* Connection management overhead and system resource usage are greatly reduced, so you no longer need to worry about P2P connection storms overwhelming the system.

## Notes

1. **Bypasses the proxy**\
   Packets handled by UDP Fast Path are forwarded directly and **do not pass through proxy rules or policy processing**.
2. **Protection for privileged ports and FakeIP**\
   To avoid impacting normal applications, the following UDP traffic is **always handled in the regular mode** and will not enter Fast Path:
   * UDP packets whose destination port is **below 1024**
   * UDP packets whose destination address is a **FakeIP**
3. **Only available with Surge Gateway VM**\
   UDP Fast Path is only effective when used together with the **Surge Gateway VM**. Enhanced mode takeover is not effective.
4. **Per-device toggle**\
   Starting from Surge Mac 6.4.2, the Dashboard provides a per-device toggle to disable UDP Fast Path.\
   You can enable or disable UDP Fast Path for specific devices as needed to balance performance and controllability.
