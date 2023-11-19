from random import randint, uniform

#Conjuntos 
Dias = range(8) # 0 (día anterior), 1 (lunes), 2, 3, 4, 5, 6, 7 (domingo)
Puntos_Dispo = range(6)
Puntos_Extra = range(3)
Zonas = range(6) # 0, 1, 2, 3, 4, 5
Camiones = range(20)


#Parametros

volumen_max_por_punto_dispo = 4 # VCB
volumen_max_por_punto_extra = 4 
demanda_diaria_volumen_por_zona_dia = {
    (0, 0): 8.81,
    (0, 1): 8.81,
    (0, 2): 8.81,
    (0, 3): 8.81,
    (0, 4): 8.81,
    (0, 5): 8.81,
    (0, 6): 8.81,
    (0, 7): 8.81,
    (1, 0): 8.81,
    (1, 1): 8.81,
    (1, 2): 8.81,
    (1, 3): 8.81,
    (1, 4): 8.81,
    (1, 5): 8.81,
    (1, 6): 8.81,
    (1, 7): 8.81,
    (2, 0): 8.81,
    (2, 1): 8.81,
    (2, 2): 8.81,
    (2, 3): 8.81,
    (2, 4): 8.81,
    (2, 5): 8.81,
    (2, 6): 8.81,
    (2, 7): 8.81,
    (3, 0): 8.81,
    (3, 1): 8.81,
    (3, 2): 8.81,
    (3, 3): 8.81,
    (3, 4): 8.81,
    (3, 5): 8.81,
    (3, 6): 8.81,
    (3, 7): 8.81,
    (4, 0): 8.81,
    (4, 1): 8.81,
    (4, 2): 8.81,
    (4, 3): 8.81,
    (4, 4): 8.81,
    (4, 5): 8.81,
    (4, 6): 8.81,
    (4, 7): 8.81,
    (5, 0): 8.81,
    (5, 1): 8.81,
    (5, 2): 8.81,
    (5, 3): 8.81,
    (5, 4): 8.81,
    (5, 5): 8.81,
    (5, 6): 8.81,
    (5, 7): 8.81,
}
costo_utilizacion_camion = 32550
volumen_max_camion = 20
costo_utilizacion_punto_extra = 5425
presupuesto_municipalidad_puntos_extra = 404977.698