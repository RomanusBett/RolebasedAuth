from flask import Blueprint
from .auth_views import Login

"""
  __name__ is a special built-in variable which evaluates to
  the name of the current module.

"""
auth_blueprint = Blueprint("auth", __name__)
