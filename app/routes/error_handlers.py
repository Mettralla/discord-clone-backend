from flask import Blueprint
from ..models.exceptions import InvalidDataError, UsernameConflictError, NotFound, UnauthorizedAccess, ForbiddenAction

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(InvalidDataError)
def handle_invalid_data_error(error):
    return error.get_response()

@errors.app_errorhandler(UsernameConflictError)
def handle_username_conflict_error(error):
    return error.get_response()

@errors.app_errorhandler(NotFound)
def handle_not_found_error(error):
    return error.get_response()

@errors.app_errorhandler(UnauthorizedAccess)
def handle_unauthorized_error(error):
    return error.get_response()

@errors.app_errorhandler(ForbiddenAction)
def handle_forbidden_action_error(error):
    return error.get_response()