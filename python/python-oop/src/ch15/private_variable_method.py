# private variable & private method無法從類別與所屬物件之外存取
#用途1：限制外部存取物件的重要資料來增強安全性和可靠性
#用途2 防止可能因繼灣所引起的名稱衝突
#類別定義私有變數後，就算父類別也有同名的私有變數，亦不會導致問題
#使用__開頭，結尾沒有__的任何方法或物件變數都是私有的
#單底線開頭的變數也是私有變數
#單底線開頭只是約定成俗的私有變數，不像雙底線開頭的變數具有無法直接存取的特性
#雖可以直接存取，但應該視為私有變數，不要隨便從外部存取
class Mine:
    def __init__(self):
        self.x=2
        self.__y=3
        pass

    def print_y(self):
        print(self.__y)

m=Mine()
#x 不是私有變數，可直接存取
print(m.x)

try:
    print(m.__y)
except Exception:
    print("不可直接存取私有變數")

m.print_y()