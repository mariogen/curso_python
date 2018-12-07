#https://docs.python.org/3/library/ctypes.html
#rodar direto no anaconda prompt

from ctypes import cdll,c_double

msvcrt = cdll.msvcrt

printf = msvcrt.printf

printf(b"Hello, %s\n", b"World!")

printf(b"%d bottles of beer\n", 42)

#printf(b"%f bottles of beer\n", 42.5)
printf(b"An int %d, a double %f\n", 1234, c_double(3.14))

printf(b"%d %d %d", 1, 2, 3)
