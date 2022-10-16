from flask import Blueprint
from .operator_views import PostMeal

"""
  __name__ is a special built-in variable which evaluates to
  the name of the current module.

"""
operator_blueprint = Blueprint("operator", __name__)
