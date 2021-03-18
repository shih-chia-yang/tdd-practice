import hashlib
from importlib.resources import path 
from pathlib import Path

FILE1_PATH=""
FILE2_PATH=""
SAME_FILE=False
def compare(file1,file2):
    global FILE1_PATH,FILE2_PATH,SAME_FILE
    FILE1_PATH = Path(file1)
    FILE2_PATH=Path(file2)
    with FILE1_PATH.open('rb') as path1_content:
       md5_1=hashlib.md5(path1_content.read()).hexdigest()

    with FILE2_PATH.open('rb') as path2_content:
        md5_2=hashlib.md5(path2_content.read()).hexdigest()
    if md5_1 ==md5_2:
        SAME_FILE=True
    return SAME_FILE

def move_to_backup(backpath):
    new_dir_path=Path(backpath)
    if new_dir_path.exists() is False:
        new_dir_path.mkdir()
    print(SAME_FILE)
    if SAME_FILE:
        old_path1=Path(FILE1_PATH.absolute())
        old_path2=Path(FILE2_PATH.absolute())
        new_path=Path.joinpath(Path.cwd(),backpath)
        old_path1.rename(Path.joinpath(new_path,old_path1.name))
        old_path2.rename(Path.joinpath(new_path,old_path2.name))

def main():
    compare("./1.tmp","./7.tmp")
    move_to_backup("./backup")

if __name__=="__main__":
    main()