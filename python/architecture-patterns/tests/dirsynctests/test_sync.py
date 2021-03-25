from datetime import datetime
import shutil
import pytest
import sys
sys.path.append("../../src")
from dirsync.sync import sync
from pathlib import Path
   
def test_dest_path_has_file_not_in_source_path_should_be_deleted(initsync):
    try:
        source_path,dest_path,deleted_file=initsync
        sync(source_path,dest_path)
        # assert len(dest)==0
        assert deleted_file.is_file()==False
    finally:
        shutil.rmtree(source_path)
        shutil.rmtree(dest_path)
        
def test_when_a_file_exists_in_the_source_but_not_in_the_destination(initsync):
    try:
        source_path,dest_path,deleted_file=initsync
        filename="source1.txt"
        sync(source_path,dest_path)
        source_file_path=source_path.joinpath(filename)
        expected_path=dest_path.joinpath(filename)
        assert expected_path.is_file()
        assert expected_path.read_text()==source_file_path.read_text()
    finally:
        shutil.rmtree(source_path)
        shutil.rmtree(dest_path)
        
def test_when_a_file_has_been_renamed_in_the_source(initsync):
    try:
        source_path,dest_path,deleted_file=initsync
        old_dest_file=dest_path.joinpath("source3.txt")
        content="test content"
        with old_dest_file.open('w') as old_file:
            old_file.write(content)
        excepted_dest_path=dest_path.joinpath("source2.txt")
        sync(source_path,dest_path)
        assert old_dest_file.is_file()==False
        assert excepted_dest_path.read_text()==content
    finally:
        shutil.rmtree(source_path)
        shutil.rmtree(dest_path)