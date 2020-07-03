import argparse
from playing_around.data import WordData
import random
import string

def get_word(first_letter=None):
   """
   Tries to return a random word starting with first_letter.
   If it cannot find it, it returns the default word.
   Input:
   - first_letter: str, None
     if none provided, it will be set to a random lowercase letter
   """
   if not first_letter:
      first_letter = random.choice(string.ascii_lowercase)
   try:
      # missing the randomization of the index in the list,
      # depending on its length
      word_list = list(WordData.word_dict[first_letter.lower()])
      return word_list[random.randrange(0, len(word_list))]
   except (KeyError, IndexError, ValueError):
      # I may want to raise a warning with the error in here
      return WordData.default_word

if __name__ == '__main__':

   # Getting the command line arguments with argparse
   parser = argparse.ArgumentParser(description="Script to get a random word. If --letter is not provided, the first letter of the word will be random. If no word starting with --letter is found, the program will return a default word.")
   parser.add_argument("-l", "--letter", help="First letter of the word. The program will attempt to get a word starting with this letter.", default=None)
   args = parser.parse_args()

   word = get_word(first_letter=args.letter)

   print(word)




