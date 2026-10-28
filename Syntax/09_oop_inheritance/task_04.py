class Employee:
    def __init__(self, name, salary):
        self.name, self.salary = name, salary
        
    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', salary={self.salary})"
    
    def get_pay(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self, name, salary, bonus):
         super().__init__(name, salary)
         self.bonus = bonus
         
    def get_pay(self):
        return super().get_pay() + self.bonus
    
class Developer(Employee):
    def __init__(self, name, salary, projects):
         super().__init__(name, salary)
         self.projects = projects
         
    def get_pay(self):
        return super().get_pay() + self.projects * 1000
    

employees = [
    Employee("Иван", 50000),
    Manager("Анна", 80000, 20000),
    Developer("Петр", 60000, 3),
    Developer("Елена", 70000, 1),
    Employee("Олег", 45000)
]

total_payout = sum(emp.get_pay() for emp in employees)

print("Список сотрудников:")
for emp in employees:
    print(emp)

print(f"\nОбщая выплата по списку: {total_payout}")