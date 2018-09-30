from flask import request, jsonify, Blueprint, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import datetime

#import local files
from app.v2.models.menuModel import Menu
from app.v2.auth import token_required

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
            return jsonify({'message': 'Menu created!'}), 201
        return jsonify({'message': 'Menu already exists!'}), 400

    return jsonify({'message': 'Cannot perform this function!'}), 401

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
    return jsonify({'message': 'No menu available!'})