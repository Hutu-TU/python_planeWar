# !/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import thread
import time

from BasePlane import BasePlane
from domain.EnemyBullet import EnemyBullet

bullet_list = []

class EnemyPlane(BasePlane):

    def __init__(self, screen, x, y):
        BasePlane.__init__(self, screen, x, y, "./images/enemy0.png")
        self.thread_exit_status = False
        num = random.randint(0, 2)
        if num == 1:
            self.direction = "LEFT"
        elif num == 2:
            self.direction = "RIGHT"
        else:
            self.direction = None
        self.auto_fire()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    @staticmethod
    def monitor_bullet():
        bullet_remove_list = []
        for bullet in bullet_list:
            bullet.display()
            bullet.move(bullet_remove_list)
        # 避免删除移位的问题
        for bullet_remove in bullet_remove_list:
            bullet_list.remove(bullet_remove)

    def move(self, enemy_remove_list):
        if self.y > 852:
            enemy_remove_list.append(self)
            self.thread_exit_status = True
        else:
            self.y += 5
        if self.direction == "RIGHT":
            self.x += 2
        elif self.direction == "LEFT":
            self.x -= 2
        if self.x > 480 - 51:
            self.direction = "LEFT"
        if self.x < 0:
            self.direction = "RIGHT"


    def fire(self):
        bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

    def auto_fire(self):
        thread.start_new_thread(self.__auto_fire, ())

    def __auto_fire(self):
        while True:
            if self.thread_exit_status:
                break
            num = random.randint(0, 100)
            if num <= 10:
                self.fire()
            time.sleep(0.5)
