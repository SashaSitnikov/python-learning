def flatten(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item
        
print(*list(flatten([1, [2, [3, [4]]], 5])))