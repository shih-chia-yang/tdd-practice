from importlib.resources import contents
import sys
from unittest import TestCase
sys.path.append("../src")
from GetContent import GetContent

class GetContentTests(TestCase):
    def setUp(self):
        self.getContent=GetContent()
        return super().setUp()

    def test_get_lines_count_from_file(self):
        self.getContent.get_content('../src/word_count.txt')
        self.assertEqual(4,self.getContent.line_count)
    
    def test_get_word_count_from_file(self):
        self.getContent.get_content('../src/word_count.txt')
        self.assertEqual(31,self.getContent.word_count)
    
    def test_get_char_count_form_file(self):
        self.getContent.get_content('../src/word_count.txt')
        self.assertEqual(188,self.getContent.char_count)