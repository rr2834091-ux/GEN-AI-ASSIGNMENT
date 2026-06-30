#Class Variable,Instance variables:
class Employee:
    Company='TCS'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
E1=Employee('Ragul',45000)
E2=Employee('Kabilesh',50000)
print(E1.name,E1.salary,E1.Company)
print(E2.name,E2.salary,E2.Company)
