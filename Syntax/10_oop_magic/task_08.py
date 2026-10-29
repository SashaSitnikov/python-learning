class CartError(Exception):
    """Неверное количество"""

class Product:
    def __init__(self, name, price):
        self._name, self._price = name, price
        
    def __repr__(self):
        return f"Name={self._name}, Price={self._price}"    
    
    def __hash__(self):
        return hash((self._name, self._price))
        
    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self._name, self._price) == (other._name, other._price)
        
class Cart:
    def __init__(self):
        self._items = {}
        
    def add(self, product, qty=1):
        if qty <= 0:
            raise CartError("Количество должно быть больше 0")
        if product in self._items:
            self._items[product] += qty
        else:
            self._items[product] = qty
            
    def remove(self, product, qty=1):
        if qty <= 0:
            raise CartError("Количество должно быть больше 0")
        if product not in self._items:
            raise CartError("Данного товара нет в корзине")
        if self._items[product] < qty:
            raise CartError("В корзине количество товара меньше, чем вы пытаетесь удалить")
        self._items[product] -= qty
        if self._items[product] == 0:
            del self._items[product]
            
    def __len__(self):
        return sum(self._items.values())
    
    def __getitem__(self, product):
        return self._items.get(product, 0)

    def __contains__(self, product):
        return product in self._items
    
    def __iter__(self):
        return iter(self._items.items())
    
    def __bool__(self):
        return bool(self._items)
    
    def __add__(self, other):
        if not isinstance(other, Cart):
            return NotImplemented
        new_cart = Cart()
        for prod, qty in self._items.items():
            new_cart.add(prod, qty)
        for prod, qty in other._items.items():
            new_cart.add(prod, qty)
        return new_cart
    
    @property
    def total(self):
        return sum(product._price * qty for product, qty in self._items.items())
    
    def __repr__(self):
        return f"Cart({self._items}, total={self.total})"
    
    
if __name__ == "__main__":
    apple = Product("Яблоко", 100)
    banana = Product("Банан", 150)
    
    cart1 = Cart()
    cart1.add(apple, 2)
    cart1.add(banana, 1)
    
    cart2 = Cart()
    cart2.add(apple, 3)
    
    print(f"Корзина 1: {cart1}")
    print(f"Всего штук в Корзине 1: {len(cart1)}")
    print(f"Количество бананов: {cart1[banana]}")
    
    cart3 = cart1 + cart2
    print(f"Объединенная Корзина 3: {cart3}")
    
    try:
        cart1.remove(banana, 5)
    except CartError as e:
        print(f"Поймали ошибку: {e}")
