

"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120

>>> factorial(20)
2432902008176640000

>>> factorial(30)
265252859812191058636308480000000
"""


import math


def main():
    import sys
    import doctest

    doctest.testmod(
        verbose = '-v' in sys.argv)


def light_factorial(n):
    """Return the factorial of n, an exact integer >= 0 (using log).

    >>> light_factorial(16)
    20922789888000
    """

    # import math

    return int(.5 + 2**sum(math.log2(x) for x in range(1,n+1)))

def safe_factorial(n): # based on https://docs.python.org/3/library/doctest.html
    """Return the factorial of n, an exact integer >= 0.

    >>> [safe_factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> safe_factorial(30)
    265252859812191058636308480000000
    >>> safe_factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> safe_factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> safe_factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> safe_factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    # import math

    if not n >= 0:
        raise ValueError("n must be >= 0")

    if math.floor(n) != n:
        raise ValueError("n must be exact integer")

    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")

    result = 1
    factor = 2

    while factor <= n:
        result *= factor
        factor += 1

    return result


def factorial(n):
    if n<=16: return light_factorial(n) 
    # else:
    return safe_factorial(n)


if __name__ == "__main__":
    main()
