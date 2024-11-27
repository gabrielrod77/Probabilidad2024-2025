# -*- coding: utf-8 -*-
#
# Ejercicio 2
# Triangulo de Pascal
# Por Gabriel Rodríguez
# CI 30172571
# Probabilidad
#

fila_ant = [1]
fila_act = [1]

print("Cuantas filas(n) tendra el triangulo?")
n = input()
print()
for i in range(int(n)):
	fila_act = []
	if i+1 > 2:		
		for j in range(i+1):
			if j == 0 or j == i:
				print(1, end=" ")
				fila_act.append(1)
			else:
				print(fila_ant[j-1] + fila_ant[j], end=" ")
				fila_act.append(fila_ant[j-1] + fila_ant[j])
		fila_ant = list(fila_act)	
	else:
		for j in range(i+1):
			print(1, end=" ")
			fila_act.append(1)
		fila_ant = list(fila_act)
	print("")