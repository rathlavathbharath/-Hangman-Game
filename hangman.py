import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)       # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)       # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()           # what the user has guessed

    lives = 7
    
    # getting user input
    print("Welcome to Hangman!")
    
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Remaining lives:', lives)
        print('Used letters:', ' '.join(used_letters))
        
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("\nNice guess!")

            else:
                lives = lives - 1          # takes away a life if wrong
                print('\nSorry,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already guessed', user_letter, '. Try another letter.')

        else:
            print('\nThat is not a valid letter. Please enter a letter from A-Z.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Oops, you ran out of lives and you died. The word was', word, 'Better luck next time!')
    else:
        print(lives_visual_dict[lives])
        print("Congratulations! You guessed the word", word, "correctly. You win!")

if __name__ == '__main__':
    hangman()