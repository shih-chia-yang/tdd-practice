from datetime import datetime
import shutil
from numpy import equal
import pytest
import sys
sys.path.append("../../src")
from dirsync.sync import FileSystem,read_paths_and_hashes,determine_actions, sync
import fake_filesystem
from pathlib import Path
   
def test_dest_path_has_file_not_in_source_path_should_be_deleted(initsync):
    try:
        source_path,dest_path,deleted_file=initsync
        sync(read_paths_and_hashes,FileSystem(),source_path,dest_path)
        assert deleted_file.is_file()==False
    finally:
        shutil.rmtree(source_path)
        shutil.rmtree(dest_path)
        
def test_when_a_file_exists_in_the_source_but_not_in_the_destination(initsync):
    try:
        source_path,dest_path,deleted_file=initsync
        filename="source1.txt"
        sync(read_paths_and_hashes,FileSystem(),source_path,dest_path)
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
        sync(read_paths_and_hashes,FileSystem(),source_path,dest_path)
        assert old_dest_file.is_file()==False
        assert excepted_dest_path.read_text()==content
    finally:
        shutil.rmtree(source_path)
        shutil.rmtree(dest_path)
        
def test_when_a_file_exists_in_the_source_but_not_the_destination():
    source={"sha1":"my-file"}
    dest={}
    filesystem =fake_filesystem.FakeFileSystem()
    reader={"/source":source,"/dest":dest}
    sync(reader.pop,filesystem,"/source","/dest")
    assert filesystem == [("copy",Path("/source/my-file"),Path("/dest/my-file"))]

def test_determine_actions_when_a_file_has_been_renamed_in_the_source():
    source={"sha1":"renamed-file"}
    dest={"sha1":"original-file"}
    filesystem=fake_filesystem.FakeFileSystem()
    reader={"/source":source,"/dest":dest}
    sync(reader.pop,filesystem,"/source","/dest")
    assert filesystem == [("move",Path("/dest/original-file"),Path("/dest/renamed-file"))]