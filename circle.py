from first import MyFigure
from color_fig import Color
from math import pi


class Circle(MyFigure):
    NAME = "Круг"

    @classmethod
    def get_name(cls):
        return cls.NAME

    def __init__(self, r, c):
        self.rad = r
        self.color = Color(c)

    def square(self):
        return pi * self.rad * self.rad

    def __repr__(self):
        return Circle.get_name() + " площадь {0}, color {1}".format(self.square(), self.color.x)