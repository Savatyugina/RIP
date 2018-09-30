from rectangle import Rectangle
from color_fig import Color


class Quadrate (Rectangle):
    NAME = "Квадрат"

    @classmethod
    def get_name(cls):
        return cls.NAME

    def __init__(self, a, c):
        self.weight = a
        self.color = Color(c)

    def square(self):
        return self.weight * self.weight

    def __repr__(self):
        return Quadrate.get_name() + " площадь {0}, color {1}".format(self.square(), self.color.x)