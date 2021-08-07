hangman = {
0:
"""      +---+
       	   |
      	   |
      	   |
       	  ===""",
1:
"""   +---+
    O   |
        |
        |
       ===""",
2:
"""   +---+
    O   |
    |   |
        |
       ===""",
3:
"""   +---+
    O   |
   /|   |
        |
       ===""",
4:
"""   +---+
    O   |
   /|\\ |
        |
       ===""",
5:
"""   +---+
    O   |
   /|\\ |
   /    |
       ===""",
6:
"""   +---+
    O   |
   /|\\ |
   / \\ |
       ==="""
}
import random, re
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
guessed_letter = []
lives = 0
def display_hangman(lives):
	print(hangman[lives])
def is_game_over(word):
	if "".join(hidden_word) == word:
		print("You won!!")
		return True
	elif lives > 7:
		print("Yoy killed Kenny")
		return True
	else:
		return False
word = random.choice(wordslist)
hidden_word = list(re.sub(r'[a-zA-Z]', '*', word))
while True:	
	print("".join(hidden_word))
	display_hangman(lives)
	if is_game_over(word):
		break
		print("these are the letters you\"ve already guessed: ", *guessed_letter)
		print("".join(hidden_word))
	while True:
		user_letter = input("Guess a letter you haven\"t guessed yet: ")
		if len(user_letter) > 1:
			print ("too many letters, try again")
		elif not user_letter.isalpha():
			print("not a letter, you\"re better than that")
		elif user_letter in guessed_letter:
			print("you\"ve already guessed that")
		else:
			guessed_letter.append(user_letter)
			break
	if user_letter in word:
		for index, letter in enumerate(word):
			if user_letter == letter:
				hidden_word[index] = user_letter
	else:
		lives = lives + 1