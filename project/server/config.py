# -*- mode: python -*- -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))
sqlite_url_prefix = 'sqlite:///'
database_name = 'data.db'

class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = sqlite_url_prefix + 'dev_' + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = sqlite_url_prefix + 'test_' + database_name
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class StagingConfig(BaseConfig):
    """Staging configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = sqlite_url_prefix + database_name

class ProductionConfig(StagingConfig):
    """Production configuration."""
    DEBUG = False
