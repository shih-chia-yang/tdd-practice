#shelve物件視為一個字典，該字典的資料是儲存在磁碟機上，不是保存在記憶體中
#意味著您仍然可以很方便的利用字典的鍵來進行存取大量資料，無需受到記憶體大小的限制
#允許在大型檔案中讀取或寫入資料片段而無需讀寫整個檔案
#shelve內部以pickle來將資料序列化

#假設通訊錄中的每個項目都由三個元素的tuple所組成
# 姓名、電話號碼、地址、使用員工編號作為索引

import shelve

test_address_file="./tests/address"
with shelve.open(test_address_file) as book:
    book['167']=('test1','0912-345678','雲林縣斗六市大學路一段')
    book['928']=('test2','0922-233456','雲林縣斗六市大學路二段')

with shelve.open(test_address_file) as book:
    print(book['167'])

#shelve.open()傳回一個shelf物件，允許基本字典操作、del、in、keys()方法
# 與dict不同的是shelf物件將資料儲存在磁碟機上
# shelf物件限制：shelf物件只能使用字串作為鍵，而字典允許使用多種類型的鍵
#可以pickle的python物件可shelf物件的鍵值