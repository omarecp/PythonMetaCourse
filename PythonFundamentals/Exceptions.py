def divideBy(a,b):
    return a/b

try:
    ans = divideBy(40,0)
except ZeroDivisionError as e:
    print(e,"we cannot divide by zero")
    print(e.__class__)
except Exception as e:
    print(e,"something went wrong")




