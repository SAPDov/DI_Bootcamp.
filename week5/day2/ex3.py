
from exercisesXP import Dog
import random


class PetDog (Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained= trained

    def train (self):
        self.bark()
        self.trained = True
        print(self.trained) 

    def play (self, *args):
        dogs_list=[self.name, *args]

        print(f"\n{','.join(dogs_list)} all play together")
        
    def do_a_trick(self):
        list_tricks=["does a barrel roll", "stands on his back legs", 
        "shakes your hand", "plays dead"]

        if self.trained:
            print(f"\n{self.name}: {random.choice(list_tricks)}\n")


dog4 = PetDog("Dov", 18, 20)
dog5=PetDog("Rendi", 4, 9,)
dog6=PetDog("Sammy", 6, 7)
dog4.train()
dog5.play(dog4.name)
dog4.do_a_trick()
dog4.bark()
dog5.fight(dog6)