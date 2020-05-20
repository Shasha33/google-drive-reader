#!/usr/bin/env python3

import http.client
import urllib.parse

params = urllib.parse.urlencode(
    {'@client_id': '480236582879-8h0b7vfns2lmou9ot9f3b3ivl2a72eg1.apps.googleusercontent>', '@response_typ': 'code', '@scope': 'https://www.googleapis.com/auth/drive.metadata.readonly', '@redirect_ur': 'urn:ietf:wg:oauth:2.0:oob' }
)


c = http.client.HTTPSConnection("accounts.google.com")

headers = {"Authorization: Basic YWxhZGRpbjpvcGVuc2VzYW1l": "Basic YWxhZGRpbjpvcGVuc2VzYW1l"}
c.request("POST", "/o/oauth2/v2/auth", params, {})
response = c.getresponse()
print(response.status, response.reason)
print(response)
