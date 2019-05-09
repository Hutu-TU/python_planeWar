# !/usr/bin/python
# -*- coding: UTF-8 -*-
import pygame

class Base:

    def __init__(self, screen, x, y, image_path):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
