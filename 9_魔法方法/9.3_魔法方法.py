class A():
    def __init__(self):
        self.name='getitem'
        self.list=[1,2,3,4,5]
    def __getitem__(self, item):
        return self.list[item]
a=A()
print(a[1])
