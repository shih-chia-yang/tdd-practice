
#pathlib說明文件
# https://docs.python.org/3/library/pathlib.html
# using pathlib 取得目前所在目錄
import pathlib
cur_path=pathlib.Path()
print(cur_path.cwd())

# .joinpath()
print(cur_path.joinpath('bin','utils','disktools'))

#將特定路徑作為參數傳入Path()，建立該路徑的路徑物件
a_path=pathlib.Path('bin/utils/disktools')
print(a_path.parts)
#傳入的路徑是相對路徑，可以用resolove()方法取得絕對路徑
print(a_path.resolve())
#basename
a_path=pathlib.Path('some','directory','path.jpg')
print(a_path.name)
#dirname
print(a_path.parent)
#副檔名
print(a_path.suffix)
