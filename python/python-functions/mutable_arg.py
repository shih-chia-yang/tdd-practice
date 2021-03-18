from subprocess import list2cmdline
# 當參數是可變物件時，當做引數傳入函式中處理且被更改時，外部變數也將會改變
nums=[1,2,3,4,5,6,7,8,9]

def sum(numlists):
    if isinstance(numlists,list):
        num=numlists.pop(0)
        print(num)

sum(nums)
print(nums)