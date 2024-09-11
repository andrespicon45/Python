fecha=input('Ingresa tu fecha de nacimiento (solo formato numerico, sin signos):')
total=0
for caracter in fecha:
    total+=int(caracter)
while True:
    if total<10:
        break
    else:
        fecha=str(total)
        total=0
        for caracter in fecha:
            total+=int(caracter)
print(total)