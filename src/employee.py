from src.person import Person 

class Employee(Person):
    def __init__(self, wage, age):
        self.wage = wage
        self.age = age
        self.wallet = 0