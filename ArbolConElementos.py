# -*- coding: utf-8 -*-
#
# Ejercicio 1
# Generador de Arboles usando combinaciones de elementos especificos
# Por Gabriel Rodríguez
# CI 30172571
#
#


conjuntos = []
final = []
nuevo = []
def combinacionesStr(ite, n):
	for val in conjuntos[ite-1]:
		print(val, end=" - ")
		nuevo.append(val)
		if ite < n:
			combinacionesStr(ite+1, n)
		else:
			final.append(list(nuevo))
			print(nuevo)
		conjuntoAct = conjuntos[ite-1]
		if val != conjuntoAct[len(conjuntoAct) - 1]:
			for i in range(ite-1):
				print("    ", end="")
		nuevo.pop()
print("Indique la cantidad de conjuntos")
cantidad = input()
cantidadesPorConjunto = []
nombres = []
for j in range(int(cantidad)):
        print("Especifique el nombre del conjunto #",j+1,":")
        nombres.append(input())
        print("Cuantos elementos tiene el conjunto #",j+1,":")
        cantidadesPorConjunto.append(int(input()))
        temp = []
        for k in range(cantidadesPorConjunto[j]):
                print("Especifique el nombre del elemento #",k+1," del conjunto ",nombres[j],":")
                temp.append(input())
        conjuntos.append(temp)
combinacionesStr(1,int(cantidad))
print("Total de combinaciones:", len(final))
print("Universo:",final)
