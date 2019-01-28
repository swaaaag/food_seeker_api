"""
Enjoy The Code!
"""
#__Auther__:__blank__
from flask import jsonify
from app.models.restaurant import Restaurant
from app.validators.restaurant import RestaurantForm
from app.libs.error_code import CreateSuccess
from app.libs.token_auth import auth
from models.base import db
from . import api


@api.route('/restaurant/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
    return jsonify(restaurant)


@api.route('/canteen/<int:canteen_id>/restaurants', methods=['GET'])
def get_restaurant_by_canteen(canteen_id):
    restaurants = Restaurant.query.filter_by(canteen_id=canteen_id).custom_paginate()
    return jsonify(restaurants)


@api.route('/restaurant', methods=['POST'])
@auth.login_required
def create_restaurant():
    form = RestaurantForm().validate_for_api()
    with db.auto_commit():
        restaurant = Restaurant()
        restaurant.set_attrs(form)
        db.session.add(restaurant)
    return CreateSuccess()