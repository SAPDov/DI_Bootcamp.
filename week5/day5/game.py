# Mini-Project 1: Rock, Paper, Scissors
import random

class Game:
	def __init__(self):
		self.input = self.get_user_item()
		self.input_com = self.get_computer_item()

	
	def get_user_item(self):

		while True:
				user_r_p_s = (input("Select (r)ock, (p)aper, or (s)cissors:").lower())
				if user_r_p_s == "r" or user_r_p_s == "p" or user_r_p_s == "s":
					return user_r_p_s
				else:
					print("Error - wrong input")


	def get_computer_item(self):
		computer_r_p_s = ["r", "p", "s"]
		return random.choice(computer_r_p_s)


	def get_game_result(self):

		if self.input  == self.input_com:
			return "draw"

		elif self.input  == "r" and self.input_com == "p":
			return "loss"

		elif self.input == "r" and self.input_com == "s":
			return "won"

		elif self.input  == "p" and self.input_com == "r":
			return "won"

		elif self.input == "p" and self.input_com == "s":
			return "loss"
		
	def play (self):
		user_choice = self.input
		computer_choice = self.input_com
		result = self.get_game_result()
		print (f"You chose: {user_choice}. The computer chose: {computer_choice}. Result: {result}")
		return result


