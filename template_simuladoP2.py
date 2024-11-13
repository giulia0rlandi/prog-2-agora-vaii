# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:50:48 2024

@author: Ferlin
"""
'''
Deseja-se analisar dados socioeconômicos 
e educacionais de cidades brasileiras, 
visando entender as relações entre 
crescimento populacional, 
desenvolvimento humano, 
educação e condições sociais. 

Pergunta 1:
Como a taxa de crescimento populacional se relaciona 
com o desenvolvimento 
humano e a renda média?

Motivação: Entender se as cidades com maior 
taxa de crescimento populacional
também apresentam IDH (Índice de Desenvolvimento Humano) elevado e maior 
renda média, ou se o crescimento é mais acelerado em 
cidades com indicadores socioeconômicos mais baixos.

Pergunta 2:
    
Há uma relação entre desigualdade de renda 
(índice de Gini) e desempenho escolar nas
 cidades brasileiras?

Motivação: Investigar se a desigualdade afeta 
a qualidade da educação, 
medindo a relação entre o índice de Gini e as 
taxas de aprovação ou as notas 
médias em disciplinas como Matemática e Português.
Análise: Podemos calcular a correlação entre o 
DESIGUALDADE e a TAXA_APROVACAO, 
e analisar as médias de desempenho escolar 
em cidades com diferentes níveis 
de desigualdade para identificar possíveis padrões.
Objetivos do Estudo
Essas questões podem ajudar a entender como 
fatores como crescimento populacional, 
desenvolvimento humano e desigualdade de renda 
influenciam diretamente nas 
condições de vida e nas oportunidades educacionais 
das cidades.
'''
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('float_format', '{:.2f}'.format)
pd.set_option('display.precision', 2)

print('=================================')
print('Análise Socioeconômica e de Crescimento Populacional')
print('=================================')

'''
O arquivo 'dados_socioeducacionais_atualizado.xlsx' contém informações sobre dados 
socioeconômicos e educacionais de diversas cidades no ano de 2023.
 O arquivo possui as seguintes planilhas:

1) CIDADES:
   - CIDADE: nome da cidade (index)
   - TAXA_CRESCIMENTO: taxa anual de crescimento populacional da cidade (%)
   - REGIAO: região do país onde a cidade está localizada
   - IDH: Índice de Desenvolvimento Humano da cidade
   - RENDA_MEDIA: renda média per capita (em reais)
   - EDUCACAO: taxa de alfabetização

2) DESEMPENHO_ESCOLAR:
   - CIDADE: nome da cidade (index)
   - NOTA_MATEMATICA: média de notas em matemática no ensino fundamental
   - NOTA_PORTUGUES: média de notas em português no ensino fundamental
   - TAXA_APROVACAO: percentual de aprovação no ensino fundamental

3) INDICADORES_SOCIAIS:
   - CIDADE: nome da cidade (index)
   - POBREZA: percentual de pessoas abaixo da linha da pobreza
   - DESIGUALDADE: índice de Gini para medir a desigualdade de renda
 O índice de Gini é um indicador que mede a desigualdade de renda e a 
 concentração de riqueza em um determinado território: 
 

Os seguintes DataFrames estão disponíveis:
- dfCidades: dados socioeconômicos das cidades
- dfDesempenhoEscolar: dados de desempenho escolar
- dfIndicadoresSociais: dados de indicadores sociais
'''

# Carregar os DataFrames a partir do arquivo
dfCidades = pd.read_excel('dados_socioeducacionais_atualizado.xlsx', sheet_name='CIDADES', index_col=0, header=0)
dfDesempenhoEscolar = pd.read_excel('dados_socioeducacionais_atualizado.xlsx', sheet_name='DESEMPENHO_ESCOLAR', index_col=0, header=0)
dfIndicadoresSociais = pd.read_excel('dados_socioeducacionais_atualizado.xlsx', sheet_name='INDICADORES_SOCIAIS', index_col=0, header=0)

print('==============================================')
print("\ndfCidades - Dados das Cidades")
print(dfCidades.head())
print("\ndfDesempenhoEscolar - Desempenho Escolar")
print(dfDesempenhoEscolar.head())
print("\ndfIndicadoresSociais - Indicadores Sociais")
print(dfIndicadoresSociais.head())
print('==============================================')

print('==============================================')
print('Questão 1 - (3.0 pontos)')
#======================================================================
# 1- Explorando dados de cada DataFrame separadamente:
# (0.3) a- dfCidades: Exiba os dados das 5 cidades com maiores taxas de crescimento,
#                    com maiores IDH
# (0.3) b- dfCidades: Exiba a média da taxa de crescimento populacional por região.
# (0.3) c- dfCidades: Visualize a média da taxa de crescimento populacional por região, 
#                     em um gráfico de barras
# (0.3) d- dfDesempenhoEscolar: Exiba a média geral das notas de matemática e português.
# (0.3) e- dfDesempenhoEscolar: Exiba para cada cidade, qual a disciplina de 
#                      pior desempenho (matemática ou português)
# (0.3) f- dfDesempenhoEscolar: Exiba a tabela de frequência das disciplinas 
#                     com piores desempenho em cada cidade, como um gráfico de pizza
# (0.3) g- dfDesempenhoEscolar: Exiba a taxa de aprovação mediana das cidades 
#                     com NOTA_MATEMATICA > 6
# (0.3) h- dfIndicadoresSociais: Exiba uma cidade com o menor taxa de pobreza.
# (0.3) i- dfIndicadoresSociais: Exiba os dados das cidades com o menores 
#                      índices de desigualdade.
# (0.3) j- dfIndicadoresSociais: Percentual de cidades com POBREZA abaixo da
#                      média e  DESIGUALDADE abaixo da média
#======================================================================

print('\n------------------------------------------------------')
print('1.a- Cidades com com maiores taxa crescimento e maiores IDH')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('1.b- Média da taxa de crescimento por região')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('1.c- Distribuição da taxa de crescimento')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('1.d- Média geral das notas em Matemática e Português')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('1.e- Pior desempenho, por cidade ( Matemática ou Português')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('''1.f- Gráfico de pizza das disciplinas com piores desempenhos, 
      por cidade ( Matemática ou Português''')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('1.g- taxa de aprovação mediana das cidades com NOTA_MATEMATICA > 6.')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('1.h- Uma cidade com o menor índice de pobreza')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('1.i- dados das cidades com os menores índices de desigualdade.')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('1.j-Percentual de cidades com POBREZA e DESIGUALDADE abaixo da média:')
print('------------------------------------------------------')


print('==============================================')
print('Questão 2 - Incluindo colunas e categorizações (1.8 pontos)')
#======================================================================
# 2- Categorizando e criando colunas para análise:
# (0.6) a- Inclua a coluna "CatIDH" no dfCidades categorizando o IDH em 
#          4 categorias de acordo com:
#          0 até 0.5: Baixo
#          0.51 até 0.7: Médio
#          0.71 até 0.85: Alto
#          ).851 até 1: Muito Alto
#          Mostre a tabela de frequência percentual das categorias
# (0.6) b- Crie uma coluna "Desempenho_Médio" no dfDesempenhoEscolar com a 
#          média de NOTA_MATEMATICA e NOTA_PORTUGUES.
#          Mostre o gráfico de dispersão (scatter )  da relação do 
#          Desempenho_Médio com a taxa de aprovação
# (0.6) c- Inclua a coluna "Nível_Pobreza" no dfIndicadoresSociais categorizando
#          o percentual de pobreza 3 faixas de mesma amplitude em Baixa, Média, Alta.
#          Mostre, juntas, as 3 primeiras linhas e as 3 últimas linhas do 
#          dfIndicadoresSociais após ordenar pelo nome da cidade
#======================================================================

print('\n------------------------------------------------------')
print('2.a- Categorização do IDH')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('2.b- Desempenho Médio das Notas')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('2.c- Nível de Pobreza ordenado por nome da cidade')
print('------------------------------------------------------')


print('==============================================')
print('Questão 3 - (1.2 pontos)')
#======================================================================
# 3- Relacionando e Explorando dados dos DataFrames
# (0.4) a - Média de notas em cidades com IDH muito alto.
# (0.4) b - Média da taxa de crescimento populacional em cidades com 
#           renda média acima de R$ 3000,00.
# (0.4) c - Correlação entre desigualdade e taxa de aprovação escolar.
#======================================================================

print('\n------------------------------------------------------')
print('3.a- Média de notas em cidades com IDH muito alto')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('3.b- Média da taxa de crescimento em cidades com renda média > 3000')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('3.c- Correlação entre Desigualdade e Taxa de Aprovação')
print('------------------------------------------------------')

print('==============================================')
print('Questão 4 - (2.3 pontos)')

print('==============================================')
print('Questão 4 - Análises Combinadas e Resultados (2.3 pontos)')
#======================================================================
# 4- Análises combinadas e resultados detalhados dos dados
#======================================================================

# 4.a - Concatenar dfCidades, dfDesempenhoEscolar e dfIndicadoresSociais em dfCompleto
#       apresente os 5 últimas linas do DF
# 4.b - Exibir cidade na região Norte com menor taxa de crescimento populacional
# 4.c - Exibir quantidade de cidades por categoria de IDH e nível de pobreza
# 4.d - Média do desempenho escolar nas cidades com desigualdade de renda > 0.5
# 4.e - Correlação entre renda média e taxa de crescimento nas cidades com IDH
#       muito alto
#======================================================================

print('\n------------------------------------------------------')
print('4.a - Crie o DataFrame dfCompleto concatenando dfCidades, dfDesempenhoEscolar e dfIndicadoresSociais')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('4.b - Exiba a cidade localizada na região Norte com a menor taxa de crescimento populacional')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('4.c - Mostre a quantidade de cidades por categoria de IDH e nível de pobreza')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('4.d - Mostre a média do desempenho escolar (matemática e português) nas cidades com alta desigualdade de renda(>0.5)')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('4.e - Calcule a correlação entre renda média e taxa de crescimento populacional nas cidades com IDH muito alto')
print('------------------------------------------------------')

print('==============================================')
print('Questão 5 - (2.0 pontos)')
#======================================================================
# 5- Análises adicionais e perguntas para aprofundamento
#======================================================================
# 5.a - Exibir cidades com taxa de pobreza > 25% e nota em português < 5
# 5.b - Exibir as 3 cidades com maior renda média em cada região
# 5.c - Taxa média de crescimento nas cidades com desigualdade > 0.2 e IDH < 0.7
#       por REGIAO x Nível_Pobreza
# 5.d - Exibir cidade com menor taxa de aprovação escolar e renda média > R$ 2500
# 5.e - Correlação entre índice de Gini (DESIGUALDADE) e taxa de crescimento 
#       nas cidades com IDH médio
# 5.f - Exibir regiões com média de IDH > 0.8
# 5.g - Total de cidades com renda média > R$ 3000 e taxa de aprovação 
#       escolar < 80%
#======================================================================
print('\n------------------------------------------------------')
print('5.a - Cidades com taxa de pobreza acima de 25% e desempenho médio em português menor que 5')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('5.b - Exiba as 3 cidades com maior renda média por região')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('5.c - POR REGIAO x Nível_Pobreza: Taxa média de crescimento nas cidades com desigualdade acima de 0.2 e IDH abaixo de 0.7')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('5.d - Exiba a cidade com a menor taxa de aprovação escolar e renda média acima de R$ 2500')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('5.e - Correlação entre índice de Gini e taxa de crescimento populacional nas cidades com IDH médio')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('5.f - Exiba as regiões com média de IDH acima de 0.8')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('5.g - Total de cidades com renda média acima de R$ 3000 e taxa de aprovação escolar menor que 80%')
print('------------------------------------------------------')
