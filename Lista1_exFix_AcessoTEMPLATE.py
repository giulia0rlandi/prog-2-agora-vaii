# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:39:27 2024

@author: Ferlin
"""
# Função que recebe uma cidade e informa a região




###################################################
#BP
# Dicionário que mapeia cidades para seus respectivos estados
cidade_para_estado = {
    "São Paulo": "SP",
    "Rio de Janeiro": "RJ",
    "Belo Horizonte": "MG",
    "Salvador": "BA",
    "Curitiba": "PR",
    "Porto Alegre": "RS",
    "Recife": "PE",
    "Manaus": "AM",
    "Florianópolis":"SC"
}

# Dicionário que mapeia estados para suas respectivas regiões
estado_para_regiao = {
    "SP": "Sudeste",
    "RJ": "Sudeste",
    "MG": "Sudeste",
    "BA": "Nordeste",
    "PR": "Sul",
    "RS": "Sul",
    "PE": "Nordeste",
    "AM": "Norte"
}


# Teste: Informar a região para algumas cidades
informar_regiao_por_cidade("Rio de Janeiro")
informar_regiao_por_cidade("Florianópolis")
informar_regiao_por_cidade("Campo Grande")
