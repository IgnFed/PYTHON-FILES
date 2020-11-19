lista1=[]
i=0
while i<5:
    
    lista= int(input())
    i=i+1
    lista1.append(lista)

lista1.sort()
print(lista1)

print("Lista revertdia ", lista1)
for posicion in range(1, len(lista1)):
     if lista1(posicion)<lista1(posicion+1):
        print("este elemento esta raro")
