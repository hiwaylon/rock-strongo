"""Tests for requests for the `activities` resource."""

import json

import api.first
from api.testing import test_base


class TestActivitiesHandler(test_base.TestBase):
    def test_create_activity(self):
        """It should create an activity resource from JSON data."""

        # TODO: Token/Auth system.
        # TODO: utils module for to_int and from_int dates

        response = self.fetch(
            "/api/v1/activities", method="POST",
            body=json.dumps({"ok": "foo"}))
        self.assertEqual(201, response.code)

        # Check a simple representation of the activity is returned.
        response = json.loads(response.body)
        self.assertTrue("uid" in response)
        first_uid = response.get("uid")

        # Make a second activity; the uids should be different.
        response = self.fetch(
            "/api/v1/activities", method="POST",
            body=json.dumps({"ok": "foo"}))
        self.assertEqual(201, response.code)
        response = response.to_dict()
        self.assertNotEqual(first_uid, response.get("uid"))
