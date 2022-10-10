from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from flask_restful import Api




app = Flask(__name__)

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# the values of those depend on your setup
POSTGRES_URL = get_env_variable("DB_HOST")
POSTGRES_USER = get_env_variable("DB_USERNAME")
POSTGRES_PW = get_env_variable("DB_PASSWORD")
POSTGRES_DB = get_env_variable("DB_NAME")

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)


@app.route("/")
def create_app(config_mode):

    from .admin import admin_blueprint as admin_blp
    admin = Api(admin_blp)
    app.register_blueprint(admin_blp, url_prefix="/api/v2")


    return app
