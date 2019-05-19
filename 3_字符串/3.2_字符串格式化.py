from  string import  Template
format="hello,%s,hello,%s"
values=('world','python')
# format % values
print(format % values)

#字符串模板
tem1=Template("hello,$A,hello,$B")
print(tem1.substitute(A='world', B='python'))


#format索引
format_str="{0} {1} {2} {3} {0} {1}".format('to','be','or','not')
print(format_str)

#format格式化
from math import  pi
print('{name} is approximately {value}'.format(value=pi,name='pi'))
print('{name} is approximately {value:.2f}'.format(value=pi,name='pi'))

#在Python3.6以后，如果变量名与替换字段名相同，可以简写，字符串前面加个f
print(f"{pi} is approximately 3.14")

#转换标志
print("{pi!s} {pi!r} {pi!a}".format(pi='π'))

#用<>^指定左对齐中对齐右对齐
print('{:010.2f}'.format(pi))
# 0代表索引
print('{0:<10.2f}\n{0:>10.2f}\n{0:^10.2f}'.format(pi))
print('{a:^10.2f}'.format(a=pi))
