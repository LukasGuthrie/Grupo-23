from random import randint, uniform

#Conjuntos
Dias = range(8)
Puntos_Dispo = range(6)
Puntos_Extra = range(3)
Zonas = range(5)
Camiones = range(20)


#Parametros

volumen_max_por_punto_dispo = 4
volumen_max_por_punto_extra = 4
demanda_diaria_volumen_por_zona_dia = {
    (0, 0): 16.76,
    (0, 1): 16.76,
    (0, 2): 16.76,
    (0, 3): 16.76,
    (0, 4): 16.76,
    (0, 5): 16.76,
    (0, 6): 16.76,
    (0, 7): 16.76,
    (1, 0): 16.76,
    (1, 1): 16.76,
    (1, 2): 16.76,
    (1, 3): 16.76,
    (1, 4): 16.76,
    (1, 5): 16.76,
    (1, 6): 16.76,
    (1, 7): 16.76,
    (2, 0): 16.76,
    (2, 1): 16.76,
    (2, 2): 16.76,
    (2, 3): 16.76,
    (2, 4): 16.76,
    (2, 5): 16.76,
    (2, 6): 16.76,
    (2, 7): 16.76,
    (3, 0): 16.76,
    (3, 1): 16.76,
    (3, 2): 16.76,
    (3, 3): 16.76,
    (3, 4): 16.76,
    (3, 5): 16.76,
    (3, 6): 16.76,
    (3, 7): 16.76,
    (4, 0): 16.76,
    (4, 1): 16.76,
    (4, 2): 16.76,
    (4, 3): 16.76,
    (4, 4): 16.76,
    (4, 5): 16.76,
    (4, 6): 16.76,
    (4, 7): 16.76,
}
costo_utilizacion_camion = 32550
volumen_max_camion = 20
costo_utilizacion_punto_extra = 5425
presupuesto_municipalidad_puntos_extra = 404977.698