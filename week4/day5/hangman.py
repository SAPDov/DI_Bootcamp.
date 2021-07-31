import random
import re

def print_gallows():
    gallows = ['0', '/', '|', '\\', '/', '\\']
    fn = gallows[:counter] + ["" for num in range(0,6-counter)]
    print(fn)
    print(*fn)
    print('''
    ____
    |   |
    |   {}
    |  {}{}{} 
    |  {} {}
    '''.format(*gallows))

def is_game_over():
	if "".join(hidden_word) == word:
		print("You won!!")
		return True
	elif counter > 5:
		print("Yoy killed Kenny")
		return True
	else:
		return False
wordslist = ['correction']
word = random.choice(wordslist)
hidden_word = list(re.sub(r'[a-zA-Z]', '*', word))
counter=0
guessed_letter = []
while True:
	print_gallows()
	if is_game_over():
		break
		print("these are the letters you\'ve already guessed: ", *guessed_letter)
		print("".join(hidden_word))

	while True:
		user_letter = input("Guess a letter you haven\'t guessed yet: ")
		if len(user_letter) > 1:
			print ("too many letters, try again")
		elif not user_letter.isalpha():
			print("not a letter, you\'re better than that")
		elif user_letter in guessed_letter:
			print("you\'ve already guessed that")
		else:
			guessed_letter.append(user_letter)
			break
	if user_letter in word:
		for index, letter in enumerate (word):
			if user_letter == letter:
				hidden_word[index] == user_letter
	else:
		counter += 1












