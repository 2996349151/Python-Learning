class CapStr(str):
    def __new__(cls, string): #before __init__
        string = string.upper()
        return super().__new__(cls, string)

cs = CapStr("aBc")
print(cs)

class A:
    def __init__(self):
        pass

    def __del__(self):
        print("end")

a = A()
del a

a = A()
b = a
del a
del b


