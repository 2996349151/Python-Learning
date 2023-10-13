import time

def time_master(func):
    def call_func():
        print("start")
        start = time.time()
        func()
        stop = time.time()
        print("end")
        print(f"cost {(stop-start):.2f} seconds")
    return call_func

@time_master
def test():
    time.sleep(2)
    print("Hello")

test()
