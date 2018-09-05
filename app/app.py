from flask import Flask

from config import app_config

from .v1.views.orderView import v1_order

def create_app(env_name):
  """ Create app """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])
  app.register_blueprint(v1_order, url_prefix='/api/v1/orders')
  
  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'This is fast food fast api'

  return app