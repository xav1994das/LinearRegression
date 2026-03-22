class AdultException(Exception):
    pass

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def get_minor_age(self):
        if self.age>18:
            raise AdultException ("is an adult")
        return self.age
        
    def display(self):
        print("name", self.name)
        print("age", self.get_minor_age())

p1=Person("xav",31)
p1.display()