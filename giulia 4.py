# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:17:11 2024

@author: Ferlin
"""
"""
1) Combinando/Invertendo tuplas
Considere
a) uma tupla de tuplas representando animais e 
b) outra tupla de tuplas representando os tipos de locais onde esses animais residem. 
Estas tuplas estão na mesma ordem e todos os animais tem local de residência
O objetivo é combinar as duas tuplas para associar cada animal ao seu respectivo habitat.


1a) construa a  função combinar_animais_locais que combina as informações em uma
 nova tupla de tuplas. Cada nova tupla contém o nome do animal, a característica 
 e o habitat."""

def busca(l,val):
    for pos, val in enumerate(l):
        if val[0] == val:
            return pos
    return

    
def combinar_animais_locais(tanimais,tlocais):
    l = []
    for (pos,(animal,carac) )in enumerate(tanimais):
        # busca o local deste anima em tlocais     --> é o mesmo do animal   
        local = tlocais[pos][1]
        l.append((animal,carac,local))
    return tuple(l)
        
            
""" 1b) construa a função exibir_animais_com_locais que exibe cada animal com sua 
    característica e o tipo de local onde ele vive, formatado de maneira legível.
    
Saída esperada para o exemplo:
    Leão (Carnívoro) vive em Savana
    Elefante (Herbívoro) vive em Floresta
    Tubarão (Carnívoro) vive em Oceano
    Pinguim (Carnívoro) vive em Antártida
    Girafa (Herbívoro) vive em Savana
    
1c) construa uma tupla de tuplinhas onde cada tuplinha possui: 
    (característica, lista e animais com esta característica)
   tupla resultante:
       (("Carnívoro",["Leão","Tubarão","Pinguim"]),
        ("Herbívoro",["Elefante","Girafa"]))
"""

# tupla de animais
tanimais = (
    ("Leão", "Carnívoro"),
    ("Elefante", "Herbívoro"),
    ("Tubarão", "Carnívoro"),
    ("Pinguim", "Carnívoro"),
    ("Girafa", "Herbívoro"),
)


# tupla de locais
tlocais = (
    ("Leão", "Savana"),
    ("Elefante", "Floresta"),
    ("Tubarão", "Oceano"),
    ("Pinguim", "Antártida"),
    ("Girafa", "Savana"),
)


# Executando o programa
# tanimais_com_locais = combinar_animais_locais(tanimais, tlocais)
# exibir_animais_com_locais(tanimais_com_locais)
# print(agrupar_animais_com_mesmacaracteristica(tanimais))

################################################################################
"""
2 -Considere uma tupla de eventos que ocorreram em diferentes cidades. 
Cada evento é representado por uma tupla contendo o nome da cidade, 
o nome do evento e o ano em que o evento ocorreu. 
Seu objetivo é constrir uma função que agrupe os eventos por cidade, 
de modo que cada cidade tenha uma lista de todos os eventos (evento,ano) que 
ocorreram nela.
tupla gerada para o exemplo
(('São Paulo',[('Carnaval', 2022),('Fórmula 1', 2021),('Bienal do Livro', 2023),('Fórmula 1', 2022)]),
 ('Rio de Janeiro',[('Rock in Rio', 2022), ('Carnaval', 2023), ('Festa de Ano Novo', 2022)]),
 ('Salvador', [('Carnaval', 2023), ('Festival de Verão', 2022)]))
"""
eventos = (
    ("São Paulo", "Carnaval", 2022),
    ("Rio de Janeiro", "Rock in Rio", 2022),
    ("São Paulo", "Fórmula 1", 2021),
    ("Salvador", "Carnaval", 2023),
    ("São Paulo", "Bienal do Livro", 2023),
    ("Rio de Janeiro", "Carnaval", 2023),
    ("Salvador", "Festival de Verão", 2022),
    ("São Paulo", "Fórmula 1", 2022),
    ("Rio de Janeiro", "Festa de Ano Novo", 2022),
)

# Função para agrupar eventos por cidade


# Função para exibir os eventos agrupados por cidade



# Executando o programa
# 




# tupla de eventos
eventos = (
    ("São Paulo", "Carnaval", 2022),
    ("Rio de Janeiro", "Rock in Rio", 2022),
    ("São Paulo", "Fórmula 1", 2021),
    ("Salvador", "Carnaval", 2023),
    ("São Paulo", "Bienal do Livro", 2023),
    ("Rio de Janeiro", "Carnaval", 2023),
    ("Salvador", "Festival de Verão", 2022),
    ("São Paulo", "Fórmula 1", 2022),
    ("Rio de Janeiro", "Festa de Ano Novo", 2022),
)

# Executando o programa
# eventos_agrupados = agrupar_eventos(eventos)
# exibir_eventos_agrupados(eventos_agrupados)


################################################################################
"""
Considere uma série de compras realizadas em uma loja online. 
Cada compra é representada por uma tupla que contém 
o nome do cliente, o nome do produto e a quantidade comprada.
Construa um programa que crie uma lista que mostre, para cada cliente, 
quantas vezes ele comprou cada produto, 
# Lista de compras
compras = [
    ("João", "Livro", 1),
    ("Maria", "Caneta", 2),
    ("João", "Livro", 1),
    ("Maria", "Livro", 1),
    ("João", "Caderno", 3),
    ("Maria", "Livro", 2),
    ("Pedro", "Livro", 1),
    ("Pedro", "Caderno", 4),
    ("João", "Caderno", 1),
]
Saída esperada
( (("João", "Livro"),2)
 (("Maria", "Caneta"), 2),
 (("João", "Caderno"),4),
 (("Maria", "Livro"), 3),
 (("Pedro", "Livro"), 1),
 (("Pedro", "Caderno"), 4))

"""