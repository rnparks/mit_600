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

print choose_word(load_words())











# word = 'cock'
# blank = ['_'] * len(word)
# print ' '.join(blank)
# available_letters = "abcdefghijklmnopqrstuvwxyz"
# old_gueses = []
# letter = 'c'
# print available_letters.replace(letter, "")
# print available_letters


# print "Welcome to the game, Hangman!"
# print "I am thinking of a word that is %i letters long" % (len(word))
# print "-------------"
# # while turns_remaining > 0:
# for index, value in enumerate(word):
#   if value == letter:
#     blank[index] = letter
# print ' ' .join(blank)



