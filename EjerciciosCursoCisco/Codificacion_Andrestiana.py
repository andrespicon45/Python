#Pedimos una linea de codigo a encriptar
texto=input('Ingresa el mensaje clave:')
#Pedimos el nunmero de espacios que se van a desplazar dentro del metodo de encriptacion
while True:
    desplazamientos=input('Ingrese el numero de desplazamiento que desea aplicar (1-24):')
    try:
        desplazamientos=int(desplazamientos)
    except ValueError:
        print('No es un caracter valido')
    if desplazamientos not in range(1,25):
        print('Debes ingresar un numero dentro del rango valido.')
    else:
        break
#Creamos el algoritmo de codificacion
#comenzamos iterando palabra a palabra
#Creamos una lista vacia donde se insetan letra a letra, y una variable que contiene el argumento
lista_encriptada=[]
argumento=''
for caracter in texto:
    #Si el caracter corresponde a un espacio vacio, se agrega a la lista directamente
    if caracter.isspace():
        argumento=caracter
    #Si no es alfanumero lo agregamos directamente
    elif not caracter.isalnum():
        argumento=caracter
    #Si es minuscula lo tratamos con el siguiente fragmento
    elif caracter.islower():
        #Creamos una variable auxiliar para obtener el valor punto codigo del caracter
        aux_caracter=ord(caracter)
        caracter_desplazado=aux_caracter+desplazamientos
        if caracter_desplazado<122:
            argumento=chr(caracter_desplazado)
        else:
            argumento=chr(caracter_desplazado-25)
        #Si no es minuscula, es mayuscula
    else:
        aux_caracter=ord(caracter)
        caracter_desplazado=aux_caracter+desplazamientos
        if caracter_desplazado<90:
            argumento=chr(caracter_desplazado)
        else:
            argumento=chr(caracter_desplazado-25)
    #Agregamos el valor del argumento a la lista
    lista_encriptada.append(argumento)
print(''.join(lista_encriptada))