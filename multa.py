#Entrada de dados
v = float(input("Insira a velocidade, em km/h:"))

#Processamento
if v > 80:
	multa = 5*(v-80)
	print("Você foi multado em R$", multa)


