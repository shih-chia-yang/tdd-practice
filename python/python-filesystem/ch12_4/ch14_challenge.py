from pathlib import  Path

def measure_size():
    path=Path(".")
    total_size=0
    for file in path.glob("*.py"):
        if file.is_symlink() is False:
            total_size+=file.stat().st_size 
    return total_size
