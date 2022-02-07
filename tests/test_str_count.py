import unittest
from exercise_1 import Counts
from exercise_3 import Anagrams

class StrCountTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.count = Counts()
    
    def test_count_chars(self):
        self.assertEqual(self.count.stringCount("P@#yn26at^&i5ve"), (8, 3, 4))

class AnagramTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.anagram = Anagrams()
    
    def test_if_anagram(self):
        self.assertEqual(self.anagram.is_anagram("arc","car"), True)

if __name__ == '__main__':
    unittest.main()
