#print('esta es una prueba para tratar de subir archivos a GitHub')
#print('conozcamos nuevas funciones en python')
#print('esta es una prueba realizada desde la obra')

lista=[1,2,3,4,5,6,7,8,9]

#x=int(input('un valor'))

lista[5]='X'
print(lista)
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
x=si_win(lista)
print(x)