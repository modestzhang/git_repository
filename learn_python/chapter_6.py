#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/8/22 22:25
# @Author    : modestzhang
# @project   : learn_python
# @File      : chapter_6.py
# @Copyright : Manjusaka


allien_0 = {'color': 'green', 'points': 5}
print(allien_0['color'])
print(allien_0['points'])
allien_0['x_position'] = 0
allien_0['y_position'] = 25
print(allien_0)
del allien_0['points']
print(allien_0)


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for k, v in user_0.items():
    print(k + v)
for k in user_0.keys():
    print(k)
for k in sorted(user_0.keys()):
    print(k.title())
