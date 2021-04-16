from pprint import pprint
from pathlib import Path
import sys
src_path=str(Path("src").absolute())
sys.path.append(src_path)
print(sys.path)