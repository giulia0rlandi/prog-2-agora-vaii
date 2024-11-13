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
# (0,3) b- Mostre os nomes dos personagens que estão com peso ausente
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
dfInfo.info()
print('------------------------------------------------------')
print('1.b- Mostre os nomes dos personagens que estão com peso ausente')
print('------------------------------------------------------')

#fazendo por partes
filtro= dfInfo.Peso.isnull()
print('filtro\n', filtro)
res_filtro = dfInfo.loc[filtro]
print('aplicando filtro\n', res_filtro)
nomes_personagens = res_filtro.index
print('somente nomes\n', nomes_personagens)

#fazendo direto
print(list(dfInfo.loc[dfInfo.Peso.isnull()].index))

print('------------------------------------------------------')

print('1.c- Total de votos atribuídos aos personagens do mal')
print('------------------------------------------------------')


#fazendo por partes 2 formas
#fazendo por query
filtro = dfInfo.query('Alinhamento=="mal"')
print('\n===filtro: dfInfo.query(Alinhamento==mal)\n', filtro)
print('\n===filtro.Votos', filtro.Votos)
print('\n===filtro.Votos.sum()', filtro.Votos.sum(axis=0))

#fazendo sem query
filtro = dfInfo['Alinhamento']=="mal"
print('\n====filtro: dfInfo[Alinhamento]==mal\n', filtro)
print('dfInfo.loc[filtro]\n', dfInfo.loc[filtro])
#* veja que dfInfo.query('Alinhamento=="mal"') é semelhante a dfInfo.loc[dfInfo['Alinhamento']=="mal"]
print('dfInfo.loc[filtro].Votos\n', dfInfo.loc[filtro].Votos)
print('dfInfo.loc[filtro].Votos.sum()\n', dfInfo.loc[filtro].Votos.sum())

#fazendo direto
print(dfInfo.query('Alinhamento=="mal"').Votos.sum())

print('------------------------------------------------------')
print('''1.d- Percentual de personagens com ano de lançamento
#          abaixo de 1960''')
print('------------------------------------------------------')

# print(dfInfo.shape)
# print('dfINFO FILTRO:\n', dfInfo['AnoLancamento']<1960)
# print('dfINFO FILTRO0:\n', type(dfInfo['AnoLancamento']<1960)) #serie de valores T/F
# print('dfINFO FILTRO1:\n', dfInfo[dfInfo['AnoLancamento']<1960])
# print('dfINFO FILTRO2:\n', dfInfo[dfInfo['AnoLancamento']<1960].shape[0])
# print('dfINFO FILTRO3:\n', dfInfo[dfInfo['AnoLancamento']<1960].index.size)
# print(dfInfo[dfInfo['AnoLancamento']<1960].index.size/dfInfo.index.size*100)

#duas soluções
#filtro com query
dfFiltrado = dfInfo.query('AnoLancamento < 1960')
print('dfInfo filtrado com query \n', dfFiltrado)
print('qt percentual\n', dfFiltrado.shape[0] / dfInfo.shape[0]*100)


#filtro sem query
filtro= dfInfo['AnoLancamento']<1960
print('dfInfo filtrado sem query\n', filtro)

qt = dfInfo.loc[filtro].shape[0]

qt=filtro.sum() #serie de valores T/F, soma somente os que tem T

print('qt\n', qt)
print(qt/dfInfo.shape[0]*100)

print('------------------------------------------------------')
print('''1.e- Quantidade de especies, altura máxima e
         o peso mediano por cor de cabelo''')
print('------------------------------------------------------')
g1e=dfInfo.groupby('Cabelo')
x= g1e.Especie.agg('count')
y= g1e.Altura.agg('max')
print(pd.concat([x,y], axis=1))

print(g1e.agg('count'))
# print(g1e.agg(['count','max','median'])) 
print(g1e.agg({'Especie':'count','Altura':'max','Peso':'median'}))

print('------------------------------------------------------')
print('1.f- Tabela de frequência do cruzamento de Alinhamento X Especie')
print('------------------------------------------------------')
print(pd.crosstab(dfInfo.Alinhamento,dfInfo.Especie, values=dfInfo.Cabelo, aggfunc='count'))
print('Quantos humanos tem do bem?')
print(pd.crosstab(dfInfo.Alinhamento,dfInfo.Especie).loc['bem'].humano)

print('==============================================')

# print('Questão 2 - (1.5 pontos)')

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

# fazendo pelo groupby, escolho qualquer coluna para contar
print('result using groupby\n', dfInfo.groupby('MidiaLancamento').Especie.agg('count'))


# fazendo pelo values_count()
print('result fazendo pelos values_count\n',dfInfo['MidiaLancamento'].value_counts())

print('------------------------------------------------------')
print('2.b- Nome, cabelo dos personagens mais votados')
print('------------------------------------------------------')
maiorQtd = dfInfo.Votos.max()

#fazendo com query
dfInfoFiltrado = dfInfo.query('Votos =='+ str(maiorQtd))
dfInfoFiltrado = dfInfo.query(f'Votos == {maiorQtd}')
print('dfInfoFiltrado por query\n', dfInfoFiltrado)

print(dfInfo.loc[dfInfo['Votos']==maiorQtd][['Especie','Cabelo']])

#fazendo por partes sem query
filtro= dfInfo['Votos']==maiorQtd
print('dfInfo.loc[filtro]\n', dfInfo.loc[filtro])
print('dfInfo.loc[filtro].Cabelo\n',dfInfo.loc[filtro].Cabelo)


# fazendo direto
print(dfInfo.loc[dfInfo['Votos']==maiorQtd]['Cabelo'])


print('------------------------------------------------------')
print('2.c- Idades mínima, máxima e mediana dos personagens')
print('------------------------------------------------------')
dfInfo['Idade'] = 2023-dfInfo['AnoLancamento']
print(dfInfo.Idade.min(), dfInfo.Idade.max(),dfInfo.Idade.median())

print(dfInfo.Idade.agg(['min','max','median']))

print('------------------------------------------------------')
print('2.d- As categorias de popularidade dos 10 primeiros personagens')
print('2.d- As categorias de popularidade dos 5 ultimos personagens')
print('------------------------------------------------------')
dfInfo['Popularidade'] = pd.cut(dfInfo.Votos,bins=[0,150,300,dfInfo.Votos.max()]
                                ,labels=['Baixa','Media', 'Alta'],include_lowest=True)
dfa= dfInfo.Popularidade.head(10)
dfb= dfInfo.Popularidade.tail(5)
print(dfInfo.Popularidade.head(10))
print(dfInfo.Popularidade.tail(5))
print(pd.concat([dfa,dfb]))

print('------------------------------------------------------')
print('2.e- Gráfico pizza da tabela de frequência percentual das faixas de popularidade')
print('------------------------------------------------------')

dfInfo.Popularidade.value_counts().plot.pie(autopct='%.2f')
plt.show()

# ou 
dfInfo.Popularidade.value_counts().plot.pie()
plt.show()

print('==============================================')

# # print('Questão 3 - (0.9 pontos)')
# #
# # #======================================================================',
# # # 3- Consertando o dfInfo:
# # # (0,3) a-	Elimine a coluna Pele. Exiba os dados dos 8 primeiros personagens
# # # (0,3) b-	Preencha os valores ausentes na coluna Peso pela
# # #           peso médio por espécie(Especie). Exiba a coluna Peso dos 5
# # #           primeiros personagens
# # #           Caso vc não consiga resolver esta questão como descrito,
# # #           substitua os valores ausentes por 1.5
# # # (0,3) c-	Selecione os 30 primeiros personagens do dfInfo após
# # #           eliminação/preenchimento.
# # #           Exiba  a especie, o alinhamento, o peso, a altura  e a popularidade
# # #           dos personagens ordenados crescentemente por especie (Especie)
# # #======================================================================',

print('------------------------------------------------------')
print('3.a- 8 primeiros personagens após eliminação da coluna Pele, ordenados pelo nome')
print('------------------------------------------------------')
dfInfo.drop('Pele',inplace=True,axis=1)
print(dfInfo.head(8).sort_index())
# OU
#print(dfInfo.sort_index().head(8))
print('------------------------------------------------------')
print('3.b- coluna Peso dos 5 primeiros personagens de dfInfo após preenchimento')
print('------------------------------------------------------')

# 1ra solucçao
# grupoEspecie = dfInfo.groupby('Especie')
# pesoMedioXEspecie = grupoEspecie['Peso'].agg(['mean'])
# print('pesoMedioXEspecie\n', pesoMedioXEspecie) #serie que tem como indice a especie
# # dfInfo[['Especie','Peso']].fillna(pesoMedioXEspecie,inplace=True)#incorreto pesso medio, o indice não é o nome
# print('pesoMedioXEspecie.mean\n ', pesoMedioXEspecie.mean) #coluna mean
# grupoEspecie['Peso'].fillna(pesoMedioXEspecie.mean,inplace=True)#indice é o grupo, deprecated
# print('grupoEspecie\n', grupoEspecie)
# dfInfo.Peso = grupoEspecie['Peso']

# print('\n===========\n dfInfo.Peso.head()\n', dfInfo.Peso.head())

print('peso sem preencher\n', dfInfo.Peso.head())
print(dfInfo.Peso.head())


# #2da solução
grEspecie=dfInfo.groupby(dfInfo.Especie,group_keys=False)
def pesoMedio(g):
    g.fillna(g.mean(),inplace=True)
    return g
dfInfo.Peso = grEspecie.Peso.apply(pesoMedio)
print('\n ============== \n peso preenchido\n',dfInfo.Peso.head())

# **
'''
group_keys=False removes the group keys (Group values) from the index.
The result is a simple Series with each group’s summary, without additional index labels to identify the groups.
'''

# 3ra solução
def preenche(grupo):
    media=grupo.mean()
    grupo.fillna(media,inplace=True)
    return grupo
grupoEspecie = dfInfo.groupby('Especie')
dfInfo['Peso']=grupoEspecie['Peso'].transform(preenche)
print('\n ============== \n peso preenchido outra solução \n',dfInfo.Peso.head())



print('------------------------------------------------------')
print('''3.c- Especie, Alinhamento, Peso, Altura e Popularidade
      dos 30 primeiros personagens após alterações, ordenado por especie''')
print('------------------------------------------------------')
print(dfInfo[['Especie','Alinhamento', 'Peso', 'Altura','Popularidade']].head(30).sort_values('Especie'))
print('==============================================')

# print('Questão 4 - (1.8 pontos)')

# #======================================================================
# # 4- Analisando os poderes dos personagens
# # (0,3) a-	dfPodG: Mostre para cada poder, quantos personagens têm esse poder
# # (0,3) b-	dfPodG: Mostre o nome dos personagens que tenham
# #                   o poder de teletransporte (TeleTransporte) E
# #                   o poder da imortalidade  (Imortalidade)
# # (0,3) c-	dfPodG : Inclua a coluna TotPodGerais com a quantidade de poderes
# #                    gerais de cada personagem do dfPodG. Mostre os 10 primeiros
# #                    valores desta coluna.
# # (0,3) d-	dfMent: Mostre um poder mais frequente entre os personagens, ou seja,
# #                   um poder no dfMent do qual a maior quantidade de personagens
# #                   seja dotado.
# # (0,3) e-	dfMent:  Mostre o DataFrame com os poderes mentais que os personagens
# #                    da espécie humano (do dfInfo) possuem.
# # (0,3) f-	dfMent: Inclua no dfMent a coluna TotPodMentais com o total de
# #                   poderes da mente de cada personagem do dfMent. Mostre as 10
# #                   últimas linhas do dfMent.
# #======================================================================

print('------------------------------------------------------')
print('4.a- dfPodG: Quantidade de personagens por poder')
print('------------------------------------------------------')
print(dfPodG.sum())
print('------------------------------------------------------')
print('4.b- dfPodG: Nome dos personagens com teletransporte e imortalidade')
print('------------------------------------------------------')

# por partes
filtro= (dfPodG['TeleTransporte']==1) & (dfPodG['Imortalidade']==1)
print('dfPodG.loc[filtro].index\n', dfPodG.loc[filtro].index)
print('dfPodG.loc[filtro].index.values\n', dfPodG.loc[filtro].index.values)

# usando query
print("usando query")
print(dfPodG.query("TeleTransporte==1 & Imortalidade==1").index.values)

print('------------------------------------------------------')
print('4.c- dfPodG: 10 primeiros valores da coluna TotPodGerais')
print('------------------------------------------------------')
dfPodG['TotPodGerais']=dfPodG.sum(axis=1)
print(dfPodG['TotPodGerais'].head(10))
print('------------------------------------------------------')
print('4.d- dfMent: Um poder mais frequente')
print('------------------------------------------------------')
print(dfMent.sum(axis=0))

print("o indice do mais frequente:\n")
print(dfMent.sum().idxmax())

# print('------------------------------------------------------')
# print('4.e- dfMent: Poderes mentais dos personagens humanos')
# print('------------------------------------------------------')


# solução com filtro
filtro=dfInfo.Especie=='humano'
print('filtro\n', filtro)
print('aplicando o filtro\n',dfMent.loc[filtro] )

print(dfMent.loc[dfInfo.Especie=='humano'])

# solução com query
print('fazendo com query\n')
dfHumano = dfInfo.query('Especie=="humano"')
print(dfMent.loc[dfHumano.index])

print('------------------------------------------------------')
print('4.f- dfMent: 10 últimas linhas')
print('------------------------------------------------------')
dfMent['TotPodMentais']=dfMent.sum(axis=1)
print(dfMent.tail(10))
print('==============================================')

# # print('Questão 5 - (1.0 pontos)')

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

print('------------------------------------------------------')
print('5.a- 5 últimos personagens do dfCompleto')
print('------------------------------------------------------')
dfCompleto=pd.concat([dfInfo,dfPodG.TotPodGerais,dfMent.TotPodMentais],axis=1,join='inner')
print(dfCompleto.tail(5))

print('------------------------------------------------------')
print('5.b- Sumarizações por Alinhamento / Especie')
print('------------------------------------------------------')

# fazendo por filtro
filtro = dfCompleto.TotPodGerais < dfCompleto.TotPodMentais
dfMais = dfCompleto.loc[filtro]
print('dfMais por filtro\n', dfMais)

# fazendo por query
dfMais = dfCompleto.query("TotPodGerais<TotPodMentais")
print('dfMais por query\n', dfMais)


grupoAlinEsp = dfMais.groupby(['Alinhamento', 'Especie'])
print(grupoAlinEsp.Votos.agg(['min', 'max']))

print('------------------------------------------------------')
print('5.c- Gráfico de dispersão de TotPod X Votos')
print('------------------------------------------------------')
dfCompleto['TotPod']=dfCompleto['TotPodGerais']+dfCompleto['TotPodMentais']
dfCompleto.plot.scatter(x='TotPod',y='Votos')
plt.show()
