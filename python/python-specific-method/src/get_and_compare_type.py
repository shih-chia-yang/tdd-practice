#可以使用type來取得型別
#type()函式就是找出物件所屬的類別，在pythond型別與類別是一個同義詞
print("type(5) : ",type(5))
print("type(['hello','goodbye']) : ",type(['hello','goodbye']))

#comapre
print(",type('hello')==type('goodbye') : ",type("hello")==type("goodbye"))
print(',type("hello")==type(5) : ',type("hello")==type(5))

#檢查變數型別
s="hello"
print("檢查參數的型別是不是字串  str : ",type(s)==str)