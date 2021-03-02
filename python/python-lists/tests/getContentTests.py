from importlib.resources import contents
import sys
from unittest import TestCase
sys.path.append("../src")
from GetContent import GetContent

class GetContentTests(TestCase):
    def setUp(self):
        self.getContent=GetContent('../src/word_count.txt')
        return super().setUp()

    def test_get_lines_count_from_file(self):
        line_func=self.getContent.line_func
        self.getContent.get_content(line_func)
        self.assertEqual(4,self.getContent.line_count)
    
    def test_get_word_count_from_file(self):
        word_func=self.getContent.word_func
        self.getContent.get_content(word_func)
        self.assertEqual(31,self.getContent.word_count)
    
    def test_get_char_count_form_file(self):
        char_func=self.getContent.char_func
        self.getContent.get_content(char_func)
        self.assertEqual(188,self.getContent.char_count)

    def test_get_max_line_length_from_input(self):
        self.getContent.count()
        self.assertEqual(56,self.getContent.max_line_length)