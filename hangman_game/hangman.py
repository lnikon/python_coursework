# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import readchar

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.read()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def char_pos_in_word(word, char):
    # Positions of char in the supplied word
    char_idx = []

    # Current position in word
    idx = 0

    for sym in word:
      if sym == char:
        char_idx.append(idx) 
      idx += 1
    
    return char_idx

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    for char in letters_guessed:
      if char not in secret_word:
        return False    

    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    partially_guessed_word = ['_'] * len(secret_word)
    for char in letters_guessed:
      char_indices = char_pos_in_word(secret_word, char)

      for char_idx in char_indices:
        partially_guessed_word[char_idx] = char

    return partially_guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    alphabet = string.ascii_lowercase
    not_yet_guessed_letters = [char for char in alphabet if char not in letters_guessed]

    return not_yet_guessed_letters



def hangman(secret_word, input_handler):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    # Initial value for rounds
    rounds_left = 6

    # Tell to the user the length of the secret word    
    print("Length of secret word is: {}\n".format(len(secret_word)))

    # Correctly guessed letter in not proper positions
    letters_guessed = []

    #### Uncomment below line only for DEBUG!
    print("Secret word is: {}\n".format(secret_word))

    while rounds_left > 0:
      print("Rounds left: {}\n".format(rounds_left))
      
      # Read from stdin one char
      guess = readchar.readchar()

      if input_handler(guess, get_guessed_word(secret_word, letters_guessed)): 
        rounds_left -= 1
        continue

      # Append to guesses list
      letters_guessed.append(guess)

      #### Uncomment below line only for DEBUG!
      #### print("Guessed letters: {}".format(letters_guessed))

      if is_word_guessed(secret_word, letters_guessed):
        # Check if @secret_word contains that char
        print("Hoola! Another correct letter guess, good job!\n")
      else:
        # If not, then remove from guesses list
        del letters_guessed[len(letters_guessed) - 1]

      if secret_word == ''.join(letters_guessed):
        print("aaaaand You win!\n")
        break
      else:
        print("See, partially matched word is...\n {}".format(get_guessed_word(secret_word, letters_guessed)))

      rounds_left -= 1

      print("Not yet guessed chars: {}\n".format(get_available_letters(letters_guessed)))




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    
    if len(my_word) != len(other_word): return False

    for a, b in zip(my_word, other_word):
      if a == '_': 
        continue

      if a != b: 
        return False

    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    prnt = lambda word: print('Word {} is a possible match\n'.format(word))
    [prnt(word) for word in wordlist if match_with_gaps(my_word, word)]
    
    pass

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''

    # Functor, that handles case when input char is '*'
    def star_handler(guess, my_word):
      if guess != '*':
        return False
      
      show_possible_matches(my_word)
      return True
    
    hangman(secret_word, star_handler)

    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #default_functor = lambda _: False

    #secret_word = choose_word(wordlist)
    #hangman(secret_word, default_functor)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
