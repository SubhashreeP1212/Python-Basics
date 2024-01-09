class Employee:
#constructors
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary =salary
        print("Employee")
#predefined constructors to print string only
    def __str__(self):
        return (self.name)

#methods inside class
    def bonus(self):
        x=(self.salary*10) + self.salary
        return x
    @staticmethod
    def companyaddress(self):
        address="Amsterdam"
        print(address)

m1=Employee("John",34,1000)
print(m1)
print(m1.bonus()) #for instance method self is not considered as ana rgument
Employee.companyaddress("address") #for static method you need to provide one argument for self