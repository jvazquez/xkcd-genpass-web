'''
Created on Jun 29, 2017

@author: jvazquez
'''
import logging
from os import getenv
from os.path import abspath, dirname, join, exists

from flask import Flask
import logconfig

from app.configuration import Development, Production
from app.web.app import web
logger = logging.getLogger(__name__)


def get_application():
    """Obtains the configured flask application
    """
    configure_logger()
    env = getenv("MODE", "development")
    logger.debug("Environment is {}".format(env))
    obj = get_object_by_environment(env)
    app = Flask("xkcd-genpass-web")
    app.config.from_object(obj)
    app.register_blueprint(web)
    return app


def get_object_by_environment(environment_path):
    if environment_path is "development":
        return Development
    elif environment_path is "production":
        return Production
    raise Exception("Unknown environment selected")


def configure_logger():
    """Setup logconfig
    """
    logfile = join(abspath(dirname(__file__)), "logging.json")
    if not exists(logfile):
        raise Exception("Logging file is missing")
    logconfig.from_autodetect(logfile)


if __name__ == "__main__":
    app = get_application()
    app.run()
