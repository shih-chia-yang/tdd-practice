from pathlib import  Path

total_size=0

def measure_size():
    path=Path("./testdir")
    global total_size
    for file in path.glob("*.py"):
        if file.is_symlink() is False:
            total_size+=file.stat().st_size 
    return total_size

def main():
    measure_size()

if __name__=="__main__":
    main()