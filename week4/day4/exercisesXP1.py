EX1_______________________________

def display_message():
	print("It was a very informative lesson - I learned functions!")
display_message()

EX2__________________________________
def favorite_book(title):
	print(f"One of my favorite books is " + title)
favorite_book("The HOBBIT")

EX3__________________________________
def describe_city(city, country="Israel"):
	print( city + " is in " + country)

describe_city("Tel aviv", "Israel")

EX4__________________________________
import random 
y = random.randint(1, 100)

	print (y)
	

return x,y 
random_num(10, y)

import random
def random_num (x):
	random.seed(10)
	y = random.randint(1, 100)
	print(x, y)
	if x == y:
 		print("a")
	elif x != y:
 		print ("Failed")
random_num (2)


EX5__________________________________
def make_shirt(size = "Large", script = "I love Python"):
	if size == "Large" or "Medium":
		print(f"The size of the shirt is " + size + " The script on the shirt is " + script)
	elif size == "Small":
		print(f"The size of the shirt is " + size + " The script on the shirt is +")

make_shirt("Small", "I love Unicorn")
make_shirt("Large")

#EX6__________________________________

# # i=0
# def show_magicians(li):
# 	magician_name=[]
# 	print(magician_name)
# show_magicians(["Steve", "Jen", "Lenon"])

# def make_great(li):
# 	great = []
# 	great = magician_name.append(" the great")
# 	print(great)
# make_great()


# 	for names in usernames: 
# 	print(show_magicians(names[i]))
# 	i+=1
# show_magicians(names)

# def highest_even(li):
# 	evens = []
# 	for item in li:
# 		if item % 2 == 0:
# 		 evens.append(item)
# 	return max (evens)
	
# print(highest_even([10, 2, 3, 4,8,11]))