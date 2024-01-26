import sys

sys.path.append("c:\\Users\\andre\\Desktop\\GitHub\\Python\\Modulos")
sys.path.append("c:\\Users\\andre\\Desktop\\GitHub\\Python\\Ejemplo de paquetes")

import modulo
import extra.iota

print(extra.iota.FunI())

import extra.good.best.sigma
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())

