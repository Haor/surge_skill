Title: HTTP Processing · GitBook

URL Source: https://manual.nssurge.com/http-processing.html

Published Time: Tue, 20 Jan 2026 02:39:14 GMT

HTTP Processing
===============

Surge includes multiple functions for modifying HTTP requests and responses, with the processing pipeline in the following order:

1.   URL Rewrite
2.   Header Rewrite
3.   Body Rewrite
4.   Script Processing

Among them, script processing can only be modified by one script, while if there are multiple hits for other rewrite rules, they will take effect in sequence.
