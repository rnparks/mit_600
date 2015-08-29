import random

WORDLIST_FILENAME = "words.txt"

def load_words():
     print("Loading word list from file...")
     # inFile: file
     inFile = open(WORDLIST_FILENAME, 'r')
     # line: string
     line = inFile.read()
     # wordlist: list of strings
     wordlist = line.split(' ')
     inFile.close()
     return wordlist

def choose_word(words):
  return random.choice(words)


def hangman():
  secret_word = choose_word(load_words())
  blank = ['_'] * len(secret_word)
  control_letters = "abcdefghijklmnopqrstuvwxyz"
  available_letters = "abcdefghijklmnopqrstuvwxyz"
  old_guesses = []
  turns = 8
  print "Welcome to the game, Hangman!"
  print "I am thinking of a word that is %i letters long" % (len(secret_word))
  print "-------------"
  while turns > 0:
    print "You have %i guesses left" % (turns)
    print "available_letters: %s" % (available_letters)
    guess = raw_input('Please enter a Letter: ').lower()
    if len(guess) > 1:
      print "You have attempted to select more than one character."
    elif guess not in control_letters:
      print "You have selected on invalid character."
    elif guess in old_guesses:
      print "You have already selected this letter."
    elif guess in secret_word:
      old_guesses.append(guess)
      available_letters = available_letters.replace(guess, "")
      for index, letter in enumerate(secret_word):
        if guess == letter:
          blank[index] = guess
      print "Good Guess: " + ' ' .join(blank)
      print "-------------"
    else:
      old_guesses.append(guess)
      available_letters = available_letters.replace(guess, "")
      print "Oops, that letter is not in my word: " + ' ' .join(blank)
      print "-------------"
      turns -= 1
    if secret_word == ''.join(blank):
      print "You Win!"
      break
    if turns == 0:
      print " Sorry you've lost!"



hangman()

# print available_letters.replace(letter, "")
# print available_letters
#   for index, value in enumerate(word):
#   if value == letter:
#     blank[index] = letter
# print ' ' .join(blank)



