
string_client = input ("write a string -10 characters long: ")

i=0
count = len(string_client)
if count < 10:
	print("The string is not long enough")
if count > 10:
	print ("The string is too long")
	print(string_client[0])
	print(string_client[count-1])

while i <= count:
	print(string_client[0:i])
	i += 1 
	
import random
l = list(string_client)
random.shuffle(l)
print (''.join(l))
