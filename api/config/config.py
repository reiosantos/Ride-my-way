"""
Config file contains global CONSTANTS
"""
from api.utils.utils import JSONSerializable


class HostConfig:
    """
    System HOST configuration settings
    They can be changed at any time.
    """
    HOST = "0.0.0.0"
    PORT = 5000


class ServerConfig(JSONSerializable):
    """
    System configuration settings
    They can be changed at any time.
    """

    SECRET_KEY = 'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'
    SECURITY_PASSWORD_SALT = 'efa27950565790fbaecfb5fb64b84a6a7c48d06d'


class EnvironmentConfig(ServerConfig):
    """
    System configuration settings for running environment
    They can be changed at any time.
    It extends the server congig class
    """
    DEBUG = True
    TESTING = True
    ENV = "development"
