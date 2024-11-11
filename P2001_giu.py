# -*- coding: latin-1 -*-
############################################################################################
#Nome completo:
#Matrícula PUC-Rio:
#Declaração de autoria: declaro que este documento foi produzido por mim em sua totalidade,
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
registrou  informações pessoais e  relacionadas à carga de trabalho,
aos rendimentos e despesas durante uma semana de trabalho  no
arquivo motoristasaplicativo.xlsx.
 
Há 4 planilhas com dados dos motoristas. Em todas as planilhas os motoristas
sao identificados pelo nome e não há repetição de nomes.
  
A planilha perfil tem as seguintes informações cadastrais sobre os motoristas:
    NOME: identificação do motorista
    ESTCIVIL: estado civil - valores: CASADO, DIVORCIADO, SOLTEIRO, OUTROS
    GENERO: valores: F, M ou X
    IDADE: em anos
    ESCOLARIDADE: valores: FUNDAMENTAL, MEDIO ou SUPERIOR.
    AREADEATUACAO: área de atuação do profissional antes de ser motorista parceiro
 
A planilha horastrabalhadas armazena, por dia da semana, a quantidade de horas
trabalhadas em cada dia da semana considerada por cada mototista.
 
A planilha valoresnasemana armazena dados do rendimento e despesas dos motoristas
na semana considerada. Há as seguintes colunas, com valores expressos em reais:
    ValorBruto:	valor bruto arrecadado na semana
    DespAlim: valor gasto (despesa) na semana com alimentação
    DespComb: valor gasto (despesa) com combustível para trabalhar na semana
    DespManut: valor gasto (despesa) com a manutenção do veículo na semana
 
A planilha temponaempresa armazena a quantidade de meses que o motorista presta
serviço para a empresa.
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
print('Questão 1 - ( pontos)')
# 
# Conhecendo os DataFrames:
# 
# Exiba:
# (0.3) a- dfPerfil: os 3 primeiros e os 5 últimos elementos
#             ordenados crescentemente por GENERO/ESTCIVIL
# (0.1) b- dfHTrab: os 4 últimos elementos
# (0.1) c- dfVal: os 4 últimos elementos
# (0.1) d- srTempo: os 4 últimos elementos
# (0.3) e- srTempo: todos os motoristas com maior tempo na empresa
#           e esse maior tempo 
# (0.3) f- dfVal: valores gastos pelos motoristas BUBA, XUXU e DUDU
#           em cada uma das seguintes despesas: alimentação e combustível
# (0.3) g- dfHTrab: um dia da semana com maior soma total de horas trabalhadas
#          (considerando as horas trabalhadas por todos os motoristas)
# 
print(' a- dfPerfil Ordenado por GENERO/ESTCIVIL')

d1a=dfPerfil.sort_values(by =['GENERO','ESTCIVIL'],ascending=True )
print(pd.concat([d1a.head(5),d1a.tail(5)]))

print(' b- 4 últimos de dfHTrab')

print(dfHTrab.tail(4))

print(' c- 4 últimos de dfVal')

print(dfVal.tail(4))

print(' d- 4 últimos de srTempo')

print(srTempo.tail(4))

print(' e- Todos os motoristas com maior tempo na empresa e maior tempo ')

f1e = srTempo.agg(['idxmax','max'])
print(f1e)

print(' f- Gastos do BUBA, XUXU e DUDU em alimentação e combustível')

nomes = ['BUBA', 'XUXU' ,'DUDU']
colunas = ['DespAlimentacao','DespCombustivel']

print(dfVal.loc[nomes,colunas])

print(' g- Um dia da semana com maior valor total de horas trabalhadas')

hdia = dfHTrab.sum(axis=0)
print(hdia.idxmax())

print('-----------------------------------')

print('-----------------------------------')
print('Questão 2 - ( pontos)')
# 
#  Visualização Gráfica dfVal:
# 
# Mostrar em um gráfico de barras, as despesas individuais com
# alimentacao e combustivel. As duas colunas no mesmo gráfico
# 
print('Visualizacao Grafica (barras, colunas juntas) das despesas com'\
      ' alimentacao e combustivel')

dfVal.plot(kind='bar', x= 'DespAlimentacao', y ='DespCombustivel')
plt.show()

print('-----------------------------------')

print('-----------------------------------')
print('Questão 3 - ( pontos)')
# 
# Considerando as seguintes categorias de horas trabalhadas na SEG (dfHTrab):
#     0 a 4 (inclusive) - POUCAS
#     a partir de 4 até 7 (inclusive) - RAZOAVEL
#     a partir de 7 até 9 (inclusive) - NORMAL
#     acima de 9 - MUITAS
# 
#  Construa um gráfico do tipo pizza da tabela de frequencia percentual 
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
print('Questão 4 - ( pontos)')
print('Apresente os nomes dos motoristas que gastaram menos do que R$ 200.00'\
      'com alimentacao e mais do que R$ 700.00 com manutenção')

print('-----------------------------------')

f4a = (dfVal['DespAlimentacao']<200) & (dfVal['DespManutencao']>700)

print(list(dfVal[f4a].index))

print('-----------------------------------')
print('Questão 5 - (pontos)')
# 
# Inclua em dfVal duas novas colunas: 
#      DespTot: com o total das despesas de cada motorista;
#      ValLiq: com o valor líquido,isto é, ValorBruto - DespTot
#              de cada motorista.
# Apresente os dados dos motoristas com valor líquido superior
# ao valor líquido mediano e despesa total inferior à despesa total média  
# 
print('Dados dos motoristas com valor líquido superior ao valor líquido mediano'\
      ' e despesa total inferior à despesa total média')

print('-----------------------------------')

dfVal['DespTot']= dfVal[['DespAlimentacao','DespCombustivel','DespManutencao']].sum(axis=1)

dfVal['ValLiq']= dfVal['ValorBruto']-dfVal['DespTot']

filtro5 = (dfVal['ValLiq'] > dfVal['ValLiq'].mean()) & (dfVal['DespTot'] <dfVal['DespTot'].mean())

print(dfPerfil[filtro5])

print('-----------------------------------')
print('Questão 6 - ( pontos)')
# 
# Considerando o dfPerfil, apresente a quantidade de motoristas por 
# AREADEATUACAO X ESCOLARIDADE, ou seja, a tabela de frequência no
# cruzamento destas colunas.
# 
print('Tabela de Frequência AREADEATUACAO X ESCOLARIDADE ')

print('-----------------------------------')

print(pd.crosstab(dfPerfil['AREADEATUACAO'],dfPerfil['ESCOLARIDADE']))

print('-----------------------------------')
print('Questão 7 - ( pontos)')
# 
# Realize as operações e concatenações adequadas que julgar necessárias
# para mostrar a relação gráfica (scatter) entre a quantidade total 
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
print('Questão 8 - (pontos)')
# 
# Mostre para os funcionários que estão há mais de 14 meses trabalhando
# para empresa as quantidades mínima, máxima, média e mediana de horas 
# trabalhadas no domingo por AREADEATUACAO/GENERO
# 
print(' Resumos por AREADEATUACAO/GENERO dos funcionários com mais de 14 meses')

print('-----------------------------------')


