"""
Config file contains global CONSTANTS
"""


class Config:
    """
    System configuration settings
    They can be changed at any time.
    """
    HOST = "0.0.0.0"
    PORT = 5000

    SECRET_KEY = 'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'
    SECURITY_PASSWORD_SALT = 'efa27950565790fbaecfb5fb64b84a6a7c48d06d'

    DEBUG = True
    TESTING = True
    ENVIRONMENT = "development"
