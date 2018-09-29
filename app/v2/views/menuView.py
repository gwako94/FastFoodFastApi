from flask import request, jsonify, Blueprint, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import datetime
from app.v2.models.menuModel import Menu

menu = Blueprint('menu', __name__)

@menu.route('', methods=['POST'])
def add_menu():
    data = request.get_json()

    menu_details = Menu(
        data['item_name'],
        data['image_url'],
        data['price']
    )

    try:
        menu_details.add_menu()
        return jsonify({'message': 'Menu created!'})

    except psycopg2.IntegrityError:
        return jsonify({'message': 'Menu already exists!'})