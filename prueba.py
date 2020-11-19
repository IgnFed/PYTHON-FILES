
V=[2,3]
W=[5,6]
A=[]
for i in range(len(V)):
    
    print(V[i],"*",W[i])
    valor1=V[i]
    valor2=W[i]
    multiplicacion=valor1*valor2
    print(multiplicacion)
    A.append(multiplicacion)

  
print(A)