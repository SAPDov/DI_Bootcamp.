text = input("Insert a text with a comma separated - not a white space: ")
items = [x for x in text.split(',')]
items.sort()
print(','.join(items))