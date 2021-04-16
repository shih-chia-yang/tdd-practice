class A:
    pass

class B(A):
    pass

b=B()
print('type(b) :',type(b))
print('透過__class__取得相同資訊: ',b.__class__)

b_class=b.__class__
print('compare reference type : ',b_class==B)
print('透過__name__取得類別名稱 :',b_class.__name__)
print('透過__basees__取得繼承那些類別',b_class.__bases__)