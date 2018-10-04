from flask import Flask, jsonify
import os

from config import app_config

#import local files
from .v1.views.orderView import v1_order
from .v1.views.userView import v1_user
from .v2.views.userView import v2_user
from .v2.views.menuView import menu
from .v2.views.orderView import v2_order

def create_app(env_name):
  """ Create app """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])
  app.register_blueprint(v1_order, url_prefix='/api/v1/orders')
  app.register_blueprint(v1_user, url_prefix="/auth")
  app.register_blueprint(v2_user, url_prefix="/api/v2")
  app.register_blueprint(menu, url_prefix="/api/v2/menu")
  app.register_blueprint(v2_order, url_prefix="/api/v2")
  

  @app.route('/', methods=['GET'])
  def index():
    return '<h1 style="text-align:center; color:red;">Welcome to fast food fast api <h1>'

  @app.errorhandler(KeyError)
  def key_handler(KeyError):
    return jsonify({'message': '{} is missing! Please input.'.format(KeyError)})

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({'message': 'Please input required fields!'}), 400
  
  @app.errorhandler(404)
  def not_found():
    return jsonify({'message': 'The requested URL was not found'})

  @app.errorhandler(405)
  def not_allowed():
    return jsonify({'message': 'Method not allowed!'})

  return app