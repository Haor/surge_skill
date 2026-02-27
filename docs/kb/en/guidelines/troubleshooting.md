# Surge Troubleshooting Guide

If you encounter problems while using Surge, please refer to this guide for troubleshooting.

{% hint style="success" %}
Before you start, you may want to read [“Official Guidance：Understanding Surge”](https://manual.nssurge.com/book/understanding-surge/en/) to learn more about the underlying mechanisms of Surge.
{% endhint %}

{% hint style="warning" %}
Before proceeding with detailed troubleshooting, please try restarting your Mac or iPhone to see if this resolves the issue. If the problem disappears after a restart and does not reappear, it’s typically a system-level occasional bug and can be ignored.

If this guide fails to resolve your issue, please contact <support@nssurge.com>, and remember to include the output of any test commands provided in this guide.
{% endhint %}

{% stepper %}
{% step %}

#### Managed Profile Issues

Please note: Surge is a networking tool and its behavior depends on profile settings. If your profile comes from a provider or a third party, and you encounter errors when installing or updating it, please contact the profile provider. We are unable to assist in such cases.
{% endstep %}

{% step %}

#### Analyzing the Source of the Problem

As a local network forwarding tool, common issues with Surge fall into two broad categories: failing to successfully take over network requests, and failing to successfully forward network traffic. These two types require fundamentally different troubleshooting approaches.

First, open the Request Viewer (Dashboard) in Surge Mac, or the Recent Requests page in Surge iOS. Then open a browser and visit a common site such as <https://bing.com>. Observe whether the request appears in the request list.

{% hint style="info" %}
If you have previously modified Surge’s capture filter settings, requests may be hidden. Make sure the capture filter is not hiding the test request.
{% endhint %}

If the request does not appear in the list, it is a takeover issue. If the request appears, it is a forwarding issue.
{% endstep %}

{% step %}

#### If You Do Not See the Request - Takeover Issues

{% tabs %}
{% tab title="Surge Mac" %}
Surge Mac has two main takeover modes: system proxy and enhanced mode (NE VIF). Go to the Overview page to confirm whether these modes are enabled and functioning. Enabling either mode allows takeover of browser requests.

**Confirming System Proxy**

If this shows as normal, you can further verify via command line. Run `scutil --proxy` in Terminal to print the current active system proxy settings. If Surge has correctly set the system proxy, the result should be:

```
<dictionary> {
  ExcludeSimpleHostnames : 1
  HTTPEnable : 1
  HTTPPort : 6152
  HTTPProxy : 127.0.0.1
  HTTPSEnable : 1
  HTTPSPort : 6152
  HTTPSProxy : 127.0.0.1
}
```

The value of ExcludeSimpleHostnames does not matter. If any other fields differ, it means Surge failed to set the system proxy successfully. Check if other similar software has taken over the system proxy.

**Confirming Enhanced Mode**

Go to System Settings › Network › VPN settings to check if Surge is enabled. If not, enhanced mode activation has failed, and you should see a clear error in the Surge interface. If other VPN entries are enabled, another app has taken over system VPN usage.

You can also test via command line. Run `ping apple.com`. If it works and the target IP is `198.18.x.x`, Surge’s enhanced mode is working. You can further check with `curl -vvv https://apple.com`.

If enhanced mode is not functioning, and a restart does not help, go to Surge Mac’s More › Settings › System Permissions Overview, remove the network extension and VPN configuration. Then reboot and try enabling enhanced mode again.
{% endtab %}

{% tab title="Surge iOS" %}
Normally, when Surge iOS is properly enabled, takeover issues rarely occur. Try restarting the system; if that fails, reset network settings in the system settings. If requests still do not appear, contact <support@nssurge.com>.
{% endtab %}
{% endtabs %}

{% hint style="info" %}
If you only encounter takeover issues with certain domains, this is usually due to profile settings:

* The `skip-proxy` parameter in your Surge profile causes requests for domains listed within to bypass system proxy/takeover. Remove those domains from the parameter if needed.
* In Surge iOS or Surge Mac enhanced mode, if you cannot take over requests to a specific internal IP, this is expected: there may be a more specific, higher-priority routing table on your network, causing requests to bypass Surge’s VIF. Be sure to assign a domain (local DNS mapping) for this IP to ensure Surge can take it over.
  {% endhint %}
  {% endstep %}

{% step %}

#### If You See the Request - Forwarding Issues

Click into the specific request and switch to the Notes tab, where the cause of failure will be detailed. Usually, failures are due to policy server faults. Common errors include:

* Connection refused: Proxy setup error or server fault
* Connection timeout: Proxy setup error or server fault
* No upstream DNS server: No valid DNS server defined in Surge profile; adjust your profile
* No route to host: Proxy setup error, or the device has no network
  {% endstep %}
  {% endstepper %}
