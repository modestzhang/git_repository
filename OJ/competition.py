#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/8/30 21:51
# @Author    : modestzhang
# @project   : git_repository
# @File      : competition.py
# @Copyright : Manjusaka


def func():
    n, k = map(int, input().split())
    score = list(int(x) for x in input().split())
    score.sort(reverse=True)
    res = score[:k]
    for i in range(k, n):
        if score[i] == score[k-1]:
            res.append(score[i])
        else:
            break
    res = [i for i in res if i > 0]
    print(len(res))


if __name__ == "__main__":
    func()
