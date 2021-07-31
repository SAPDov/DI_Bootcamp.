  
import re


matrix_list = [[7, ' ', 3],
    ['T','s','i'],
    ['h','%','x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['i', 'r', '!']]


i = 0
matrix_decode =[]
while i < len(matrix_list[0]):

    for element in matrix_list:
        matrix_decode.append(element[i])
    i += 1
    
line = ''.join(map(str, matrix_decode))
line = re.sub('\s+', '', line)
line = re.sub('[%#$]+', ' ', line)
line = re.sub(r'[0-9]', '', line)

print(line)



