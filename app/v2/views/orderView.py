from flask import request, jsonify, Blueprint
import psycopg2
import datetime
import json

#import local files
from app.v2.models.orderModel import Order
from app.v2.auth import token_required

v2_order = Blueprint('v2_orders', __name__)


@v2_order.route('/users/orders', methods=['POST'])
@token_required
def place_order(current_user):
    data = request.get_json()
    cart = data['cart']
    total = Order.get_total(cart)
    order_data = Order(
        current_user["id"],
        cart,
        total
    )
   
    try:
        order_data.add_order()
        return jsonify({'Message': 'Order successfully placed!'})
    except psycopg2.ProgrammingError:
        return jsonify({'message': 'Item not found!'})

@v2_order.route('/users/orders', methods=['GET'])
@token_required
def fetch_order_history(current_user):
    orders = Order.get_all_orders()
    user_orders = []
    try:
        for order in orders:
            if order['user_id'] == current_user['id']:
                user_orders.append(order)
        return jsonify({'Orders': user_orders})
    except TypeError:
       return jsonify({'Orders': 'New here? Please Order!'}) 
    





