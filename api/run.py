# -*- coding: utf-8 -*-
"""
Main app root of the api endpoints
"""

import sys
import os
from flask import Flask
from flask_cors import CORS

sys.path.append(os.path.pardir)

from api.config.config import HostConfig, EnvironmentConfig
from api.handlers.errors import ErrorHandlers
from api.routes import Urls


class Server:

    """ Creates flask object to start the server"""

    @staticmethod
    def create_app(config=None):
        app = Flask(__name__)
        app.config.update(config.__dict__ or {})
        app.errorhandler(404)(ErrorHandlers.not_found)
        app.errorhandler(400)(ErrorHandlers.bad_request)
        Urls.generate(app)
        CORS(app)
        return app


APP = Server().create_app(config=EnvironmentConfig)

if __name__ == '__main__':
    APP.run(host=HostConfig.HOST, port=HostConfig.PORT)
