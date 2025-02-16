def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
    
def myfunc1():
    x = "jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())