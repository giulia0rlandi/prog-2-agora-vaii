# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:52:04 2021

@author: Ferlin
"""

# #1.	Considere os seguintes dicionários:
dAlunosTurmas = {
    'Ana':'33A',
    'Patinhas':'33A',
    'Zé':'33A',
    'Pedro':'33C',
    'Carla':'33B',
    'So':'33B', 
    'Margarida':'33A',
    'Donald':'33B',
    'Lola':'33C',
    'Carlos':'33A',
    'Maios':'33G'
}

dTurmasLabProvas = {
    '33A': 'L258',
    '33B': 'L270',
    '33C': 'L314',
    '33G': 'L258'
}    



# a) Construa uma função que 
#     receba estes dicionários e o nome de um aluno e 
#     mostre para este aluno qual sua sala de prova

def mostrar_sala_prova(dAlunosTurmas, dTurmasLabProvas, nome):
    turma = dAlunosTurmas.get(nome)
    if turma:
        sala = dTurmasLabProvas.get(turma)
        print(f'a sala de {nome} é {sala}')
    else:
        print(f'aluno {nome} nao encontrado')
        
# b)	Construa uma função que 
#     receba estes dicionários e 
#     construa um novo dicionário onde :
#           chave: aluno
#           valor: sala de prova

def constroi(dAlunosTurmas, dTurmasLabProvas):
    dnovo = {}
    for aluno, turma in dAlunosTurmas.items():
        sala = dTurmasLabProvas.get(turma)
        dnovo[aluno] = sala
    return dnovo

# c) Construa uma função que 
#     receba o dicionário do item b) e 
#     construa um novo dicionário cuja 
#         a chave é o laboratório e 
#         o valor é a quantidade de alunos que farão prova neste laboratório (dicionário de frequências)

def freq(dnovo):
    dfreq = {}
    for aluno , sala in dnovo.items():
        cont = dfreq.get(sala,0)
        cont +=1
        dfreq[sala] = cont 
    return dfreq

# d) Construa uma função que 
#     receba o dicionário do item b) e 
#     construa um novo dicionário cuja 
#         a chave é a sala e 
#         o valor é uma lista do nome dos alunos que farão prova neste laboratório ( dicionário de agrupamentos)

def lista(dnovo):
    dlist = {}
    for aluno , sala in dnovo.items(): 
        if sala not in dlist:
            dlist[sala] = []
        dlist[sala].append(aluno)
    return dlist

# e) Construa uma função que 
#     receba dAlunosTurmas   e 
#     construa o dicionário dTurmasAlunos, 
#         onde a chave é a turma e 
#         o valor é a lista de alunos desta turma. (dicionário inverso)

def inv(dAlunosTurmas):
    dTurmasAlunos = {}
    for aluno , turma in dAlunosTurmas.items():
        if turma not in dTurmasAlunos:
            dTurmasAlunos[turma] = []
        dTurmasAlunos[turma].append(aluno)
    return dTurmasAlunos
        
# f) Utilizando o dicionário dTurmasAlunos ( chave: Turma, valor: lista de alunos) 
#     construa o dicionário dLabComTurmas 
#         onde a chave é o laboratório e 
#         o valor é o dicionário dTurmasAlunos
#             dLabComTurmas--> {
#                 'L258’ : {'33A’ : [   'Patinhas',  'Zé', 'Margarida', 'Carlos'] , ‘33G’:[‘Maios’] },
# 	 'L270' :  {'33B’ : [   'Carla',  'So', 'Donald']},
# 	 'L314' :  {'33C’ : [   'Pedro',  'Lola']}
# 	     }

def lab(dTurmasAlunos,dTurmasLabProvas):
    dLabComTurmas = {}
    for turma , sala in dTurmasLabProvas.items():
        if sala not in dLabComTurmas:
            dLabComTurmas[sala] = {}
        if turma in dTurmasAlunos:
            dLabComTurmas[sala][turma] = dTurmasAlunos[turma]
    return dLabComTurmas
        

# g) Construa uma função que receba dTurmasLabProvas e 
#   retorne um novo dicionário, onde 
#                chave: lab e 
#                valor: lista de turmas do lab

def dnovo(dTurmasLabProvas):
    dSalas = {}
    for turma , sala in dTurmasLabProvas.items():
        if sala not in dSalas:
            dSalas[sala] = []
        dSalas[sala].append(turma)
    return dSalas

#TESTE FUNÇÂO a       
mostrar_sala_prova(dAlunosTurmas, dTurmasLabProvas, 'Ana')
mostrar_sala_prova(dAlunosTurmas, dTurmasLabProvas, 'Juca')
print('---------------------------------------')

#TESTE FUNÇÂO b
print(constroi(dAlunosTurmas,dTurmasLabProvas))
print('---------------------------------------')

#TESTE FUNÇÂO c
dicfrequencias = constroi(dAlunosTurmas, dTurmasLabProvas)
print(freq(dicfrequencias))
print('---------------------------------------')

#TESTE FUNÇÂO d
dicfrequencias = constroi(dAlunosTurmas, dTurmasLabProvas)
print(lista(dicfrequencias))
print('---------------------------------------')

#TESTE FUNÇÂO e
print(inv(dAlunosTurmas))
print('---------------------------------------')

#TESTE FUNÇÂO f
dTurmasAlunos = inv(dAlunosTurmas)
print(lab(dTurmasAlunos,dTurmasLabProvas))
print('---------------------------------------')

#TESTE FUNÇÂO g
print(dnovo(dTurmasLabProvas))
print('---------------------------------------')