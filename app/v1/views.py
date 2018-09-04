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

	return jsonify({'message': 'Order placed successfully'})

@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
	""" Gets all existing orders """
	return jsonify({'Orders': orders})



if __name__ == '__main__':
	app.run(debug=True)