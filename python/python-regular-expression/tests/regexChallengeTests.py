import re,sys
from unittest import TestCase
import unittest
sys.path.append("../")
import regexChallenge 

num_list=[('+1 223-456-7890','1-223-456-7890'),
                  ('1-223-456-7890','1-223-456-7890'),
                  ('+1 223 456-7890','1-223-456-7890'),
                  ('(223) 456-7890','1-223-456-7890'),
                  ('1 223 456 7890','1-223-456-7890'),
                  ('223.456.7890','1-223-456-7890')]

error_num_list=[('1-123-456-7890'),
                  ('1-023-456-7890'),
                  ('1-223-123-7890'),
                  ('1-223-023-7890'),
                  ('1-223-22307890'),
                  ('1-223-091-7890')]

class regexChallengeTests(TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_format1_phone_standardize_to_standard_format(self):
        for number,expected in num_list:
            self.assertEqual(expected,regexChallenge.number_formatting(number))

    def test_error_format_number_should_be_throw_ValueError(self):
        with self.assertRaises(ValueError):
            for number in error_num_list:
                regexChallenge.number_formatting(number)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
    