from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
import rq
from .config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('background-task', connection=app.redis)

    # Register blueprints
    from app.transaction.view import bp
    app.register_blueprint(bp)

    return app