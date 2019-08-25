#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/8/25 21:19
# @Author    : modestzhang
# @project   : learn_python
# @File      : chapter_8.py
# @Copyright : Manjusaka


# def greet_user():
#     print("Hello")
#
#
# greet_user()


# def describe_pet(animal_type, pet_name, pet_year=''):
#     print("\nI have a " + animal_type + ".")
#     print("My" + animal_type + "'s name is " +pet_name.title() + ".")
#
#
# describe_pet(animal_type='hamster', pet_name='harry')


# 禁止函数修改列表
# function_name(list_name[:])


# 传递任意数量的实参
# def make_pizza(*toppings):
#     print(toppings)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'elinstein', location='princeton', field='physics')
print(user_profile)

# 导入模块中的所有函数
# from moudle_name import *
# make_pizza()  不需要用 .

# 给形参制定默认值时，等号两边不要有空格