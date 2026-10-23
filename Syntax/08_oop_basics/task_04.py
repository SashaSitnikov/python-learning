class Basket:
    def __init__(self):
        self.items = []
        
    def add(self, item):
        self.items.append(item)
        
b1 = Basket()
b2 = Basket()

b1.add("apple")
print(b2.items)
