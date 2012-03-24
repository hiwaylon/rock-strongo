"""Test the id generation utility."""

import unittest

from api.utils import ids


class TestIds(unittest.TestCase):
    """Test class."""
    def test_id_generation(self):
        """It should generate a unique id."""
        first_uid = ids.generate()
        self.assertIsNotNone(first_uid)
        second_uid = ids.generate()
        self.assertNotEqual(first_uid, second_uid)
