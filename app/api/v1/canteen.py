"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify
from app.models.canteen import Canteen
from app.validators.canteen import CanteenForm
from app.libs.error_code import CreateSuccess
from models.base import db
from . import api


@api.route('/canteen/<int:canteen_id>', methods=['GET'])
def get_canteen(canteen_id):
    canteen = Canteen.query.filter_by(id=canteen_id).first_or_404()
    return jsonify(canteen)


@api.route('/campus/<int:campus_id>/canteens', methods=['GET'])
def get_canteen_by_campus(campus_id):
    # TODO 分页
    canteens = Canteen.query.filter_by(campus_id=campus_id).all()
    return jsonify(canteens)


@api.route('/canteen', methods=['POST'])
def create_canteen():
    # TODO 权限控制
    form = CanteenForm().validate_for_api()
    with db.auto_commit():
        canteen = Canteen()
        canteen.set_attrs(form)
        db.session.add(canteen)
    return CreateSuccess()
