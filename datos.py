from random import randint, uniform

#Conjuntos
Dias = range(7)
Puntos_Dispo = range(6)
Puntos_Extra = range(3)
Puntos_Totales = range(9)
Zonas = range(5)
Camiones = range(20)


#Parametros

volumen_max_por_punto_dispo = 1000
volumen_max_por_punto_extra = 600
demanda_diaria_volumen_por_zona_dia = {
    (0, 0): 0,
    (0, 1): 0,
    (0, 2): 0,
    (0, 3): 0,
    (0, 4): 0,
    (0, 5): 0,
    (0, 6): 0,
    (1, 0): 0,
    (1, 1): 0,
    (1, 2): 0,
    (1, 3): 0,
    (1, 4): 0,
    (1, 5): 0,
    (1, 6): 0,
    (2, 0): 0,
    (2, 1): 0,
    (2, 2): 0,
    (2, 3): 0,
    (2, 4): 0,
    (2, 5): 0,
    (2, 6): 0,
    (3, 0): 0,
    (3, 1): 0,
    (3, 2): 0,
    (3, 3): 0,
    (3, 4): 0,
    (3, 5): 0,
    (3, 6): 0,
    (4, 0): 0,
    (4, 1): 0,
    (4, 2): 0,
    (4, 3): 0,
    (4, 4): 0,
    (4, 5): 0,
    (4, 6): 0,
}
costo_utilizacion_camion = 60000
volumen_max_camion = 1200
costo_utilizacion_punto_extra = 50000
presupuesto_municipalidad_puntos_extra = 1000000