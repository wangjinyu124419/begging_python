s1='hello\nworld'
s2='hello world2'
print(str(s1))
print(repr(s1))
print('-'*100)

#sep参数，默认空格，设置为sep，s1和s2用sep连接，
s1='hello world'
s2='hello world2'
print(s1,s2,sep='sep')
print('-'*100)

# end默认值\n,换行，
print(s1)
print(s2)
print(s1,end='')
print(s2)
print('-'*100)
# file默认None，如果设置为文件对象f，s1和s2不会再控制台输出，直接写入到文件中
f=open('str.txt','w')
s='file_test'
print(s,file=f)

#flush默认为Flase，如果设置True，控制台不会输出内容
s='flush'
# print(s,)
print(s,flush=True)


#原始字符串
print(r'wangji\nnyu/')
#不能以反斜杠\结尾
# print(r'wangji\nnyu\')
print(r'wangji\nnyu\\')
print(r'wangji\nnyu'+'\\')

print('-'*100)

print('\u00C6')
print('\U0001F60A')
print('\N{cat}')
print('\N{dog}')
print('\N{fish}')
print('-'*100)

x=bytearray(b'hello world')
print(x)
x[0]=ord(b'r')
print(x)
