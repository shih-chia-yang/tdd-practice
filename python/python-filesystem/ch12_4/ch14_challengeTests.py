from unittest import TestCase
import unittest
import ch14_challenge

class ChallengeTest(TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_all_py_file_size_in_directory(self):
        size=ch14_challenge.measure_size()
        self.assertEqual(12322,size)

def main():
    unittest.main()
if __name__=="__main__":
    main()