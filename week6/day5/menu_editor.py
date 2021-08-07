from ex import MenuItem

def load_manager(item, price):
	new_menu = MenuItem(item, price)
	return new_menu

 
def show_user_menu():
	menu_input = input("""
			MENU
		(a) Add an item
		(d) Delete an item
		(v) View the menu
		(x) Exit
		""")
	return menu_input

def add_item_to_menu(item, price):
	load_manager(item, price).save_item()
	print("item was added successfully")
	
def remove_item_from_menu(item, price = None):
	load_manager(item, price).delete_item()
	return True

def show_restaurant_menu(item = None, price = None):
	load_manager(item, price).all()

while True:
	menu_input = show_user_menu()
	if menu_input == "a":
		item_name = input("insert an item's name to add: ")
		item_price = input("insert an item's price: ")
		add_item_to_menu(item_name, item_price)
	elif menu_input == "d":
		item_name = input("insert an item's name to delete: ")
		remove_item_from_menu(item_name)
		if True:
			print("item was removed successfully")
		else: print("error")
	elif menu_input == "v":
		show_restaurant_menu()
	elif  menu_input == "x":
		print("goodbye!")
		show_restaurant_menu()
		break
	else:
		print("enter a vaild letter")


