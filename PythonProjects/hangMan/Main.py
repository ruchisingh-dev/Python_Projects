import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed by the user
    lives = 6  # Number of wrong guesses allowed

    while len(word_letters) > 0 and lives > 0:
        # Display the current state of guessed letters
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        
        # Display the current word with guessed letters and dashes for missing ones
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        
        # Get user input
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1  # Take away a life if wrong
                print('\nYour letter', user_letter, 'is not in the word.')
        
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Please try again.')
        
        else:
            print('\nInvalid character. Please try again.')

    # Game over conditions
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')

hangman()
