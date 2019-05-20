#不定长解包
a,b,*args=1,2,3,4,5
print(a,b,args,type(args))

#链式赋值
x=y=1
print(x,y)


#布尔转换
print(bool('a'))
print(bool(''))
print(bool([1]))
print(bool([]))

#条件表达式
a=5 if 1>0 else -5
print(a)
a=5 if 1<0 else -5
print(a)


#字符串和序列比较大小

print('abc'>"aac")

#ord获取字母shunxuzhi
print(ord('a'))
print(ord('c'))
print(ord('A'))

print([1,2]>[1,1])
#延时求值
#and,如果为假返回前面，如果如果为真，返回后面
print([] and 1)
print(1 and [1])
#or如果为真，返回第一个真值，如果为假，返回最后一假值
print([1] or 0)
print(0 or [])
print(0 or [1])

#exec执行字符串语句，无返回值
exec("4+8")


#字符串返回值
res=eval("4+8")
print(res)