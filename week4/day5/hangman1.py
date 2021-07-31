import random

def print_gallows():
    gallows = ['0', '/', '|', '\\', '/', '\\']
    fn = gallows[:counter] + [" " for num in range(0,6-counter)]
    print(fn)
    print(*fn)
    print('''
    ____
    |   |
    |   {}
    |  {}{}{} 
    |  {} {}
    '''.format(*gallows))
    
def is_game_over():
    if ''.join(hidden) == word:
        print('you won!!')
        return True
    elif counter > 5:
        print('you killed kenny')
        return True
    else:
        return False
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
word = 'credit card'
hidden = ['*' if letter != ' ' else ' ' for letter in word  ]
counter = 0
guessed_letters = []
while True:
    print_gallows()
    if is_game_over():
        break
    print('these are the letters you\'ve already guessed: ', *guessed_letters)
    print(''.join(hidden))
    while True:
        current_guess = input('Guess a letter you haven\'t guessed yet: ')
        if len(current_guess) > 1:
            print('too many letters, try again')
        elif not current_guess.isalpha():
            print('not a letter, you\'re better than that')
        elif current_guess in guessed_letters:
            print('you\'ve already guessed that')
        else:
            guessed_letters.append(current_guess)
            break
    if current_guess in word:
        for index, letter in enumerate(word):
            if current_guess == letter:
                hidden[index] = letter
    else:
        counter += 1