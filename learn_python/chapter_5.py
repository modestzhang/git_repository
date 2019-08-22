 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/8/21 22:34
# @Author    : modestzhang
# @project   : git_repository
# @File      : chapter_5.py
# @Copyright : Manjusaka

# for 循环
cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 判断
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

age = 19
if age >= 18:
    print("You are old enough to vote")
elif age > 16:
    print("You")
else:
    print("Sorry, you are too young to vote")
