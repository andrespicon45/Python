texto=input('Ingrese una cadena de texto:')
texto=texto.lower()

lista=[]

for caracter in texto:
    if caracter.isspace():
        continue
    else:
        lista.append(caracter)
    
texto=''.join(lista)
texto_inverso=texto[::-1]

if texto==texto_inverso:
    print('Es un palindromo.')
else:
    print('No es un palindromo.')
