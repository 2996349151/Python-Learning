class D:
    def __get__(self, instance, owner):
        print(f"get~\nself -> {self}\ninstance - > {instance}\nowner - > {owner}")

    def __set__(self, instance, value):
        print(f"set~\nself -> {self}\ninstance - > {instance}\nvalue - > {value}")

    def __delete__(self, instance):
        print(f"del~\nself -> {self}\ninstance - > {instance}")

class C:
    x= D()

c = C()
c.x = 250
c.x
del c.x
#-------------------------------------------------------------------------------
class E:
    def __get__(self, instance, owner):
        return instance._x
    def __set__(self, instance, value):
        instance._x = value
    def __delete__(self, instance):
        del instance._x

class F:
    def __init__(self, x=250):
        self._x = x
    x = E()

f = F()
print(f.x)
print(f.__dict__)
del f.x
print(f.__dict__)
#------------------------------------------------------------------------------
class MyProperty():
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel

    def __get__(self,instance,owner):
        return self.fget(instance)
    def __set__(self,instance,value):
        return self.fset(instance,value)
    def __delete__(self,instance):
        self.fdel(instance)
    def getter(self, func):
        self.fget = func
        return self
    def setter(self, func):
        self.fset = func
        return self
    def deleter(self,func):
        self.fdel = func
        
class G:
    def __init__(self):
        self._x = 250
    def getx(self):
        return self._x
    def setx(self,value):
        self._x = value
    def delx(self):
        del self._x
    x = MyProperty(getx,setx,delx) #descriptor

g = G()
print(g.x)
g.x=520
print(g.__dict__)
del g.x
print(g.__dict__)
#-------------------------------------------------------------------
class H:
    def __init__(self):
        self._x = 250
    @MyProperty
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x
h = H()
print(h.x)
h.x=520
print(h.__dict__)
del h.x
print(h.__dict__)
