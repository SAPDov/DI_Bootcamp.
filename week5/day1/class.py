

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        print("Hello my name is " + self.name)

    def over_18 (self):
    	if self.age > 18:
    		return True
    	else:
    		return False

person1 = Person('dvir', 17)
person2 = Person('dan', 5)
print(person1.over_18())   
print(person2.over_18())

class Cat:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Exercise 1: Cats external function : ‏max(numbers)‏numbers.append(new_number)‏ Internal cat1.name‏

cat1=Cat("Kitty", 5)
cat2=Cat("Pinki", 25)
cat3=Cat("Doxy", 13)

def oldest_cat(*cats):
	old_cat=cats[0]
	if old_cat.age > 15:
		print(f' {old_cat.name} is the oldest cat')
		print(f'The oldest cat is {old_cat.name}, and it is {old_cat.age} years old.')
	else:
		print('You are not the oldest')

oldest_cat(cat2)

# Exercise 2 : Dogs
class Dog:
	def __init__(self, name, height):
		self.name = name
		self.height = height

	def bark(self):
		print(f'{self.name} goes woof!')

	def jump(self):
		print(f'{self.name} jumps {self.height *2} cm high!')


davids_dog=Dog("Rex", 50)
sarah_dog =Dog("Teacup", 20)

def high_dog():
	if davids_dog.height > sarah_dog.height:
		print(f'{davids_dog.name} is bigger')
	else:
		print(f'{sarah_dog.name} is bigger')

davids_dog.bark()
davids_dog.jump()
sarah_dog.bark()
sarah_dog.jump()
high_dog()


# Exercise 3 : Who’s The Song Producer?

class Song:
	def __init__(self, lyrics):
		self.lyrics=lyrics
	def sing_me_a_song(self):
			for line in self.lyrics:
				print(line)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo

class Zoo:
  def __init__(self, name):
    self.animals = []
    self.name = name
  def add_animal(self, animal):
    if animal not in self.animals:
      self.animals.append(animal)
    print(self.animals)
  def get_animal(self):
    for animal in self.animals:
      print(animal)

  def sell_animal(self, animal_sold):
    if animal_sold in self.animals:
      self.animals.remove(animal_sold)
    print(self.animals)

  def sort_animals(self):
    sort_animal = sorted(self.animals)
    test_list=[]
    tmp=[sort_animal.pop(0)]

    while len(sort_animal) > 0:
      if tmp[0][0] == sort_animal[0][0]:
        tmp.append(sort_animal.pop(0))
      else:
        test_list.append(tmp)
        tmp=[sort_animal.pop(0)]
    test_list.append(tmp)
    number_list=[]

    for i in range(len(test_list)):
      number_list.append(i+1)
    result_dct=dict((key,value) for key,value in zip(number_list, test_list))
    print(result_dct)
		


safari=Zoo('Ramat-Gan')
safari.add_animal('Giraffe')
safari.add_animal('Tiger')
safari.add_animal('Telli')
safari.add_animal('Dog')
safari.add_animal('Donkey')
safari.add_animal('Dolphin')
safari.add_animal('Dolin')
safari.add_animal('Rov')
safari.get_animal()
# safari.sell_animal('Donkey')
safari.sort_animals()

# making a point