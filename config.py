import os

from environs import Env

env = Env()
env.read_env()


class Configuration(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

    SECRET_KEY = os.environ['SECRET_KEY']

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'

    DEBUG = os.environ['DEBUG']
