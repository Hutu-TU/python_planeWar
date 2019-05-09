# !/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import time

import pygame
import thread
from pygame.locals import *

from domain.HeroPlane import HeroPlane
from domain.EnemyPlane import EnemyPlane


# 界面主入口
def main():
    # 1、设定窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2、加载背景
    background = pygame.image.load("./images/background.png")
    
    # 英雄
    hero = HeroPlane(screen)
    hero.auto_fire()


    # 敌机
    enemy_list = []
    thread.start_new_thread(generate_enemy, (enemy_list, screen))

    # 3、把图片放入窗口
    while True:
        # 加入显示的图片
        screen.blit(background, (0, 0))
        
        hero.display()
        enemy_remove_list = []
        for enemy in enemy_list:
            enemy.display()
            # 移动敌机
            enemy.move(enemy_remove_list)

        # 更新显示内容
        # 监控敌机子弹
        EnemyPlane.monitor_bullet()
        pygame.display.update()
        hero_move(hero)

        # hero子弹打中敌机
        for bullet in hero.bullet_list:
            for enemy in enemy_list:
                if enemy.x - 11 < bullet.x + 11 < enemy.x + 51 + 11 and enemy.y - 11 < bullet.y < enemy.y + 39 + 11:
                    enemy_remove_list.append(enemy)
                    hero.bullet_list.remove(bullet)

        # 移除敌机（避免列表删除时导致的位移问题）
        for enemy_remove in enemy_remove_list:
            if enemy_list.__contains__(enemy_remove):
                enemy_remove.thread_exit_status = True
                enemy_list.remove(enemy_remove)

        time.sleep(0.01)

def generate_enemy(enemy_list, screen):
    while True:
        enemy_list.append(EnemyPlane(screen, random.randint(0, 480 - 51), 0))
        time.sleep(0.75)

def hero_move(hero):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero.move_left_status = True
            elif event.key == K_d or event.key == K_RIGHT:
                hero.move_right_status = True
            elif event.key == K_w or event.key == K_UP:
                hero.move_up_status = True
            elif event.key == K_s or event.key == K_DOWN:
                hero.move_down_status = True
            elif event.key == K_SPACE:
                hero.fire()
        elif event.type == KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                hero.move_left_status = False
            elif event.key == K_d or event.key == K_RIGHT:
                hero.move_right_status = False
            elif event.key == K_w or event.key == K_UP:
                hero.move_up_status = False
            elif event.key == K_s or event.key == K_DOWN:
                hero.move_down_status = False
    hero.move_left()
    hero.move_right()
    hero.move_up()
    hero.move_down()


if __name__ == '__main__':
    main()
