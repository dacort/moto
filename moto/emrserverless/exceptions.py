"""Exceptions raised by the emrserverless service."""
from moto.core.exceptions import JsonRESTError


class ResourceNotFoundException(JsonRESTError):
    code = 400

    def __init__(self, resource):
        super().__init__("ResourceNotFoundException", resource)


class ValidationException(JsonRESTError):
    code = 400

    def __init__(self, message):
        super().__init__("ValidationException", message)
