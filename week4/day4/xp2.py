# xercise 7: When Will I Retire ?

from datetime import date

def get_age(birth_date):
	today = date.today()
	age = today.year - birth_date.year
	return age

def can_retire(gender, age):
	if gender == 'm':
		if age > 67:
			return True
		else: return False
	elif gender == 'f':
		if age > 62:
			return True
		else: return False

age = get_age(date(1991, 11, 18))
print(can_retire('m', age))

# Exercise 8:



def multi_x(x):
	x = str(x)
	li_number = [(x*1), (x*2), (x*3), (x*4)]
	numbers_int = [int(x) for x in li_number]
	total = sum(numbers_int)
	print(total)
	
multi_x(3)







