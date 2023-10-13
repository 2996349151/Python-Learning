def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of

square = power(2)
cube = power(3)

print(square(2))
print(cube(5))
