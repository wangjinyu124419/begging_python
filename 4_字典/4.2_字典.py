#字典格式化
d1={'wang':123,'li':321}
print("wang's num is {wang}".format_map(d1))
#fromkeys创建字典
d2=dict.fromkeys(['a','b','c'])
d3=dict.fromkeys(['a','b','c'],True)
print(d2)
print(d3)