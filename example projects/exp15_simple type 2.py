class A:
    x = 1

    def show(self):
        print("I am A.")

    def go(self):
        print("A")

class B:
    x = 2

    def show(self):
        print("I am B")
        
class C(A, B):
    
    def go(self):
        print("C")
class Letter:
    x = 3
    a = A()
    b = B()
    def show(self):
        self.a.show()
        self.b.show()

    def set_x(self, v):
        self.x = v
        
c = C()
print(c.x)
c.go()

l = Letter()
l.show()

l.set_x(-1)
print(l.x)
