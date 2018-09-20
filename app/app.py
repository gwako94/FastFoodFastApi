from flask import Flask

from config import app_config

from .v1.views.orderView import v1_order
from .v1.views.userView import v1_user

def create_app(env_name):
  """ Create app """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])
  app.register_blueprint(v1_order, url_prefix='/api/v1/orders')
  app.register_blueprint(v1_user, url_prefix="/api/v1/auth/register")

  @app.route('/', methods=['GET'])
  def index():
    return '<h1 style="text-align:center; color:red;">Welcome to fast food fast api <h1>\
    <h2 style="text-align:center; color:#329495;">Endpoints covered <h2>\
    <div style="text-align:center; background-color:#fff;">\
            POST: /api/v1/orders<br><br>\
            GET: /api/v1/orders/order_id<br><br>\
            GET: /api/v1/orders<br><br>\
            PUT: /api/v1/orders/order_id<br><br>\
    <div> '
    
  
  return app