def outer():
    x = 0
    y = 0
    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"now, x = {x}, y = {y}")
    return inner

move = outer()
move(1,2)
move(1,2)
