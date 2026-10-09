def is_even(n):
    return True if n % 2 == 0 else False


def max_of_three(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result
    

print(is_even(7))
print(max_of_three(17, 3, 92))