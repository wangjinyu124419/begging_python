class Father():
    def __init__(self):
        self.name = 'father'

class Parent(Father):

    # def __init__(self):
    #     pass
        # self.name=  'parent'
    def __call__(self, *args, **kwargs):
        pass

class Children(Parent):
    def __init__(self):
        # super(Children,self).__init__()
        super().__init__()
    @property
    def fun(self):
        pass


child = Children()
print(child.name)