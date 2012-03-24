"""The Rock Strongo web server."""

import logging

from tornado import ioloop
from tornado import web

def main():
    """Run the server.

    All command line arguments and configuration is handled here before the
    server is started.

    """
    routes = []
    application = web.Application(routes)
    logging.info("Starting server on port 1337.")
    print("Server started.")
    application.listen(port=1337)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
