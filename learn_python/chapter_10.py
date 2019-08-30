#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/8/30 22:37
# @Author    : modestzhang
# @project   : git_repository
# @File      : chapter_10.py
# @Copyright : Manjusaka


with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
