
strng='Ser o no ser, esa es la cuestión'
#Cambiamos dos palabras "esa" y "la"
strng.replace("esa","eso").
strngreplace('la','el').replace('cuestión','pregunta')
#Separamos la cadena en una lista
lista_cadena=strng.split()
#Iteramos por cada una de las cadenas contenidas en la lista
for i in lista_cadena:
    #Creamos un contador para controlar la posicion en la que estamos en la lista
    count=+1
    #Convertimos todo a minuscula
    i.lower()
    #Comprobamos si comienza con la palabra "ser"
    if i=="ser":
        lista_cadena.insert(count-1,"A")
        count+=1
strng=" ".join(lista_cadena).capitalize()
lista_cadena1=strng.split()
print(lista_cadena1)
