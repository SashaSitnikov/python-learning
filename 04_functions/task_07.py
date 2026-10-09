def add_item(item, items=[]):
    items.append(item)
    return items


add_item(1) 
add_item(2) 

# Так нельзя, так как список items с каждым вызовом будет только пополняться




def add_item_fixed(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items