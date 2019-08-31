x=1
scope = vars()
# print(scope['x'])


arg=1
def func(arg):
    print (arg+globals()['arg'])

func(2)