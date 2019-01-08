class Color:
    def __init__(self, col):
        self._x = col
        self.x = col

        @property
        def x2(self):
            return self._x

        @x2.setter
        def x2(self, value):
            self._x = value

        @x2.deleter
        def x2(self):
            del self._x
