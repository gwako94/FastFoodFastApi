from flask import request, jsonify, Blueprint
from app.v1.models.orderModel import Menu, Order

v1_order = Blueprint('orders', __name__)


menu = Menu() #Menu instance
orders = Order() #Order instance

@v1_order.route('', methods=['POST'])
def add_order():
	data = request.get_json()
	orders.place_order(
		user = data["user"],
		cart = data["cart"]
	)
	return jsonify({'message': 'Order placed successfully'}), 201

@v1_order.route('', methods=['GET'])
def get_orders():
	""" Gets all existing orders """
	if not orders:
 		return jsonify({'message': 'No orders found!'}), 404

	return jsonify({'Orders': orders.orders}), 200