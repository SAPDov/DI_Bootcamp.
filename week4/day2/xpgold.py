#Exercise 1 : Concatenate Lists

li1 = [1, 2, 3, 5, 8]
li2 = ['a', 'f', 'r', 'e', 'l']

for letter in li2:
	li1.append(letter)

print(li2)
print(li1)

#Exercise 2: Greatest Number


	
num1 = input(f"Input the 1st number ")
num2 = input(f"Input the 2nd number ")
num3 = input(f"Input the 3rd number ")

list_num = [num1, num2, num3]
print(max(list_num))



# Exercise 3 : The Alphabet

import string
alphabet_upper = list(string.ascii_uppercase)
alphabet_lower = list(string.ascii_lowercase)
list = alphabet_upper + alphabet_lower
vowels= ['a','e','i','o','u']

for letter in list:
	if letter in vowels:
		print (letter , " is a vowel")
	else:
		print (letter , " is a consonant")


# Exercise 4 :

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
current_name = input("Insert you name: ")

for i, name in enumerate (names):	
	if current_name in name:
		print("The index is ", i)
else:		
	print(current_name, "is not found")

# Exercise 5 : Words And Letters

words=[]
num = 0
letter = input("Insert a letter ")
if len(letter) > 1:
	print('Insert a valid letter')

while num < 8:
	word = input("Insert a word - total of 7 words ")
	words.append(word)
	num += 1

for i, word in enumerate (words):
	if letter in word:
		print(f'In {word} The index is {i}')
	else:
		print(f"{word} doesn't contain the {letter}")


# Exercise 6 :
list_num = [num for num in range (1, 1000001)]
print(min(list_num))
print(max(list_num))
print(sum(list_num))


# Exercise 7 :
seq_input = input("Insert a sequence of comma - separated numbers")

list_seq = seq_input.split(',') 
print(list_seq)

tuple_list = tuple(list_seq)
print(tuple_list)

# Exercise 8 : Random Number
import random
random_num = random.randint(1,9)
print(random_num)
dic_lost_win = {}
# {"lost": 0, "won": 0}
active = True

while active:
	user_num = int(input("Guess a number between 1-9 (including), to quit press q "))
	if user_num == random_num:
		print("Winner")
		active = False
		dic_lost_win['won'] = dic_lost_win.get("won", 0) + 1

	elif user_num != random_num:
		print("Better luck next time")
		dic_lost_win['lost'] = dic_lost_win.get("lost", 0) + 1

	elif user_num == 'q':
		active = False
		print(dic_lost_win)




