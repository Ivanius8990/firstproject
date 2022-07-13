def newfunc(n):
    def myfunc(x):
        return x + n
    return myfunc
new = newfunc(100)
print(myfunc(100))