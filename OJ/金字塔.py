#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/8/29 22:43
# @Author    : modestzhang
# @project   : git_repository
# @File      : 金字塔.py
# @Copyright : Manjusaka


def func():
    while True:
        try:
            n = int(input())
            for i in range(1, n+1):
                res = []
                for j in range(1, i+1):
                    res.append(j)
                for j in range(i-1, 0, -1):
                    res.append(j)
                result = ''.join(str(s) for s in res)
                const = 2*n-1
                print("{0:^19}".format(result))
        except:
            break


if __name__ == "__main__":
    func()
