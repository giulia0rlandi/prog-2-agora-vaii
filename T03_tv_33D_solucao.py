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

# ENUNCIADO:
# Q1) 
# Series srPrecos a partir da planilha preco do arquivo TV.xlsx. A planilha tem uma linha de 
# cabeçalho e a primeira coluna deve ser usada como índice. 

# Series srVendidas a partir da planilha vendidas do arquivo TV.xlsx. A planilha tem uma 
# linha de cabeçalho e a primeira coluna deve ser usada como índice. 

# Series srEstoque a partir da planilha estoque do  arquivo TV.xlsx. A planilha tem uma 
# linha de cabeçalho e a primeira coluna deve ser usada como índice.

# Nas series criadas cada indice e´ um nome de modelo de TV, que tem 
# sempre incluido o fabricante (AA), o tamanho da tela (BB)e o tipo da TV(CC), 
# no seguinte formato:    AABBCCxxxx
# Por exemplo se o modelo e´ JG49HD5000 
# - o fabricante e´JG
# - o tamanho da tela e´ 49 polegadas.  No arquivo so´ ha´ TVs de 40,43,49 e 55. 
# - o tipo da tv e´  HD.  No arquivo há os seguintes tipos de  TV (FU (Full HD), 
# HD, UH (UltraHD)) . 


# Q2) => VALE 1.0 (0.2 por item)
# 2A)Crie a partir da srEstoque a series srNulos, apenas com as linhas com NAN. 
# Exiba a srNulos
# 2B)Exiba o percentual de valores invalidos na srEstoque 
# 2C)Apresente a visualização grafica do percentual de valores validos na srEstoque
# 2D)Exiba da srPrecos somente os elementos cujos indices estejam na srNulos 
# 2E)Exiba da srVendidos somente os elementos cujos indices NÃO estejam na srNulos 
# OBS: Não ALTERE nenhuma das 3 series 



#Q3) => VALE 0.6 (0.2 por item)

# Q3A) Para a srVendidas exiba juntos: os 4 primeiros com os 3 últimos
# Q3B) Exiba a srPrecos ordenada descrescentemente pelo preco
# Q3C) Exiba a srVendidas ordenada pelo modelo

# Q4) Considerando a series srPrecos responda:  => VALE 5.2 (0.4 por item)
# - A)Qual o preco da TV mais cara? Uma TV com esse preco?
# - B)Qual o menor preco de uma TV? Exiba todos os nomes dos modelos de TV 
#   com esse preco
# - C)Exiba todas as TVS com preço abaixo de 3500. 
# - D)Exiba os precos de todas as TVs do tipo FU.
# - E)Em média, qual o tipo de TV mais caro? Qual o valor médio de uma TV desse tipo? 
# - F)Quais os precos max, min e medio das TVs de 49 polegadas?
# - G)Quais as 5 TVs mais caras? 
# - H)Categorize as TVs em 4 faixas de preco: até 1500 (inclusive)- BARATA, de 1500 até 
# 2500(inclusive) - REGULAR, de 2500 até 3500(inclusive)-CARA, acima de 3500 -MuitoCara. 
# (Crie e exiba a srFxPreco) 

# - I)Exiba a srFxPreco ordenada por categoria. 
# - J)Apresente a tabela de frequências das faixas de preco. 
# - K)Apresente a tabela de frequências ordenada por categoria. 
# - L)Apresente a tabela de frequência percentual (relativa) das faixas de preco 
# - M)Apresente uma visualização gráfica (pizza) da tabela de frequência percentual. 

# Q5) Considerando a series srVendidas responda: => VALE 1.2 (0.3 por item)
# - A)Quantas TVs foram vendidas no total? 
# - B)Qual(is) as TVs menos vendidas? Quantas unidades? 
# - C)Exiba as TVs que tiveram quantidade vendida entre 180 e 500. 
# - D)Por TIPO de TV, apresente: Quantidade total vendida, modelo mais vendido, modelo 
# menos vendido 

# Q6) Agrupe a srVendidas pelas Faixas de Preço obtidas anteriormente. 
# Por Faixa de Preço exiba: total de TVs vendidas, um modelo mais vendido na faixa, 
# valor desse modelo. => VALE 0.6

# Q7) GANHOS COM AS VENDAS : =>VALE 0.9 (0.3 por item)
# 7A) Valor total com as vendas por MODELO
# 7B) Valor total com as vendas de todos os MODELOs
# 7C) Valor total com as vendas POR FABRICANTE

# Q8) (vale 0.5) Preencha os valores ausentes da srEstoque com a mediana de estoque 
# por FABRICANTE da TV. Exiba a srEstoque.
 
    
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_rows", 999) 
pd.set_option("display.max_columns", 999) 
pd.set_option("display.precision", 2) 
pd.set_option("float_format", '{:.2f}'.format)

srPrecos = pd.read_excel('TV232.xlsx',sheet_name='preco', header=0, 
                         index_col=0).squeeze()

srPrecos= pd.Series(srPrecos) # para dicas do ambiente

srVendidas= pd.read_excel('TV232.xlsx',sheet_name='vendidas', header=0, 
                          index_col=0).squeeze()
srVendidas= pd.Series(srVendidas)

srEstoque= pd.read_excel('TV232.xlsx',sheet_name='estoque', header=0, 
                          index_col=0).squeeze()
srEstoque= pd.Series(srEstoque)

print('\n---------- 1 - series criadas -----------------')
print('\nsrPrecos:')
print(srPrecos)
print('\nsrVendidas')
print(srVendidas)
print('\nsrEstoque')
print(srEstoque)



print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n--- 2 - Lidando com NaN-------')

print('\n2.A- Nulos')
srNulos= srEstoque.loc[srEstoque.isnull()]
print(srNulos)

print('\n2.B- Exiba o percentual de valores invalidos na srEstoque')
print(srEstoque.isnull().sum()/srEstoque.size *100 ) # pode não multiplicar por 100

print('\n2.C- Visualização grafica do percentual de valores validos na srEstoque')
ss= srEstoque.notnull()
ss.replace({True:'NaoNulo', False:'Nulo'},inplace=True)
ss.value_counts().plot.pie(title='Perc de ausentes na srEstoque',
                           autopct=':.1f')
plt.show()

print('\n2.D- srPrecos: somente os elementos cujos indices estejam na srNulos  :')
print(srPrecos.loc[srNulos.index])

print('\n2.E - srVendidas: somente os elementos cujos indices estejam na srNulos :')
print(srVendidas.drop(srNulos.index))


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n------ 3.A - srVendidas: juntos: 4 primeiros com 4 ultimos ------')
print(srVendidas.head(4).append(srVendidas.tail(4)))

print('\n------ 3.B - srPrecos ordenada decrescentemente pelo preco ------')
print(srPrecos.sort_values(ascending=False))

print('\n------ 3.C - srVendidas ordenada pelo modelo ------')
print(srVendidas.sort_index())


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n------4-Responda sobre a srPrecos ------')

print('\n4.A- Qual o preco da TV mais cara? Uma TV com esse preco?')
print(srPrecos.max(), '-',srPrecos.idxmax())

print('\n4.B- Qual o menor preco? Exiba todos os nomes dos modelos de TV com esse preco')
print(srPrecos.min())
print(srPrecos.loc[srPrecos==srPrecos.min()].index)

print('\n4.C- Exiba todas as TVs com preço abaixo de 3500.')
scAb3500 = srPrecos.loc[srPrecos<3500]
print(scAb3500)

print('\n4.D- Exiba os precos de todas as TVs do tipo FU.')
#Sol1:
srFU= srPrecos.loc[srPrecos.index.str.contains('FU')]
print(srFU)

#Sol2
def qualTipo(indice):
    return indice[4:6]
agTipo = srPrecos.groupby(qualTipo)
srFU = agTipo.get_group('FU')
print(srFU)

print('\n4.E- Em media, qual o tipo  mais caro? Qual o valor medio de uma TV desse tipo?')

#Tem q ter feito ou fazer agora o agrupamento por qualTipo
srMedTipo= agTipo.mean()
print(srMedTipo.idxmax(),'-',srMedTipo.max())


print('\n4.F-Quais os precos max, min e medio das TVs de 49 polegadas?')

#Sol1:
sr49 = srPrecos.loc[srPrecos.index.str.contains('49')]
print(sr49.agg(['max','min','mean']))

#Sol2
def tela(indice):
    return indice[2:4]
agTela = srPrecos.groupby(tela)
sr49= agTela.get_group('49')
print(sr49.agg(['max','min','mean']))

print('\n4.G-Quais as 5 TVs mais caras?')
print(srPrecos.sort_values(ascending=False).head(5))

'''
Categorize as TVs em 4 faixas de preco: ate 1500 (inclusive), de 1500 ate 2500(inclusive), 
de 2500 ate 3500(inclusive), acima de 3500. 
(Crie e exiba a srFxPreco)
'''
print('\n4.H- series srFxPreco:' )
srFxPreco= pd.cut(srPrecos, bins=[0,1500,2500,3500,srPrecos.max()],
                  labels=['BARATA','REGULAR','CARA','MuitoCara'])
print(srFxPreco)

print('\n4.I- series srFxPreco ordenada por categoria:' )
print(srFxPreco.sort_values())

print('\n4.J- Tabela de frequencia das faixas de preco (categorias):' )
srTabFreqFxPreco = srFxPreco.value_counts()
print(srTabFreqFxPreco)

print('\n4.K- Tabela de frequencia das faixas de preco ORDENADA por categoria:' )
srTabFreqFxPreco = srFxPreco.value_counts()
print(srTabFreqFxPreco.sort_index())

print('\n4.L- Tabela de frequência percentual (relativa) das faixas de preco')
srPerc = srTabFreqFxPreco*100/srTabFreqFxPreco.sum()
print(srPerc)

print('\n4.M- Visualizacao grafica (PIZZA) da tabela de freq perc das faixas de preco')
srTabFreqFxPreco.plot.pie(title='Tab de Freq das faixas de preco', figsize=(6,6 ),
                          autopct="%.1f", colors=['r','b','y','m','g'])
plt.show()



print('\n-------------------------------------------------')
print('-------------------------------------------------')

print('\n------5-Responda sobre a srVendidas ----------------')

print('\n5.A-	Quantas TVs foram vendidas no total? ')
print(srVendidas.sum())

print('\n5.B-Qual(is) as TVs menos vendidas (modelos)? Quantas unidades?')
minVend= srVendidas.min()
srMenosVend= srVendidas.loc[srVendidas==minVend]
print(srMenosVend.index.values)

print('\n5.C-Exiba as Tvs que tiveram quantidade vendida entre 180 e 500.')
srEntre180e500= srVendidas.loc[(srVendidas>180) & (srVendidas<500)]
print(srEntre180e500)


print('\n5.D- Por TIPO de TV :Quantidade total vendida, modelo mais vendido, modelo menos vendido' )
agVendPorTipo= srVendidas.groupby(qualTipo)
print(agVendPorTipo.agg(['sum','idxmax','idxmin']))


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n--6- Agrupando srVendidas por Faixas de Preco ---')
'''
Agrupe a srVendidas pelas Faixas de Preço obtidas anteriormente
Por Faixa de Preço exiba: total de TVs vendidas, modelo mais vendido na faixa, valor desse modelo.
'''
agVendPorFxPr= srVendidas.groupby(srFxPreco)
print(agVendPorFxPr.agg(['sum','idxmax','max']))


print('\n-------------------------------------------------')
print('-------------------------------------------------')

print('\n--7- GANHOS COM AS VENDAS ---')
print('\n7A- Valor total com as vendas por MODELO')
srTotalMod=  srPrecos*srVendidas
print(srTotalMod)
print('\n7B- Valor total com as vendas de todos os MODELOs')
print(srTotalMod.sum())
print('\n7C- Valor total com as vendas POR FABRICANTE')
def fab(s):
    return s[:2]
print(srTotalMod.groupby(fab).sum())


print('\n-------------------------------------------------')
print('-------------------------------------------------')
print('\n8- Preenchendo valores ausentes da srEstoque')
def qualTipo(s):
    return s.split()[0]

ag= srEstoque.groupby(fab)
srEstoque.fillna(ag.transform('median'),inplace=True)
print(srEstoque)


