# -*- coding: latin-1 -*-
############################################################################################
#Nome completo:
#Matr�cula PUC-Rio:
#Declara��o de autoria: declaro que este documento foi produzido por mim em sua totalidade,
#                 sem consultas a outros alunos, professores ou qualquer outra pessoa.
##############################################################################1#############
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('==========+++++++++================')
print('Trabalhando com SERIES E DATAFRAME')
print('=============++++++++==============')
'''
Um estudo sobre os motoristas parceiros da empresa de transporte CRAJOPA
registrou  informa��es pessoais e  relacionadas � carga de trabalho,
aos rendimentos e despesas durante uma semana de trabalho  no
arquivo motoristasaplicativo.xlsx.
 
H� 4 planilhas com dados dos motoristas. Em todas as planilhas os motoristas
sao identificados pelo nome e n�o h� repeti��o de nomes.
  
A planilha perfil tem as seguintes informa��es cadastrais sobre os motoristas:
    NOME: identifica��o do motorista
    ESTCIVIL: estado civil - valores: CASADO, DIVORCIADO, SOLTEIRO, OUTROS
    GENERO: valores: F, M ou X
    IDADE: em anos
    ESCOLARIDADE: valores: FUNDAMENTAL, MEDIO ou SUPERIOR.
    AREADEATUACAO: �rea de atua��o do profissional antes de ser motorista parceiro
 
A planilha horastrabalhadas armazena, por dia da semana, a quantidade de horas
trabalhadas em cada dia da semana considerada por cada mototista.
 
A planilha valoresnasemana armazena dados do rendimento e despesas dos motoristas
na semana considerada. H� as seguintes colunas, com valores expressos em reais:
    ValorBruto:	valor bruto arrecadado na semana
    DespAlim: valor gasto (despesa) na semana com alimenta��o
    DespComb: valor gasto (despesa) com combust�vel para trabalhar na semana
    DespManut: valor gasto (despesa) com a manuten��o do ve�culo na semana
 
A planilha temponaempresa armazena a quantidade de meses que o motorista presta
servi�o para a empresa.
'''
dfPerfil=pd.read_excel('motoristasaplicativo.xlsx',sheet_name='dadoscadastrais',index_col=0,header=0)
dfPerfil = pd.DataFrame(dfPerfil)
dfHTrab=pd.read_excel('motoristasaplicativo.xlsx',sheet_name='horastrabalhadas',index_col=0,header=0)
dfHTrab = pd.DataFrame(dfHTrab)
dfVal=pd.read_excel('motoristasaplicativo.xlsx',sheet_name='valoresnasemana',index_col=0,header=0)
dfVal = pd.DataFrame(dfVal)
srTempo =pd.read_excel('motoristasaplicativo.xlsx',sheet_name='temponaempresa',index_col=0,header=0,squeeze=True)
srTempo = pd.Series(srTempo)

print('-----------------------------------')
print('Quest�o 1 - ( pontos)')
# 
# Conhecendo os DataFrames:
# 
# Exiba:
# (0.3) a- dfPerfil: os 3 primeiros e os 5 �ltimos elementos
#             ordenados crescentemente por GENERO/ESTCIVIL
# (0.1) b- dfHTrab: os 4 �ltimos elementos
# (0.1) c- dfVal: os 4 �ltimos elementos
# (0.1) d- srTempo: os 4 �ltimos elementos
# (0.3) e- srTempo: todos os motoristas com maior tempo na empresa
#           e esse maior tempo 
# (0.3) f- dfVal: valores gastos pelos motoristas BUBA, XUXU e DUDU
#           em cada uma das seguintes despesas: alimenta��o e combust�vel
# (0.3) g- dfHTrab: um dia da semana com maior soma total de horas trabalhadas
#          (considerando as horas trabalhadas por todos os motoristas)
# 
print(' a- dfPerfil Ordenado por GENERO/ESTCIVIL')

d1a=dfPerfil.sort_values(by =['GENERO','ESTCIVIL'],ascending=True )
print(pd.concat([d1a.head(5),d1a.tail(5)]))

print(' b- 4 �ltimos de dfHTrab')

print(dfHTrab.tail(4))

print(' c- 4 �ltimos de dfVal')

print(dfVal.tail(4))

print(' d- 4 �ltimos de srTempo')

print(srTempo.tail(4))

print(' e- Todos os motoristas com maior tempo na empresa e maior tempo ')

f1e = srTempo.agg(['idxmax','max'])
print(f1e)

print(' f- Gastos do BUBA, XUXU e DUDU em alimenta��o e combust�vel')

nomes = ['BUBA', 'XUXU' ,'DUDU']
colunas = ['DespAlimentacao','DespCombustivel']

print(dfVal.loc[nomes,colunas])

print(' g- Um dia da semana com maior valor total de horas trabalhadas')

hdia = dfHTrab.sum(axis=0)
print(hdia.idxmax())

print('-----------------------------------')

print('-----------------------------------')
print('Quest�o 2 - ( pontos)')
# 
#  Visualiza��o Gr�fica dfVal:
# 
# Mostrar em um gr�fico de barras, as despesas individuais com
# alimentacao e combustivel. As duas colunas no mesmo gr�fico
# 
print('Visualizacao Grafica (barras, colunas juntas) das despesas com'\
      ' alimentacao e combustivel')

dfVal.plot(kind='bar', x= 'DespAlimentacao', y ='DespCombustivel')
plt.show()

print('-----------------------------------')

print('-----------------------------------')
print('Quest�o 3 - ( pontos)')
# 
# Considerando as seguintes categorias de horas trabalhadas na SEG (dfHTrab):
#     0 a 4 (inclusive) - POUCAS
#     a partir de 4 at� 7 (inclusive) - RAZOAVEL
#     a partir de 7 at� 9 (inclusive) - NORMAL
#     acima de 9 - MUITAS
# 
#  Construa um gr�fico do tipo pizza da tabela de frequencia percentual 
#  de cada categoria de horas trabalhadas.
# 
print('Tabela de frequencia percentual das categorias de horas trabalhadas na SEG'\
      ' como grafico de pizza')
    
segundou = pd.cut(dfHTrab['SEG'], bins = [0,4,7,9,dfHTrab['SEG'].max()], labels = ['POUCAS','RAZOAVEL','NORMAL','MUITAS'])

tabfreq = segundou.value_counts(normalize=True)*100
print(tabfreq)

tabfreq.plot(kind='pie')
plt.show()

print('-----------------------------------')

print('-----------------------------------')
print('Quest�o 4 - ( pontos)')
print('Apresente os nomes dos motoristas que gastaram menos do que R$ 200.00'\
      'com alimentacao e mais do que R$ 700.00 com manuten��o')

print('-----------------------------------')

f4a = (dfVal['DespAlimentacao']<200) & (dfVal['DespManutencao']>700)

print(list(dfVal[f4a].index))

print('-----------------------------------')
print('Quest�o 5 - (pontos)')
# 
# Inclua em dfVal duas novas colunas: 
#      DespTot: com o total das despesas de cada motorista;
#      ValLiq: com o valor l�quido,isto �, ValorBruto - DespTot
#              de cada motorista.
# Apresente os dados dos motoristas com valor l�quido superior
# ao valor l�quido mediano e despesa total inferior � despesa total m�dia  
# 
print('Dados dos motoristas com valor l�quido superior ao valor l�quido mediano'\
      ' e despesa total inferior � despesa total m�dia')

print('-----------------------------------')

dfVal['DespTot']= dfVal[['DespAlimentacao','DespCombustivel','DespManutencao']].sum(axis=1)

dfVal['ValLiq']= dfVal['ValorBruto']-dfVal['DespTot']

filtro5 = (dfVal['ValLiq'] > dfVal['ValLiq'].mean()) & (dfVal['DespTot'] <dfVal['DespTot'].mean())

print(dfPerfil[filtro5])

print('-----------------------------------')
print('Quest�o 6 - ( pontos)')
# 
# Considerando o dfPerfil, apresente a quantidade de motoristas por 
# AREADEATUACAO X ESCOLARIDADE, ou seja, a tabela de frequ�ncia no
# cruzamento destas colunas.
# 
print('Tabela de Frequ�ncia AREADEATUACAO X ESCOLARIDADE ')

print('-----------------------------------')

print(pd.crosstab(dfPerfil['AREADEATUACAO'],dfPerfil['ESCOLARIDADE']))

print('-----------------------------------')
print('Quest�o 7 - ( pontos)')
# 
# Realize as opera��es e concatena��es adequadas que julgar necess�rias
# para mostrar a rela��o gr�fica (scatter) entre a quantidade total 
# de horas trabalhadas e tempo na empresa. As colunas no novo DataFrame
# devem ser nomeadas de forma apropriada.
# 
print(' Horas trabalhadas X Tempo na Empresa (scatter)')

print('-----------------------------------')

# dfHTrab['HTOTAL'] = dfHTrab[['DOM' , 'SEG' , 'TER' , 'QUA' , 'QUI' , 'SEX' , 'SAB']].sum(axis=1)
# dfTempo = pd.concat([srTempo, dfHTrab], axis=1)

# tab = pd.crosstab(dfTempo['HTOTAL'],dfTempo['TempoEmMesesNaEmpresa'].sum(axis=0))
# tab.plot(kind='scatter')
# plt.show()


print('-----------------------------------')
print('Quest�o 8 - (pontos)')
# 
# Mostre para os funcion�rios que est�o h� mais de 14 meses trabalhando
# para empresa as quantidades m�nima, m�xima, m�dia e mediana de horas 
# trabalhadas no domingo por AREADEATUACAO/GENERO
# 
print(' Resumos por AREADEATUACAO/GENERO dos funcion�rios com mais de 14 meses')

print('-----------------------------------')


