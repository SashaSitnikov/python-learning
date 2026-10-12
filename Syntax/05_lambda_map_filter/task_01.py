# 1 version
num = int(input())
square = lambda x: x ** 2
print(square(num))

# 2 version
print((lambda x: x ** 2)(num))


# 1 version
a, b = int(input()), int(input())
add = lambda a, b: a + b
print(add(a, b))

# 2 version
print((lambda a, b: a + b)(a, b))