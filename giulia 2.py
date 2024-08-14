# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
''' 
1-------------------------------------------------------------------------------------------------------
Teste as funções abaixo considerando a seguinte lista:
    
L=[10,-10,3,89,34,-66,23,9,89,12,23,34,-11,20,31,89,20]


a) Construa uma função qualMaior que receba esta lista e retorna o maior valor função max()) (R:89)
    
b) Construa uma função ondeMaior que receba esta lista e retorna o índice da primeira ocorrência do
maior valor ( método .index) (R:3)

c) Construa uma função ondeTodosMaior que receba esta lista e retorna uma lista com os índices do maior
valor. (R: [3, 8, 15])

d) Construa uma função somaOutros que receba esta lista e exibe a soma dos valores diferentes do maior.
Esta função deve chamar a função do item a) (R:132)
    
e) Construa uma função somaPosteriores que receba esta lista e exibe a soma dos valores que são
subsequentes à primeira ocorrência do maior valor da lista (R: 307)

f) Construa uma função alteraPares que receba esta lista e dobrando todos os valores pares. Esta função
deve alterar a própria lista recebida
---------------------------------------------------------------------------------------------------------
'''

#1a
L=[10,-10,3,89,34,-66,23,9,89,12,23,34,-11,20,31,89,20]

def qualMaior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior
    # return max(lista)

#---------------------------------------------------------------------------------------------------------

#1b

def ondeMaior(lista):
    for (pos,num) in enumerate(lista):
        if num == qualMaior(lista):
            return pos
    #return lista.index(89)

#---------------------------------------------------------------------------------------------------------
    
#1c

def ondeTodosMaior(lista):
    # lnova = []
    # num = lista.index(89)
    # l.append(num)
    # return lnova
    
    
    # lnova = list(lista.index(89))
    # return 
    maior= qualMaior(lista)
    lnova = []
    for (pos,num) in enumerate(lista):
        if num == maior:
            lnova.append(pos)
    return lnova

# usar enumerate sempre que precisar da posição e do valor

#---------------------------------------------------------------------------------------------------------

#1d

def somaOutros(lista):
    soma = 0
    maior= qualMaior(lista)
    for num in lista:
        if num != maior:
            soma+=num
    return soma

#---------------------------------------------------------------------------------------------------------

#1e

def somaPosteriores(lista):
    soma = 0
    
    posI=ondeMaior(lista)+1
    for num in lista[posI:]:
        soma+=num
    return soma

            

'''2) Uma pessoa fez várias apostas (jogos) de 6 a 10 números na Megasena. Os jogos dessa pessoa estão
guardados como uma lista de listas, em que cada lista interna corresponde a uma aposta. O resultado do sorteio da
Megasena é representado por meio de uma lista de 6 elementos.
Obs: As apostas e o resultado não estão necessariamente ordenados.

a) Escreva uma função, chamada maiorNumeroAcertos, que:
• Receba uma lista de apostas (lista de listas) e a lista com o resultado do sorteio da Megasena;
• Retorne uma lista com:
    
i. Um número inteiro correspondente à maior quantidade de acertos em uma aposta;
ii. As listas correspondentes às apostas que tiveram essa quantidade de acertos.


b) Escreva um programa para testar a função maiorNumeroAcertos.
Exemplo:
    
Lista de apostas: [ [6,3,18,49,45,57], [6,2,25,37,38,39,42,54], [51,18,37,40,44,4], [6,25,40,41,51,52,57], [1,2,6,37,49,59] ]

Resultado do sorteio: [18,6,40,42,51,58
                       ]
Lista que deve ser retornada: [3, [ [4, 18, 37, 40, 44, 51], [6, 25, 40, 41, 51, 52, 57] ] ]'''










'''
3) Uma lista contém os nomes e as médias finais de cada um dos alunos inscritos em cada uma das disciplinas
oferecidas em determinado semestre.
Exemplo:
mediasFinais = [ ['INF1025', [ [ 'joão',9.0 ], [ 'maria',8.0 ], [ 'josé',4.9 ] ] ],
['INF1026', [ [ 'joão',7.0 ], [ 'maria',4.1 ] ] ],
['INF1007', [ ['josé',4.3 ] ] ]
]
Escreva uma função em Pyhton, chamada gerarSituacaoFinal, que receba como parâmetro a lista mediasFinais e
retorne uma nova lista (lst) contendo n elementos, em que n representa o número de alunos (sem repetições)
existentes na lista mediasFinais. Cada elemento de lst tem de conter o nome de um aluno e uma sublista,
possivelmente vazia, com as disciplinas nas quais esse aluno foi aprovado (média final maior ou igual a 5,0).
Caso a função gerarSituacaoFinal receba a lista mediaFinais como parâmetro, a seguinte lista (lst) deverá ser
retornada:
lst = [ [ 'joão', [ 'INF1025','INF1026' ] ], [ 'maria', [ 'INF1025' ] ], [ 'josé', [] ] ]
Escreva um programa em Python para testar a sua implementação da função gerarSituacaoFinal.'''

    
    



