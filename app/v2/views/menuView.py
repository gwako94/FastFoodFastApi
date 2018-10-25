from flask import request, jsonify, Blueprint
import psycopg2
import datetime

# import local files
from app.v2.models.menuModel import Menu
from app.v2.migration import Database
from app.v2.auth import token_required

db = Database()
cur = db.cur

menu = Blueprint('menu', __name__)


@menu.route('', methods=['POST'])
@token_required
def add_menu(current_user):
    data = request.get_json()

    menu_details = Menu(
        data['item_name'],
        data['image_url'],
        data['price']
    )
    if current_user['admin']:
        if menu_details.add_menu():
            return jsonify({'message': 'Menu item created!'}), 201
        return jsonify({'message': '{} already exists!'.format(data['item_name'])}), 409

    return jsonify({'message': 'You are not authorized to perform this function!'}), 403


@menu.route('', methods=['GET'])
def get_all_menu():
    all_menu = Menu.get_all_menu()
    if all_menu:
        menu = [{
            "id": menu["menu_id"],
            "item_name": menu["item_name"],
            "image_url": menu["image_url"],
            "price": str(menu["price"]),
            "created_at": menu["created_at"]
        } for menu in all_menu]
        return jsonify({'Menu': menu}), 200
    return jsonify({'message': 'No menu available!'}), 404

@menu.route('/<menu_id>', methods=['DELETE'])
@token_required
def delete_menu(current_user, menu_id):
    menu = Menu.get_menu_by_id(menu_id)
    if current_user["admin"]:
        if menu:
            query = "DELETE FROM menu WHERE menu_id=%s"
            cur.execute(query, (menu_id, ))
            db.conn.commit()
            return jsonify({"message": "Item deleted successfully!"}), 200
        return jsonify({"message": "Item not found!"}), 404