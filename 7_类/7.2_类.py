
#私有属性
class Private():
    def __init__(self):
        self.__name='wang'
    def get_name(self):
        print (self.__name)

p=Private()
# print(p.__name)
# print(p._name)
p.get_name()

"在类定义中，对所有以两个下划线打头的名称都进行转换，即在开头加上一个下划线和类名"
print(p._Private__name)

"""
如果你不希望名称被修改，又想发出不要从外部修改属性或方法的信号，可用一个下划线打
头。这虽然只是一种约定，但也有些作用。例如，from module import *不会导入以一个下划线
打头的名称
"""

#继承
"要确定一个类是否是另一个类的子类，可使用内置方法issubclass。"
class Parent():
    pass
class Grandfather():
    pass
class Other():
    pass
class Children(Parent,Grandfather):
    pass

# print(issubclass(Parent,Children))
print(issubclass(Children,(Parent,Grandfather)))
print(issubclass(Children,(Parent,Other)))

#访问基类
print(Children.__bases__)

#确定实例是哪个类
c=Children()
print(c.__class__)
print(isinstance(c,Children))
print(isinstance(c,Parent))
print(isinstance(c,Grandfather))

print(hasattr(list,'__len__'))
print(getattr(list,'__len__'))
print(callable(getattr(list,'__len__')))

#抽象基类
from abc import ABC ,abstractmethod
class A(ABC):
    @abstractmethod
    def test(self):
        pass

class B():
    def test(self):
        print('test')
b=B()
print(isinstance(b,A))
