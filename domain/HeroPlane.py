# !/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time

from BasePlane import BasePlane
from Bullet import Bullet


class HeroPlane(BasePlane):

    def __init__(self, screen):
        BasePlane.__init__(self, screen, 200, 700, "./images/hero.gif")
        self.bullet_list = []
        self.move_left_status = False
        self.move_right_status = False
        self.move_up_status = False
        self.move_down_status = False

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        bullet_remove_list = []
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move(bullet_remove_list)
        # 避免删除移位的问题
        for bullet_remove in bullet_remove_list:
            self.bullet_list.remove(bullet_remove)

    def move_left(self):
        if self.x > 0 and self.move_left_status:
            self.x -= 10

    def move_right(self):
        if self.x < (480 - 100) and self.move_right_status:
            self.x += 10

    def move_up(self):
        if self.y > 0 and self.move_up_status:
            self.y -= 10

    def move_down(self):
        if self.y < (852 - 124) and self.move_down_status:
            self.y += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

    def auto_fire(self):
        thread.start_new_thread(self.__auto_fire, ())

    def __auto_fire(self):
        while True:
            self.fire()
            time.sleep(0.25)
