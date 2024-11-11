# -*- coding: utf-8 -*-
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
pd.set_option('display.float_format', '{:.2f}'.format)

print('=================================')
print('Trabalhando com PANDAS')
print('=================================')
'''
    
O arquivo Herois20212Final.xlsx armazena os dados de personagens (heróis, vilões,
etc) de obras de ficção como histórias em quadrinhos, filmes, séries, etc. 
Os personagens têm um alinhamento moral (bem, mal ou neutro) e em sua maioria 
possuem super-poderes.

Todas as planilhas tem o nome do personagem na primeira coluna
- A planilha Informacoes tem os seguintes dados dos personagens:
    o	Publicador: responsável pela publicação do personagem pela primeira vez
                     (nome da Editora/Produtora/Autor);
    o	MidiaLancamento: mídia da primeira aparição do personagem;
    o	AnoLancamento: ano da primeira aparição do personagem;
    o	Olhos: cor dos olhos do personagem; 
    o	Especie: especie do personagem (humano, deus, mutante, etc.);
    o	Cabelo: cor do cabelo do personagem;
    o	Peso: peso do personagem;
    o	Altura: altura do personagem; 
    o	Pele: cor da pele do personagem;
    o	Alinhamento: alinhamento moral (BEM, MAL ou NEUTRO) do personagem;
    o	Votos: quantidade de votos recebidos pelos participantes de uma votação 
              mundial para escolher o personagem mais querido do público 
              (cada unidade corresponde a 1 mil)
              
- A planilha PoderesGerais apresenta habilidades e/ou poderes gerais dos personagens. 
  Cada coluna representa um poder/habilidade e possui um dos seguintes valores:
      1- significa que o personagem é dotado do poder ou tem a habilidade 
      0- significa que o personagem não possui o poder ou habilidade.
   Poderes representados nesta planilha:
      Voa, SuperVelocidade, SuperForca, RespiraNaAgua, MestreDeArmas,  
      PoderesAnimais, Teletransporte, MudancaDeForma, Imortalidade, 
      Elasticidade, Insanidade, Regeneracao, ViagemNoTempo, Invisibilidade

- A planilha PoderesMente apresenta habilidades e/ou poderes mentais.
  Cada coluna representa um poder/habilidade e possui um dos seguintes valores:
      1- significa que o personagem é dotado do poder ou tem a habilidade 
      0- significa que o personagem não possui o poder ou habilidade.
   Poderes/habilidades representados nesta planilha:
      Inteligencia, Telepatia, Telecinese, Clarividencia, ControleDaMente
      
Os seguintes DataFrames estão disponibilizados:

    -->dfInfo (da planilha Informacoes): descriçao do personagem,
       índice: NOME,
       colunas: Publicador, MidiaLancamento, AnoLancamento, Olhos, Especie,
               Cabelo, Peso, Altura, Pele, Alinhamento, Votos
       valores: dados descritos acima,

    -->dfPodG (da planilha PoderesGerais): tem ou não habilidade/poder
        índice: NOME,
        colunas: Voa, SuperVelocidade, SuperForca, RespiraNaAgua, MestreDeArmas,  
                 PoderesAnimais, TeleTransporte, MudancaDeForma, Imortalidade, 
                 Elasticidade, Insanidade, Regeneracao, ViagemNoTempo, Invisibilidade
        valores: 0 - não apresenta,  1 - apresenta

    --> dfMent (da planilha PoderesMente): tem ou não habilidade/poder mental
        índice: NOME,
        colunas: Inteligencia, Telepatia, Telecinese, Clarividencia, 
                 ControleDaMente
        valores: 0 - não apresenta,  1 - apresenta     
Obs: algumas informações foram alteradas/introduzidas para efeito didático.
'''


dfInfo=pd.read_excel('Herois2023_2.xlsx',sheet_name='Informacoes',header=0,index_col=0)
dfPodG=pd.read_excel('Herois2023_2.xlsx',sheet_name='PoderesGerais',header=0,index_col=0)
dfMent=pd.read_excel('Herois2023_2.xlsx',sheet_name='PoderesMente',header=0,index_col=0)
print('==============================================\n')
print("dfInfo - Descrição do personagem\n")
print(dfInfo.head(10))
print('==============================================\n')
print("dfPodG - Personagem tem ou não certa habilidade/poder geral\n")
print(dfPodG.head(10))
print('==============================================\n')
print("dfMent -Personagem tem ou não certa habilidade/poder mental\n")
print(dfMent.head(10))
print('==============================================\n')

print('Questão 1 - (1.8 pontos)')

#======================================================================
# 1- Conhecendo o dfInfo:
# (0,3) a- Exiba as informações da estrutura do DataFrame
# (0,3) b- Mostre os nomes dos personagens que estão com altura ausente
# (0,3) c- Total de votos atribuídos aos personagens do mal (Alinhamento)
# (0,3) d- Mostre o percentual de personagens com ano de lançamento
#          abaixo de 1960
# (0,3) e- Mostre,juntos, a quantidade de especies, a altura máxima e 
#          o peso mediano por  cor de cabelo (Cabelo)
# (0,3) f- Mostre a tabela de frequência no cruzamento das colunas
#          Alinhamento x Especie 

#======================================================================

print('------------------------------------------------------')
print('1.a- Estrutura do dfInfo ')
print('------------------------------------------------------')
print(dfInfo.info())

print('------------------------------------------------------')
print('1.b- Mostre os nomes dos personagens que estão com altura ausente')
print('------------------------------------------------------')

print(dfInfo[dfInfo['Peso'].isnull()].index)

print('------------------------------------------------------')

print('1.c- Total de votos atribuídos aos personagens do mal')
print('------------------------------------------------------')

f1c = dfInfo[dfInfo['Alinhamento'] == 'MAL']
print(f1c['Votos'].sum())

print('------------------------------------------------------')
print('''1.d- Percentual de personagens com ano de lançamento
#          abaixo de 1960''')
print('------------------------------------------------------')

f1d = dfInfo[dfInfo['AnoLancamento'] < 1960]
print(f1d['AnoLancamento'].count())
percent = (f1d['AnoLancamento'].count())

print('------------------------------------------------------')
print('''1.e- Quantidade de especies, altura máxima e 
         o peso mediano por  cor de cabelo''')
print('------------------------------------------------------')
g1e = dfInfo.groupby('Cabelo')
print(g1e.agg({'Especie':'count','Altura':'max','Peso':'median'}))

print('------------------------------------------------------')
print('1.f- Tabela de frequência do cruzamento de Alinhamento X Especie')
print('------------------------------------------------------')

print(pd.crosstab(dfInfo['Alinhamento'],dfInfo['Especie']))

print('==============================================')
print('Questão 2 - (1.5 pontos)')
#======================================================================
# 2- Analisando rapidamente o dfInfo: 
# (0,3) a- Quantidade de personagens por mídia de lançamento (MidiaLancamento)
# (0,3) b- Mostre os nomes e espécies dos personagens mais 
#          votados, ou seja, todos com a maior quantidade de votos
# (0,3) c- Inclua a coluna Idade, a partir da coluna AnoLancamento e 
#          considerando o ano de 2023, ou seja, a diferença entre 2023 
#          e o ano de lançamento do personagem. 
#          Em seguida, exiba, junto,  as idades mínima, máxima e mediana dos personagens.
# (0,3) d- Inclua a coluna Popularidade com a respectiva categoria de popularide. 
#          Devem ser criadas 3 categorias de acordo com os seguintes critérios:
#             "Baixa":  até 150 votos (inclusive), 
#             "Media":  de 151 a 300 votos  e a 
#             "Alta" :  acima de 300 votos.
#          Em seguida, exiba a coluna Popularidade dos 10 primeiros personagens.
# (0,3) e- Apresente como gráfico de pizza, a tabela de frequência 
#          percentual das faixas de Popularidade dos personagens.
#======================================================================

print('------------------------------------------------------')
print('2.a- Quantidade de personagens por mídia de lançamento')
print('------------------------------------------------------')

g2a = dfInfo.groupby('MidiaLancamento')
print(g2a['MidiaLancamento'].count())

print('------------------------------------------------------')
print('2.b- Nome, espécie dos personagens mais votados')
print('------------------------------------------------------')

queridos = dfInfo[dfInfo['Votos'] == dfInfo['Votos'].max()]

print('------------------------------------------------------')
print('2.c- Idades mínima, máxima e mediana dos personagens')
print('------------------------------------------------------')

dfInfo['Idade'] = (2023 - dfInfo['AnoLancamento'])
print(dfInfo['Idade'].agg(['min','max','median']))

print('------------------------------------------------------')
print('2.d- As categorias de popularidade dos 10 primeiros personagens')
print('------------------------------------------------------')

dfInfo['Popularidade'] = pd.cut(dfInfo['Votos'], bins = [0,150,300,dfInfo['Votos'].max()], labels = ['baixa','media','alta'])
print(dfInfo['Popularidade'].tail(5))

print('------------------------------------------------------')
print('2.e- Gráfico pizza da tabela de frequência percentual das faixas de popularidade')
print('------------------------------------------------------')
 
tabfreq = dfInfo['Popularidade'].value_counts(normalize=True)*100

plt.pie(tabfreq,labels=tabfreq.index, autopct='%1.1f%%')
plt.show()

print('==============================================')
print('Questão 3 - (0.9 pontos)')
#======================================================================',
# 3- Consertando o dfInfo: 
# (0,3) a-	Elimine a coluna Pele. Exiba os dados dos 8 primeiros personagens
# (0,3) b-	Preencha os valores ausentes na coluna Peso pela 
#           peso médio por espécie(Especie). Exiba a coluna Peso dos 5 
#           primeiros personagens
#           Caso vc não consiga resolver esta questão como descrito, 
#           substitua os valores ausentes por 1.5           
# (0,3) c-	Selecione os 30 primeiros personagens do dfInfo após 
#           eliminação/preenchimento. 
#           Exiba  a especie, o alinhamento, o peso, a altura  e a popularidade 
#           dos personagens ordenados crescentemente por especie (Especie)
#======================================================================',

print('------------------------------------------------------')
print('3.a- 8 primeiros personagens após eliminação da coluna Pele, ordenados pelo nome')
print('------------------------------------------------------')

dfInfo.drop(['Pele'], axis = 1, inplace = True)
print(dfInfo.head(8))

print('------------------------------------------------------')
print('3.b- coluna Peso dos 5 primeiros personagens de dfInfo após preenchimento')
print('------------------------------------------------------')

g3b = dfInfo.groupby('Especie')
dfInfo.fillna(value = {'Peso':g3b.Idade.transform('mean')},inplace = True)
print(dfInfo['Peso'].head(5))

print('------------------------------------------------------')
print('''3.c- Especie, Alinhamento, Peso, Altura e Popularidade
      dos 30 primeiros personagens após alterações, ordenado por especie''')
print('------------------------------------------------------')
 
print(dfInfo['Especie','Alinhamento','Peso','Altura','Popularidade'].head(30).sort_values(by='Especie',ascending = True))

print('==============================================')
print('Questão 4 - (1.8 pontos)')
#======================================================================
# 4- Analisando os poderes dos personagens
# (0,3) a-	dfPodG: Mostre para cada poder, quantos personagens têm esse poder
# (0,3) b-	dfPodG: Mostre o nome dos personagens que tenham 
#                   o poder de teletransporte (TeleTransporte) E 
#                   o poder da imortalidade  (Imortalidade)
# (0,3) c-	dfPodG : Inclua a coluna TotPodGerais com a quantidade de poderes
#                    gerais de cada personagem do dfPodG. Mostre os 10 primeiros 
#                    valores desta coluna.
# (0,3) d-	dfMent: Mostre um poder mais frequente entre os personagens, ou seja, 
#                   um poder no dfMent do qual a maior quantidade de personagens 
#                   seja dotado.
# (0,3) e-	dfMent:  Mostre o DataFrame com os poderes mentais que os personagens 
#                    da espécie humano (do dfInfo) possuem. 
# (0,3) f-	dfMent: Inclua no dfMent a coluna TotPodMentais com o total de
#                   poderes da mente de cada personagem do dfMent. Mostre as 10 
#                   últimas linhas do dfMent.
#======================================================================

print('------------------------------------------------------')
print('4.a- dfPodG: Quantidade de personagens por poder')
print('------------------------------------------------------')

print('------------------------------------------------------')
print('4.b- dfPodG: Nome dos personagens com teletransporte e imortalidade')
print('------------------------------------------------------')
 
print('------------------------------------------------------')
print('4.c- dfPodG: 10 primeiros valores da coluna TotPodGerais')
print('------------------------------------------------------')
 
print('------------------------------------------------------')
print('4.d- dfMent: Um poder mais frequente')
print('------------------------------------------------------')
 
print('------------------------------------------------------')
print('4.e- dfMent: Poderes mentais dos personagens humanos')
print('------------------------------------------------------')
 
print('------------------------------------------------------')
print('4.f- dfMent: 10 últimas linhas')
print('------------------------------------------------------')
 
print('==============================================')
# print('Questão 5 - (1.0 pontos)')
# #======================================================================
# # 5- Analisando os personagens 
# # (0,3) a- Crie o DataFrame dfCompleto, concatenando apropriadamente dfInfo e
# #           as colunas TotPodGerais do dfPodG e a coluna TotPodMentais do 
# #           dfMent. Só os personagens que constam nos três DFs devem estar no 
# #           dfCompleto. Mostre os 5 últimos personagens do dfCompleto 
# #
# # (0,4) b- dfCompleto: Selecione os personagens que tenham mais poderes mentais
# #                    do que gerais e mostre a quantidade de votos mínima e 
# #                    máxima dos personagens por Alinhamento/Especie
# #                   
# # (0,3) c- dfCompleto: Inclua a coluna TotPod com a soma das colunas TotPodGerais
# #          e TotPodMentais. Mostre o gráfico de dispersão das colunas 
# #                       TotPod X Votos
# #======================================================================

# print('------------------------------------------------------')
# print('5.a- 5 últimos personagens do dfCompleto')
# print('------------------------------------------------------')
 
# print('------------------------------------------------------')
# print('5.b- Sumarizações por Alinhamento / Especie')
# print('------------------------------------------------------')
 

# print('------------------------------------------------------')
# print('5.c- Gráfico de dispersão de TotPod X Votos')
# print('------------------------------------------------------')
 