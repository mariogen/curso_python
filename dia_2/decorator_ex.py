"""
para mais info sobre lru_cache
docs.python.org/3/library/functools.html
"""

from functools import lru_cache
from time import sleep

@lru_cache()
def calculo_demorado(num):
    sleep(3) #simulando um computação complexa
    return 2*num

calculo_demorado(1)
calculo_demorado(1)
calculo_demorado(2)
calculo_demorado(2)
calculo_demorado(1)
calculo_demorado.cache_info()
calculo_demorado.cache_clear()

def my_decorator(f):
    def g(x):
        print('input = ',x)
        y = f(x)
        print('output = ',y)
        return y
    return g

@my_decorator
def mais_um(x):
    return x+1

@my_decorator
def menos_um(x):
    return x-1

mais_um(7)
menos_um(7)


