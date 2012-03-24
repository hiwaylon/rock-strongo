"""Helpers for testing Tornado applications."""

import json

from tornado import httpclient


# Patch HTTPResponse to automatically parse its body of JSON.
def to_dict(self):
    return json.loads(self.body)

httpclient.HTTPResponse.to_dict = to_dict
