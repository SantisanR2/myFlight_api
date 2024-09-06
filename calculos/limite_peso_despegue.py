# Calculos del limite de peso por despegue

# Importar las librerias
import math
import pandas as pd

#Función que encuentra el multiplo mayor de 125 de un número dado
def encontrar_multiplo_mayor(numero_dado):
    multiplo_mayor = 125 * math.ceil(numero_dado / 125)
    return multiplo_mayor

# *************** PARAMETROS ***************
# alt_pres_despegue: Dato sacado de otro módulo (aeropuerto) (int)
# temp: Dato sacado de otro módulo (aeropuerto) (int)
# CR: Dato sacado de otro módulo (combustible) (int o String)
# CD: Dato sacado de otro módulo (combustible) (int)
# aeronave_tripulacion_combustible: Dato sacado de otro módulo (peso) (int)
# carga_req: Valor dado por el usuario (int)

def calcular(alt_pres_despegue, temp, CR, CD, aeronave_tripulacion_combustible, carga_req):
    # Lee el archivo CSV
    df = pd.read_csv(filepath_or_buffer='data/max_peso_despegue.csv', delimiter=';')

    # Objeto de retorno
    result = {
        'carga_req_despegue': carga_req,
    }

    # La pista es encontrada a partir del multiplo mayor de 125, ya que estos datos son con los que se cuentan
    pista = str(encontrar_multiplo_mayor(alt_pres_despegue))

    # La temperatura se encuentra en la columna de la temperatura
    temperatura = str(temp)

    # Filtra los datos para la longitud de pista y la temperatura específicas
    fila_seleccionada = df.loc[df['PISTA'] == pista]

    # Obtener el peso máximo para la longitud de pista y la temperatura específicas
    peso = fila_seleccionada[temperatura].iloc[0]
    result['max_to_weight_despegue'] = peso

    # Revisar si es el primer vuelo y calcular ldg_weight
    if (CR != 110):
        ldg_weight = peso - CD
    else:
        ldg_weight = peso - (CD + CR)

    result['ldg_weight_despegue'] = ldg_weight

    # Revisar si es el primer vuelo y calcular la carga paga limmitada por despegue
    if (CR != 110):
        carga_paga_limitada_despegue = peso - aeronave_tripulacion_combustible
    else:
        carga_paga_limitada_despegue = peso - (aeronave_tripulacion_combustible - CR)

    result['carga_paga_limitada_despegue'] = carga_paga_limitada_despegue

    # Calcular pasajeros a 200
    pasajeros_200 = (carga_paga_limitada_despegue - carga_req) / 200
    result['pasajeros_200_despegue'] = pasajeros_200

    # Calcular pasajeros a 220
    pasajeros_220 = (carga_paga_limitada_despegue - carga_req) / 220
    result['pasajeros_220_despegue'] = pasajeros_220

    # Calcular pasajeros a 250
    pasajeros_250 = (carga_paga_limitada_despegue - carga_req) / 250
    result['pasajeros_250_despegue'] = pasajeros_250

    return result


#print(calcular(3185, 24, 'FALSO', 864, 13100, 0))
