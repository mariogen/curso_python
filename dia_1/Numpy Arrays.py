
""" NumPy is a Linear Algebra Library for Python, the reason it is so important for Data 
    Science with Python is that almost all of the libraries in the PyData Ecosystem rely on 
    NumPy as one of their main building blocks.
    
    Numpy is also incredibly fast, as it has bindings to C libraries. For more info on why 
    you would want to use Arrays instead of lists 
    
    Numpy has many built-in functions and capabilities. 
    Exemplos de utilização do Numpy: vectors, arrays, matrices, and number generation.
    Arrays: vetores (1-D) e matrizes(2-D).
    
    conda install numpy    or      pip install numpy 
    
    User Guide:     https://docs.scipy.org/doc/numpy-1.15.0/numpy-user-1.15.0.pdf """
    
import numpy as np
# ________________________________________________ Criar Arrays
# Array a partir de uma lista    
lista = [1,2,3,4]   
print(lista)
np.array(lista) 
ar_lista = np.array(lista)
print(ar_lista)
array = np.array([5,3,9])
print(array)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)
np.array(matriz)

# Built-in Methods: built-in to generate Arrays
np.arange(10)               # Return evenly spaced values within a given interval."
np.arange(1,10,0.5)         # start(inclusive), stop(exclusive), step


# Random: numpy tem varias formas de criar random number arrays
np.random.rand(2)          # Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1)
np.random.rand(3,5)

np.random.randn(2)          # Return a sample (or samples) from the standard normal distribution
np.random.randn(6,6)

np.random.randint(10)
np.random.randint(1,100)    # Return random integers from low (inclusive) to high(exclusive) 
np.random.randint(1,100,10)

## ________________________________________________ Array Attributes and Methods
np.random.seed(303)         # todos usarem os mesmos numeros aleatorios
arr = np.arange(10)
a1 = np.random.randint(0,50,10)

print(a1)
a1.max()
a1.min()
a1.argmin()
a1.argmax()

# Shape:  is an attribute that arrays have (not a method):"
a1.shape
a1.reshape(2,5)
a8 = np.array([[5,7],[7,9],[9,11],[11,13],[13,15]])
a1.reshape(a8.shape)


# ________________________________________________ Array indexing / SLICE
d = np.arange(0,11)
c = np.arange(10,21)
print( 'c: ', c,'\nd: ', d)
d[2]
d[-1]
#  !!!!! começa sempre com indice 0
d[3:6]  # [ inicio(inclusive):fim(exclusive)]
c[8]
c[2:5]
c[0:7] 
c[:7]
d[5:]
d[::-1]


a3 = np.arange(0,11)
a3 > 5   #boolean
bol_a3 = a3>5
a3[bol_a3] # retorna somente os valores com 'True'
a3[a3>5]
a4 = a3[a3>5]

#Funções para Array

np.sqrt(array)
np.exp(2)
np.exp(array)
np.max(array)
array.max()

np.pi
np.sin(10)              # radianos
np.sin(90*np.pi/180)    # 90 graus
np.sin(array)
graus = np.arange(0,361,90)
np.sin(graus) 
np.sin(graus*np.pi/180)
np.rint(np.sin(graus*np.pi/180))

# https://docs.scipy.org/doc/numpy/reference/ufuncs.html



