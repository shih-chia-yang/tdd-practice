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
