from gettext import find
import random

w_list = open('words.txt', 'r')
guess_word = ((random.choice(w_list.readlines())).lower())[:-1]
t_g_w = guess_word

strike = 0 #11
cache = []
word_line = len(guess_word) * '_'

print("-- H A N G M A N --")
print()
print(f"The word is {len(guess_word)} characters long.")
print()

while True:
    guess_letter = input('Guess a letter: ').lower()
    print()

    if len(guess_letter) > 1 or not guess_letter.isalpha():
        print('Check your input.')
        print('Only letters are allowed and they have to be entered one at the time.')
    
    elif guess_letter in cache:
        print(f"'{guess_letter}' has already been guessed.")
    
    else:
        if guess_letter in t_g_w:
            cache.append(guess_letter)
            for letter in t_g_w:
                if letter == guess_letter:
                    letter_index = t_g_w.find(guess_letter)
                    word_line = word_line[0:letter_index] + guess_letter + word_line[letter_index+1:]
                    t_g_w = t_g_w[:letter_index] + '*' + t_g_w[letter_index+1:]
                else:
                    pass
            
            print(word_line)
            
            if word_line == guess_word:
                print()
                print('You won! :)')
                break
        
        elif strike == 11:
            print('11/11 srtikes, you lost.')
            print(f"The correct word was '{guess_word}'.")
            break

        else:
            cache.append(guess_letter)
            strike += 1
            print(f'Incorrect, you have {strike}/11 strikes.')
            
    print()
  