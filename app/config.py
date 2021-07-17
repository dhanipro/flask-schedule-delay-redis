import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:example@db/example'
    REDIS_URL = os.getenv('REDIS_URL')