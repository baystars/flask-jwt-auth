# -*- mode: python -*- -*- coding: utf-8 -*-
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
sqlite_url_prefix = 'sqlite:///'
database_name = 'data.db'
data_dir = 'data'
migrate_dir = 'migrations'

class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    TOKEN_EXPIRED = 360
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MIGRATE_DIR = os.path.join(base_dir, migrate_dir, 'prod')

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = sqlite_url_prefix + os.path.join(base_dir, data_dir, 'dev.db')
    MIGRATE_DIR = os.path.join(base_dir, migrate_dir, 'dev')

class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRED = 1
    SQLALCHEMY_DATABASE_URI = sqlite_url_prefix
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    MIGRATE_DIR = os.path.join(base_dir, migrate_dir, 'test')

class StagingConfig(BaseConfig):
    """Staging configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = sqlite_url_prefix + database_name
    SQLALCHEMY_DATABASE_URI = sqlite_url_prefix + os.path.join(base_dir, data_dir, 'stage.db')
    MIGRATE_DIR = os.path.join(base_dir, migrate_dir, 'stage')

class ProductionConfig(StagingConfig):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = sqlite_url_prefix + base_dir + data_dir + database_name
