# Calculos relacionados con el peso real de la areonave

# *************** PARAMETROS ***************
# peso_carga: Valor dado por el usuario (int)
# cantidad_pax_200: Valor dado por el usuario (int)
# cantidad_pax_220: Valor dado por el usuario (int)
# cantidad_pax_250: Valor dado por el usuario (int)
# total_peso_pax_manual: Valor dado por el usuario (int)
# aeronave_tripulacion_combustible: Dato sacado de otro módulo (peso) (int)
# carga_paga_limitada_despegue: Dato sacado de otro módulo (limite peso despegue) (int)
# carga_paga_limitada_aterrizaje: Dato sacado de otro módulo (limite peso aterrizaje) (int)

def calcular(peso_carga, cantidad_pax_200, cantidad_pax_220, cantidad_pax_250, total_peso_pax_manual, aeronave_tripulacion_combustible, carga_paga_limitada_despegue, carga_paga_limitada_aterrizaje):

    # Objeto de retorno
    result = {
        'total_peso_pax_manual': total_peso_pax_manual,
        'cantidad_pax_200': cantidad_pax_200,
        'cantidad_pax_220': cantidad_pax_220,
        'cantidad_pax_250': cantidad_pax_250,
        'peso_carga': peso_carga
    }

    # Calcular total peso pax promedio
    total_peso_pax_promedio = cantidad_pax_200 * 200 + cantidad_pax_220 * 220 + cantidad_pax_250 * 250
    result['total_peso_pax_promedio'] = total_peso_pax_promedio

    # Calcular total carga + pax validando el total peso pax manual
    if total_peso_pax_manual == 0:
        total_carga_pax = peso_carga + total_peso_pax_promedio
    else:
        total_carga_pax = peso_carga + total_peso_pax_manual
    result['total_carga_pax'] = total_carga_pax

    # Calcular peso real actual aeronave en lbs
    peso_real_actual_lbs = total_carga_pax + aeronave_tripulacion_combustible
    result['peso_real_actual_lbs'] = peso_real_actual_lbs

    # Calcular peso reak actual aeronave en kg
    peso_real_actual_kg = peso_real_actual_lbs / 2.2
    result['peso_real_actual_kg'] = peso_real_actual_kg

    # Calcular carga disponible limitado despegue
    carga_disponible_limitado_despegue = carga_paga_limitada_despegue - total_carga_pax
    result['carga_disponible_limitado_despegue'] = carga_disponible_limitado_despegue

    # Calcular cargad disponible limitado aterrizaje
    carga_disponible_limitado_aterrizaje = carga_paga_limitada_aterrizaje - total_carga_pax
    result['carga_disponible_limitado_aterrizaje'] = carga_disponible_limitado_aterrizaje
    
    return result

# Pruebas
#print(calcular(0, 0, 0, 0, 0, 13100, 2900, 4188))