from unittest import TestCase
import unittest
import ch14_challenge2

class Challenge2Test(TestCase):
    def setUp(self) :
        return super().setUp()

    def test_if_campare_2_same_files_then_return_False(self):
        is_same=ch14_challenge2.compare("./1.tmp","./7.tmp")
        print(is_same)
        self.assertEqual(True,is_same)

def main():
    unittest.main()
 
if __name__=="__main__":
    main()