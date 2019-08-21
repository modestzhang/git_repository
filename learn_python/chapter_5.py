#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/8/21 22:34
# @Author    : modestzhang
# @project   : git_repository
# @File      : chapter_5.py
# @Copyright : Manjusaka


cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
