"""The mixins module provides starndard resource handler mixins."""

import abc

from api.utils import error


class ResourceCreationMixin(object):
    """This mixin provides a standard resource creation interface.

    The ``create_resource`` method is called by the subclass. It is a template
    method that will perform request data validation and resource creation.

    These are performed by the ``_validate_internal`` and ``_create_internal``
    abstract base methods which must be implemented by subclasses.

    ``_validate_internal`` should return ``True`` if ``request_data`` can be
    validated. If ``False`` is returned, a 400 Bad Request exception will be
    raised and returned to the client.

    """
    __metaclass__ = abc.ABCMeta

    def create_resource(self, request_data):
        if not self._validate_internal(request_data):
            error.bad_request(
                "Could not create resource. Request data (%s) is invalid." % (
                    request_data))
        return self._create_internal(request_data)

    @abc.abstractmethod
    def _validate_internal(self, request_data):
        """This method should run validation on the request data.

        If ``False`` is returned a 400 will be raised.

        Derived classes must implement this method.

        """
        pass

    @abc.abstractmethod
    def _create_internal(self, request_data):
        """This method should create a resource and return it.

        Derived classes must implement this method if they are to use the
        ``create`` helper.

        """
        pass
