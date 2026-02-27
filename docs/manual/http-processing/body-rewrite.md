Title: Body Rewrite · GitBook

URL Source: https://manual.nssurge.com/http-processing/body-rewrite.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

Body Rewrite iOS 5.10.0+Mac 5.6.0+
==================================

Surge can rewrite the body of HTTP request or response, replacing the original content with regular expressions. Example:

```
[Body Rewrite]
http-request ^http(s)?://example\.com value abc
http-response ^http(s)?://example\.com documents Surge
```

### Syntax

Each line contains a rewrite rule, with parameters separated by spaces, starting with `http-request` or `http-response`. The second parameter is the regular expression for the URL to take effect. The third parameter is the regular expression for replacement, and the fourth parameter is the content of replacement.

`http-response ^https?://example\.com/ regex replacement`

Allow to continue adding regular expressions and replacement content afterwards for consecutive replacements.

```
http-response ^https?://example\.com/ regex1 replacement1 regex2 replacement2
http-response ^https?://example\.com/ regex1 replacement1 regex2 replacement2 regex3 replacement3
…
```

1.   If a request hits multiple body rewrite rules, they will be executed in sequence.
2.   Even if the original request does not contain a body, new content may still be generated through body rewrite, such as using the `^$` expression.

### JQ Body Rewrite iOS 5.14.0+Mac 5.9.0+

You can use JQ expressions to manipulate the JSON body.

```
http-request-jq url-pattern jq-expexpression
http-response-jq url-pattern jq-expexpression
```

For example:

```
http-response-jq ^http://httpbingo.org/anything '.headers |= with_entries(select(.key | test("^X-") | not))'
```
