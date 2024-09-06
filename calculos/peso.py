# Calculos relacionados al peso de la aeronave

# *************** PARAMETROS ***************
# combustible: Módulo de combustible (dict)
# trip: Valor dado por el usuario (int)
# aeronave: Valor dado por el usuario (int)

def calcular(combustible, trip, aeronave):
    # Objeto de retorno
    result = {
        'trip': trip,
        'aeronave': aeronave
    }

    # Calculo de peso aeronave + tripulacion
    aeronave_tripulacion = aeronave + trip
    result['aeronave_tripulacion'] = aeronave_tripulacion
    # Calculo de peso aeronave + tripulacion + combustible
    aeronave_tripulacion_combustible = aeronave_tripulacion + combustible['TMRN']
    result['aeronave_tripulacion_combustible'] = aeronave_tripulacion_combustible
    # Variable vacia por el momento
    result['zero_fuel'] = 0

    return result

#Pruebas
#print(calcular(
#    {'TMRN': 2281},
#    800,
#    10129
#    ))