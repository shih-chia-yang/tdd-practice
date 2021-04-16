from pathlib import  Path

TOTAL_SIZE=0

def measure_size():
    path=Path("./testdir")
    global TOTAL_SIZE
    for file in path.glob("*.py"):
        if file.is_symlink() is False:
            TOTAL_SIZE+=file.stat().st_size 
    return TOTAL_SIZE

def main():
    measure_size()

if __name__=="__main__":
    main()