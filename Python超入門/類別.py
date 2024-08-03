class Staff:
    def __init__(self, b):
        self.bonus = b
    def salary(self):
        salary = 30000 + self.bonus
        return salary
    
yamamoto = Staff(10000)
print(yamamoto.salary())

mary = Staff(20000)
print(mary.salary())