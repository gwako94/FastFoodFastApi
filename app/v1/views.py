from flask import Flask, request, jsonify
from models import Menu, Order


app = Flask(__name__)

menu = Menu()
orders = Order().orders

@app.route('/api/v1/orders', methods=['POST'])
def create_order():
	data = request.get_json()
	order_id = str(len(orders) + 1)
	item_price = menu.get_item_price(data["item"])
	item_quantity = data["quantity"]
	order_details = []
	new_order = {
		"id": order_id,
		"owner": data["owner"],
		"item": data["item"],
		"price": item_price,
		"quantity": data['quantity'],
		"total": item_price * item_quantity,
		"status": "pending"
	}
	order_details.append(new_order)

	return jsonify({'message': 'Order placed successfully'})


if __name__ == '__main__':
	app.run(debug=True)