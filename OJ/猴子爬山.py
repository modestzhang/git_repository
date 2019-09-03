#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/9/3 21:55
# @Author    : modestzhang
# @project   : git_repository
# @File      : 猴子爬山.py
# @Copyright : Manjusaka

from functools import reduce


def func():
    n = int(input())
    num_3 = n // 3
    res = 0
    if num_3 > 1:
        for i in range(1, num_3+1):
            res += reduce(lambda x, y: x*y, range((n-3*i+1), (n-2*i+1))) // reduce(lambda x, y: x*y, range(1, i+1))
        res += 1
    elif num_3 == 1:
        res = n % 3 + 2
    else:
        res = 1
    print(res)


if __name__ == "__main__":
    func()
