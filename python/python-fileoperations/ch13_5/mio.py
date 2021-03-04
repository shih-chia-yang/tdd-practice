""" capture_output,restore_output,print_file,clear_file"""

import sys
from pathlib import Path
_file_object=None


def msg_sent_file_path(output_path):
    print(f'output will be sent to file :{output_path.absolute()}')

def msg_exec_function():
    print("restore to normal by calling 'mio.restore_output()'")

def msg_restore_output():
    print("standard output has been restored back to normal")

def restore_output():
    sys.stdout=sys.__stdout__

def capture_output(file):
    """將標準輸出重新導向至檔案"""
    global _file_object
    output_path=Path(file)
    msg_sent_file_path(output_path)
    msg_exec_function()
    with open(output_path,'w') as write_file:
        sys.stdout=write_file
    restore_output()

def print_file(file):
    source_file=Path(file)
    with open(source_file,'r') as read_source:
        print(read_source.read())

def clear_file(file):
    with open(file,'w') as write_empty:
        write_empty.write("")

