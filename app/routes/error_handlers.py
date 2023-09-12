from flask import Blueprint
from ..models.exceptions import InvalidDataError, UsernameConflictError

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(InvalidDataError)
def handle_invalid_data_error(error):
    return error.get_response()

@errors.app_errorhandler(UsernameConflictError)
def handle_username_conflict_error(error):
    return error.get_response()