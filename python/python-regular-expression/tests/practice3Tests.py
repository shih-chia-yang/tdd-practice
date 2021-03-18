import re,sys
from unittest import TestCase
import unittest
sys.path.append("../")
from practice3 import replace_number

num_list=[('001-002-1234','+1-001-002-1234'),
                 ('+123-001-223-322','+123-001-223-322'),
                 ('003-2234','003-2234')]

class Practice3Tests(TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_replace_number(self):
        for number,expected in num_list:
            self.assertEqual(expected,replace_number(number))

def main():
    unittest.main()

if __name__=="__main__":
    main()