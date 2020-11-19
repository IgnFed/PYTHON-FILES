Pan=3.49
descuento=0.6

Pan_Ayer=int(input("Ingrese la cantidad de barras viejas de pan vendidas: "))

Total=Pan*Pan_Ayer*(1-descuento)
print("El precio del pan es: ", Pan, "euros ,más descuento de ", descuento*100, " % ")
print("El precio total es: ", round(Total, 2), " euros")
