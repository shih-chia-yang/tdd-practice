import unittest,sys
from io import StringIO
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch
import mio

class mioTests(TestCase):
    def setUp(self):
        self.mio=mio
        self.source_file="example.txt"
        return super().setUp()

    @patch('sys.stdout',new_callable=StringIO)
    def test_capture_sent_file_path_output_from_print(self,mock_stdout):
        file_path=Path(self.source_file)
        mio.msg_sent_file_path(file_path)
        self.assertEqual(mock_stdout.getvalue().strip(),f'output will be sent to file :{Path(file_path).absolute()}')

    @patch('sys.stdout',new_callable=StringIO)
    def test_capture_exec_function_output_from_print(self,mock_stdout):
        mio.msg_exec_function()
        self.assertEqual(mock_stdout.getvalue().strip(),"restore to normal by calling 'mio.restore_output()'")
    
    @patch('sys.stdout',new_callable=StringIO)
    def test_capture_msg_restore_output_from_print(self,mock_stdout):
        mio.msg_restore_output()
        self.assertEqual(mock_stdout.getvalue().strip(),"standard output has been restored back to normal")

    @patch('sys.stdout',new_callable=StringIO)
    def test_restore_output_it_should_be_init_stdout(self,mock_stdout):
        sys.stdout="123"
        mio.restore_output()
        self.assertEqual(mock_stdout.getvalue().strip(),"")
    
    @patch('sys.stdout',new_callable=StringIO)
    def test_print_file_output_to_stdout(self,mock_stdout):
        mio.print_file(self.source_file)
        with open(self.source_file,'r') as read_content:
            content=read_content.read()
        self.assertEqual(mock_stdout.getvalue().replace('\n',""),content)

    def test_clear_file_then_content_should_be_empty(self):
        mio.clear_file(self.source_file)
        with open(self.source_file,'r') as read_source:
            self.assertEqual("",read_source.read())

def main():
    unittest.main()
    

if __name__ =="__main__":
    main()