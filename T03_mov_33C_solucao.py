# -*- coding: utf-8 -*-
"""
NOME:
MAT:
TURMA:
PROF:

Teste unico do Bloco2
@author: Joisa
"""
#OBS: ALUNO TEMPO EXTRA: Não fazer questões 5 e 7


import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_rows", 999) 
pd.set_option("display.max_columns", 999) 
pd.set_option("display.precision", 2) 
pd.set_option("float_format", '{:.2f}'.format)

# ENUNCIADO:
# Q1)
# Series srPrecos a partir da planilha preco do arquivo moveis.xlsx. A planilha tem 
# uma linha de cabeçalho e a primeira coluna deve ser usada como índice.
# 
# Series srVendidos a partir da planilha vendidos do arquivo moveis.xlsx. A planilha 
# tem uma linha de cabeçalho e a primeira coluna deve ser usada como índice.

# Series srEstoque a partir da planilha estoque do arquivo moveis.xlsx. A planilha 
# tem uma linha de cabeçalho e a primeira coluna deve ser usada como índice.

# Nas series criadas cada indice e´ um  movel com identificado  
# por duas palavras: tipoDoMovel linhaDoMovel
# Por exemplo  se o movel e´: MESA BAMBUI
# - o tipo do movel e´ MESA
# - a linha do movel e´BAMBUI


# Q2) => VALE 1.0 (0.2 por item)
# 2A)Crie a partir da srEstoque a series srNulos, apenas com as linhas com NAN. 
# Exiba a srNulos
# 2B)Exiba o percentual de valores validos na srEstoque 
# 2C)Apresente a visualização grafica do percentual de valores ausentes na srEstoque
# 2D)Exiba da srPrecos somente os elementos cujos indices NÃO estejam na srNulos 
# 2E)Exiba da srVendidos somente os elementos cujos indices estejam na srNulos 
# OBS: Não ALTERE nenhuma das 3 series 

# Q3) => VALE 0.6 (0.2 por item)
# Q3A) Para a srPrecos exiba JUNTOS (em um print): os 3 últimos com os 3 primeiros    
# Q3B) Exiba a srPrecos ordenada pelo movel
# Q3C) Exiba a srVendidos ordenada pelo quantidade vendida


# Q4) Considerando a series srPrecos responda:  => VALE 5.2 (0.4 por item)
# 4A)   Qual o preco do movel mais barato e um movel com esse preco
# 4b)	Qual o maior preco? Exiba todos os moveis com esse preco
# 4C)	Exiba todos os moveis com preço abaixo de 3000. 
# 4D)	Exiba todos os moveis da linha KANOA.
# 4E)	Em média, qual a linha de moveis mais barata? Qual o valor medio de um produto dessa linha?
# 4F)	Qual o preço médio de uma mesa?
# 4G)	Quais os 5 moveis mais baratos? 
# 4H)  Categorize os moveis em 5 faixas de preco: até 1500 (inclusive), de 1500 até 4000(inclusive), 
# de 4000 até 6000(inclusive),de 6000 até 8000 (inclusive), acima de 8000. 
# (Crie e exiba a srFxPreco)
# 4I)   Exiba a srFxPreco ordenada por categoria. 
# 4J)	Apresente a tabela de frequências das faixas de preco
# 4K)   Apresente a tabela de frequencias ordenada por categoria
# 4L)	Apresente a tabela de frequência percentual (relativa) das faixas de preco
# 4M)	Apresente uma visualização gráfica (pizza) da tabela de frequência percentual.

# 5) Considerando a series srVendidos responda: => VALE 1.2(0.3 por item)
# 5A)	Quantos móveis foram vendidos no total?
# 5B)	Qual(is) o móvel menos vendido? Quantas unidades?
# 5C)	Exiba os moveis que tiveram quantidade vendida entre 25 e 90.
# 5D)	Por LINHA de móveis, exiba:  Quantidade total vendida, 1 produto 
# mais vendido, 1 produto menos vendido

# Q6) Agrupe a srVendidos pelas Faixas de Preço obtidas anteriormente
# Por Faixa de Preço exiba: total de moveis vendidos, um movel menos vendido na faixa, 
# valor desse movel. => VALE 0.6

# Q7) GANHOS COM AS VENDAS : =>VALE 0.9 (0.3 por item)
# 7A) Valor total com as vendas por MÓVEL (nao e´por tipo de movel))
# 7B) Valor total com as vendas de todos os moveis
# 7C) Valor total com as vendas POR LINHA

# Q8) (vale 0.5) Preencha os valores ausentes da srEstoque com a média de estoque 
# por TIPO do  movel. Exiba a srEstoque.


srPrecos = pd.read_excel('moveis232.xlsx',sheet_name='preco', header=0, 
                         index_col=0).squeeze()

srPrecos= pd.Series(srPrecos) #para ter as dicas do ambiente

srVendidos= pd.read_excel('moveis232.xlsx',sheet_name='vendidos', header=0, 
                          index_col=0).squeeze()
 
srVendidos= pd.Series(srVendidos)

      
srEstoque= pd.read_excel('moveis232.xlsx',sheet_name='estoque', header=0, 
                          index_col=0).squeeze()
 
srEstoque= pd.Series(srEstoque)


                  
print('\n---------- 1 - series criadas -----------------')
print('\nsrPrecos:')
print(srPrecos)

print('\nsrVendidos')
print(srVendidos)

print('\nsrEstoque')
print(srEstoque)


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n--- 2 - Lidando com NaN-------')

print('\n2.A- Nulos')
srNulos= srEstoque.loc[srEstoque.isnull()]
print(srNulos)

print('\n2.B- Exiba o percentual de valores validos na srEstoque')
print(srEstoque.count()/srEstoque.size *100 ) # pode não multiplicar por 100

print('\n2.C- Visualização grafica do percentual de valores ausentes na srEstoque')
ss= srEstoque.isnull()
ss.replace({True:'Nulo', False:'NaoNulo'},inplace=True)
ss.value_counts().plot.pie(title='Perc de ausentes na srEstoque',
                           autopct=':.1f')
plt.show()

print('\n2.D- srPrecos: somente os elementos cujos indices NÃO estejam na srNulos  :')
print(srPrecos.drop(srNulos.index))

print('\n2.E - srVendidos: somente os elementos cujos indices estejam na srNulos :')
print(srVendidos.loc[srNulos.index])


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n------ 3.A - srPrecos: juntos:  3 ultimos com 3 primeiros------')
print(srPrecos.tail(3).append(srPrecos.head(3)))

# print('\n------ 3.B - srVendidas: juntos: 5 ultimos  com 2 primeiros ------')
# print(srVendidos.tail(5).append(srPrecos.head(2)))

print('\n------ 3.B - srPrecos ordenada pelo  movel ------')
print(srPrecos.sort_index())

print('\n------ 3.C - srVendidos ordenada pela quantidade vendida ------')
print(srVendidos.sort_values())


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n------4-Responda sobre a srPrecos ----------------')

print('\n4.A- Qual o preco do movel mais barato e um movel com esse preco?')
print(srPrecos.agg(['min','idxmin']))

print('\n4.B- Qual o maior preco? Exiba todos os moveis com esse preco')
print(srPrecos.max())
sma= srPrecos.loc[srPrecos==srPrecos.max()]
print(sma) # ou sma.index

print('\n4.C- Exiba todos os moveis com preço abaixo de 3000.')
sAb3000= srPrecos.loc[srPrecos<3000]
print(sAb3000)

print('\n4.D- Exiba todos os moveis da linha KANOA.')
print(srPrecos.loc[srPrecos.index.str.contains('KANOA')])
#ou pode agrupar por funcao no indice e pegar grupo KANOA


print('\n4.E- Em media, qual a linha de moveis mais barata? Qual o valor medio de um produto dessa linha?')
def qualLinha(mv):
    l=mv.split()
    return l[1]

agLin= srPrecos.groupby(qualLinha)
sPrMed= agLin.mean()
print(sPrMed)
print(sPrMed.agg(['min','idxmin']))

print('\n4.F-Qual o preco medio de uma mesa?')
print(srPrecos.loc[srPrecos.index.str.contains('MESA')].mean())


print('\n4.G-Quais os 5 moveis mais baratos?')
print(srPrecos.sort_values().head(5))

'''
Categorize os moveis em 5 faixas de preco: até 1500 (inclusive), de 1500 até 4000(inclusive), 
de 4000 até 6000(inclusive),de 6000 até 8000 (inclusive), acima de 8000. 
(Crie e exiba a srFxPreco)
'''

srFxPreco= pd.cut(srPrecos, bins=[0,1500,4000,6000,8000,srPrecos.max() ])
print('\n4.H- series srFxPreco:' )
print(srFxPreco)

print('\n4.I- series srFxPreco ordenada por categoria:' )
print(srFxPreco.sort_values())


print('\n4.J- Tabela de frequencia das faixas de preco (categorias):' )
srTabFreqCatPr= srFxPreco.value_counts()
print(srTabFreqCatPr)

print('\n4.K- Tabela de frequencia das faixas de preco ORDENADA por categoria:' )
print(srTabFreqCatPr.sort_index())

print('\n4.L- Tabela de frequência percentual (relativa) das faixas de preco')
srTabFreqCatPrPERC= srFxPreco.value_counts(normalize=True)*100
print(srTabFreqCatPrPERC)

print('\n4.M- Visualizacao grafica (PIZZA) da tabela de freq perc das faixas de preco')
srTabFreqCatPr.plot.pie(title='Categorias de Precos', autopct='%.1f')
plt.show()


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n------5-Responda sobre a srVendidos ----------------')

print('\n5.A-Quantos móveis foram vendidos no total? ')
print(srVendidos.sum())

print('\n5.B-Qual(is) o móvel menos vendido (nomes)? Quantas unidades?')
minVend= srVendidos.min()
print(srVendidos.loc[srVendidos==minVend].index)   #idxmin só daria 1
print('Menor quantidade vendida:', minVend)

print('\n5.C-Exiba os moveis que tiveram quantidade vendida entre 25 e 90.')
print( srVendidos.loc[(srVendidos>25) & (srVendidos<90)])

print('\n5.D- Por LINHA de moveis:Quantidade total vendida, 1 produto mais vendido, 1 produto menos vendido' )
print(srVendidos.groupby(qualLinha).agg(['sum','idxmax','idxmin']))


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n--6- Agrupando srVendidos por Faixas de Preco ---')
'''
Agrupe a srVendidos pelas Faixas de Preço obtidas anteriormente
Por Faixa de Preço exiba: total de moveis vendidos, um movel menos vendido na faixa, 
valor desse movel.
'''
agFxPr= srVendidos.groupby(srFxPreco)
print(agFxPr.agg(['sum','idxmin','min']))


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n--7- GANHOS COM AS VENDAS ---')
print('\n7A- Valor total com as vendas por MOVEL (nao tipo)')
sTotPorMovel = srVendidos*srPrecos
print(sTotPorMovel)

print('\n7B- Valor total com as vendas de todos os MOVEIS')
print(sTotPorMovel.sum())

print('\n7C- Valor total com as vendas POR LINHA')
print(sTotPorMovel.groupby(qualLinha).sum())


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n8- Preenchendo valores ausentes da srEstoque')
def qualTipo(s):
    return s.split()[0]

ag= srEstoque.groupby(qualTipo)
srEstoque.fillna(ag.transform('mean'),inplace=True)
print(srEstoque)
