"""General helpers for developing Tornado applications."""

import json

from tornado import httpserver
from tornado import httpclient

from api.utils import error


def to_dict(self):
    """Convert the body attribute of self to a dictionary.

    Useful when self is a Tornado httpserver.HTTPRequest or
    httpclient.HTTPResponse.

    """
    try:
        return json.loads(self.body)
    except ValueError:
        raise error.bad_request("Request body does not contain valid JSON.")

httpserver.HTTPRequest.to_dict = to_dict
httpclient.HTTPResponse.to_dict = to_dict
