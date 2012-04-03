"""Unit tests for the Workouts resource instace."""

import unittest

from api.models import workout as workout_module


class TestWorkout(unittest.TestCase):
    def test_simple_view(self):
        """A workout should provide a simple representation of itself."""
        workout = workout_module.Workout.create()
        simple_view = workout.simple_view()
        self.assertTrue("uid" in simple_view)

        fetched = workout_module.Workout.fetch(uid=simple_view["uid"])
        self.assertNotEqual(None, fetched)
