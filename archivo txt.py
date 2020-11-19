
from io import open
archivo_texto=open("archivo.txt","w")
frase="Primer archivo externo \n jejejeje"
archivo_texto.write(frase)

archivo_texto.close()

