#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2019/9/19 21:58
# @Author    : modestzhang
# @project   : git_repository
# @File      : alien_invasion.py
# @Copyright : Manjusaka


import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
