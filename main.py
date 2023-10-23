from gurobipy import Model, GRB, quicksum
from random import randint
from datos import *

model = Model()

#Variables

cv = model.addVars(Puntos_Dispo, Zonas, Dias, vtype = GRB.continuous) #, name = 'cv_p,z,d'
rv = model.addVars(Camiones, Dias, vtype = GRB.continuous) #, name = 'rv_a,d'
ev = model.addVars(Puntos_Extra, Zonas, Dias, vtype = GRB.continuous) #, name = 'ev_t,z,d'
e = model.addVars(Zonas, Dias, vtype = GRB.continuous) #, name = 'e_z,d'
rn = model.addVars(Dias, vtype = GRB.continuous) #, name = 'rn_d'

model.update()

#Funcion Objetivo

objective = quicksum(rn[d] for d in Dias) + quicksum(e[z,d] for z in Zonas for d in Dias)
model.setObjective(objective, GRB.MINIMIZE)

#Restricciones

#1 Volumen max que recibe el punto de reciclaje segun los requerimientos del area que abarca el punto de reciclaje debe de ser respetado
model.addConstrs()

#2 Restriccion inventario de los puntos
model.addConstrs()

#3 Se satisface la demanda de requerimiento de reciclaje por zona.
model.addConstrs()

#4 Los puntos de reciclaje extra anadidos siguen los requerimientos de que el area que abarca el punto de reciclaje debe ser respetado.
model.addConstrs()

#5 La cantidad de puntos de reciclaje extra se realiza segun la cantidad de material necesario extra recibido.
model.addConstrs()

#6 La seleccion del numero de camiones se realiza segun la cantidad de material necesario para retirar.
model.addConstrs()

#7 Los camiones no pueden superar su capacidad maxima de reciclaje.
model.addConstrs()

#8 Los camiones no pueden superar el numero de camiones disponibles.
model.addConstrs()

#9 Los puntos de reciclaje extra no pueden superar el n´umero de puntos extra disponibles para el despliegue.
model.addConstrs()

#10 No se debe sobrepasar el presupuesto asignado por la municipalidad para los puntos de reciclaje extra.
model.addConstrs()


model.optimize()
