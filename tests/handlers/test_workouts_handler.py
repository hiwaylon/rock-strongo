"""Test requests for the Workouts resource instance."""

import json

import api.first
from api.testing import test_base
from api.models import workout as workout_module

_RESOURCE_URL = "/api/v1/workouts"


class TestWorkoutsHandler(test_base.TestBase):
    def test_factory_resource(self):
        """It should create an activity resource from JSON data."""

        # TODO: Token/Auth system.
        # TODO: utils module for to_int and from_int dates

        # TODO: How are things like 4x 800m with a 3 mile warmup going to be
        # handled? It could be delegaed back to the user in the form of a log
        # entry such as "distance completed" or "time completed".

        # TODO: Date as YYYY-MM-DD, workout template uid
        # TODO: Workout templates as factories for workouts?

        response = self.fetch(
            _RESOURCE_URL, method="POST",
            body=json.dumps({"description": "Lorem ipsum dolor set."}))
        self.assertEqual(201, response.code)

        # Check a simple representation of the activity is returned.
        response = json.loads(response.body)
        self.assertTrue("uid" in response)
        self.assertTrue("description" in response)

        first_uid = response.get("uid")

        # Make a second activity; the uids should be different.
        response = self.fetch(
            _RESOURCE_URL, method="POST",
            body=json.dumps({"description": "Turpis vut, hac dis nec hac."}))
        self.assertEqual(201, response.code)
        response = response.to_dict()
        self.assertNotEqual(first_uid, response.get("uid"))

        # TODO: Test somethings in the DB.
        workout = workout_module.Workout.fetch(response["uid"])
        self.assertNotEqual(None, workout)
