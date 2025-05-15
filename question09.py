#A:
#This line creates the class "Customer" which takes from the parent class "Person"
#class Customer(Person):
#B:
#This line creates the method for the class, allowing it to have a name inputted
    #def __init__(self, name):
       #self.name = name
#C:
class Person():
    def __init__(self):
        self.name = ""

class Customer(Person):
    def __init__(self):
        super().__init__()

    def yell(self):
        print(self.name, ":", "AAAAAAAAH!")

def main():
    bob_customer = Customer()
    bob_customer.name = "Bob"
    bob_customer.yell()

main()