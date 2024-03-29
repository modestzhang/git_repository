#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/9/19 22:23
# @Author    : modestzhang
# @project   : git_repository
# @File      : ship.py
# @Copyright : Manjusaka


import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settigs = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将新飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船属性centere中存储小数值
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #  根据移动标志调整飞船位置
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settigs.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settigs.ship_speed_factor

        # 根据center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
