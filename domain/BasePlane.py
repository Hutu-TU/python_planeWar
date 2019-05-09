# !/usr/bin/python
# -*- coding: UTF-8 -*-

from Base import Base


class BasePlane(Base):
    def __init__(self, screen, x, y, image_path):
        Base.__init__(self, screen, x, y, image_path)
