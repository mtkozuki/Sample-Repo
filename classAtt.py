#Class attributes and class methods
class Person():
    number_of_people = 0 #Class variable
    GRAVITY = -9.8

    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod #Act on the class itself
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("tim")
print(Person.number_of_people_())
p2 = Person("jill")
print(Person.number_of_people_())
