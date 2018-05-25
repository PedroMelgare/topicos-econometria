"""
Programa multa.py
Descrição: Entrada, processamento e saída de dados em Python
Autor: Pedro de Bitencourt Melgare
Data: 18/05/2018
Versão: 0.0.1
"""
#Entrada de dados
v = float(input("Insira a velocidade, em km/h:"))

#Processamento
if v > 80:
	multa = 5*(v-80)
	print("Você foi multado em R$", multa)


