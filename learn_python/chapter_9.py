#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/8/27 21:55
# @Author    : modestzhang
# @project   : learn_python
# @File      : chapter_9.py
# @Copyright : Manjusaka


# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def sit(self):
#         print(self.name.title() + "is now sitting.")
#
#
#     def roll_over(self):
#         print(self.name.title() + "rolled over!")
#
#
# my_dog = Dog('willie', 6)
# my_dog.sit()
# my_dog.roll_over()

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_describe_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return  long_name .title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectriCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # 继承父类的方法__init__()
        self.battery_size = 70


my_tesla = ElectriCar('tesla', 'model s', 2016)
print(my_tesla.get_describe_name())

