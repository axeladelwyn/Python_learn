# Problem Set 2, hangman.py
# Name: Axel
# Collaborators:
# Time spent: 

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # iterate through all the letter in letter guess and match 
    # match and compare with secret word
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True
# print(has_player_won("buncis", "buncs"))

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Check letters gusssed input
    # print the letter guessed
    guessed_letter = ""
    for letter in secret_word:
      if letter in letters_guessed:
        guessed_letter += letter
      else:
        guessed_letter += "*"
      # if letter is guessed then show it
      # append letter to the guessed letter
    return guessed_letter
# print(get_word_progress("buncas", "buncos"))

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Return string in alphabetical order
    all_letters = set(string.ascii_lowercase)
    remaining_letters = all_letters - set(letters_guessed)
    return "".join(sorted(remaining_letters))



def hangman(secret_word, with_help):
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # append user input to letter guessed
    guess = 10
    letters_guessed = set()
    vowels = {'a','e','i','o','u'}

    print(f"Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"--------------")


    while guess > 0:
        print(f"You currently have {guess} guess left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        user_input = input("Please guess a letter: ")

        if with_help and user_input == "!":
            # Implement the help functionality
            missing_letters = set(secret_word) - letters_guessed
            if missing_letters:
                revealed_letter = missing_letters.pop()
                print(f"Letter revealed '{revealed_letter}'")
                letters_guessed.add(revealed_letter)
                print(f"{get_word_progress(secret_word, letters_guessed)}")
                guess -= 3

                if has_player_won(secret_word, letters_guessed):
                    print(f"--------------")
                    print("Congratulations, you won!")
                    total_score = (guess + 4 * len(set(secret_word)) + (3 * len(secret_word)))
                    print(f"Your total score for this game is {total_score}")
                    break
            else:
                print("No missing letters to reveal.")
        else:
            if user_input.isalpha() and len(user_input) == 1:
                if user_input in letters_guessed:
                    print(f"You've already guessed '{user_input}'. Try a different letter.")
                    print(f"--------------")
                else:
                    letters_guessed.add(user_input)
                    if user_input in secret_word:
                        print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
                        print(f"--------------")
                    else:
                        # Deterine penalty based on whether the guess is a vowel or consonants
                        if user_input in vowels:
                            guess -= 2
                            if guess < 0:
                                guess = 0
                        else:
                            guess -= 1

                        print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
                        print(f"--------------")
                    if has_player_won(secret_word, letters_guessed):
                        print("Congratulations! You've won the game.")
                        total_score = (guess + 4 * len(set(secret_word)) + (3 * len(secret_word)))
                        print(f"Your total score for this game is {total_score}")
                        break
            else:
                print("Please enter a valid alphabetic characters!")
        
        if guess <= 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")

    # Return whether the player has won (you need to implement this)
    return has_player_won
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman("hi", True)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

