#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/9/18 22:09
# @Author    : modestzhang
# @project   : git_repository
# @File      : chapter_11.py
# @Copyright : Manjusaka


# from name_function import get_formatted_name
#
# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == "q":
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
#
#     format_name = get_formatted_name(first, last)
#     print("\nNeatly formatted name: " + format_name + '.')
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        format_name = get_formatted_name('first', 'last')
        self.assertEqual(format_name, 'First last')


unittest.main()
