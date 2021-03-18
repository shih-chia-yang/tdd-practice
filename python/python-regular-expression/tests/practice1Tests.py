import sys
from unittest import TestCase
import unittest
sys.path.append("../")
import practice1  

num_list = [('55555', False), ('-5',True), ('0', True),('-10',False),('3',True)]
hex_list=[('7B',True),('1g',False),('9f',True),('100',True),('0',True)]

class PracticeTest(TestCase):
    def setUp(self):
        return super().setUp()

    def test_specific_number_range(self):
        for value,result in num_list:
            self.assertEqual(result,practice1.specific_number_range(value))

    def test_hexadecimal(self):
        for value,expectd in hex_list:
            actual=practice1.Hexadecimal(value)
            if actual!=expectd:
                print(value,expectd)
            self.assertEqual(expectd,actual)
            
def main():
    unittest.main()

if __name__=="__main__":
    main()