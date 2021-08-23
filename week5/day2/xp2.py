# Exercise 1 : Family

class Family:
	def __init__(self, members, last_name):
		self.members = members
		self.last_name = last_name

	def born(self, **members):
		self.members.append(members)
		print('congratulations')


	def is_18 (self, name):
		for member in self.members:
			if member['name'] == name and member['age'] > 17:
					return True
		else: return False

	def review_family (self):
		print(self.members)

members = [
		{'name':'Michael','age':35,'gender':'Male','is_child':False},
		{'name':'Sarah','age':32,'gender':'Female','is_child':False}
	]

# smith_family = Family(members, 'Smith')
# smith_family.born(name ='Jon',age = 0 ,gender ='Male',is_child = True)
# print(smith_family.is_18('Jon'))
# smith_family.review_family()

# Exercise 2 : TheIncredibles Family


class TheIncredibles(Family):
	def __init__(self, power, incredible_name):
		super().__init__(members, last_name)
		self.power = power
		self.incredible_name = incredible_name

	def use_power(self):
		for members in self.members:
			if members['age'] > 17:
				print(members ['name'] + 'is' + members['power'] )


members2 = [
		{'name':'Bob','age':35,'gender':'Male','is_child':False,'power':'superhuman strength','incredible_name':'Mr.Incredible'},
        {'name':'Helen','age':35,'gender':'Female','is_child':False,'power':'stretch and reshape her body','incredible_name':'Elastigirl'},
        {'name':'Violet','age':14,'gender':'Female','is_child':True,'power':'invisibility','incredible_name':'Violet'},
        {'name':'Dashiel','age':11,'gender':'Male','is_child':True,'power':'superspeed','incredible_name':'Dash'}]
members2 = [
		{'name':'Bob','age':35,'gender':'Male','is_child':False,'power':'superhuman strength','incredible_name':'Mr.Incredible'},
        {'name':'Helen','age':35,'gender':'Female','is_child':False,'power':'stretch and reshape her body','incredible_name':'Elastigirl'},
]
incredible_family = TheIncredibles(members2)
incredible_family.use_power()

