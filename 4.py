#http://www.jianshu.com/p/920bd6cdde61
from itertools import *

def fib():
    x,y = 0,1
    while True:
        yield x
        x,y = y,x+y

n = int(input())
print(next(islice(fib(), n, None)))

# for i in list(islice(fib(), n)):
#     print(i)


# max = int(input())
# n,a,b = 0,0,1
#
# while n < max:
#     print(b)
#     a,b = b,a+b
#     n += 1