from Interfaz import interfaz as ifz
from random import randrange as random

"""
Creamos una funcion la cual ayude a asignar a la interfaz los valores guardados en la lista donde se
almacenan las selecciones
"""

def asignacion_val(lista):

    impresion=ifz(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8])

    return impresion

'''
Creamos una funcion que genere la seleccion de la maquina entre los numeros 1-9
'''

def sel_maq():
    return random(1,10)

'''
Creamos una funcion que reciba la seleccion del usuario
'''

def sel_usuario():

    while True:
        x=int(input('Ingrese la celda que desea:'))
        if x not in range(1,10):
            print('No es un valor valido.')
        else:
            break
    return x

'''
Creamos una lista por defecto donde se almacenan las selecciones realizadas
'''

lista=[1,2,3,4,5,6,7,8,9]

'''
Creamos las condiciones de victoria, derrota y empate
'''
p=[1,2,'O',4,'O',6,'O',8,9]
def resultado(lista):

    win=((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(7,5,3))

    for i in win:
        if lista[i[0]-1]=='X' and lista[i[1]-1]=='X' and lista[i[2]-1]=="X":
            print('FELICIDADES!!! Haz vencido a la maquina.')
            break
        elif lista[i[0]-1]=='O' and lista[i[1]-1]=='O' and lista[i[2]-1]=="O":
            print('Haz sido derrotado por SKYNET :(')

resultado(p)

'''
Creamos el algoritmo del juego
'''

#u=sel_usuario()

# for val in lista:
#     indice=lista.index(val)
#     if u==val:
#         lista[indice]="X"
#         print(lista)
#     else:
#         print('Elige otra casilla.')

