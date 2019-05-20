#zip并行迭代
l1=['a','b','c','d']
l2=[1,2,3]
l3=[4,5,6]
for i in zip(l1,l2,l3):
    print(i)

#sorted排序可迭代对象，排序字符粗
s='hello world'
print(sorted(s))
s=['a','B','c']
print(sorted(s))
print(sorted(s,key=str.lower))

#多层列表推导式
l1=[(x,y) for x in range(3) for y in range(3)]
print(l1)
#等价于

l1=[]
for x in range(3):
    for y in range(3):
        l1.append((x,y))
print(l1)

#字典推导式
d1={i:i**2 for i in range(5)}
print(d1)