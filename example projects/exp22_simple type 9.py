class L:    
    def __getitem__(self, index):
        print(index)

l = L()
print(l[2:8])

class LL:
    def __init__(self,data):
        self.data = data
        
    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self,index,value):
        self.data[index] = value

ll = LL([1,2,3,4,5])
print(ll[1])
ll[2:4] = [-1,-1]
print(ll[:])

class I:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value * 2

i = I(1,5)
for x in i:
    print(x, end = " ")

class C:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        print("Found")
        return item in self.data

c = C([1,2,3,4,5])
print(3 in c)

class D:
    def __init__(self,data):
        return self.data

    def __iter__(self):
        print("Iter", end=" -> ")
        self.i = 0
        return self

    def __next__(self):
        print("Next", edn=" -> ")
        if self.i == len(data):
            raise StopIteration
        item = self.data[self.i]
        self.i += data
        return item

    
