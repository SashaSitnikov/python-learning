class Countdown:
    def __init__(self, n):
        self.n = n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        value = self.n
        self.n -= 1
        return value

c = Countdown(3)
print(list(c))
print(list(c))  # []

class Range2:
    def __init__(self, n):
        self.n = n
        
    def __iter__(self):
        for i in range(self.n, 0, -1):
            yield i
            

r = Range2(3)
print(list(r))
print(list(r))