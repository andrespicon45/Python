#Creamos una lista vacia que contendra el sudoku
sudoku=[]
#Creamos un input para ingresar los valores del sudoku
for i in range(9):
    linea=input(f'Ingrese la {i+1} linea del sudoku:')
    sudoku.append(linea)
#Realizamos una iteracion por todos los valores del sudoku y comprobamos que sea un digito
for fila in sudoku:
    for ch in fila:
        if not ch.isdigit():
            print('El sudoku no contiene solo numeros.')
#Comprobamos que en cada fila solo haya numeros del 1 al 9 y no se repitan
for fila in sudoku:
    for num in range(1,10):
        if fila.count(str(num))>1:
            print('El sudoku es invalido.')
#Comprobamos que en cada columna solo haya un numero del 1 al 9
for col in range(9):
    columna=[]
    for fila in sudoku:
        columna.append(fila[col])
    for i in range(1,10):
        if columna.count(i)>1:
            print('El sudoku es invalido.')
#Comprobamos que en cada subcuadro de 3X3 existan los numeros del 1-9 sin repetirse
invalido=False
for w in range(3):
    for z in range(3):    
        if invalido:
            break
        cuadro=[]
        for x in range(3):
            if invalido:
                break
            subfila=sudoku[x+(w*3)]
            for y in range(3):
                cuadro.append(subfila[y+(z*3)])
        for i in range(1,10):
            if cuadro.count(str(i))>1:
                invalido=True
                print('El sudoku es invalido.')
                break
if not invalido:
    print('FELICIDADES! Sudoku completado.')
