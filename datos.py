from random import randint, uniform

#Conjuntos
Dias = range(8)
Puntos_Dispo = range(11)
Puntos_Extra = range(5)
Zonas = range(6)
Camiones = range(8)


#Parametros

volumen_max_por_punto_dispo = 4
volumen_max_por_punto_extra = 4
demanda_diaria_volumen_por_zona_dia = {
    (0, 0): 6.61,
    (0, 1): 6.61,
    (0, 2): 6.61,
    (0, 3): 6.61,
    (0, 4): 6.61,
    (0, 5): 6.61,
    (0, 6): 6.61,
    (0, 7): 6.61,
    (1, 0): 6.61,
    (1, 1): 6.61,
    (1, 2): 6.61,
    (1, 3): 6.61,
    (1, 4): 6.61,
    (1, 5): 6.61,
    (1, 6): 6.61,
    (1, 7): 6.61,
    (2, 0): 6.61,
    (2, 1): 6.61,
    (2, 2): 6.61,
    (2, 3): 6.61,
    (2, 4): 6.61,
    (2, 5): 6.61,
    (2, 6): 6.61,
    (2, 7): 6.61,
    (3, 0): 6.61,
    (3, 1): 6.61,
    (3, 2): 6.61,
    (3, 3): 6.61,
    (3, 4): 6.61,
    (3, 5): 6.61,
    (3, 6): 6.61,
    (3, 7): 6.61,
    (4, 0): 6.61,
    (4, 1): 6.61,
    (4, 2): 6.61,
    (4, 3): 6.61,
    (4, 4): 6.61,
    (4, 5): 6.61,
    (4, 6): 6.61,
    (4, 7): 6.61,
    (5, 0): 6.61,
    (5, 1): 6.61,
    (5, 2): 6.61,
    (5, 3): 6.61,
    (5, 4): 6.61,
    (5, 5): 6.61,
    (5, 6): 6.61,
    (5, 7): 6.61,
}
costo_utilizacion_camion = 32550
volumen_max_camion = 20
costo_utilizacion_punto_extra = 5425
presupuesto_municipalidad_puntos_extra = 404977.698