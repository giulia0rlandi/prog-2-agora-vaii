
'''
1) Tarefa obter pontos
        Perguntar coordenadas dos pontos ao usuário
        Não pode ser função pq precisa retornar mais de um valor

2) Tarefa calcular perímetro  (função)
        E: ptos A,B,C
        S: perímetro
        Proc: 
            somar calc dist AB, calc dist AC, calc dist BC
        
3)Tarefa exibir perímetro: (função)
        E: perímetro
        S: nada
        Proc: 
            mostrar (exibir no monitor) moldura,perímero,moldura

Funçoes auxilares para execução das tarefas
A) calcula distância entre dois pontos
        E: pto1, pto2
        S: distãncia
        Proc: 
            fórmula da distância euclidiana

B) exibir moldura
        E: qtdade e símbolo
        S: nada
        Proc: 
            exibir qtdade vezes do símbolo no monitor
        
C) Tarefa verificar se 3 pontos são colinares 
        E: ptos A,B,C
        S: True/False
            -->Teste de  Colinear: ​   DP – DS == 0​
                DP = xA*yB  +  yA*xC  +  xB*yC​
                DS = yA*xB  +  xA*yC  +  yB*xC
    
'''
def calcDistancia(x1,y1,x2,y2):
    d = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return d
    
def calcPerim(xA,yA,xB,yB,xC,yC):
    l1 = calcDistancia(xA, yA, xB, yB)
    l2 = calcDistancia(xA, yA, xC, yC)
    l3 = calcDistancia(xB, yB, xC, yC)
    p = l1 + l2 + l3
    return p
    
    
def moldura(qtd,simb):
    m = qtd*simb
    print(m)
    print(m)
    
def exibeRes(perim):
    


def saoColineares(xA,yA,xB,yB,xC,yC): 
        
# #BP

