import os

#default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "\x92!\x06\x89{d\xb4P\x80\xd4\xe5\xb0\x91" \
			"\x17\xa8\xdd\xc1\x15U`H\xf0\x11z"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False