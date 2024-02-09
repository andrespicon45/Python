palabra=input('Ingrese la palabra a buscar:')
cadena=input('Ingrese la cadena de busqueda:')
posicion=0
buscar=True
for caracter in palabra:
    posicion=cadena.find(caracter,posicion)
    if posicion<0:
        buscar=False
        break
    posicion+=1
if buscar==False:
    print('No se encuentra.')
else:
    print('Se encuentra.')
