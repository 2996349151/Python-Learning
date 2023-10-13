def funA():
    x = 1
    def funB():
        print(x)
    return funB

funC = funA()
funC()
