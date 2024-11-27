# -*- coding: utf-8 -*-
#
# Ejercicio 1
# Generador de Arboles usando combinaciones de dados
# Por Gabriel Rodríguez
# CI 30172571
#
#


dado = []
final = []
nuevo = []
def combinaciones(act, n):
	for val in dado:
		print(val, end="-")
		nuevo.append(val)
		if act < n:
			combinaciones(act+1, n)
		else:
			final.append(list(nuevo))
			print(nuevo)
		if val != dado[len(dado) - 1]:
			for i in range(act-1):
				print("  ", end="")
		nuevo.pop()
def combinacionesDif(ite, n):
	for val in dados[ite-1]:
		print(val, end="-")
		nuevo.append(val)
		if ite < n:
			combinacionesDif(ite+1, n)
		else:
			final.append(list(nuevo))
			print(nuevo)
		dadoAct = dados[ite-1]
		if val != dadoAct[len(dadoAct) - 1]:
			for i in range(ite-1):
				print("  ", end="")
		nuevo.pop()
print("Indique usando el numero especificado si los dados son unicos:\n[1] Cada dado tiene la misma cantidad de caras \n[2] Cada dado tiene una cantidad especifica de caras")
tipoEntrada = input()
print("Indique la cantidad de dados")
cantidad = input()
if int(tipoEntrada) == 1:
	print("Indique el número de caras que tienen los dados")
	caras_dado = input()
	for i in range(int(caras_dado)):
		dado.append(i+1)
	combinaciones(1,int(cantidad))
else:
	caras_dado = []
	dados = []
	for j in range(int(cantidad)):
		print("Cuantas caras tiene el dado",j+1,":")
		caras_dado.append(int(input()))
		temp = []
		for k in range(caras_dado[j]):
			temp.append(k+1)
		dados.append(temp)
	combinacionesDif(1,int(cantidad))
print("Total de combinaciones:", len(final))
print("Universo:",final)