"""This module should import other modules that need to perform import time
initialiazation.

"""

import api.utils.tornado_helpers
from api.utils import error

import api.handlers.create_routes
import api.utils.routes
api.utils.routes.Routes.instance().print_routes()
