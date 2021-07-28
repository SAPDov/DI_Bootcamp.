
class Farm:
	def __init__(self, farm_name):
		self.farm_name =farm_name
		print(f"{farm_name}'s farm")
		self.dct_animals= {}

	def add_animal(self, animal, count=1):
		if animal in self.dct_animals.keys():
			self.dct_animals [f'{animal}'] = self.dct_animals [f'{animal}'] + count
		else:
			self.dct_animals [f'{animal}'] = count

		print (self.dct_animals)
 
	def get_animal_types(self):
		sort_list = self.dct_animals.keys()
		print(sorted(sort_list))
	
	def get_info (self):
		print(f"{self.farm_name}'s farm")
		for animal, count in self.dct_animals.items():	
			print("{}: {}".format(animal, count))
		print("E-I-E-I-0!")
		
	def get_short_info (self):
		print("{}'s has {}".format(self.farm_name, "s,".join(list(self.dct_animals.keys()))))


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_animal_types()
macdonald.get_short_info()
macdonald.get_info()