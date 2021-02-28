from subprocess import list2cmdline

nums=[1,2,3,4,5,6,7,8,9]

def sum(numlists):
    if isinstance(numlists,list):
        num=numlists.pop(0)
        print(num)

sum(nums)
print(nums)