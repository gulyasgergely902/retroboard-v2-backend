# Configurations for Development and Production environments


class Config:
    """Base configuration with common settings."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development configuration with debugging enabled."""
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    """Production configuration with debugging disabled."""
    DEBUG = False
    ENV = 'production'
