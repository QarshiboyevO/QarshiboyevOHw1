import random
import time
def decorator_1(func):
    def wrapper(*args, **kwargs):
        starttime = time.time()
        result=func(*args, **kwargs)
        endtime = time.time()
        totaltime = endtime - starttime
        print(f"{func.__name__} the time for execution, {totaltime:.6f} seconds")
        return result
    return wrapper
@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)


@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


@decorator_1
def printingname(string):
    print(string+string[::-1] )


