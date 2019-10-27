class A():
    def __init__(self):
        self.name="A"
    @staticmethod
    def static_method():
        print("I'm static method")
    @classmethod
    def class_method(cls):
        print("I'm class method")

a=A()
a.static_method()
A.static_method()

a.class_method()
A.class_method()

