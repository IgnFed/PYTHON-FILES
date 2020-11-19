
#AGREGAR ELEMENTOS A VECTORES A TRAVÉS DE UNA FUNCIÓN


def element(n):
   
    global H
    global B
    H=[]
    B=[]
    for z in range(0,n):
        print(" Para el vector H Ingrese el valor", z)
        listH=input()
        H.append(listH)

    for x in range(0,n):
        print(" Para el vector B Ingrese el valor", x)
        listB=input()
        B.append(listB)
    return H,B
n=int(input("Valor:    "))

print(element(n))
V=H
W=B










#AGREGAR ELEMENTOS A VECTORES A TRAVÉS DE UNA FUNCIÓN

n=int(input("Marque cuantos elementos tendran los vectores: "))
V=[]
W=[]

for z in range(0,n):
    print(" Para el vector V Ingrese el valor", z)
    listV=input()
    V.append(listV)

for x in range(0,n):
    print(" Para el vector W Ingrese el valor", x)
    listW=input()
    W.append(listW)