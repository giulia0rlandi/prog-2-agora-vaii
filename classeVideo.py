# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:44:54 2021

@author: Ferlin
"""
'''
Classe Video:
    atributos: 
        nome: string  
        tema: string
        ano: inteiro
        duracao: inteiro (expresso em segundos)
        qtLike:0
        qtUnlike:0
        
        
               
Para criá-la é obrigatório fornecer o nome e duracao. 
O tema tem como valor default, 'Python' e o ano, 2020. 
Os atributos qtlike e qtUnlike são criados com 0, 
na construção do objeto

Ao dar print em um video deve ser exibido:
Video  nome  é sobre tema. Foi criado em ano e tem duração de hh:mm:ss h
likes: qtLike  unlikes: unlike
           
Métodos:
	
. Construtor (__init__)	 este método recebe os valores e 
                         cria um objeto .
                         Valores default conforme descrito acima
. Apresentação (__str__ e __repr__)	 retorna uma string com os 
                                    valores dos atributos 
                                    no formato especificado acima
                                     
. Getters e Setters:
    getNome, getTema, getAno, getDuracao, getLike, getUnLike: 
        retorna o valor equivalente
    setNome, setTema, setAno,setDuracao: 
        recebe um valor e altera o atributo equivalente

. dar_like: aumenta qtLike em 1 
. dar_unlike: aumenta qtUnlike em 1    


Métodos especiais:  

ARITMETICOS:

+   recebe  como parâmetro um outro objeto da classe Video e constroi um
    novo objeto da classe Video onde:
        nome: concatenação dos nomes --> 
                nome do obj1 + '&' + nome do obj2 
        tema: concatenação dos nomes --> 
                nome do obj1 + '&'  + nome do obj2 
        duracao: soma das durações
        ano: maior ano entre os obj
*   recebe  como parâmetro um número inteiro n e constroi um
    novo objeto da classe Video onde:
        nome: nome do obj + ' replicado '  
        duracao: n * duracao
        demais atributos: iguais aos do objeto 

ATRIBUIÇÃO

+=  recebe  como parâmetro um outro objeto da classe Video e   
            retorna o objeto alterado onde:
        nome: concatenação dos nomes --> 
            nome do obj1 + '#' + nome do obj2 
        tema: concatenação dos temas --> 
            nome do obj1 + '#'  + nome do obj2 
        duracao: soma das durações
        ano: maior ano entre os obj
        
COMPARAÇÃO                         	
==	recebe  como parâmetro um outro objeto da classe Video e 
    retorna True  se tiver os mesmos valores de atributo e False caso contrário.
!=	recebe  como parâmetro um outro objeto da classe Video e 
    retorna False  se tiver os mesmos valores e True caso contrário.
>	recebe  como parâmetro um outro objeto da classe Video e 
    retorna True se tem maior duracao, False cc. 
<=	recebe  como parâmetro um outro objeto da Classe Video e 
    retorna True se tiver duração menor ou igual ao do outro e False, caso contrário


'''        
