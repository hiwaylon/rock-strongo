"""Implementation of the activity resource.

An activity represents a particular instance of some activity performed on
some date at some time for some duration or distance.

For example, I ran 5 miles on 3-15-2012.

Activities are associated with ActivityTemplates which define the type of
activity performed.

"""

from api.utils import ids


class Activity(object):
    def __init__(self):
        self._uid = ids.generate()

    def simple_view(self):
        return {
            "uid": self._uid
        }
