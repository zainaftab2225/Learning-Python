import copy

'''
class Head():
    size = 0

    def __init(self):
        print("head created.")

    def change_size(self, size):
        self.size = size


class Cat():
    name = ""
    color = ""
    weight = 0
    cat_head = None
    # Main Constructor Calls

    def __init__(self, copy_object=None, name=Zain, color=None, weight=None):
        if copy_object is not None:
            self.copy_constructor(copy_object)
        elif name is not None and color is not None and weight is not None:
            self.parameterized_constructor(name, color, weight)
        else:
            self.default_constructor()

    # Parameter Constructor
    def parameterized_constructor(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        self.cat_head = Head()
        print("Parameters set, Cat created.")

    # Copy Constructor
    def copy_constructor(self, copy_object):
        self.name = copy_object.name
        self.color = copy_object.color
        self.weight = copy_object.weight
        print("Parameters copied, a copy Cat is created.")

    # Default Constructor
    def default_constructor(self):
        print("Default Cat created.")

    def meow(self):
        print(self.name, " meows.")


Gat = Cat(None, "Gat", "Red", 50)
Fat = copy.copy(Gat)
Slat = copy.deepcopy(Gat)

print(id(Gat))
print(id(Fat))
print(id(Slat))
Fat.cat_head.size = 100
Slat.cat_head.size = 200

print(Gat.cat_head.size)
print(Fat.cat_head.size)
print(Slat.cat_head.size)
'''

'''
class Person():
    def __init__(self):
        self.name = ""

    def report(self):
        # Basic report
        print("Report for", self.name)


class Employee(Person):
    def __init__(self):
        # Call the parent/super class constructor first
        super().__init__()

        # Now set up our variables
        self.job_title = ""

    def report(self):
        # Here we override report and just do this:
        print("Employee report for", self.name)


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.email = ""

    def report(self):
        # Run the parent report:
        super().report()
        # Now add our own stuff to the end so we do both
        print("Customer e-mail:", self.email)


john_smith = Person()
john_smith.name = "John Smith"

jane_employee = Employee()
jane_employee.name = "Jane Employee"
jane_employee.job_title = "Web Developer"
john_smith = jane_employee

bob_customer = Customer()
bob_customer.name = "Bob Customer"
bob_customer.email = "send_me@spam.com"

john_smith.report()
jane_employee.report()
bob_customer.report()
'''


class Cat():
    def __init__(self):
        self.name = "cat"


class Person():
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        self.cat = Cat()


zain = Person()
zain.name = "Zain"
age = 20
roshaan = Person("Roshaan", 20)

print(zain.name)
print(roshaan.name)

shayan = copy.deepcopy(zain)
zain.cat.name = "GATT"
print(zain.cat.name)
print(shayan.cat.name)
