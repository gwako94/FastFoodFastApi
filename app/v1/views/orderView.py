from flask import request, jsonify, Blueprint
from app.v1.models.orderModel import Menu, Order
import datetime
v1_order = Blueprint('orders', __name__)


menu = Menu()  # Menu instance
orders = Order()  # Order instance


@v1_order.route('', methods=['POST'])
def add_order():
    data = request.get_json()
    cart = data["cart"]
    total = orders.total(cart)
    orders.place_order(
        user=data["user"],
        cart=data["cart"],
        total=total
    )
    return jsonify({'message': 'Order placed successfully'}), 201


@v1_order.route('', methods=['GET'])
def get_orders():
    """ Gets all existing orders """
    all_orders = orders.get_all_orders()
    if not all_orders:
        return jsonify({'message': 'No orders found!'}), 404

    return jsonify({'Orders': all_orders}), 200


@v1_order.route('<order_id>', methods=['GET'])
def fetch_specific_order(order_id):
    the_order = orders.get_order_by_id(order_id)
    if the_order:
        return jsonify({'Order': the_order}), 200
    return jsonify({'message': 'Order not found!'}), 404


@v1_order.route('<order_id>', methods=['PUT'])
@auth_token_required
def update_order_status(current_user, order_id):
    data = request.get_json()

    all_orders = orders.get_all_orders()
    if not all_orders:
        return jsonify({'message': 'Order not found!'}), 404
    new_status = data['status']
    updated_time = datetime.datetime.now()
    orders.update_order(order_id, new_status, updated_time)
    return jsonify({'message': "Order updated successfully"})
