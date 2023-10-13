class S(str):
    def __add__(self, other):
        return len(self) + len(other)

class Ss(str):
    def __add__(self, other):
        return NotImplemented
    
class SS(str):
    def __radd__(self, other): #valid only for two different types
        return len(self) + len(other)

class SSS(str):
    def __iadd__(self,other): #valid when add or radd not valid
        return len(self) + len(other)
    
s1 = S("a")
s2 = S("bcd")
s3 = "bcd"
print(s1 + s2)
print(s1 + s3)
print(s3 + s1)

s4 = Ss("asdfg")
s5 = SS("asdf")
print(s4 + s5)

s6 = SSS("asdf")
s6 += s1
print(s6)

s5 += s5
print(s5)
