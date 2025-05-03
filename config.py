"""Secret key configuration for CSRF protection"""
import os


class Config:
    """App secret key and database server credentials"""
    SECRET_KEY = os.environ['SECRET_KEY']

class ConfigDev(Config):
    """ConfigDev setting"""
    TESTING = False