import unittest
from exercise_1 import Counts

class StrCountTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.count = Counts()
    
    def test_count_chars(self):
        self.assertEqual(self.count.stringCount("P@#yn26at^&i5ve"), (8, 3, 4))

if __name__ == '__main__':
    unittest.main()
