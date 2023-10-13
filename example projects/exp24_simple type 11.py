class C:
    def funA(self):
        print(self)

    @classmethod
    def funB(cls):
        print(cls)

c = C()
c.funA()
c.funB()

class D:
    count = 0
    def __init__(self):
        D.count += 1

    @classmethod
    def get_count(cls):
        print(f"total {cls.count} object")

    @staticmethod
    def funC():
        print(f"total {D.count} object")
d1 = D()
d2 = D()
d3 = D()

d3.get_count()
d3.funC()

