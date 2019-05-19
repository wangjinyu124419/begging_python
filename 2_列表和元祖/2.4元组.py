#创建只包含一个元素的元组，一定要加逗号
t1=(2)
t2=(2,)
print(type(t1),type(t2))
#<class 'int'> <class 'tuple'>
print(t1*10,t2*10)
#20 (2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
t1=('a')
t2=('a',)
print(type(t1),type(t2))
#<class 'str'> <class 'tuple'>

t3=('a','a','b')
print(t3.index('a'))
print(t3.count('a'))
