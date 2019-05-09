# !/usr/bin/python
# -*- coding: UTF-8 -*-
from Base import Base

class BaseBullet(Base):

    def __init__(self, screen, x, y, image_path):
        Base.__init__(self, screen, x, y, image_path)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
