# Exercise 1 : Favorite Numbers


# my_fav_numbers ={7, 18, 5, 36, 21}
# my_fav_numbers.add(27)
# my_fav_numbers.add(23)
# print(my_fav_numbers)
# my_fav_numbers.remove(27)
# print(my_fav_numbers)

# friend_fav_numbers = {8, 9, 5, 20, 15}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)


# # Exercise 3: Print A Range Of Numbers
# for num in range(1,21):
# 	print(num)

# # Exercise 5: Shopping List
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.append("Kiwi")
# print(basket)
# basket.insert(0, "Apples")
# print(basket)
# print(basket.count("Apples"))
# print(basket)
# basket.clear()
# print(basket)

# Exercise 6 : Loop

# my_name = "Sapir"
# your_name = input("What is your name")
# while my_name != your_name:
# 	your_name = input("What is your name")

# Exercise 7

# li = [1, 2, 14, 17, 20, 21, 80]
# print(li[::2])

# Exercise 8
# for num in range(1500, 2501):
# 	if (num % 5 == 0 and num % 7 == 0 ): 
# 		print(num)

# Exercise 9: Favorite Fruits

Favorite_fruits = input("Input your favorite fruit/s, put a space between each fruit:")
li_fruit = list(Favorite_fruit)
i=0
one_fruit = input("Input a name of any fruit:")
for i in li_fruit:  
 	if one_fruit == Favorite_fruit[i]:
		print("You chose one of your favorite fruits Enjoy") 
		i+=1
	else:
		print("You chose a new fruit. I hope you enjoy!”)
		
