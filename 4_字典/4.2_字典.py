#字典格式化
d1={'wang':123,'li':321}
print("wang's num is {wang}".format_map(d1))
#fromkeys创建字典
d2=dict.fromkeys(['a','b','c'])
d3=dict.fromkeys(['a','b','c'],True)
print(d2)
print(d3)

print(d1.pop('wang'))
print(d1)

print(d1.popitem())
print(d1)
# setdefault
d4={'a':1,'b':2}
d4.setdefault('a','2')
d4.setdefault('c','2')
print(d4)

#update更新字典
d1={'a':1,'c':3}
d2={'b':2,'c':4}
print(d1.update(d2))
print(d1)