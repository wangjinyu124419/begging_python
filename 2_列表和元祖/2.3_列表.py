# list方法可以将任何可迭代对象转换成列表
test_dict={'a':1,'b':2}
print(list(test_dict))
print(list(test_dict.items()))

#给切片赋值
name= list('abcd')
print(name)
name[2:]=list('ef')
print(name)


#extend与+拼接的不同
#extend无返回值，直接对list1修改
list1=[1,2]
list2=[3,4]
res=list1.extend(list2)
print(res,list1)
#+拼接返回新列表，不改变list1
list3=list1+list2
print(list1)
print(list3)


#pop是为一个一个既有返回值有修改原列表的方法
print(list2)
res=list2.pop()
print(res,list2)

#reverse反转列表
list_reverse=[1,2,5,4]
list_reverse.reverse()
print(list_reverse)