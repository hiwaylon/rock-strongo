"""Error handling helpers for Tornado based projects."""

import logging
from tornado import web


def bad_request(message):
    _log_and_raise(400, message)


def _log_and_raise(error_code, message):
    logging.error(message)
    raise web.HTTPError(error_code, message)
