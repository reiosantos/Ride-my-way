# -*- coding: utf-8 -*-
"""
Main app root of the api endpoints
"""

import sys
import os
from flask import Flask
from flask_cors import CORS
sys.path.append(os.path.pardir)

from api.config import HOST, PORT, DEBUG, SECRET_KEY, SECURITY_PASSWORD_SALT, ENVIRONMENT, TESTING
from api.urls import Urls

APP = Flask(__name__)
APP.secret_key = SECRET_KEY
APP.testing = TESTING
APP.config['SECURITY_PASSWORD_SALT'] = SECURITY_PASSWORD_SALT
APP.env = ENVIRONMENT

CORS(APP)
Urls.generate(APP)

if __name__ == '__main__':
    APP.run(debug=DEBUG, host=HOST, port=PORT)
