from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
import os

# local imports
from .admin import CreateMeal

from flask_restful import Api
app = Flask(__name__)


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


# # the values of these depend on your setup
# POSTGRES_URL = get_env_variable("DB_HOST")s
# POSTGRES_USER = get_env_variable("DB_USERNAME")
# POSTGRES_PW = get_env_variable("DB_PASSWORD")
# POSTGRES_DB = get_env_variable("DB_NAME")

# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
#     user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URLs
# # silence the deprecation warning
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


@app.route("/")
def create_app(config_mode):

    # register blueprint
    from .admin import admin_blueprint as admin_blp
    admin = Api(admin_blp)
    app.register_blueprint(admin_blp, url_prefix="/api/admin/")

    from .operator import operator_blueprint as operator_blp
    operator = Api(operator_blp)
    app.register_blueprint(operator_blp, url_prefix="/api/operator/")

    # define app routes
    admin.add_resource(CreateMeal, "/create_meal")
    # operator.add_resource()

    return app
