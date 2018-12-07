# -*- coding: utf-8 -*-
"""
 Multiplas linhas podem ser utilizadas como strings

"""

######################################################################
#########              Elementos Básicos de Python           #########  
######################################################################

# usado para comentar linhas
# Shift + Enter para rodar seleção

# Operações Matemáticas 
1 + 5               # Soma
2 - 8               # Subtração
2 * 5               # Multiplicação
20 / 3              # Divisão
2 ** 5              # Potência
13 % 2              # Módulo (Resto da Divisão Inteira)

# Uso do parênteses
( 5 + 3 ) * 2
5 + 3 * 2

# Strings sao criadas com " ou '
'Isso é uma string'
"Palavra"

# Atribuição
a = 3
b = 5
c = a * b
c

# Booleanos: True ou False
3 == 3
3 == 4

1 != 1 # diferente
1 != 2

1 > 10
1 < 10
2 < 2
2 <= 2

# And / or

a < 5 and a > 1
a > 1 and a < 3
a > 1 or a < 3


######################################################################
##################                 LISTA            ##################
######################################################################

a = [ 1, 2, 3, 4 ]  # Criar uma lista
a

b = [ 190, 10, -3, 'b']     # pode conter strings, e até mesmo uma lista
b

lista = [ a, 3, 28 ]
lista

# _________________ Indexing 
# Acessar elementos específicos dentro de uma lista, de acordo com a sua posição

d = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
c = [ 10, 11, 12, 13, 14, 15, 16, 17]

d[2]
#  !!!!! começa sempre com indice 0
d[0]
d[1]

d[-1]   # sinal de '-' -> começa pelo fina da lista


# fazer comparações com a lista 'c'

# mesmo para strings
'palavra'[3]
nome = 'Gustavo'
nome[0]
nome[5]
nome[-1]


# _________________  SLICE
# acessar partes das listas

d[3:6]  # [ inicio(inclusive):fim(exclusive)]

c[2:5]
c[0:7] 
c[:7]
d[5:]
d[::-1]

d[5:2:-1]
#d[5:8:-1]     # retorna vazia, pq a lista é acessada de tras para frente

# retornar [14, 13, 12] por meio de slice da lista 'c'

# _________________  FUNÇÕES

len(c)
len(d)
len('palavra e string')

abc = [ ]       # criando uma lista vazia

# ( shift + tab para descrição
# ponteiro do mouse em cima da caixa de descrição para nao desaparecer

# adiciona um elemento no fim da lista
abc.append(3)
abc.append(4)
abc.append(6)
abc.append(8)
abc.append([5, 6])

# remove o elemento dado
abc.remove(3)

# remove o ultimo da lista e o retorna
abc.pop()

# inserir um elemento num local específico
abc.insert(0,1)  # insert(local, elemento)
abc

abc.insert(1,3)
abc

abc.insert(1,2)
abc

abc.index(6) # retorna a posição do elemento dado


######################################################################
#################     Control Flow and Iterables     #################
######################################################################

for i in range(4): 
    print(i)
    
for i in range(100,105): 
    print(i)
    

li = [ i for i in range(10)]
potencias = [ i**2 for i in range(10)]

d = [ i for i in range(35,46)] 
            
pares = [ i for i in range(0,20,2)]
         
ope = [ i+j for i in pares for j in potencias ]
len(pares), len(potencias)

li = list(range(0,10))

# for é iterável em listas
for animal in ['cachorro', 'gato', 'papagaio']:
    print(animal)

## if statement -> identação é necessária
numero = 10

if numero > 10:
    print('O numéro é maior que 10' )
elif numero < 10:
    print ('O numero é menor que 10')
else:
    print('O número é exatamente igual a 10')    

palavras = ['meia', 'paralelepipedo', 'uniforme', 'carro', 'universidade', 'dinheiro']    

for x in palavras:
    if len(x) < 4 :
        print('A palavra ', x, ' é PEQUENA')
    elif len(x) >= 4 and len(x) < 9:
        print( 'A palavra {a} é MEDIA'.format(a=x) )
    else:
        print('A palavra {y} é GRANDE'.format(y=x) )
              
x = 0
while x < 4:
    print(x)
    x += 1 

    # Not in
grupo1 = ['oleo', 'paralelepipedo', 'edificio', 'carro', 'casa']

for x in palavras:
    if x not in grupo1:
        print(x)    


        # Try and Except
# Usado para lidar com possíveis erros
# Se um erro é encontrado no bloco try, esse bloco é parado e vai para o bloco except
# Ainda pode ser usado um bloco finally que pode ser executado independente do resultado try/except

try:
    print(xrty)
except:
    print("An exception occurred")

# erro ocorreu pq xrty não foi definido anteriormente
  
try:
    print(xrty)
except NameError:
    print("Variable xrty is not defined")
except:
    print("Something else went wrong")

# # aproveita para falar do Ctrl + 1
#IOError '(Arquivo nao pode ser aberto)' 
#ImportError 'Um Modulo nao pode ser encontrado'
#ValueError 'Buil-in function com argumento de entrada errado/inapropriado'

try:
    print(xrty)
except:
    print("Something went wrong")
finally:
    print("The 'try / except' is finished")

x0 = 23   
x1 = 12
x2 = 0
    
try:
    y = x1/x2
except:
    y = 10**100
finally:
    z = y*x0
    print (z)

# testar com x2 = 0 

    
######################################################################
#################               Funções              #################
######################################################################

def adicao(x, y):
    resultado = x + y
    return resultado
    
def adicao(x, y):
    return x+y    

adicao(3,5)


#Continuando o exemplo de palavra pequena, media e grande, dessa vez chamando de tipo 1, 2 e 3
def tipo_palavra(palavra):
    if len(palavra) < 4 :
        tipo = 1
    elif len(palavra) >= 4 and len(palavra) < 9:
        tipo = 2
    else:
        tipo = 3
    return tipo


tipo_palavra('feijao')
tipo_palavra('bikvraoemnvgfda')

comidas = ['arroz', 'feijao', 'macarrao', 'maca', 'tomate', 'ovo', 'escondidinho']

tipos = [ tipo_palavra(i) for i in comidas ]
tipos

# Agora fazendo uma função que separe uma lista de palavras de entrada em listas do grupo pequeno, media e grande
def grupo_palavra (lista):
    p = []
    m = []
    g = []
    for palavra in lista: 
        if len(palavra) < 4 :
            p.append(palavra)
        elif len(palavra) >= 4 and len(palavra) < 9:
            m.append(palavra)
        else:
            g.append(palavra)
    return p,m,g

grupo_palavra(comidas)
p, m, g = grupo_palavra(comidas)
p,m,g

# Um exemplo usando mais de um dado de entrada e not in
def grupo_palavra_ex (lista,exceto):
    p,m,g = [],[],[]
    for palavra in lista: 
        if palavra not in exceto:
            if len(palavra) < 4 :
                p.append(palavra)
            elif len(palavra) >= 4 and len(palavra) < 9:
                m.append(palavra)
            else:
                g.append(palavra)
    return p,m,g

comidas = ['arroz', 'feijao', 'macarrao', 'maca', 'tomate', 'ovo', 'escondidinho']
gluten = ['macarrao', 'pao', 'bolo', 'farinha']

p, m, g = grupo_palavra_ex(comidas,gluten)
p,m,g


# exempplo numérico
# função só muda LOCAL 
# o GLOBAL não é alterado

def limites(lista):
    media = sum(lista)/len(lista)
    lim_sup = media*2
    lim_inf = media/2
    for i in lista:
        if i > lim_sup or i < lim_inf:
            lista.remove(i)
    return lista

idade = [35, 23, 31, 28, 2, 36, 31, 39, 30, 25, 85, 26, 28, 32 ]
nova = limites(idade)

          
######      Lambda:     Anonymous Function

a = lambda x: x**2
a(2)
a(10)

b = lambda x,y: x*2 + y*x + 2*y
b(5,3)

c = lambda x: x>5   # boolean
c(2)
c(10)


######################################################################
#################             Dicionário             #################
######################################################################

# coleção de itens NAO ORDENADOS
# composto pelo par key:value

my_dict = {}
my_dict = {'name':'Jack', 'age': 26}
my_dict

my_dict['name']
my_dict['age']

my_dict['adress'] = 'Downtown'
my_dict['age'] = 27
my_dict

del my_dict['age']
my_dict

my_dict.pop('adress')
my_dict

my_dict = {'name':'Jack', 'age': 26, 'adress':'Downtown', 'Occupation':'Engineer'}

my_dict.items()
my_dict.   #verificar o que tem disponivel de methods
my_dict.keys()
my_dict.values()




