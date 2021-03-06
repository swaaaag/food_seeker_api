"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify
from app.models.canteen import Canteen
from app.models.canteen_image import CanteenImage
from app.validators.canteen import CanteenCreateForm, CanteenUpdateForm
from app.libs.error_code import CreateSuccess, UpdateSuccess, DeleteSuccess
from app.libs.token_auth import auth
from app.models.base import db
from . import api


@api.route('/canteen/<int:canteen_id>', methods=['GET'])
def get_canteen(canteen_id):
    canteen = Canteen.query.filter_by(id=canteen_id).first_or_404()
    return jsonify(canteen)


@api.route('/campus/<int:campus_id>/canteens', methods=['GET'])
def get_canteens_by_campus(campus_id):
    canteens = Canteen.query.filter_by(campus_id=campus_id).custom_paginate()
    return jsonify(canteens)


@api.route('/canteen', methods=['POST'])
@auth.login_required
def create_canteen():
    form = CanteenCreateForm().validate_for_api()
    Canteen.create_canteen(form)
    return CreateSuccess()


@api.route('/canteen/<int:canteen_id>', methods=['PUT'])
@auth.login_required
def update_canteen(canteen_id):
    # TODO 支持修改图片
    form = CanteenUpdateForm().validate_for_api()
    with db.auto_commit():
        canteen = Canteen.query.get_or_404(canteen_id)
        canteen.set_attrs(form)
        db.session.add(canteen)
    return UpdateSuccess()


@api.route('/canteen/<int:canteen_id>', methods=['DELETE'])
@auth.login_required
def delete_canteen(canteen_id):
    with db.auto_commit():
        canteen = Canteen.query.filter_by(id=canteen_id).first_or_404()
        canteen.delete()
    return DeleteSuccess()
