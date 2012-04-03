"""Error handling helpers for Tornado based projects."""

from tornado import web


def bad_request(message):
    _raise_http_error(400, message)


def _raise_http_error(error_code, message):
    raise web.HTTPError(error_code, message)
