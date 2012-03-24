"""Unique id generation module."""

import random
import string

CHARS = string.letters + string.digits
DEFAULT_LENGTH = 8


def generate(length=DEFAULT_LENGTH):
    uid = u""
    for x in xrange(length):
        uid += random.choice(CHARS)
    return uid
