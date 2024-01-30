def quitar_espacios(texto):
    lista=[]
    for caracter in texto:
        if caracter.isspace():
            continue
        else:
            lista.append(caracter)
    texto=''.join(lista)
    return texto

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

texto1=input('Ingrese el primer texto:')
texto2=input('Ingrese el segundo texto:')

texto1=quitar_espacios(texto1).lower()
texto2=quitar_espacios(texto2).lower()

for letra in alfabeto:
    if texto2.count(letra)!=texto1.count(letra):
        print('No es un anagrama')
        break
else:
    print('Es un anagrama.')
