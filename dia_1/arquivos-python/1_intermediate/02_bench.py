

import time

t0 = time.time()
# code_block
t1 = time.time()

total = t1-t0




from math import sqrt

def fib_v1(n):
    if   n == 0:return 0
    elif n == 1: return 1
    return fib_v1(n-1)+fib_v1(n-2)

def fib_v2(n):
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))




fibs = fib_v1, fib_v2 #, fib_v3
nums = range(5)

res = [ [ f(n) for n in nums ] for f in fibs ]















# from pprint import *
# pprint(res)


# import numpy as np

# print(np.array(res))


# def fib_v3(n):
#     return list(_fib_v3(n))

# def _fib_v3(n):
#     a,b = 0,1
#     c = 0
#     while True:
#         c+=1
#         if c<n: return
#         yield a
#         a, b = b, a + b