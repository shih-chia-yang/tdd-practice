#絕對路徑
# from mathproj import version
# from mathproj.comp import c1
# from mathproj.comp.numeric.n2 import h
#相對路徑
from ... import version
from .. import c1
from .n2 import h
#與模組的__name__屬性有相關性，若是套件中的模被當成主程式來執行
#該模組的__name__屬性將會是__main__，此時便無法使用相對路徑的方式匯入

def g():
    print(f'version is : {version}')
    print(h())