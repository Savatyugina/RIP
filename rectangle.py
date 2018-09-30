from first import MyFigure
from color_fig import Color


class Rectangle (MyFigure):

        NAME = "Прямоугольник"

        @classmethod
        def get_name(cls):
            return cls.NAME


        def __init__ (self, w, h, c):
            self.weight = w
            self.height = h
            self.color = Color(c)

        def square(self):
            return self.weight * self.height

        def __repr__ (self):
            return Rectangle.get_name() + " площадь {0}, color {1}".format(self.square(), self.color.x)