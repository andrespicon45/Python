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
Creamos las condiciones de victoria, derrota y empate
'''

def si_win(lista):

    win=((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(7,5,3))

    for i in win:
        if lista[i[0]-1]=='X' and lista[i[1]-1]=='X' and lista[i[2]-1]=="X":
            print('FELICIDADES!!! Haz vencido a la maquina.')
            return True
        elif lista[i[0]-1]=='O' and lista[i[1]-1]=='O' and lista[i[2]-1]=="O":
            print('Haz sido derrotado por SKYNET :(')
            return True
        else:
            return False

'''
Creamos la comprobacion de si el movimiento ingresado es valido.
'''

def mov_val(mov,lista):

    if mov not in lista:
        return False #Movimiento no valido.
    else:
        return True #Movimiento valido

'''
Creamos la comprobacion de si el juego queda en empate(no hay mas movimientos).
'''
def empate(lista):
    contar=0
    for i in range(1,10):
        if i not in lista:
            continue
        else:
            contar+=1
    if contar==0: 
        return True #No hay movimientos posibles, ES UN EMPATE!!!

'''
Creamos una lista por defecto donde se almacenan las selecciones realizadas
'''

lista=[1,2,3,4,5,6,7,8,9]

'''
Creamos el algoritmo del juego
'''
print('Bienvenido a TicTacToe!!!')
asignacion_val(lista)

while True:
    while True:
        u=sel_usuario() #Usuario elije un movimiento
        if mov_val(u,lista)==False: #Se comprueba si se puede realizar el movimiento
            print('Movimiento invalido, ingresa otro movimiento:')
            continue #Continua el bucle de ingresar un valor por el usuario
        else:
            break #Salgo de este minibucle

    lista[u-1]='X' #Se asigna el valor del usuario a la lista
    asignacion_val(lista)

    if si_win(lista)==True: 
        break #Si gana o pierde, acaba el juego

    if empate(lista)==True: 
        print('No hay movimientos posibles, ES UN EMPATE!!!')
        break
    
    print('Es el turno de la maquina.')

    while True:
        u=sel_maq() #Maquina elije un movimiento
        if mov_val(u,lista)==False: #Se comprueba si se puede realizar el movimiento
            continue #Continua el bucle de ingresar un valor por la maquina
        else:
            break #Salgo de este minibucle
    
    lista[u-1]='O' #Se asigna el valor del usuario a la lista
    asignacion_val(lista)
    print(si_win(lista))
    if si_win(lista)==True: 
        break #Si gana o pierde, acaba el juego

    if empate(lista)==True: 
        print('No hay movimientos posibles, ES UN EMPATE!!!')
        break