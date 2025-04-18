# super(): Returns a proxy object that delegates method calls to a parent or sibling class
class MyClass:
    x = 10
class SubClass(MyClass):
    def __init__(self, x):
        super().__init__(x)