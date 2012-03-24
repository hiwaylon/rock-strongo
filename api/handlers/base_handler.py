"""Provides base testing functionality for testing request handlers with
Tornados testing framework.

"""

from tornado import testing
from tornado import web

from api.utils import routes


class TestBase(testing.AsyncHTTPTestCase):
    def get_app(self):
        """Reqired torando hook for handler tests."""
        return web.Application(routes.Routes.get_instance().routes)
