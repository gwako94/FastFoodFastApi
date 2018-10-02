from flask import request, jsonify, Blueprint
import psycopg2
import datetime
import json

#import local files
from app.v2.models.orderModel import Order
from app.v2.auth import token_required

now = datetime.datetime.now()
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
        return jsonify({'message': 'Order successfully placed!'}), 201
    except psycopg2.ProgrammingError:
        return jsonify({'message': 'food item not found!'}), 404

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
       return jsonify({'Orders': 'New here? Please Order!'}), 404
    
@v2_order.route('/orders', methods=['GET'])
@token_required
def fetch_all_orders(current_user):
    orders = Order.get_all_orders()
    if current_user['admin']:
        if orders:
            return jsonify({'Orders': orders}), 200
        return jsonify({'message': 'No orders found!'}), 404
    return jsonify({'message': 'You are not authorized to perform this function!'}), 403

@v2_order.route('/orders/<order_id>', methods=['GET'])
@token_required
def fetch_specific_order(current_user, order_id):
    order = Order.get_order_by_id(order_id)
    if current_user['admin']:
        if order:
            return jsonify({'Order': order}), 200
        return jsonify({'message': 'Order not found!'}), 404
    return jsonify({'message': 'You are not authorized to perform this function!'}), 403


@v2_order.route('/orders/<order_id>', methods=['PUT'])
@token_required
def update_status(current_user, order_id): 
    order = Order.get_order_by_id(order_id)
    data = request.get_json()
    if current_user['admin']:
        if order:
            status = data['status']
            updated_at = now
            order = Order.update_order(order_id, status, updated_at)
            return jsonify({'message': 'Order updated successfully!', 
                            'Order': order}), 200
        return jsonify({'message': 'Order not found!'}), 404
    return jsonify({'message': 'You are not authorized to perform this function!'}), 403


