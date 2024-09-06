# Calculos del limite de peso por aterrizaje

# Importar las librerias
import math
import pandas as pd

#Función que encuentra el multiplo mayor de 125 de un número dado
def encontrar_multiplo_mayor(numero_dado):
    multiplo_mayor = 125 * math.ceil(numero_dado / 125)
    return multiplo_mayor

# *************** PARAMETROS ***************
# elevacion: Dato sacado de otro módulo (aeropuerto) (int)
# alt_pres_aterrizaje: Dato sacado de otro módulo (aeropuerto) (int)
# temp: Dato sacado de otro módulo (aeropuerto) (int)
# CD: Dato sacado de otro módulo (combustible) (int)
# CR: Dato sacado de otro módulo (combustible) (int o String)
# aeronave_tripulacion: Dato sacado de otro módulo (peso) (int)
# FUEL_EN_EL_DESTINO_LBS: Dato sacado de otro módulo (combustible) (int)
# carga_req: Valor dado por el usuario (int)

def calcular(elevacion, alt_pres_aterrizaje, temp, CD, CR, aeronave_tripulacion, FUEL_EN_EL_DESTINO_LBS, carga_req):
    # Lee el archivo CSV
    df = pd.read_csv(filepath_or_buffer='data/max_ldg_weight.csv', delimiter=';')

    # Objeto de retorno
    result = {
        'carga_req_aterrizaje': carga_req
    }

    # La presión es encontrada a partir del multiplo mayor de 125, ya que estos datos son con los que se cuentan
    alt_pres = encontrar_multiplo_mayor(alt_pres_aterrizaje)

    # La temperatura se encuentra en la columna de la temperatura
    temperatura = str(temp)

    # Filtra los datos para la presión y la temperatura específicas
    fila_seleccionada = df.loc[df['alt_pres'] == alt_pres]
    
    # Obtener el peso máximo para la presión y la temperatura específicas
    peso = fila_seleccionada[temperatura].iloc[0]
    
    # Se revisa la elevación, de acuerdo a esta se determina el peso final
    if(elevacion != 0):
        result['max_ldg_weight_aterrizaje'] = peso
    else:
        result['max_ldg_weight_aterrizaje'] = 0

    # Revisar el rango del peso y calcular to weight
    if(peso>1 and peso<=16976):
        if(CR != 110):
            to_weight_aterrizaje = CD + peso
        else:
            to_weight_aterrizaje = CD + peso + CR
    else:
        if(peso>16976 and peso<=20000):
            to_weight_aterrizaje = 16976
        else:
            to_weight_aterrizaje = 0

    result['to_weight_aterrizaje'] = to_weight_aterrizaje

    # Calcular la carga paga limmitada por aterrizaje
    carga_paga_limitada_aterrizaje = peso - (aeronave_tripulacion + FUEL_EN_EL_DESTINO_LBS)

    result['carga_paga_limitada_aterrizaje'] = carga_paga_limitada_aterrizaje

    # Calcular pasajeros a 200
    pasajeros_200 = (carga_paga_limitada_aterrizaje) / 200
    result['pasajeros_200_aterrizaje'] = pasajeros_200

    # Calcular pasajeros a 220
    pasajeros_220 = (carga_paga_limitada_aterrizaje) / 220
    result['pasajeros_220_aterrizaje'] = pasajeros_220

    # Calcular pasajeros a 250
    pasajeros_250 = (carga_paga_limitada_aterrizaje) / 250
    result['pasajeros_250_aterrizaje'] = pasajeros_250

    return result


#print(calcular(98, 98, 30, 864, 'FALSO', 10929, 1307, 0))
