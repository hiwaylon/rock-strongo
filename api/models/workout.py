"""Model for the Workout resource instance."""


# TODO: Elsewhere...
import pymongo

_CONNECTION = pymongo.Connection("localhost", 27017)
_DB = _CONNECTION["__testing_api"]


import abc


class BaseResource(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def simple_view(self):
        """Generates and returns a dict containing a simple representation of
        the resource.

        This is a public view, generally returned to the client.

        """
        pass

    @abc.abstractmethod
    def _serializable_view(self):
        """Generate and return a dict containing the serializable
        representation of the resource.

        This is an private view that will be written to the database.

        """
        pass

import logging as logger

from api.utils import ids


class Workout(BaseResource):
    @classmethod
    def create(cls):
        instance = cls()
        # TODO: Create an "insert_view" standard? Yes, to uphold encapsulation
        # of the model, i.e. the object itself generates its serializable view.
        _DB.workouts.insert(instance._serializable_view())

        return instance

    @classmethod
    def fetch(cls, uid):
        # TODO: Abstractions for database, collection names, ...
        workout = _DB.workouts.find_one({"uid": uid})
        if not workout:
            logger.info("No document exists for fetch (%s).", uid)
            return None

        logger.info("Fetched document (%s).", workout)
        return workout

    def __init__(self):
        self._uid = ids.generate(length=4)

    def simple_view(self):
        return {
            "uid": self._uid
        }

    def _serializable_view(self):
        return self.simple_view()
