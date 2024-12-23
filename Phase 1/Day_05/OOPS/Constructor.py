class MyClass1:
    # name=''
    # c=MyClass1()
    # c.name='Ram'
    # print(c.name)
    def __init__(self,name):
        self.name=name
obj=MyClass1("Ram")
print(obj.name)