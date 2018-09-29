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
        try:
            menu_details.add_menu()
            return jsonify({'message': 'Menu created!'})

        except psycopg2.IntegrityError:
            return jsonify({'message': 'Menu already exists!'})
    return jsonify({'message': 'Only admin can add menu!'})