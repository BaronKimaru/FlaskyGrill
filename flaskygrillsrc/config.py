import os

class Config:
	"""Common Configurations"""
	DEBUG = False
	CSRF_ENABLED = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/flaskapi'



class DevelopmentConfig(Config):
	"""Configurations for Development Environment"""
	DEBUG = True


class TestingConfig(Config):
	"""Configurations for Testing Environment, with a separate database"""
	DEBUG = True
	TESTING = True
	SQL_DATABASE_URI = os.environ.get("DB_TEST_SQLALCHEMY")


class StagingConfig(Config):
	"""Configurations for Staging Environment"""
	DEBUG = True


class ProductionConfig(Config):
	"""Configuration for Production Environment"""
	DEBUG = False
	TESTING = False

app_config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'staging': StagingConfig,
	'production': ProductionConfig,
}
