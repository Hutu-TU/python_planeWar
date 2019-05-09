# !/usr/bin/python
# -*- coding: UTF-8 -*-
from BaseBullet import BaseBullet

class EnemyBullet(BaseBullet):
    def __init__(self, screen, x, y):
        BaseBullet.__init__(self, screen, x + 22, y + 35, "./images/bullet1.png")

    def move(self, bullet_remove_list):
        self.y += 10
        if self.y > 852:
            bullet_remove_list.append(self)
