class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.__secret = "1234"

acc = Account("Иван", 5000)
print("Атрибуты объекта через vars():")
print(vars(acc))

print(f"\nОбращение к секрету: {acc._Account__secret}") 
