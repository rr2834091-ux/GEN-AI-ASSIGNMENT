# Inheritance Example
class Employee:
    def details(self):
        print("Employee Name:R.Ragul")
        print("Company: TCS")
class Developer(Employee):
    def work(self):
        print("Role:GenAi eng")
obj = Developer()
obj.details()   
obj.work()       
