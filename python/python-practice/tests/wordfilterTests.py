import sys,unittest
sys.path.append("../src/wordfilter")
import fetch

class wordfilterTests(unittest.TestCase):
    
    def test_get_word(self):
        self.assertTrue(len(fetch.get_word("../sample/moby01.txt"))>0)

    def test_replace_line_symbol_to_empty(self):
        contents =fetch.get_word("../sample/moby01.txt")
        for content in contents:
            self.assertFalse("," in content)
            self.assertFalse("." in content)

if __name__ == '__main__':
    unittest.main()
    