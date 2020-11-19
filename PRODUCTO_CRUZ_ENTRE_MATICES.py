#MULTIPLICACIÓN ENTRE DOS VECTORES
import os as cln
import time as clock

n=int(input("Marque cuantos elementos tendran los vectores: "))
V=[]
W=[]
cln.system("cls")

print(f"{' '*35} {'--'*5} Empezando con la Vector V {'--'*5}  ")

cln.system("cls")

for z in range(0,n):
    print(f" Para el vector V Ingrese el valor {z+1} ")
    listV=input()
    V.append(listV)
    cln.system("cls")

print(f" {' '*35} {'--'*5} Cambiando a la Vector W {'--'*5}  "); clock.sleep(2)
cln.system("cls")

for x in range(0,n):
    print(f" Para el vector W Ingrese el valor {x+1} ")
    listW=input()
    W.append(listW)
    cln.system("cls")

A=[]


for i in range(0,n):
    
    print("La multiplicación: " ,V[i],"*",W[i], end="\t")
    value1=V[i]
    value2=W[i]
    multiplication=int(value1)*int(value2)
    print("   Es igual a:   ", multiplication)
    A.append(multiplication)
    print()

input("Press Enter to view the result")

cln.system("cls")

print("La matriz es :  ", A)
