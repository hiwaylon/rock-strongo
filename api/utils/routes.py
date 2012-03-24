"""Modified from Jeremy Kelley's github.com/nod/tornado_addons

The Routes singleton is used to track all of the controller routes,
and the @route decorator is a shortcut to add new routes.

A sample controller file looks like::

        from ustudioapi.libraries.routes import route
        from ustudioapi.libraries.controller import Controller

        @route("/path/to/object", name="route_name")
        class SampleController(Controller):
            pass

You can get information about the routes through several methods on the
Routes instance:

    Routes.instance().print_routes()

"""

import tornado.web
import collections

# TODO: Use termcolor or colorama package.
TERM_COLOR_FAIL = '\033[91m'
TERM_COLOR_ENDC = '\033[0m'

PRINT_SPACE = 2


class Routes(object):
    """The singleton which holds all of the route information."""

    _instance = None

    def __init__(self):
        self.routes = []

    @classmethod
    def instance(cls):
        """Returns the master instance of the Routes object."""
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def add_route(self, the_route):
        """Adds a new route to the routes list """
        tornado_uri = tornado.web.url(
            the_route.uri, the_route.handler, name=the_route.name)
        self.routes.append(tornado_uri)

    def print_routes(self):
        """Prints out all routes, spacing between name and regex."""
        max_name_length = 0
        max_route_length = 0
        route_names = collections.defaultdict(lambda: 0)
        for route_obj in self.routes:
            url = getattr(route_obj, "_path")
            route_names[route_obj.name] += 1
            if len(route_obj.name) > max_name_length:
                max_name_length = len(route_obj.name)
            if len(url) > max_route_length:
                max_route_length = len(url)
        for route_obj in self.routes:
            message = ''
            if route_names[route_obj.name] > 1:
                message += TERM_COLOR_FAIL
            spaces = max_name_length + PRINT_SPACE - len(route_obj.name)
            message += route_obj.name
            if route_names[route_obj.name] > 1:
                message += TERM_COLOR_ENDC
            message += ' ' * spaces
            message += getattr(route_obj, "_path")
            print message


class Route(object):
    """Just holds the name and URI and adds to Routes when wrapping."""
    def __init__(self, uri, name=None):
        self.uri = uri
        self.name = name
        self.handler = None

    def add_handler(self, handler):
        """Updates the name and assigns the handler to the Route."""
        self.name = self.name or handler.__name__
        self.handler = handler


def route(uri, name=None):
    """The decorator for adding routes to the Routes instance."""
    route_instance = Route(uri, name)

    def wrap(handler):
        """Adds handler to the route, adds route to Routes, and returns."""
        route_instance.add_handler(handler)
        Routes.instance().add_route(route_instance)
        return handler
    return wrap
