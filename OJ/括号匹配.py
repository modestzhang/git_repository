#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/9/5 21:40
# @Author    : modestzhang
# @project   : git_repository
# @File      : 括号匹配.py
# @Copyright : Manjusaka


def func():
    for i in range(6):
        s = list(input())
        res = ['error']
        for j in range(len(s)):
            if s[j] == '(' or s[j] == '[' or s[j] == '{' or s[j] == '<':
                res.append(s[j])
            elif s[j] == ')' and res[-1] == '(':
                res.pop()
            elif s[j] == ']' and res[-1] == '[':
                res.pop()
            elif s[j] == '}' and res[-1] == '{':
                res.pop()
            elif s[j] == '>' and res[-1] == '<':
                res.pop()
            else:
                print('no')
                break
        if len(res) == 1:
            print('yes')
        else:
            print('no')


if __name__ == "__main__":
    func()
