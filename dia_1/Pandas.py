"""
    Pandas: open source library built on top of Numpy.
    - fast analysis and data cleaning and preparation
    - has built-in visualization features
    - work with datda from a wide variety of sources

    conda install pandas / pip install pandas

"""
import numpy as np
import pandas as pd

# _________________________________________ DataFrames
# Ferramenta mais usada no Pandas
# Sao Séries com mais de uma coluna, onde cada coluna é uma Série
np.random.seed(101)         # todos usarem os mesmos numeros aleatorios
df = pd.DataFrame(data=np.random.randn(5,4) ,index=['A','B','C','D','E'], columns=['W','X','Y','Z'])
type(df)
type(df['W'])
print(df)
df['W']                                     # selecionar coluna
df[['W','X']]
df['new'] = df['W'] + df['X']               # adicionar coluna
print(df)
df.drop('new', 1)                           # Remover coluna    # duas OBS, axis e inplace
# deve ser colocado o 1 pq o default é remover linha (axis=0), para remover coluna axis=1
df.shape                                    # explica o pq de linha ser axis=0, e coluna axis=1

df.drop('new')                              # da erro
print(df)
df.drop('C')                                # Remover Linha, nao precisa especificar o axis
print(df)

df.drop('new', axis=1, inplace=True)         # para a modificação ocorrer no DataFrame
print(df)


#selecionar linha
df.loc['A']                                 # pelo indice da linha 
df.iloc[0]                                  # pelo indice da localização (numérica) da linha
df.loc[['A','B']]                           # lista de linhas
df.iloc[0:2]                                # intervalo de linhas

df.loc['A','Y']                             # valor especifico [linha,coluna]

df['W'].loc['A']

#Conditional Selection
df > 0                  
df[df>0]                                    # retorna apenas os valores do dataframe maiores que 0

df['lugar']=['casa','apto','apto','casa', 'apto']
print(df)
casa = df[df['lugar']=='casa']                               
apto = df[df['lugar']=='apto']
print('Matriz Casa: \n', casa, '\n')
print('Matriz Apto: \n',apto)

df[(df['lugar']=='casa') and (df['Y']>0)]         # erro   
df[ (df['lugar']=='casa') & (df['Y']>0) ]         # condições multiplas em Series
   
df[ (df['lugar']=='casa') or (df['W']<0) ]        # erro
df[ (df['lugar']=='casa') | (df['W']<0) ]         # condições multiplas em Series

df[df['lugar']=='casa']['W']

# _________________________________________ Operations

df = pd.DataFrame({'col1':[1,2,3,-4],'col2':[444,555,666,444],'lugar':['abc', 'def','ghi','xyz']})
print(df)
df['col2'].unique()                 # retorna um array com os valores nao repetidos(unicos) da coluna
df['col2'].nunique()                #retorna a quantidade de valores sem considerar as repetiçoes, é o mesmo que len(df['col2'].unique())
df['col2'].value_counts()           #retorna o numero de vezes que cada valor aparece na coluna
df['col2'].max()
df['col2'].idxmax()
df['col2'].min()
df['col2'].mean()
df['col2'].median()
df['col2'].quantile([0.5])
df['col2'].quantile([0.25])

# USEFUL
#  possibilita aplicar uma função em cada linha de uma determinada coluna
df['col1'].apply(abs)
df['col3'].apply(len)
df['col1'].apply(lambda x: x*2)

df.columns
df.index

df.sort_values('col2')                      # Reparar que o indice fica associado a linha
print(df)


# _________________________________________ MissingData

d = {'A':[1,2,np.nan], 'B':[5,np.nan, np.nan], 'C':[1,2,3]}
df = pd.DataFrame(d)

df.dropna()                         # default: axis=0 linhas
df.dropna(axis=1)
df
#df.dropna(axis=1, inplace=True)
df.dropna(thresh=2)                 # fica as linhas com pelo menos 2 valores NAO NA
df.fillna('PREENCHIDO')
df['A'].fillna('PREENCHIDO')
df
df['A'].fillna( df['A'].mean() )
df.fillna( df.mean() )


# _________________________________________ Merging, Joining and Concatenating

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']}, index=[0,1,2,3])
df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],'B':['B4','B5','B6','B7'],'C':['C4','C5','C6','C7'],'D':['D4','D5','D6','D7']}, index=[4,5,6,7])
df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],'B':['B8','B9','B10','B11'],'C':['C8','C9','C10','C11'],'D':['D8','D9','D10','D11']},index=[8,9,10,11])
print('\n',df1)
print('\n',df2)
print('\n',df3)
pd.concat([df1,df2,df3])                            # Default axis = 0 concatena pelas linhas
pd.concat([df1,df2,df3], axis=1)                    # axis = 1 concatena pelas colunas

df4 = pd.DataFrame({'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']}, index=[0,1,2,3])
df5 = pd.DataFrame({'E':['E0','E1','E2','E3'],'F':['F0','F1','F2','F3'],'G':['G0','G1','G2','G3'],'H':['H0','H1','H2','H3']}, index=[0,1,2,3])
print('\n',df4)
print('\n',df5)
pd.concat([df4, df5], axis=1 )                      # axis = 1 concatena pelas colunas


# combinar dataframes com indices diferentes, essa função faz a uniao de acordo com os indices
left = pd.DataFrame({'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']}, index=[0,1,2,3])
right = pd.DataFrame({'C':['C2','C3','C4','C5'],'D':['D2','D3','D3','D5']}, index=[2,3,4,5])
print('\n',left)
print('\n',right)
left.join(right)                        # permanece os indices do dataframe left
left.join(right, how='outer')           # todos os indices dos dois dataframe permanecem (sem perda de linhas/indices)


# _________________________________________ Data Input and Output

dados = pd.read_csv('exemplo.csv',sep=';')
dados
dados = pd.read_csv('C:\\Users\\Pro-Barco\\Desktop\\Gabi\\Curso Data Mining\\exemplo.csv')
dados = pd.read_csv('C:/Users/Pro-Barco/Desktop/Gabi/Curso Data Mining/exemplo.csv')

#salvar dataframe
dados.to_csv('saida.csv',index=False)
pd.read_csv('saida.csv')


# _________________________________________ GoupBy
# Possibilita juntar linhas baseado em dados de uma coluna e pode agregar alguma função a uma das colunas
dados = { 'Empresa':['A','A','B','B','C', 'C'], 
         'Pessoa':['Ana','Bia','Joao','Carlos','Dani','Bruno'],
        'Vendas':[200,120,340,124,243,350] }
df = pd.DataFrame(dados)
print(df)
empresa = df.groupby('Empresa')
empresa.mean()
df.groupby('Empresa').sum()
df.groupby('Empresa').std()
df.groupby('Empresa').sum().loc['A']
df.groupby('Empresa').count()
df.groupby('Empresa').max()         # string por ordem alfabetica
df.groupby('Empresa').describe()
df.groupby('Empresa').describe().loc['B']
df.groupby('Empresa').describe().transpose()
df.groupby('Empresa').describe().transpose()['B']






