#!/usr/bin/env python3

import http.client
import urllib.parse
import json

params = urllib.parse.urlencode(
    {'client_id': '480236582879-8h0b7vfns2lmou9ot9f3b3ivl2a72eg1.apps.googleusercontent.com', 'response_type': 'code', 'scope': 'https://www.googleapis.com/auth/drive.readonly', 'redirect_uri': 'urn:ietf:wg:oauth:2.0:oob' }
)

print(params)
c = http.client.HTTPSConnection("accounts.google.com")

headers = {"Authorization: Basic YWxhZGRpbjpvcGVuc2VzYW1l": "Basic YWxhZGRpbjpvcGVuc2VzYW1l"}
c.request("POST", "o/oauth2/v2/auth", params, {})
response = c.getresponse()
print(response.status, response.reason)
print(response.read().decode())
