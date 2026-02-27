Title: Event · GitBook

URL Source: https://manual.nssurge.com/scripting/event.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

### event

Evaluates a script while the specified event occurs. The value is the event name. Only one event is supported currently: network-changed.

Please invoke $done() to complete.

#### Event Types

*   `network-changed`: Triggered when the system network changes.

```
// network-changed = script-path=network-changed.js,type=event,event-name=network-changed

$notification.post('DNS Update', $network.dns.join(', '));

$done();
```

*   `notification`: Triggered when Surge shows a notification. The script can still get the message even if the notification's category is off. 

```
// notification = script-path=notification.js,type=event,event-name=notification

console.log($event.data);

$done();
```
