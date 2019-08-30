#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/8/30 21:46
# @Author    : modestzhang
# @project   : git_repository
# @File      : equal.py
# @Copyright : Manjusaka


def func():
    while True:
        try:
            a, b = map(int, input().split())
            if a == b:
                print('YES')
            else:
                print('NO')
        except:
            break


if __name__ == "__main__":
    func()
