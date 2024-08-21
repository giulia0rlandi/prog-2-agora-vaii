"""
Spyder Editor

This is a temporary script file.
"""

'''
1)Faça a função divisaoInteira, que recebe dois valores 
   (o dividendo e odivisor). Esta função retorna:
• uma tupla com o quociente e o resto, se a operação for possível;
• uma tupla vazia quando o resultado é indeterminado ou
• None: quando a divisão é impossível

   
2a) Faça uma função que receba uma string e retorne uma tupla com dois
    elementos: o maior valor e qtas ocorrências desse valor
   OBS: Uma função retorna  APENAS um valor: para retornar 2 valores 
        deve-se retornar UMA tupla com 2 elementos
   No Bloco Principal a ativação pode ser:
    --> tResp = maiorqtos(string) => tResp referencia o objeto TUPLA criado na função
    -->(maior,qtd)=  maiorqtos("baboseirasssss")=> tupla de variáveis, cada cariável recebe um dos valores'''

def receba(s):
    maior = max(s)
    qtd = s.count(maior)
    t = (maior,qtd)
    return t

s = 'giulia'
 
'''2b) Escreva a função minmax() que recebe uma lista de números inteiros e
   retorna uma tupla com 
   ((menor valor da lista , nº de ocorrências deste valor), 
    (maior valor da lista, nº de ocorrências deste valor))
   Construa um programa para testar sua função, exibindo o(s) valor(es).'''
   
def minmax(l):
    maior = max(l)
    menor = min(l)
    qtdmaior = l.count(maior)
    qtdmenor = l.count(menor)
    t = ((menor,qtdmenor),(maior,qtdmaior))
    return t
l = [1,2,3,4,4,3,2,1,1,2,3,4,5,6,6,6,6,4,3,2,1]        

'''3) Escreva a função reajusta que receba como parâmetros:
    -o mínimo e máximo: dois valores decimais,
    -preço: um valor decimal representando o preço de uma mercadoria
    -taxa: um valor decimal entre 0 e 1 indicando porcentagem de aumento para 
     preços que estiverem dentro da faixa [mínimo,máximo](inclusive)
     
     Caso o preço esteja dentro da faixa indicada, ele deve ser reajustado 
     conforme a taxa de ajuste. A função deve retornar:
         (valor antigo, valor novo) caso tenha sido feito um ajuste, ou
         (valor antigo) caso contrário.
 
    Atenção: a tupla de retorno pode ter 1 ou 2 valores
    Construa um programa para testar sua função, exibindo o(s) valor(es).''' 

def reajusta(mi,ma,p,tx):
    if p >= mi and p <= ma:
        reajuste = p*(tx+1)
        return (p,reajuste)
    else:
        return (p,)
    
t= reajusta(10,20,15,1)
if len(t) == 2:
    print(f'Preço = {t[0]}, Reajuste = {t[1]}')
else:
    print('Preço = {t[0]}')

'''4)
Uma conta a pagar é representada como uma tupla de 3 elementos:
    (descrição, valor, dtPagto),
onde dtPagto é uma string no formato dd/mm'''

# 4)
# Uma conta a pagar é representada como uma tupla de 3 elementos:
#     (descrição, valor, dtPagto),
# onde dtPagto é uma string no formato dd/mm

# 4A) Escreva uma funcao denominada exibeContas 
#     para mostrar na tela,
#     um por linha, os dados de cada conta de uma 
#    tupla de contas a
#     pagar recebida (tupla de tuplas).
def exibeContas(tupla_de_tuplas):
  for (descricao, valor, dtPagto) in tupla_de_tuplas:     
      print(f" conta: {descricao} --> R$ {valor} em {dtPagto}")

# 4B) Escreva uma funcao denominada 
#     valorMedioContas que recebe 
#     uma tupla de contas a pagar (tupla de tuplas) e 
#     retorna o valor
#     médio das contas
def valorMedioContas(tupla_de_tuplas):
    soma=0
    for (descricao, valor, dtPagto) in tupla_de_tuplas:     
        soma+=valor
    return soma/len(tupla_de_tuplas)

# 4C) Escreva uma funcao denominada 
 #    eixbeContasMaisCarasQueValorMedio
#     que recebe uma tupla de contas a pagar (tupla de tuplas) e 
#     exibe o valor médio das contas e todas
#     as contas a pagar
#     cujo valor é superior ao  valor médio
#     Esta função deve ativar a função 4B
def exibeContasMaisCarasQueValorMedio(tupla_de_tuplas):
    media=valorMedioContas(tupla_de_tuplas)
    for (descricao, valor, dtPagto) in tupla_de_tuplas:     
        if valor > media:
            print(f" conta: {descricao} --> R$ {valor} em {dtPagto}")
    
# 4D)Escreva uma funcao denominada 
#    contasMaisCarasQueValorMedio
#     que recebe uma tupla de contas a pagar (tupla de tuplas que representam 
#     as contas a pagar) e 
#     retorna uma tupla com dois valores: 
#         (o valor médio das contas, 
#           tupla de contas com valor > valor médio)
#     Esta função deve ativar a função 4B
def contasMaisCarasQueValorMedio(tupla_de_tuplas):
    media=valorMedioContas(tupla_de_tuplas)
    l=[]
    for t in tupla_de_tuplas:     
        if t[1] > media:
            l.append(t)
    return (media, tuple(l))

# 4E) Escreva uma funcao denominada contasDaData que 
#     receba uma tupla
#     de contas a pagar e uma data, 
#     e exibe as contas a pagar nessa data
def contasDaData(tupla_de_tuplas,dt):
   
    for (descricao, valor, dtPagto) in tupla_de_tuplas:     
        if dtPagto == dt:
            print(f" conta: {descricao} --> R$ {valor} em {dtPagto}")
 
    
# 4F) Escreva uma funcao denominada 
#    exibeDescrValor que receba uma
#     tupla de contas a pagar, 
#     um mês inicial  e um mês final, e  
#     retorne 
#     uma tupla com as contas 
#     (tuplas que representam as contas a pagar) 
#     a serem pagas nesse intervalo (extremos inclusos).
#
def exibeDescrValor(tupla_de_tuplas,mesI,mesF):
    for (descricao, valor, dtPagto) in tupla_de_tuplas:     
        mesdtPagto=dtPagto.split('/')[1] #dtPagto[3:5]
        if mesdtPagto>= mesI and mesdtPagto<=mesF:
            print(f" conta: {descricao} --> R$ {valor} em {dtPagto}")
   


'''5)  Desenvolva a função raízes, que calcula e retorna as raízes x1 e x2 de uma
    equação do segundo grau, do tipo ax**2+ bx + c = 0.
    a, b e c representam os coeficientes da equação.
    Observações:
    a) Se as raízes forem reais e distintas, a função deve retornar os dois
        valores e x1 deve ser associado ao menor valor e x2 ao maior valor.
    b) Se as raízes forem reais e iguais, a função deve retornar apenas um valor
    c) Se não existirem raízes reais, a função deve retornar None.
    Faça um programa completo que pergunte um número indeterminado de
    coeficientes a, b e c ao usuário 
    (o programa deverá terminar quando o valor do coeficiente de a for zero) e, 
    para cada grupo de coeficientes, chame afunção raízes e as exiba, 
    caso elas sejam reais, ou a mensagem RaízesImaginárias, 
    caso elas sejam imaginárias.

6) Baseado em questão de profa Joisa
a) Escreva a funcao menorPrecoDeUmProduto que recebe uma tupla de 4 elementos 
com as seguintes informacoes de um produto: nome e os preços de 3 avaliacoes em
diferentes lojas e retorna uma nova tupla de 2 elementos com nome e menor preco
desse produto
'''



'''
b) Escreva uma funcao denominada menorPrecoDeCadaProdutoDeUmaCestaBasica que:
- receba uma tupla de  tuplinhas de 4 elementos, em que cada tuplinha possui 
 as seguintes informacoes  de um produto da cesta basica: nome e os preços de 3 avaliacoes
- retorne uma nova tupla de tuplinhas de 2 elementos, em que cada tuplinha 
tenha as seguintes informações de um produto: nome e seu menor preco. Para isso 
deve ser usada a funcao do item a
'''


'''
c) Escreva a funcao procCestaBasica que recebe uma tupla de tuplinhas de 2 elementos, 
em que cada tuplinha possui  as seguintes informações de um produto: nome e seu 
menor preco . A funcao retorna uma tupla com a  preco medio dos produtos e preço  
total da cesta basica
'''


'''
d) Escreva a funcao produtosAcimaDoPrecoMedio que recebe uma tupla de tuplinhas de 
2 elementos (nome e menor preco de cada produto) e retorna uma nova tupla apenas 
com as tuplinhas dos produtos com menor preco maior do que o preco medio dos 
produtos da cesta.
Deve ser utilizada a funcao do item c
'''
 

'''
e) Escreva um programa completo para testar suas funcoes acima. Considere 
a seguinte tupla correspondente a uma cesta básica, em que cada elemento (uma tupla 
de 4 elementos) contem os dados de um produto da cesta.
Ao final seu programa deve exibir nome e menor preco dos produtos que estão
acima do preco mínimo medio dos produtos da cesta
'''

# # Teste da funcao a) menorPrecoDeUmProduto:

# produto = ("Arroz", 7.5, 8.4, 9.6)
# resposta1= menorPrecoDeUmProduto(produto)
# print(resposta1)


# # Outra forma de receber a resposta retornada:
# (nome,prMinProd)=  menorPrecoDeUmProduto(produto)
# print(nome, '-',prMinProd )



# Para testar as demais funcoes
tCestaBasica=( ("Arroz", 7.5, 8.4, 9.6), ("Feijao", 5.6, 5.1, 4.9), ("Leite", 5.3, 6.3, 9.9),
         ("Cafe", 17.5, 18.4, 19.6), ("Macarrao", 4.4, 5.1, 3.7), ("Oleo", 7.7, 8.3, 6.5))

# b) contsrução da tupla ((prod,prMinProd),...(prod,prMinProd))

# tPrProdsCB=menorPrecoDeCadaProdutoDeUmaCestaBasica(tCestaBasica)

# c) pr medio dos produtos e total  preco medio da cesta basica
#(prMedio,totalCB)=procCestaBasica(tPrProdsCB)
#print("Preco medio dos produtos da CB: R$ %.2f - Total cesta basica: R$ %.2f"%(prMedio,totalCB)

# d) produtos da cesta basica com preco mínimo superior  ao preco medio dos produtos da CB
#resposta3=produtosAcimaDoPrecoMedio(tPrProdsCB,prMedio)
