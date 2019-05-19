import  string

print(string.digits)
print(string.ascii_letters)
print('1' in string.digits)
print('a' in string.ascii_letters)

s='center'
print(s.center(100,'-'))
print(s.ljust(100,'-'))
print(s.rjust(100,'-'))
print(s.zfill(100))
print(s.find('te'))
print(s.find('te',1,3))
print(s.find('ted'))
print('ce' in s)
print(s.replace('ce','cb'))
s2='**wangjinyu**python**'
print(s2.strip())
print(s2.strip('*'))

#translate方法
# 只能转换单个字符
#首先建立转换表
table1=str.maketrans('ab','xy')
table2=str.maketrans('ab','xy','c')
s3='abcbacacb'
print(s3.translate(table1))
print(s3.translate(table2))
