#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/9/4 22:11
# @Author    : modestzhang
# @project   : git_repository
# @File      : 数列之和.py
# @Copyright : Manjusaka


def func():
    m, n = map(int, input().split())
    res = []
    tmp = 0
    for i in range(n, 0, -1):
        res.append(str(int(str(m * i)[-1]) + tmp))
        if m * i > 10:
            tmp = int(str(m * i)[-2])
        else:
            tmp = 0
    res.reverse()
    if res.count('0') == n:
        print('0')
    else:
        print(''.join(res))


if __name__ == "__main__":
    func()
