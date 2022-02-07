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
        self.assertEqual(self.anagram.is_anagram("brag","grab"), True)
        self.assertEqual(self.anagram.is_anagram("bored","robed"), True)
        self.assertEqual(self.anagram.is_anagram("cat","act"), True)
        self.assertEqual(self.anagram.is_anagram("cider","cried"), True)
        self.assertEqual(self.anagram.is_anagram("dusty","study"), True)
        self.assertEqual(self.anagram.is_anagram("elbow","below"), True)
        self.assertEqual(self.anagram.is_anagram("inch","chin"), True)
        self.assertEqual(self.anagram.is_anagram("night","thing"), True)
        self.assertEqual(self.anagram.is_anagram("peach","cheap"), True)
        self.assertEqual(self.anagram.is_anagram("players","parsley"), True)
        self.assertEqual(self.anagram.is_anagram("sadder","dreads"), True)
        self.assertEqual(self.anagram.is_anagram("save","vase"), True)
        self.assertEqual(self.anagram.is_anagram("state","taste"), True)
        

if __name__ == '__main__':
    unittest.main()
