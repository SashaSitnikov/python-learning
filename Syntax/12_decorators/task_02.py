def make_multiplier(n):
    def mul(x):
        return x * n
    return mul
    
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(11))
print(triple.__closure__[0].cell_contents)


def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())