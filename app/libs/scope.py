# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/17 17:08
'''
from app.libs.enums import ScopeEnum


class Scope:
    permitted = []
    forbidden = []

    def __add__(self, other):
        self.permitted = self.permitted + other.permitted
        self.permitted = list(set(self.permitted))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class User(Scope):
    permitted = [
        'get_authenticated_user',
        'delete_user',
        'update_user',
        'get_canteen_by_campus',
        'get_canteen',
        'get_restaurant_by_canteen',
        'get_restaurant',
        'get_food_by_restaurant',
        'get_food',
        'get_comment_by_restaurant',
        'get_comment',
        'create_comment',
        'get_comment_by_user',
        'delete_comment'
    ]


class Administrator(Scope):
    permitted = [
        'create_canteen',
        'create_restaurant',
        'create_food'
    ]

    def __init__(self):
        self + User()


def is_permitted(scope, endpoint):
    key = str(ScopeEnum(scope).name).title()
    scope = globals()[key]()
    endpoint = endpoint.split('.')[1]

    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.permitted:
        return True

    return False
