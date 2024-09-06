# Calculos relacionados con el driftdown

# *************** PARAMETROS ***************
# peso_despegue: Valor dado por el usuario (int)
# fuel_consumido: Valor dado por el usuario (int)
# qnh_act: Valor dado por el usuario (int)
# oat: Valor dado por el usuario (int)
# fl: Valor dado por el usuario (int)

def calcular(peso_despegue, fuel_consumido, qnh_act, oat, fl):
    # Objeto de retorno
    result = {
        'peso_despegue': peso_despegue,
        'fuel_consumido': fuel_consumido,
        'qnh_act': qnh_act,
        'oat': oat,
        'fl': fl
    }

    # Calcular peso actual de la aeronave
    peso_actual_lbs = peso_despegue - fuel_consumido
    result['peso_actual_lbs'] = peso_actual_lbs

    # Calcular peso actual de la aeronave en kg
    peso_actual_kg = peso_actual_lbs / 2.2
    result['peso_actual_kg'] = peso_actual_kg

    # Calcular la temperatura isa ideal
    temp_isa_ideal = ((-2*fl)/1000) + 15
    result['temp_isa_ideal'] = temp_isa_ideal

    # Calcular la temperatura isa real
    temp_isa_real = oat - temp_isa_ideal
    result['temp_isa_real'] = temp_isa_real

    # Calcular alt pres driftdown
    alt_pres_driftdown = (fl-(qnh_act-29.92)*1000)
    result['alt_pres_driftdown'] = alt_pres_driftdown

    # Calcular alt den
    alt_den = ((oat - temp_isa_ideal)*120) + alt_pres_driftdown
    result['alt_den'] = alt_den

    return result

# Pruebas
#print(calcular(14000, 350, 30.1, 4, 15000))