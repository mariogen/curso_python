'''
https://docs.python.org/3/tutorial/inputoutput.html
Esse script mostra algumas maneiras de ler um arquivo csv
O arquivo csv contem dados de plano de saúde individual
referência: www.kaggle.com/mirichoi0218/insurance
'''

#para ler um arquivo usamos a função open
#o primeiro parametro é o  nome do arquivo
#o segundo r: leitura, w: escrita, a: apendar, r+:leitura + escrita
f = open('datasets/data/insurance.csv', 'r')

#a função read lê o arquivo inteiro e devolve uma string com todo o conteúdo
arquivo = f.read()

#após as operações no arquivo não esquecer de fecha-lo
f.close()

#usando a função split para separar o arquivo linhas
linhas = arquivo.split('\n')

#o número total de linhas é:
print('numero de linhas:',len(linhas))

#a primeira linha do arquivo é:
print('cabeçalho   :', linhas[0])

# ultima linha do arquivo é:
print('ultima linha:', linhas[-1],'\n')

#podemos usar o split novamente para obter uma lista dos campos no cabeçalho
campos = linhas[0].split(',')
for i,campo in enumerate(campos):
    print('campo',i,'==>',campo)

'''
Outra maneira de ler o arquivo é usando a sintaxe with-as
O arquivo é fechado automaticamente ao fim do bloco,
o que é considerado uma boa prática.
'''

with open('datasets/data/insurance.csv', 'r') as f:
    arquivo = f.read()

'''
Ao invés de ler o arquivo todo com a função read, podemos usar readline
ou mesmo usar o arquivo como um iterador nas linhas
'''

with open('datasets/data/insurance.csv', 'r') as f:
    cabecalho = f.readline().split(',')
    #para ler os próximos linhas podemos usar o arquivo como um iterador 
    registros = []
    for linha in f:
        registros.append(linha.split(','))
    #registros = [linha.split(',') for linha in f]
    #registro = f.readlines()
    #registros = list(f)
    
#imprime cada campo do cabecalho, separando por tab 
print(*cabecalho,sep='\t')
#imprime os 10 primeiros registros
for i in range(10):
    print(*registros[i],sep='\t')

#obtendo lista de idades
idades = [int(registro[0]) for registro in registros]
print('min idade:',min(idades),'\nmax idade:',max(idades))

'''
Analogamente para escrver um arquivo podemos usamos open com a flag 'w'
podemos usar a função join para tranformar listas em strings
'''
with open('datasets/data/insurance_out.csv', 'w') as f:
    f.write(','.join(cabecalho))
    #para ler os próximos linhas podemos usar o arquivo como um iterador 
    for registro in registros:
        f.write(','.join(registro))






