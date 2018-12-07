

class Set(set):
    def __add__(self, other):
        return Set.union(self, other)
    def __mul__(self, other):
        return Set.intersection(self, other)
    def __xor__(self, other):
        return Set.union((self-other),(other-self))
    __and__ = __mul__
    __or__  = __add__

print(Set([1,2,3]) + Set([3,4,5]))
print(Set([1,2,3]) * Set([3,4,5]))
print(Set([1,2,3]) ^ Set([3,4,5]))



class Range(tuple):

    def __new__(cls, *args):
        n = len(args)

        if n==0:
            tup = ()

        elif n==1:
            a = args[0]
            if a>0:
                tup = tuple(range(int(a)))
            else:
                tup = tuple(-x for x in range(int(-a)))[::-1]

        elif n==2:
            a, b = args

            if a <= b:
                tup = tuple(a+x for x in range(int(b-a)))
            else:
                tup = tuple(a-x for x in range(int(a-b)))

        elif n==3:
            a, b, k = args

            if a <= b:
                tup = tuple(a+x*k for x in range(int(b-a)))
            else:
                tup = tuple(a-x*k for x in range(int(a-b)))

        return tuple.__new__(Range, tup)

    def __mul__(self, other):
        if isinstance(other, (int, float, complex) ):
            return tuple( x*other for x in self )
        return tuple( (i, j) for i in self for j in other )

    def __rmul__(self, other):
        if isinstance(other, (int, float, complex) ):
            return tuple( x*other for x in self )
        return tuple( (j, i)  for j in other for i in self )


print()
print(Range(10)*Range(-10))
print()

print(Range(10))
print(Range(-10))
print(Range(1,10))
print(Range(-1,-10))
print(Range(10,1))
print(Range(-10,-1))
print(Range(1,10, 2))
print(Range(-1,-10, 2))
print(Range(10,1, 2))
print(Range(-10,-1, 2))
print(Range(1,10, 0.5))
print(Range(-1,-10, 0.5))
print(Range(10,1, 0.5))
print(Range(-10,-1, 0.5))
print(Range(-10,-1, 0.5))
print()

print(Range(-10)*5)
print(Range(1,10)*5)
print(5*Range(-10))
print(5*Range(1,10))
print()


# Estrutura de grafo e árvore (fazer junto com os alunos se houver tempo)

# class Tree(object): pass
# class Graph(object): pass
