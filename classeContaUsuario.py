# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 07:34:40 2024

@author: PC-PROF
"""

class ContaUsuario:
    def __init__(self,login,senha='123'):   # como construir um obj desta classe
        self.login=login
        self.senha=senha
        self.ativa=False
        
    def __str__(self):
        if self.ativa:
            resp='sim'
        else:
            resp='não'
        return f"Login:{self.login} Ativa?{resp}"
    
    def __repr__(self):
        return f"Login:{self.login} Ativa?{self.ativa}"
    
    def alteraStatus(self):
        self.ativa=not self.ativa
        
    def alteraSenha(self,novasenha):
        self.senha=novasenha