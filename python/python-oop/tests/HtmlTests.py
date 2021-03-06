import unittest,sys
from unittest import TestCase
sys.path.append("../src/challenge")
from Html import Body
from Html import Html
from Html import P

class HtmlTests(TestCase):
    
    def setUp(self):
        return super().setUp()

    def test_html_output(self):
        self.assertEqual("<html></html>",str(Html()))

    def test_body_output(self):
        value="456"
        self.assertEqual(f'<body>{value}</body>',str(Body(_text=value)))

    def test_p_output(self):
        value="test1"
        self.assertEqual(f'<p>{value}</p>',str(P(_text=value)))

    def test_html_contain_body_output(self):
        bodyvalue="123"
        result=str(Html(Body(bodyvalue)))
        self.assertEqual("<html><body>123</body></html>",result)

    def test_html_conatin_body_contain_p_output(self):
        p_value="this p text"
        p_node=P(p_value)
        body_node=Body(p_node)
        html=Html(body_node)
        result=str(html)
        self.assertEqual("<html><body><p>this p text</p></body></html>",result)

def main():
    unittest.main()

if __name__=="__main__":
    main()