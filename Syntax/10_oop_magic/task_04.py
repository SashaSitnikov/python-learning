from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        
    def __repr__(self):
        return f"Money={self.amount}, Value={self.currency}"
        
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return (self.amount, self.currency) == (other.amount, other.currency)
    
    def __lt__(self, other):
        if self.currency != other.currency:
            return NotImplemented
        return self.amount < other.amount
    
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if other.currency != self.currency:
            raise ValueError(f"Неверная валюта! Возможная валюта: {self.currency}")
        return Money(self.amount + other.amount, self.currency)
    
    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

wallet = [
    Money(500, "RUB"),
    Money(100, "RUB"),
    Money(1000, "RUB"),
    Money(50, "RUB")
]

wallet.sort()
print(f"Отсортированный кошелек: {wallet}")

total_sum = sum(wallet)
print(f"Общая сумма в кошельке: {total_sum}")

print("\n--- Пробуем сложить разные валюты ---")
try:
    Money(100, "RUB") + Money(10, "USD")
except ValueError as e:
    print(f"Поймали ошибку: {e}")