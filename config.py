import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email Settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER')  # SMTP server for sending emails
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))  # Port for the SMTP server
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Email account username
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Email account password

# API Keys
    SOME_API_KEY = os.environ.get('SOME_API_KEY')  # Replace with the actual API key

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    # Add more configurations if needed
}

def get_config(env):
    return config_by_name[env]
