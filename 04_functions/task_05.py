def average(*args):
    if not args:
        return None
    return sum(args) / len(args)

print(average(3, 4, 5))
nums = [3, 4, 5]
print(average(*nums))
print(average())
