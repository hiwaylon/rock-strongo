"""Handle requests for an Workouts resource instance.

"""

from tornado import web

import api.first

from api.models import workout
from api.handlers import mixins
from api.utils import routes  # api.first


@routes.route("/api/v1/workouts")
class WorrkoutsHandler(web.RequestHandler, mixins.ResourceCreationMixin):
    def post(self):
        """Handles requests for new activity resources."""
        request_data = self.request.to_dict()
        resource = self.create_resource(request_data)
        self.set_status(201)
        self.write(resource.simple_view())

    def _validate_internal(self, request_data):
        if "description" not in request_data:
            return False
        return True

    def _create_internal(self, request_data):
        return workout.Workout.create(request_data["description"])
