class MyClass:
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    x = property(get_x, set_x)