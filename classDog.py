#Object Oriented Programming in Python

#By default the module that you run is __main__
class Dog:
    #Instantiate the object right when it is created
    def __init__(self, name, age):
        self.name = name #Define a attribute that is inside the class
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def add_one(self, x):
        return x + 1

    def set_age(self, age):
        self.age = age
    
    def set_name(self, name):
        self.name = name

    #A method is a function that goes inside a class
    def bark(self):
        print("bark")

d = Dog("Tim", 32) #When this line is written the init will be called
print(d.get_age(),d.get_name())
