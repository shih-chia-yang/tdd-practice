class TypedList:
    def __init__(self,example_element,initial_list=[]):
        self.type=type(example_element)
        if not isinstance(initial_list ,list):
            raise TypeError("TypedList的第2個參數必須是list")
        for element in initial_list:
            self.check(element)
        self.elements=initial_list[:]

    def check(self,value):
        if type(value) is not self.type:
            raise TypeError("新元素型別不允許加入此TypedList.")
        return True
    
    def __setitem__(self,index,element):
        self.check(element)
        self.elements[index]=element

    def __getitem__(self,index):
        return self.elements[index]

    def __len__(self):
        return len(self.elements)

    def __delitem__(self,index):
        del self.elements[index]

    def append(self,element):
        self.check(element)
        self.elements.append(element)

# x=TypedList('hello',["list","of","strings"])
# print(x.elements)
