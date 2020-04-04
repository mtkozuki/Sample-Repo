#inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("idk")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age) #Runs the initialization of the parent class
        self.color = color

    def speak(self):
        print("meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("bark")

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34, "Brown")
c.show()