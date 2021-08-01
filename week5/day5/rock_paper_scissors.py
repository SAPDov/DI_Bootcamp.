from game import Game
	
def get_user_menu_choice():

	menu_choice=input(f"(g) Play a new game \n (x) Show scores and exit ")

	while menu_choice not in ["x", "g"]:
		menu_choice = input(f"(g) Play a new game \n (x) Show scores and exit ") 
	return menu_choice

def print_results(results):
	print(f"You won {results['won']} times\n You lost {results['loss']} times\n You won {results['draw']} times\n Thank you for playing")

# num_of_play = 0

found = True
while found:
	def main():
		results_dict = {"won": 0, "loss": 0, "draw": 0}
		choice = get_user_menu_choice()

		if choice == "g":

			new_game = Game()
			result = new_game.play()
			result = f"{result}"
			results_dict[result] += 1

		else:
			print(results_dict)
			found = True
	


main()



	
	

