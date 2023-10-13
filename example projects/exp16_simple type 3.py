class A:
    def __init__(self,x=2,y=2):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

class B(A):
    def __init__(self,x=2,y=2,z=1):
        super().__init__()
        self.z = z

    def add(self):
        return A.add(self) + self.z
    
a = A(y=5)
print(a.add())

b = B()
print(b.add())
