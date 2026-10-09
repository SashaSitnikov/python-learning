def power(base, exp=2):
    return base ** exp


first = power(14)
second = power(2, 10)
third = power(exp=3, base=4)

print(first, second, third, sep='\n')