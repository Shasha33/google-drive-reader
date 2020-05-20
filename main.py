#!/usr/bin/env python3

import http.client

c = http.client.HTTPSConnection("www.googleapis.com")

headers = {"key": "password_key"}
c.request("POST", "/auth/documents.readonly", "", headers)
response = c.getresponse()
print(response.status, response.reason)
