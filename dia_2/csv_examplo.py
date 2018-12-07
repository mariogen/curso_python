'''
https://docs.python.org/3/library/csv.html
O leitor de csv já abstrai os delimitadores, quotechar e outras facilidades
A ideia é obter uma matrix de dados com facilidade
Na abertura do arquivo deve ser passado o argumento newline=''
'''

import csv

with open('files/insurance.csv', 'r', newline='') as f:
    reader = csv.reader(f,delimiter=',',quotechar='"')
    linhas = []
    for linha in reader:
        linhas.append(linha)
    #linhas = [linha for linha in reader]
    #linhas = list(reader)

idades = [int(linha[0]) for linha in linhas[1:]]
print('min idade:',min(idades),'\nmax idade:',max(idades))

print()

with open('files/insurance_out.csv', 'w', newline='') as f:
    writer = csv.writer(f,delimiter=',',quotechar='"')
    for linha in linhas:
        writer.writerow(linha)
    
#Podemos ler cada linha como um dicionário, manipular os dados + naturalmente
with open('files/insurance.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    linhas = []
    for linha in reader:
        linhas.append(linha)
    #linhas = [linha for linha in reader]
    #linhas = list(reader)

idades = [int(linha['age']) for linha in linhas]
print('min idade:',min(idades),'\nmax idade:',max(idades))

#Podemos escrever cada linha como um dicionário também
with open('files/insurance_out.csv', 'w', newline='') as f:
    campos = linhas[0].keys()
    writer = csv.DictWriter(f, fieldnames=campos)

    writer.writeheader()
    for linha in linhas:
        writer.writerow(linha)

