# Single Inheritance 
class Employee(): # Base Class
    company = "Google"
    name = "Sahil"

    def showDetails(self):
        print(f"The company name is {self.company}")

class Programmer(Employee): # inheriting Employee class
    company = "YouTube"

    def showDetails(self):
        print(f"The company name is {self.company}") # Method overriding

    def pName(self):
        print(f"The company name is {self.name}") # will take value of name from Employee class
        

e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
p.pName()


