from random import randint, uniform

#Conjuntos
Dias = range(7)
Puntos_Dispo = range(6)
Puntos_Extra = range(3)
Puntos_Totales = range(9)
Zonas = range(5)
Camiones = range(20)


#Parametros

volumen_max_por_punto_dispo = 3
volumen_max_por_punto_extra = 5
demanda_diaria_volumen_por_zona_dia = {
    (0, 0): 2.79,
    (0, 1): 2.79,
    (0, 2): 2.79,
    (0, 3): 2.79,
    (0, 4): 2.79,
    (0, 5): 2.79,
    (0, 6): 2.79,
    (1, 0): 2.79,
    (1, 1): 2.79,
    (1, 2): 2.79,
    (1, 3): 2.79,
    (1, 4): 2.79,
    (1, 5): 2.79,
    (1, 6): 2.79,
    (2, 0): 2.79,
    (2, 1): 2.79,
    (2, 2): 2.79,
    (2, 3): 2.79,
    (2, 4): 2.79,
    (2, 5): 2.79,
    (2, 6): 2.79,
    (3, 0): 2.79,
    (3, 1): 2.79,
    (3, 2): 2.79,
    (3, 3): 2.79,
    (3, 4): 2.79,
    (3, 5): 2.79,
    (3, 6): 2.79,
    (4, 0): 2.79,
    (4, 1): 2.79,
    (4, 2): 2.79,
    (4, 3): 2.79,
    (4, 4): 2.79,
    (4, 5): 2.79,
    (4, 6): 2.79,
}
costo_utilizacion_camion = 32550
volumen_max_camion = 20
costo_utilizacion_punto_extra = 5425
presupuesto_municipalidad_puntos_extra = 404977.698