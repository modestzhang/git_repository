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
#for......else......的执行顺序为：当迭代对象完成所有迭代后且此时的迭代对象为空时，如果存在else子句则执行else子句，
#没有则继续执行后续代码；如果迭代对象因为某种原因（如带有break关键字）提前退出迭代，则else子句不会被执行，程序将会直接跳过else子句继续执行后续代码
