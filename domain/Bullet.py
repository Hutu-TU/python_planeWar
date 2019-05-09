# !/usr/bin/python
# -*- coding: UTF-8 -*-
from BaseBullet import BaseBullet


class Bullet(BaseBullet):
    def __init__(self, screen, x, y):
        BaseBullet.__init__(self, screen, x + 40, y - 20, "./images/bullet.png")

    def move(self, bullet_remove_list):
        self.y -= 10
        if self.y <= 0:
            bullet_remove_list.append(self)
