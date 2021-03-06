from Circle import Circle

c1=Circle(2)
c1.move(3,4)

print(c1.x,c1.y)


#類別變數與物件變數的繼承
#若為變數賦值時，該變數會在物件內自動產生，不會影響父類別的類別變數
#以下範例呈現 Class  C的set_c與print_c都會參照到同一個變數c.x
#參照到的物件變數名稱相同時，理應指向同一個變數，若需要不同的行為
#可透過使用私有變數實現
class P:
    z="hello"
    def set_p(self) :
        self.x="Class p"
    def print_p(self):
        print(self.x)

class C(P):
    def set_c(self):
        self.x="Class c"
    def print_c(self):
        print(self.x)

c=C()
c.set_p()
c.print_p()
c.print_c()

c.set_c()
c.print_p()
c.print_c()

print(c.z,C.z,P.z)
C.z="Bonjour"
print(c.z,C.z,P.z)
c.z="Ciao"
print(c.z,C.z,P.z)

c2=Circle()
print(c2.radius,c2.x,c2.y)
#提供初始值參數
c3=Circle(2,1,1)
print(c2.radius,c2.x,c2.y)

#呼叫move方法，在Circle類別中找不到move方法
#會沿著繼承層次結構向上尋找，最後會使用shape類別的move方法
c2.move(2,2)
print(c2.radius,c2.x,c2.y)

print(Circle.all_circles)
print(c1,c2,c3)

#類別方法
print(Circle.sum_area())
#物件方法
print(c2.sum_area())

#靜態方法不會傳遞物件或類別至第一個參數，反而比較像是類別內的獨立函式。
#通常會用靜態方法將一些公用函式包在類別裡

#把靜態方法當公用函式直接使用
print(Circle.circle_area(c3.radius))
print(c3.circle_area(c3.radius))