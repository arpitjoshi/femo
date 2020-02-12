import os


class Config:
    # General Config
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    SESSION_COOKIE_NAME = 'my_cookie'

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:pleasehackme@1.1.1.1:1738/imamoron'
    SQLALCHEMY_USERNAME='admin'
    SQLALCHEMY_PASSWORD='pleasehackme'
    SQLALCHEMY_DATABASE_NAME='imamoron'
    SQLALCHEMY_TABLE='passwords_table'
    SQLALCHEMY_DB_SCHEMA='public'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AWS
    AWS_SECRET_KEY = 'OBIVU5BIG$%&*IRTU#GV&^UHACKEDYGFTI7U5EGEWRG'
    AWS_KEY_ID = 'B&*D%F^&IYGUIFU'

    # My API
    API_ENDPOINT = 'http://unsecureendpoint.com/'
    API_ACCESS_TOKEN = 'HBV%^&UDFIUGFYGJHVIFUJ'
    API_CLIENT_ID = '3857463'

    # Test User Details
    TEST_USER = 'Johnny "My Real Name" Boi'
    TEST_PASSWORD = 'myactualpassword'
    TEST_SOCIAL_SECURITY_NUMBER = '420-69-1738'
    TEST_SECURITY_QUESTION = 'Main Street, USA'


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
