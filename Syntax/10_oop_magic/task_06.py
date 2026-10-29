class ReprMixin:
    def __repr__(self):
        items = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        return f"{type(self).__name__}({items})"
    
class JsonMixin:
    def to_dict(self):
        return dict(vars(self))
    
class User(ReprMixin):
    def __init__(self, name, age):
        self.name, self.age = name, age

class Product(ReprMixin):
    def __init__(self, product, price):
        self.product, self.price = product, price 
        
class Employee(ReprMixin, JsonMixin):
    def __init__(self, experience, post):
        self.experience, self.post = experience, post
        
print(Employee(14, "Программист"))
print(Employee.__mro__)