import sys
from unittest import TestCase
import unittest
sys.path.append("../")
from practice2 import extract_number

phone_list=[('+01-001-113-1234',True),
                    ('+001-001-113-1234',True),
                    ('+1-001-113-1234',True),
                    ('+2311-001-113-1234',False),
                    ('001-113-1234',True)]

class Practice2Tests(TestCase):
    def setUp(self):
        return super().setUp()

    def test_extract_number(self):
        for phone,expected in phone_list:
            self.assertEqual(expected,extract_number(phone))

def main():
    unittest.main()

if __name__=="__main__":
    main()