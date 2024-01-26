
#Creamos una lista con los patrones de los numeros
graf_num=['1011111',    #0
          '0000101',    #1
          '1110110',    #2
          '1110101',    #3
          '0101101',    #4
          '1111001',    #5
          '1111011',    #6
          '1000101',    #7
          '1111111',    #8
          '1111101',    #9
         ]
#Pedimos el ingreso de un numero
numero=str(input('Ingrese un numero entero no negativo:'))
#Creamos una lista vacia con el numero de impresiones a realizar
lista_impresiones=[' ' for x in range(len(numero))]
#Leemos cada uno de los digitos contenidos en el numero y determinamos cual es
count=0
for i in numero:
    #Creamos una lista vacia que contenga un digito temporalmente
    num_temp=[[' ' for x in range(3)] for x in range(5)]
    digito=graf_num[int(i)]
    #Ahora iteramos en los valores del digito para dibujar el numero
    if digito[0]=='1':
        num_temp[0][0]=num_temp[0][1]=num_temp[0][2]='#'
    if digito[1]=='1':
        num_temp[2][0]=num_temp[2][1]=num_temp[2][2]='#'
    if digito[2]=='1':
        num_temp[4][0]=num_temp[4][1]=num_temp[4][2]='#'
    if digito[3]=='1':
        num_temp[0][0]=num_temp[1][0]=num_temp[2][0]='#'
    if digito[4]=='1':
        num_temp[0][2]=num_temp[1][2]=num_temp[2][2]='#'
    if digito[5]=='1':
        num_temp[2][0]=num_temp[3][0]=num_temp[4][0]='#'
    if digito[6]=='1':
        num_temp[2][2]=num_temp[3][2]=num_temp[4][2]='#'
    #Agregamos el numero a la lista que contiene las impresiones
    lista_impresiones[count]=num_temp
    count+=1
#Imprimimos las lineas de los numeros
for w in range(5):
    linea=[]
    for y in lista_impresiones:
        sub_linea=''.join(y[w])
        linea.append(sub_linea)
    print(' '.join(linea))


