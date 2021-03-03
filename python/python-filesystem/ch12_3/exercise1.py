#os.path.exists(路徑)，檢查路徑是否存在，存在回傳true，不存在回傳false
#os.path.isfile(路徑)，檢查路徑是否指向檔案，是則回傳true,不是則回傳false
#os.path.isdir(路徑)，檢查路徑是否指向目錄，是則回傳true，不是則回傳false
#os.path.islink(路徑),檢查路徑是否為symbolic link，適用linux 
#os.path.ismount(路徑)，檢查路徑是否為挂載點(mount point)
#os.path.samefile(路徑1，路徑2)檢查路徑1與路徑2是否為相同檔案
#os.path.isabs(路徑)，檢查路徑是否為絕對路徑
#os.path.getsize(路徑)，傳回路徑的大小
#os.path.getmtime(路徑)，傳回路徑的上次修改時間
#os.path.getatime(路徑)，傳回路徑的上次存取時間
#os.scandir()取得目錄內所有子目錄與檔案完整的資訊，會傳回可走訪的os.dirEntry物件，包含所有子目錄與檔案，可以使用for迴圈逐一取得各項目
import os
with os.scandir("../../python-filesystem") as my_dir:
    for entry in my_dir:
        print(entry.name,entry.is_file())