x=y=['a','c']

#del只是删除引用，相当于只删除名字，不会删除真正地址内容
del x
# print(x)

print(y)

# exec将字符串作为代码执行
exec("if 1>0:print('exec')")
#命名空间
from math import sqrt
scope={}
exec('sqrt=1',scope)
exec('sqrt=1')
print(sqrt(4))

eval()