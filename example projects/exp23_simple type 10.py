class C:
    def __call__(self, *args, **kwargs):
        print(f"positional args: {args}, keyword args: {kwargs}")

c = C()
c(1,2,3,x=250,y=250)

class D:
    def __init__(self):
        self._x=250
        self._xx=520
    def getx(self):
        return self._x

    def setx(self,value):
        self._x = value

    def delx(self):
        del self._x
    x = property(getx,setx,delx)

    def getxx(self):
        return self._xx
    xx = property(getxx)
    
d = D()
del d.x
print(d.__dict__)
del d.xx
