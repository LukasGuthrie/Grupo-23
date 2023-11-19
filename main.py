from gurobipy import Model, GRB, quicksum
from random import randint
from datos import *

model = Model()

model.setParam("TimeLimit", 1800)

#Variables

cv = model.addVars(Puntos_Dispo, Zonas, Dias, vtype = GRB.CONTINUOUS) #, name = 'cv_p,z,d'
rv = model.addVars(Camiones, Dias, vtype = GRB.CONTINUOUS) #, name = 'rv_a,d'
ev = model.addVars(Puntos_Extra, Zonas, Dias, vtype = GRB.CONTINUOUS) #, name = 'ev_t,z,d'
e = model.addVars(Zonas, Dias, vtype = GRB.INTEGER) #, name = 'e_z,d'
rn = model.addVars(Dias, vtype = GRB.INTEGER) #, name = 'rn_d'

model.update()

#Funcion Objetivo

objective = quicksum(costo_utilizacion_camion * rn[d] for d in Dias) + quicksum(costo_utilizacion_punto_extra * e[z,d] for z in Zonas for d in Dias)
model.setObjective(objective, GRB.MINIMIZE)

#Restricciones

#1 Volumen máximo que recibe el punto de reciclaje, según los requerimientos del área que abarca el punto de reciclaje, debe de ser respetado
model.addConstrs(cv[p,z,d] <= volumen_max_por_punto_dispo for p in Puntos_Dispo for z in Zonas for d in Dias)

#2 Restricción de inventario de los puntos de reciclaje
model.addConstrs(cv[p,z,0] == 0 for p in Puntos_Dispo for z in Zonas)
model.addConstrs(quicksum(cv[p,z,d] for p in Puntos_Dispo for z in Zonas) == quicksum(cv[p,z,(d-1)] for p in Puntos_Dispo for z in Zonas) + quicksum(demanda_diaria_volumen_por_zona_dia[z,d] for z in Zonas) - quicksum(ev[t,z,d] for t in Puntos_Extra for z in Zonas) - quicksum(rv[a,d] for a in Camiones) for d in range(1,7))

#3 Se satisface la demanda de requerimiento de reciclaje por zona
model.addConstrs(demanda_diaria_volumen_por_zona_dia[z,d] >= quicksum(cv[p,z,d] for p in Puntos_Dispo) + quicksum(ev[t,z,d] for t in Puntos_Extra) for z in Zonas for d in Dias)

#4 Los puntos de reciclaje extra anadidos, siguen los requerimientos de que el área que abarca el punto de reciclaje debe ser respetado
model.addConstrs(ev[t,z,d] <= volumen_max_por_punto_extra for t in Puntos_Extra for z in Zonas for d in Dias)

#5 La cantidad de puntos de reciclaje extra se realiza según la cantidad de material necesario extra recibido
model.addConstrs(quicksum(ev[t,z,d] for t in Puntos_Extra) <= (volumen_max_por_punto_extra * e[z,d]) for z in Zonas for d in Dias)

#6 La seleccion del numero de camiones se realiza segun la cantidad de material necesario para retirar
model.addConstrs(quicksum(rv[a,d] for a in Camiones) <= (volumen_max_camion * rn[d]) for d in Dias)

#7 Los camiones no pueden superar su capacidad máxima de reciclaje
model.addConstrs(rv[a,d] <= volumen_max_camion for a in Camiones for d in Dias)

#8 Los camiones no pueden superar el número de camiones disponibles
model.addConstrs(rn[d] <= len(Camiones) for d in Dias)

#9 Los puntos de reciclaje extra no pueden superar el número de puntos extra disponibles para el despliegue
model.addConstrs(quicksum(e[z,d] for z in Zonas) <= len(Puntos_Extra) for d in Dias)

#10 No se debe sobrepasar el presupuesto asignado por la municipalidad para los puntos de reciclaje extra
model.addConstr(objective <= presupuesto_municipalidad_puntos_extra)
model.addConstr(objective >= 0)


model.optimize()
print(model.ObjVal)
print(f' Los costos operativos resultantes son {round(model.ObjVal,0)} pesos')

with open('resultados/resultados_cv.csv', 'w') as archivo:
    archivo.write('Variable cv: p, z, d')
    for p in Puntos_Dispo:
        for z in Zonas:
            for d in Dias:
                archivo.write(f' \n{float(cv[p , z, d].x)}, {p}, {z}, {d}')

with open('resultados/resultados_rv.csv', 'w') as archivo:
    archivo.write('Variable rv: a, d')
    for a in Camiones:
        for d in Dias:
            archivo.write(f' \n{float(rv[a, d].x)}, {a}, {d}')

with open('resultados/resultados_ev.csv', 'w') as archivo:
    archivo.write('Variable ev: t, z, d')
    for t in Puntos_Extra:
        for z in Zonas:
            for d in Dias:
                archivo.write(f' \n{float(ev[t , z, d].x)}, {t}, {z}, {d}')

with open('resultados/resultados_e.csv', 'w') as archivo:
    archivo.write('Variable e: z, d')
    for z in Zonas:
        for d in Dias:
            archivo.write(f' \n{float(e[z, d].x)}, {z}, {d}')

with open('resultados/resultados_rn.csv', 'w') as archivo:
    archivo.write('Variable rn: d')
    for d in Dias:
        archivo.write(f' \n{float(rn[d].x)}, {d}')
