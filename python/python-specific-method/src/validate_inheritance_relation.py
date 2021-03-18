class A:
    pass

class B(A):
    pass 

class C:
    pass

class D(B):
    pass 

class E(D):
    pass

x=12
c=C()
d=D()
e=E()

#isinstrance()函式可以判斷物件與類別是否有從屬或繼承關係
print('isinstance(x,E) : ', isinstance(x,E))
print('isinstance(c,E) : ',isinstance(c,E))
print('isinstance(e,E) : ',isinstance(e,E))
print('isinstance(e,D) : ',isinstance(e,D))
print('isinstance(e,B) : ',isinstance(e,B))
print('isinstance(d,E) : ',isinstance(d,E))

y=12
print('isinstance也可以測試內建型別 isinstance(y,type(5)) : ',isinstance(y,type(5)))

#issubclass(類別1,類別2)
#判斷類別是否有繼承關係

print('issubclass(C,D) : ',issubclass(C,D))
print('issubclass(E,D) : ', issubclass(E,D))
#E 繼承類別D，類別D又繼承類別B
print('issubclass(E,B) : ',issubclass(E,B))
print('issubclass(e.__class__,D) : ',issubclass(e.__class__,D))
#類別會被視為是自己的子類別
print('issubclass(D,D) : ', issubclass(D,D))

