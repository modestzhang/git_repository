#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/9/11 22:19
# @Author    : modestzhang
# @project   : git_repository
# @File      : 命令提示符.py
# @Copyright : Manjusaka


def func():
    n = int(input())
    dir = ['Users', 'hp']
    for i in range(n):
        cmd = input()
        if cmd[:3] == 'cd ':
            if cmd[3:] == '..':
                if dir:
                    dir.pop()
                    print('C:\\' + '\\'.join(dir))
                else:
                    print('C:\\')
            elif cmd[3:]:
                dir.append(cmd[3:])
                print('C:\\' + '\\'.join(dir))
            else:
                break
        else:
            break


if __name__ == "__main__":
    func()