# Exercise 1 : Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


cat1 = Bengal('Bengal', 10)
cat2 = Chartreux('Chartreux', 12)
cat3 = Persian('Burmese', 7)
my_cats = [cat1, cat2, cat3]
my_pets = Pets(my_cats)
my_pets.walk()

 # Exercise 2 : Dogs

class Dog():
    def __init__(self, name, age, weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark (self):
        print(f"{self.name} is barking.")

    def run_speed (self):
        return self.weight / self.age * 10


    def fight (self, other_dog):
        if self.run_speed()* self.weight > other_dog.run_speed()*10: 
            print(f"{self.name} is the winner")
        else:
            print(f"{other_dog.name} is the winner")

dog1=Dog("Rexi", 7, 10)
dog2=Dog("Pinki", 9, 20)
dog3=Dog("Shadow", 14, 9)

dogs=[dog1, dog2, dog3]

for dog in dogs:
    dog.run_speed()

for dog in dogs:
    dog.bark()

dog3.fight(dog1)
dog2.fight(dog3)