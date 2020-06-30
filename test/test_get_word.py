from playing_around.get_word import get_word
from playing_around.data import WordData as OriginalWordData
from random import randrange
from string import ascii_lowercase
from unittest import TestCase
from unittest.mock import patch


class TestGetWord(TestCase):

   @patch('playing_around.get_word.WordData')
   def test_get_word_gets_only_word_available_with_letter(self, MockWordData):
      MockWordData.default_word = 'default word'
      MockWordData.word_dict = OriginalWordData.word_dict
      MockWordData.word_dict['t'] = {
         'test word': 'definition of the test word'
      }
      tested_word = get_word('t')
      self.assertEqual(tested_word, 'test word')

   @patch('playing_around.get_word.WordData')
   def test_get_word_gets_default_word_if_none_with_letter(self, MockWordData):
      MockWordData.default_word = 'default word'
      MockWordData.word_dict = OriginalWordData.word_dict
      MockWordData.word_dict['t'] = {}
      tested_word = get_word('t')
      self.assertEqual(tested_word, 'default word')

   @patch('playing_around.get_word.WordData')
   def test_get_word_gets_random_word_if_many_with_letter(self, MockWordData):
      MockWordData.default_word = 'default word'
      MockWordData.word_dict = OriginalWordData.word_dict
      MockWordData.word_dict['t'] = {
         'test word zero': 'definition of test word zero',
         'test word one': 'definition of test word one',
         'test word two': 'definition of test word two'
      }
      with patch('playing_around.get_word.random') as mock_random:
         mock_random.randrange.return_value = 0
         tested_word = get_word('t')
         self.assertEqual(tested_word, 'test word zero')

         mock_random.randrange.return_value = 2
         tested_word = get_word('t')
         self.assertEqual(tested_word, 'test word two')

         mock_random.randrange.return_value = 1
         tested_word = get_word('t')
         self.assertEqual(tested_word, 'test word one')

   @patch('playing_around.get_word.WordData')
   def test_get_word_searches_word_within_length_available(self, MockWordData):
      MockWordData.default_word = 'default word'
      MockWordData.word_dict = OriginalWordData.word_dict
      MockWordData.word_dict['t'] = {
         'test word zero': 'definition of test word zero',
         'test word one': 'definition of test word one'
      }
      with patch('playing_around.get_word.random') as mock_random:
         get_word('t')
         mock_random.randrange.assert_called_with(0, 2)

         MockWordData.word_dict['t']['test word two'] = 'definition'
         get_word('t')
         mock_random.randrange.assert_called_with(0, 3)


   @patch('playing_around.get_word.WordData')
   def test_get_word_gets_default_word_if_index_not_found(self, MockWordData):
      MockWordData.default_word = 'default word'
      MockWordData.word_dict = OriginalWordData.word_dict
      MockWordData.word_dict['t'] = {
         'test word zero': 'definition of test word zero',
         'test word one': 'definition of test word one',
         'test word two': 'definition of test word two'
      }
      with patch('playing_around.get_word.random') as mock_random:
         mock_random.randrange.return_value = 4
         tested_word = get_word('t')
         self.assertEqual(tested_word, 'default word')

   @patch('playing_around.get_word.WordData')
   def test_get_word_gets_default_word_if_letter_not_found(self, MockWordData):
      MockWordData.default_word = 'default word'
      MockWordData.word_dict = OriginalWordData.word_dict
      MockWordData.word_dict.pop('t')
      tested_word = get_word('t')
      self.assertEqual(tested_word, 'default word')

   @patch('playing_around.get_word.WordData')
   def test_get_word_uses_random_letter_if_no_letter_given(self, MockWordData):
      MockWordData.default_word = 'default word'
      MockWordData.word_dict = OriginalWordData.word_dict
      MockWordData.word_dict['t'] = {
         'test word': 'definition of test word'
      }
      MockWordData.word_dict['a'] = {
         'another test word': 'definition of another test word'
      }
      with patch('playing_around.get_word.random') as mock_random:
         # keep mock working as expected of random
         mock_random.randrange.side_effect = randrange

         mock_random.choice.return_value = 't'
         tested_word = get_word()
         self.assertEqual(tested_word, 'test word')

         mock_random.choice.return_value = 'a'
         tested_word = get_word()
         self.assertEqual(tested_word, 'another test word')

         mock_random.choice.assert_called_with(ascii_lowercase)
