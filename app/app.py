from flask import Flask
from app import authentication, simple_pages
import os
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager

def create_app():
  app = Flask(__name__)

  app.config.from_object('app.config')
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1) if os.environ.get('DATABASE_URL') else 'sqlite:///database.db'

  register_extensions(app)
  register_blueprints(app)

  return app


def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db)
  login_manager.init_app(app)

  return None

def register_blueprints(app: Flask):
  app.register_blueprint(simple_pages.routes.blueprint)
  app.register_blueprint(authentication.routes.blueprint)

  return None

# registration + login validation error handeling