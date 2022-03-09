import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 9997
HOST = "0.0.0.0"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

#Secret config
SQLALCHEMY_DATABASE_URI = "mysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}?charset=utf8".format(DB_USER="admin", DB_PASS="$tV+&gEjZ6JH", DB_ADDR="deeprespred.ciwvug7b8ip8.us-east-1.rds.amazonaws.com", DB_NAME="deeprespredDB")