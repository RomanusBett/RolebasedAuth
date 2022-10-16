import os
from app import create_app

from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = create_app(os.getenv("APP_SETTINGS") or "default")

"""
    By default since the interpreter will run this module the
    __name__ variable will be set to __main__. The module that
    is being run is the main entry point to the app.
"""
if __name__ == '__main__':
    app.run()
