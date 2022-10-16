from flask import Blueprint
from .admin_views import CreateMeal

"""
  __name__ is a special built-in variable which evaluates to
  the name of the current module.
  
"""
admin_blueprint = Blueprint("admin", __name__)
