import sys
from unittest import TestCase
import unittest
sys.path.append("../src")

import practice1

param_list=["1",2]
list=[2,3,4,5]
class Practice1Tests(TestCase):

    # def test_addend_list(self):
    #     self.assertEqual(4,len(practice1.append_list_by_isinstance(list)))

    def test_validate_append_type(self):
        for param in param_list:
            with self.assertRaises(TypeError):
                practice1.append_list_by_isinstance(param)
    
    def test_append_list1(self):
        self.assertEqual(4,len(practice1.append_list_by_type(list)))
    
    def test_validate_append_type1(self):
        for param in param_list:
            with self.assertRaises(TypeError):
                practice1.append_list_by_type(param)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
    