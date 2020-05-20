#!/usr/bin/env python3

import http.client

c = http.client.HTTPSConnection("google.com")
c.request("GET", "/")
response = c.getresponse()
print(response.status, response.reason)
