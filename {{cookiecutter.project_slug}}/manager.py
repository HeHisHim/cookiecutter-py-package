from flask import Flask
from {{cookiecutter.project_slug}}.config import config

def create_app():
    _app = Flask("{{ cookiecutter.project_slug }}")
    _app.config.from_object(config)
    return _app

def init():
    # Log Initialization
    # DB Initialization
    # Blue Print    
    pass

app = create_app()
init()