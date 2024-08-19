# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:54:36 2024

@author: Ferlin
"""
"""
Enunciado:  Sistema de Gestão de Inscrições em Atividades de um Evento
Este programa foi desenvolvido para gerenciar as inscrições dos participantes em 
diferentes atividades oferecidas durante um evento. 
Ele organiza e processa as informações dos participantes e das atividades,
 permitindo que se façam consultas e análises sobre as inscrições.

Estrutura de Dados Utilizada
Lista de Atividades (latividades):

A lista de atividades contém todas as atividades disponíveis no evento.
Cada atividade é representada por uma sublista que contém:
   -O nome da atividade.
   - Uma lista de participantes que se inscreveram nessa atividade.
A princípio, as atividades disponíveis são:
    "Palestra de Abertura"
    "Workshop de Python"
    "Workshop de Machine Learning"
    "Mesa Redonda de IA"
    "Sessão de Networking"
    "Palestra de Encerramento"


# Lista de Participantes: (lparticipantes)
A lista de participantes contém informações sobre todos os inscritos no evento.
Cada participante é representado por uma sublista que inclui:
    Nome do participante.
    Idade do participante.
    E-mail do participante.
    Uma lista das atividades em que o participante está inscrito.


Funcionalidades do Programa
# Atualização de Inscrições: percorre a lista de participantes e atualiza a 
lista de inscritos para cada atividade. Isso garante que cada atividade tenha 
uma lista atualizada de quem está participando.

# Exibição das Atividades com Inscritos: exibe todas as atividades do evento e,
 para cada uma delas, lista dos dados dos participantes que se inscreveram. 
 Isso facilita a visualização de quantos e quais participantes estão envolvidos
 em cada atividade.

#Exibição de Quem Escolheu uma Determinada Atividade como Primeira Tarefa:
Exibe a lista de participantes que escolheram uma atividade específica como 
sua primeira tarefa. Essa funcionalidade é útil para identificar o nível 
de interesse inicial em atividades específicas.. A atividade a ser verificada é 
passada como argumento.

"""
#  Função atualizar_inscricoes: recebe as duas listas e atualiza a lista de 
#  inscritos em cada atividade com base nas escolhas dos participantes.
#  inclui apenas o nome do participante na lista de atividades
#  Para as listas exemplos, a latividades resultante seria;
  #  [
  #   ["Palestra de Abertura", ["Bruno Silva", "Eduarda Lima"]],
  #   ["Workshop de Python", ["Alice Souza", "Daniel Oliveira"]],
  #   ["Workshop de Machine Learning", ["Bruno Silva", "Daniel Oliveira"]],
  #   ["Mesa Redonda de IA", ["Alice Souza", "Carla Mendes"]],
  #   ["Sessão de Networking", ["Alice Souza", "Eduarda Lima"]],
  #   ["Palestra de Encerramento", ["Carla Mendes", "Daniel Oliveira"]]
  # ]

def busca(l,valor):
    for (pos,val) in enumerate(l):
        if val[0] == valor:
            return pos
    return None

def atualizar_inscricoes(lativ,lpart):
    for inscrito in lpart:
        nome = lpart[0]
        atividades_inscritas = lpart[3]
        for ativ in atividades_inscritas:
            pos = busca(lativ,ativ)
            if pos != None:
                lativ[pos][1].append(nome)
                
# Função exibir_atividades_com_inscritos: Exibe todas as atividades disponíveis 
# e seus respectivos inscritos (nome, idade e email dos inscritos)

def exibir_atividades_com_inscritos(lativ,lpart):
    for atividade in lativ:
        nome_atividade = atividade[0]
        inscritos = atividade[1]
        print(f"Atividade: {nome_atividade}")
        if inscritos:
            print("Inscritos:")
            for inscrito in inscritos:
                pos=busca(lparticipantes,inscrito)
                participante=lparticipantes[pos]
                print(f"- Nome: {participante[0]}, Idade: {participante[1]}, Email: {participante[2]}")
        else:
            print("Nenhum inscrito.")
        print("-" * 20)
        
# Função exibir_quem_escolheu_primeira_atividade: Exibe quais participantes 
# escolheram uma determinada atividade como a primeira escolha. 
# As listas e a atividade a ser verificada são recebidas pela função
# Uma mensagem adequada deve ser exibida, caso nenhum perticipante tenha
# escolhido a atividade como primeira opção
# Saída para listas exemplos e Workshop de Python
#        Participantes que escolheram 'Workshop de Python' como primeira atividade:
#         - Alice Souza
#         - Daniel Oliveira 
def exibir_quem_escolheu_primeira_atividade(latividades, lparticipantes, atividade_escolhida):
    print(f"\nParticipantes que escolheram '{atividade_escolhida}' como primeira atividade:")
    encontrados = False
    for participante in lparticipantes:
        if participante[3] and participante[3][0] == atividade_escolhida:
            print(f"- {participante[0]}")
            encontrados = True
    if not encontrados:
        print(f"Nenhum participante escolheu '{atividade_escolhida}' como primeira atividade.")
    print("-" * 20)

#BP        

# Lista de atividades, onde cada atividade tem uma lista de inscritos, inicialmente vazia
latividades = [
    ["Palestra de Abertura", []],
    ["Workshop de Python", []],
    ["Workshop de Machine Learning", []],
    ["Mesa Redonda de IA", []],
    ["Sessão de Networking", []],
    ["Palestra de Encerramento", []]
]

# Lista de participantes, onde cada participante tem uma lista de atividades inscritas
lparticipantes = [
    ["Alice Souza", 28, "alice.souza@example.com", ["Workshop de Python", "Mesa Redonda de IA", "Sessão de Networking"]],
    ["Bruno Silva", 35, "bruno.silva@example.com", ["Palestra de Abertura", "Workshop de Machine Learning"]],
    ["Carla Mendes", 24, "carla.mendes@example.com", ["Mesa Redonda de IA", "Palestra de Encerramento"]],
    ["Daniel Oliveira", 31, "daniel.oliveira@example.com", ["Workshop de Python", "Palestra de Encerramento", "Workshop de Machine Learning"]],
    ["Eduarda Lima", 29, "eduarda.lima@example.com", ["Palestra de Abertura", "Sessão de Networking"]]
]

#Teste Atualizar as listas de inscritos nas atividades
#atualizar_inscricoes(lparticipantes,latividades)
atualizar_inscricoes(latividades,lparticipantes)

#Teste Exibir as atividades com seus inscritos
#exibir_atividades_com_inscritos(latividades,lparticipantes)
exibir_atividades_com_inscritos(latividades,lparticipantes)

#Teste Exibir quem escolheu uma atividade específica como 1ª opcão
#exibir_quem_escolheu_primeira_atividade(latividades,lparticipantes,"Workshop de Python")
#exibir_quem_escolheu_primeira_atividade(latividades,lparticipantes,"Sessão de Networking")
exibir_quem_escolheu_primeira_atividade(latividades, lparticipantes, "Workshop de Python")
exibir_quem_escolheu_primeira_atividade(latividades, lparticipantes, "Sessão de Networking")