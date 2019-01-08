from abc import ABCMeta, abstractmethod

class MyFigure(metaclass=ABCMeta):

    @abstractmethod
    def square(self):
        pass