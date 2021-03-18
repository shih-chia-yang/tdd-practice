# 函式是python first-class object 
# 可以將函式指定給變數
# 可以將函式作為引數傳遞給函式
# 當作其他函式的傳回值

# tip first-class object
#從社會學的first-class citizen延伸的名詞，指函式與數字、字串等一視同仁，可以進行任何操作
#例如存放在list中、傳遞為函式參數、當作函式傳回值，相對來說，c語言的函式便不能當作其
#他函式的參數，沒有和數字、字串等一視同仁，就像二等公民一樣缺少某些權利

#example
def decorate(func):
    def wrapper_func(*args):
        print(f'befor exec {func.__name__}')
        func("<html>{0}</html>".format(*args))
        print(f'after exec {func.__name__}')
    return wrapper_func

@decorate
def myfunction(parameter):
    print(parameter)

# myfunction=decorate(myfunction)
# myfunction("hello")

# using @decorate syntactic sugar
myfunction("hello")