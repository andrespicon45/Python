def verify(numero):
    range_min=-10
    range_max=10
    try:
        num=int(numero)
        assert num>-10 and num<10
        return num
    except ValueError:
        return 'Ingresa unicamente numeros enteros.'
    except AssertionError:
        return 'Ingrese un valor dentro del rango valido.'
    except:
        return 'UPS! Ha ocurrido un error desconocido.'
    
print(verify(input('Ingrese un numero entre -10 a 10:')))