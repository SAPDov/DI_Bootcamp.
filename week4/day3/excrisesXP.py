# Exercise 1 : Convert Lists Into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary) 

# Exercise 2 : Cinemax 2

class_list = dict() 
family_num=0

members = input("How many family members do you have?")

while family_num <= int(members):
	data = input('Enter names & ages separated by ":" ') 
	temp = data.split(':') 
	class_list[temp[0]] = int(temp[1]) 
  
	for key, value in class_list.items(): 
		'Name: {}, age: {}'.format(key, value)
		family_num += 1

print(class_list) 
	

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


total=0 
for age in class_list.values():
	if age > 2 and age < 13:
		total += 10  
	if age > 12:
		total += 15 
	if age < 3:
		total +=0 
print(f"The total amount is: {total}$")



# Exercise 3: Zara
brand = {
"name": "Zara", 
"creation_date":1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"], 
"number_stores": 7000, 
"major_color":{
 	"France":"blue", 
    "Spain": "red",
    "US": ["pink", "green"],	
}
}

print(brand)

brand["number_stores"] = 2
print("Zara's client are: ", brand["type_of_clothes"]) 
print(brand)
brand["country_creation"] = "Spain"
print(brand)
x = brand.setdefault("international_competitors", "a")
if x != "a":
	print(brand["international_competitors"].append("Desigual"))
print(brand["international_competitors"][2])
print(brand["major_color"]["US"])
print(len(brand))
brand.pop("creation_date")
print(len(brand))
print(brand.keys())

more_on_zara = {
"creation_date": 1975, 
"number_stores": 10000,
}

new_dict=brand | more_on_zara
print(new_dict)
# print(new_dict.value("number_stores"))

# Exercise 4 : Disney Characters
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
sort_users = sorted(users)
dic =[]
dic1=[]
dic2=[]

for num in range(0,5):
	dic.append(num)
	x=dict(zip(users, dic))
	y=dict(zip(sort_users, dic))
print(x, y)

for i, char in enumerate(users):
	dic1.append(i)
print(dict(zip(dic1, users)))

#Only recreate the 1st result for:
The characters, which names contain the letter ???i???.
The characters, which names start with the letter ???m??? or ???p???.
for item in users:
	f = item.find("i")
	if f != -1:
	  dic2.append(item)
for num1 in range(0,2):
	dic2.append(num1)
	j=dict(zip(dic2, num1))	  
 print(j)

 