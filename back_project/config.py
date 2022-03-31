import os
from constants import DB_USER
from constants import DB_PASS
from constants import DB_ADDR
from constants import DB_NAME 

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 9997
HOST = "0.0.0.0"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

#Secret config
SQLALCHEMY_DATABASE_URI = "mysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}?charset=utf8".format(DB_USER=DB_USER, DB_PASS=DB_PASS, DB_ADDR=DB_ADDR, DB_NAME=DB_NAME)