# Differences between REJECT Policies

Surge has built-in multiple different REJECT policies, with some subtle differences between them:

* `REJECT`: Rejects the request; when the connection type is HTTP, an error page will be returned. (This behavior can be controlled by the `show-error-page-for-reject` parameter)
* `REJECT-TINYGIF`: Rejects the request; when the connection type is HTTP, it returns a 1px GIF image response. If the connection is of other types, it is disconnected directly. This policy is mainly used for Web ad blocking.
* `REJECT-DROP`: Rejects the request; unlike `REJECT`, this policy silently discards the request. Some applications have very aggressive retry logic and will immediately retry when the connection fails, causing a request storm that can waste system resources.

{% hint style="info" %}
If a large number of requests to a particular hostname trigger the REJECT/REJECT-TINYGIF policy within a short period (the threshold for the current version is 10 times within 30 seconds), Surge will automatically upgrade the REJECT policy to the REJECT-DROP policy.
{% endhint %}

* `REJECT-NO-DROP`: Generally, it is the same as the `REJECT` policy. The difference is that using this rule will not trigger the automatic upgrade behavior mentioned above.
