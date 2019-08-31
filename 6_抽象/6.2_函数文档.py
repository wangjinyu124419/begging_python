def fun(*args):
    '这是函数文档'
    print (args)
    return args

print(fun.__doc__)
fun(1,2,3)