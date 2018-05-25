"""
Programa soma3.py
Descrição: Entrada, processamento e saída de dados em Python
Autor: Pedro de Bitencourt Melgare
Data: 18/05/2018
Versão: 0.0.1
"""
#Definição de funções
def soma(x,y):
	soma=x+y
	return(soma)
	
	

#Entrada de dados
a = float(input('Digite o primeiro numero'))

b = float(input('Digite o segundo numero'))

#Processamento

z = soma(a,b)

#Saída

print("A soma de seus números é:", z)
