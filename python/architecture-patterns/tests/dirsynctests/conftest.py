from datetime import datetime
import pytest
from pathlib import Path

source_path=Path("/home/chia-yang-shih/work/tests/dirsync_temp_test/test_source_dir")
dest_path=Path("/home/chia-yang-shih/work/tests/dirsync_temp_test/test_dest_dir")
test_file="test3.txt"
deleted_file=dest_path.joinpath(test_file)

@pytest.fixture
def create_path():
    if source_path.is_dir() ==False:
        source_path.mkdir()
    if dest_path.is_dir() ==False:
        dest_path.mkdir()
    return source_path,dest_path

@pytest.fixture
def create_dest_file(create_path):
    test_file=Path(deleted_file)
    with test_file.open('w') as new_file:
        new_file.write(str(datetime.now()))

@pytest.fixture
def create_source_file(create_path):
    test1=source_path.joinpath("source1.txt")
    test2=source_path.joinpath("source2.txt")
    with test1.open('w') as new_file1:
        new_file1.write(str(datetime.now()))
    with test2.open('w') as new_file2:
        new_file2.write("test content")

@pytest.fixture
def initsync(create_dest_file,create_source_file):
    return source_path,dest_path,deleted_file
        
