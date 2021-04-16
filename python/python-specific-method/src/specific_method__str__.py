#特殊method是python預先定義好名稱的method，對python有特殊含義
#特殊method不會直接被呼叫，是python會自動呼叫它(但我們可以定義)
#特殊method都是__開頭，__結尾
#如__init__，__str__

#以下範例為__str__，當python需要以字串形式表示刻類所產生的物件時
#就會自動呼叫__str__
class Color:
    def __init__(self,red,green,blue):
        self._red=red
        self._green=green
        self._blue=blue
    
    def __str__(self):
        return f'Color: R={self._red:d}, G={self._green:d}, B={self._blue:d}'

c=Color(15,2,3)
print(c)