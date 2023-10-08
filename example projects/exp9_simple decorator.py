import time

def logger(msg):
    def time_master(func):
        def call_func():
            start = time.time()
            func()
            stop = time.time()
            print(f"{msg} costs {(stop - start):.2f}")
        return call_func
    return time_master

@logger(msg="A")
def funA():
    time.sleep(1)

@logger(msg="B")
def funB():
    time.sleep(2)

funA()
funB()
