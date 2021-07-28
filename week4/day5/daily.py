
text=input("Insert a text with a comma separated: ")
li =[]
sorted_li =[]
word = " "
for letter in text:
	if letter != ",":
	 	word += letter
	else:		
	 	li.append(word)
	 	word = " "
li.append(word)
sorted_li= sorted(li)
print(str(", ".join(sorted_li)))



