# Exercise 1 : Hello World

print("hello world. "*4)

# Exercise 2 : Some Math
x = pow(99, 3)*8

print(x)

 # Exercise 4 : Your Computer Brand
 
computer_brand = "DELL"
print(f"I have a {computer_brand} computer")

# Exercise 5 : Your Information
my_name = "Sapir"
age = "29"
shoe_size = "39"
info = my_name + " " + age + " " + shoe_size 
print(info)


# Exercise 6 : A & B
a = 9
b = 7
if a > b:
	print ("Hello World")


# Exercise 7 : Odd Or Even
number = input("Pick a number")

if int(number) % 2 == 0:
	print("even number")
else: 
	print("odd number")

# Exercise 8 : What’s Your Name ?

your_name = input("What is your name? ")

if your_name == my_name:
	print ("You have a wonderful name")
else:
	print("I never heard of such a name")	 

# Exercise 9 : Tall Enough To Ride A Roller Coaster


height = input("What is your height in inches? ")
height = int(height)* 2.54
if height > 145:
	print ("You are tall enough to ride")
else:
	print("You need to grow some more to ride")
