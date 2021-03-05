#pickle模組可以儲存任何資料，可以處理list,tuple,數字,字串,字典，自訂類別與物件instance
#還能正確處理共享物件(多個變數參照到同一個物件)、循環參照、和其他複雜的記憶體結構
#pickle能儲存共享物件並將它們恢復為共享物件

import pickle

a="break"
b="ok"
c="rework"
_tset_file_path="./tests/data1"
def save_data():
    global a,b,c
    with open(_tset_file_path,'wb') as data:
        pickle.dump(a,data)
        pickle.dump(b,data)
        pickle.dump(c,data)

def restore_data():
    global a,b,c
    with open(_tset_file_path,'rb') as data:
        print(pickle.load(data))
        print(pickle.load(data))
        print(pickle.load(data))