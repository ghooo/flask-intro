import os

#default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "\x92!\x06\x89{d\xb4P\x80\xd4\xe5\xb0\x91" \
			"\x17\xa8\xdd\xc1\x15U`H\xf0\x11z"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	
class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(BaseConfig):
	DEBUG = True

# to enable at heroku use this command:
# heroku config:set APP_SETTINGS=config.ProductionConfig --remote heroku
class ProductionConfig(BaseConfig):
	DEBUG = False