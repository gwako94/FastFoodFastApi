from flask import request, jsonify, Blueprint
from app.v1.models.orderModel import Menu, Order
import datetime
v1_order = Blueprint('orders', __name__)


menu = Menu()  # Menu instance
orders = Order()  # Order instance

now = datetime.datetime.now()


@v1_order.route('', methods=['POST'])
def add_order():
    data = request.get_json()
    orders.place_order(
        user=data["user"],
            cart=data["cart"]
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
def update_order_status(order_id):
    all_orders = orders.get_all_orders()
    if not all_orders:
        return jsonify({'message': 'Order not found!'}), 404
    orders.update_order(order_id)
    return jsonify({'message': "Order updated successfully"})
