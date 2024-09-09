# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 08:07:13 2024

@author: Ferlin
"""
'''
Enunciado do Problema: 
    Gerenciamento de Contas de Usuários
Você foi contratado para desenvolver parte de um sistema de gerenciamento de 
contas de usuários para uma plataforma de aprendizado online. 
Nesta plataforma, cada usuário tem 
    um nome de usuário e uma senha. 
Os usuários podem 
    ativar e desativar suas contas, 
    além de atualizar suas senhas quando necessário.
    se exibir
'''
from classeContaUsuario import ContaUsuario

# A classe precisa atender aos seguintes requisitos:
# 1.	Criação de contas de usuário:
    # Ao criar uma nova conta, o usuário deve 
    # fornecer um nome de usuário e uma senha. 
    # a conta quando criada deve estar inativa.
# 2.	Ativação e desativação de contas: O usuário deve ser capaz de ativar ou desativar sua conta a qualquer momento. Contas desativadas não podem acessar os serviços da plataforma.
# 3.	Atualização de senha: O usuário deve poder alterar sua senha sempre que desejar.
# 4.	Exibição de detalhes da conta: A plataforma deve exibir as seguintes informações sobre uma conta de usuário: o nome de usuário e o status da conta (ativa ou inativa).
# 5.	Comparação entre contas: O sistema deve ser capaz de comparar duas contas de usuário para verificar se elas têm o mesmo nome de usuário e senha.
# 6.	Verificação de força da senha: O sistema deve permitir que o administrador verifique a força da senha de um usuário, retornando o número de caracteres da senha.

# Tarefas:
# 1.	Crie uma classe chamada ContaUsuario 
#       que atenda a todos os requisitos acima.
# 2.	A classe deve conter:
# o	Um método para ativar e outro para desativar a conta.
# o	Um método para atualizar a senha.
# o	Um método para exibir os detalhes da conta, como nome de usuário e status.
# o	Um método mágico __str__() para exibir as informações da conta em formato amigável ao usuário.
# o	Um método mágico __repr__() para representar a conta de forma mais detalhada, útil para depuração.

# o	Um método mágico __eq__() para comparar se duas contas têm o mesmo nome de usuário e senha.
# o	Um método mágico __len__() que retorne o comprimento da senha do usuário.

# 3.	Teste sua classe:
# o	Crie três contas de usuário com diferentes combinações de nomes de usuário e senhas.
# o	Ative e desative contas e atualize senhas conforme necessário.
# o	Compare duas contas para verificar se elas são iguais.
# o	Use o método len() para verificar o tamanho da senha de um dos usuários.
# Exemplo de Teste:
# •	Crie uma conta com o nome de usuário "joao_silva" e a senha "senha123". Exiba os detalhes da conta.
# •	Ative a conta de "joao_silva" e atualize sua senha para "nova_senha456". Exiba os detalhes novamente.
# •	Crie outra conta com o nome de usuário "maria_oliveira" e senha "senha456". Compare com a conta de "joao_silva".
# •	Verifique o comprimento da nova senha de "joao_silva".
# Requisitos Extras (Opcional):
# •	Adicione uma validação para garantir que a senha tenha no mínimo 6 caracteres.
# •	Implemente um método que retorne uma mensagem se a senha do usuário é considerada fraca, moderada ou forte, baseado no número de caracteres.




c1 = ContaUsuario('bolota','bol333')
print(c1)

c2 = ContaUsuario('bolota','bol333')
print(c1)        
print(c2)         
        
c1.alteraStatus()
print(c1)  
