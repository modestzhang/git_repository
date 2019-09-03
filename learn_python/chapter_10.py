#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/8/30 22:37
# @Author    : modestzhang
# @project   : git_repository
# @File      : chapter_10.py
# @Copyright : Manjusaka


# with open('pi_digits.txt') as file_object:
#     # contents = file_object.read()
#     # print(contents.rstrip())
#     for line in file_object:
#         # print(line)
#         print(line.rstrip())
#
#     lines = file_object.readlines()
#
# for x in lines:
#     print(x.rstrip())


# file_name = 'programming.txt'
#
#
# with open(file_name, 'a') as file_object:
#     file_object.write('I love you.\n')
#     file_object.write('I love you too.\n')

import json

# numbers = [2, 3, 5, 7, 11, 13]
#
# filename = 'numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)


# filename = 'numbers.json'
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
#
# print(numbers)

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("Name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome" + username)
    else:
        username = get_new_username()
        print("will remember" + username)


greet_user()
