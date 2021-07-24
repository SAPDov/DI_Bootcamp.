
import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
combine_list = alphabet_lower + alphabet_upper 
new_text= ""
text=input("Insert a text: ")
encrypt=input("Do you to encrypt or decrypt your text?")
if encrypt != "encrypt":
	print(text)
else:
	for letter in text:
		if letter == " ":
			new_text+= " "
		else:
			index = (combine_list.index(letter)-3)
			new_text+=combine_list[index]
	print(new_text)	




