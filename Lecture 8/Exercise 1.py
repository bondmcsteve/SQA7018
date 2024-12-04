class Employee:
    def __init__(self, set_salary, n):
        self.salary = set_salary #Saves the input salary value
        self.n = n

    def calculate_future_salary(self):
        return 1.03 ** self.n * self.salary

class Employee:
    def __init__(self, set_salary):
        self.salary = set_salary #Saves the input salary value
        #self.n = n

    def calculate_future_salary(self, n):
        return 1.03 ** n * self.salary