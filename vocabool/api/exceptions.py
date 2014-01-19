from rest_framework.exceptions import APIException, status

class DuplicateNotAllowed(APIException):
    """Raised when trying to insert a duplicate."""
    status_code = status.HTTP_409_CONFLICT
    detail = 'Already exists.'

