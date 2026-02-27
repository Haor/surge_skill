Title: URL Scheme · GitBook

URL Source: https://manual.nssurge.com/others/url-scheme.html

Published Time: Tue, 20 Jan 2026 02:39:15 GMT

URL Scheme for Surge iOS
------------------------

Surge iOS supports 4 actions and one option.

Action:

*   surge:///start

Start with selected configuration.

*   surge:///stop

Stop current session.

*   surge:///toggle

Start or stop with selected configuration.

*   surge:///install-config?url=x

Install a configuration from a URL. The URL should be encoded in percent encoding.

Option:

*   autoclose=true

Auto close Surge after action completed. (Cannot be used with install-config)

Example: surge:///toggle?autoclose=true

x-callback-url
--------------

Surge supports x-callback-url specification from v3.4. The URL scheme is 'surge' and the available actions are 'start', 'stop' and 'toggle'.
