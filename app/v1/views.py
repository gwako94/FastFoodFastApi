from flask import Flask, request, jsonify
from models import Menu, Order


app = Flask(__name__)

menu = Menu()
orders = Order().orders

@app.route('/api/v1/orders', methods=['POST'])
def create_order():
	data = request.get_json()
	order_id = str(len(orders) + 1)
	item_price = int(menu.get_item_price(data["item"]))
	item_quantity = int(data["quantity"])
	total = item_price * item_quantity
	order_details = []
	new_order = {
		"id": order_id,
		"owner": data["owner"],
		"item": data["item"],
		"price": item_price,
		"quantity": item_quantity,
		"total": total,
		"status": "pending"
	}
	order_details.append(new_order)
	orders[order_id] = order_details

	return jsonify({'message': 'Order placed successfully'}), 201

@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
	""" Gets all existing orders """
	if not orders:
		return jsonify({'message': 'No orders found!'}), 404

	return jsonify({'Orders': orders}), 200

@app.route('/api/v1/orders/<order_id>', methods=['GET'])
def fetch_specific_order(order_id):
	""" Fetch a specific order using given id"""
	if not orders:
		return jsonify({'message': 'Order not found!'}), 404

	the_order = orders[order_id]
	return jsonify({'Order': the_order}), 200


@app.route('/api/v1/orders/<order_id>', methods=['PUT'])
def update_order_status(order_id):
	""" Updates order status to either accepted, declined, or completed"""
	if not orders:
		return jsonify({'message': 'Order not found!'}), 400

	updated_order = orders[order_id]
	updated_order[0]['status'] = "completed"
	return jsonify({'message': 'Order updated successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)