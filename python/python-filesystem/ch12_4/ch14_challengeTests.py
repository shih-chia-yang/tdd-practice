from unittest import TestCase
import ch14_challenge

class ChallengeTest(TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_all_py_file_size_in_directory(self):
        size=ch14_challenge.measure_size()
        self.assertEqual(3942,size)