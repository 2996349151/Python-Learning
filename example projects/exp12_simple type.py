class exp:
    x = 1
    y = "2"
    z = True

    def get_self(self):
        print(self)
        
    def show(self):
        print("show something")



t = exp()
print(t.x)

t.show()

t.k = 10
print(t.k)
