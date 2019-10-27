from  warnings import warn
def fun(x,y):
    try:
        a=x/y
    except ZeroDivisionError:
        print('异常')
    else:
        print(a)
    finally:
        print(a)
# print('继续执行')

# try:
#     1/0
# except ZeroDivisionError:
    #异常上下文
    #raise ValueError from  None


#warn只执行一次
while True:
    warn('warning something')
if __name__ == '__main__':
    pass
    # fun(2,1)