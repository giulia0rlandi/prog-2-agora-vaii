# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:23:36 2024

@author: Ferlin
"""
'''
Considere os seguintes dicionários:

    Dicionário dAlunosTurmas: Mapeia o nome dos alunos para suas respectivas turmas.
    Exemplo: 'Ana': '33A' indica que a aluna Ana está na turma 33A.

    Dicionário dTurmasLabProvas: Mapeia as turmas para os laboratórios onde as provas serão realizadas.
    Exemplo: '33A': 'L258' indica que a turma 33A fará a prova no laboratório L258.
    
a)	Construa a função mostrar_sala_prova que receba estes dicionários, e o nome de um aluno e
    mostre para este aluno qual sua sala de prova ou ua mensagem caso o aluno
    não esteja no dicionário

b)	Construa a função construir_dicionario_frequencias que receba estes dicionários
    e construa um novo dicionário que contará quantos alunos estão alocados 
    para cada laboratório. O novo dicionário tem como:
         chave é o laboratório e o 
         valor é a quantidade de alunos que farão prova neste laboratório (dicionário de frequências)
'''

dAlunosTurmas = {'Ana':'33A',
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

dTurmasLabProvas = {'33A': 'L258',
        '33B': 'L270',
        '33C': 'L314',
	'33G': 'L258'
}    


#TESTE FUNÇÂO a       
#mostrar_sala_prova(dAlunosTurmas, dTurmasLabProvas, 'Ana')
#mostrar_sala_prova(dAlunosTurmas, dTurmasLabProvas, 'Juca')

#TESTE FUNÇÂO b) 
#dicfrequencias = construir_dicionario_frequencias(dAlunosTurmas, dTurmasLabProvas)
#print(dicfrequencias)
