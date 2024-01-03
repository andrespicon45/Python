import sys

direccion=sys.path[0]
direccion=direccion+"\\Modulos"

print(direccion)

sys.path.append(direccion)

import modulo

print(sys.path)