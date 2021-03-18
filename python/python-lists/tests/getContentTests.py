import sys
from unittest import TestCase
import unittest
sys.path.append("../src/getcontent")
from GetContent import Getcontent

class GetContentTests(TestCase):
    def setUp(self):
        self.getContent=Getcontent(["./word_count.txt"])
        return super().setUp()

    def test_get_lines_count_from_file(self):
        self.getContent.get_content()
        self.assertEqual(4,self.getContent.line_count)
    
    def test_get_word_count_from_file(self):
        self.getContent.get_content()
        self.assertEqual(31,self.getContent.word_count)
    
    def test_get_char_count_form_file(self):
        self.getContent.get_content()
        self.assertEqual(188,self.getContent.char_count)

    def test_get_max_line_length_from_input(self):
        self.getContent.get_content()
        self.assertEqual(56,self.getContent.max_line_length)

def main():
    unittest.main()

if __name__=="__main__":
    main()