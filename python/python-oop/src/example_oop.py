import Circle

c1=Circle.Circle(5)
print(c1.area())
#定義類別變數後，可以使用class.variable來存取與修改
#Circle.pi與Circle類別的任何物件無關
#直接用類別名稱存取類別變數具有缺點，萬一日後更改類別名稱時，沒有連動去更改類別名稱
#會發生錯誤，避免發生這個問題，可以用python物件的特殊屬性__class__來代表類別
c1.__class__.pi=4
print(c1.area())

c2=Circle.Circle(3)
c3=Circle.Circle(5)
print(Circle.Circle.total_area())
c2.radius=10
print(c2.total_area())

print(c2.total_perimeter())
assert c2.total_perimeter() == (2*4*5)+(2*4*10)+(2*4*5),"錯誤"