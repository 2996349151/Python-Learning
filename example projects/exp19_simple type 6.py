class C:
    def __init__(self, x):
        self.__x = x #private variable

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        print(self.__x)

    def __hide(self):
        print("123")
        
c = C(1)
c.get_x()
print(c._C__x)
c._C__hide()
c.__dict__['y'] = 666
c.__dict__

class D:
    __slots__ = ["x"] #class can only has "x" attribute

    def __init__(self,x,y):
        self.x = x
        self.y = y

d = D(1,2)
