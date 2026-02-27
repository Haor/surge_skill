# 关于 User Agent 规则

Surge 的规则系统中有提供依据 User-Agent 进行判别的规则。使用该规则时请注意：

1. 该规则仅对 HTTP/HTTPS 请求有效。如果是一个 raw TCP 请求中提取的 HTTP header，规则无法生效，需配置 `force-http-engine` 参数，详见[《Surge 官方中文指引：理解 Surge 原理 》](https://manual.nssurge.com/book/understanding-surge/cn/#%25E5%25A4%2584%25E7%2590%2586)。
2. 对于 HTTPS 请求，存在发给 HTTP 代理的 CONNECT 请求 User-Agent 和真实的 HTTP 请求 User-Agent ，两者的内容可能相同也可能不同。前者的内容通常是由系统生成，不可被 app 调整。在未开启 MITM 的情况下，匹配时仅对前者生效。开启 MITM 后仅对后者生效。
3. 在 iOS 15 系统后，系统出于隐私保护考虑，不再于 CONNECT 请求中提供 User-Agent，这意味着对于所有 HTTPS 请求，在未开启 MITM 时，User-Agent 均不可见且规则无法生效。
