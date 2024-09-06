# Calculos relacionados con datos de navegacion

# Importar las librerias
import datetime


# *************** PARAMETROS ***************
# first_flight: Valor dado por el usuario (True o False)
# mn_min: Valor dado por el usuario (int)
# f_f: Valor dado por el usuario (int)
# distancia_destino: Valor dado por el usuario (int)
# distancia_alterno: Valor dado por el usuario (int)

def calcular(first_flight, mn_min, f_f, distancia_destino, distancia_alterno):
    # Objeto de retorno
    result = {
        'first_flight': first_flight,
        'mn_min': mn_min,
        'f_f': f_f,
        'distancia_destino': distancia_destino,
        'distancia_alterno': distancia_alterno
    }
    # Calcula la velocidad crucero
    vel_crucero = mn_min * 60
    result['vel_crucero'] = vel_crucero
    # Calcula el tiempo destino en horas
    tiempo_destino = (distancia_destino / mn_min) / 60
    # Convertir a horas, minutos y segundos
    horas_destino = int(tiempo_destino)
    minutos_destino = int((tiempo_destino * 60) % 60)
    segundos_destino = int((tiempo_destino * 3600) % 60)
    # Crear un objeto de tiempo
    tiempo_destino = datetime.time(horas_destino, minutos_destino, segundos_destino)
    result['tiempo_destino'] = tiempo_destino
    # Calcula el tiempo alterno en horas
    tiempo_alterno = (distancia_alterno / mn_min) / 60
    # Convertir a horas, minutos y segundos
    horas_alterno = int(tiempo_alterno)
    minutos_alterno = int((tiempo_alterno * 60) % 60)
    segundos_alterno = int((tiempo_alterno * 3600) % 60)
    # Crear un objeto de tiempo
    tiempo_alterno = datetime.time(horas_alterno, minutos_alterno, segundos_alterno)
    result['tiempo_alterno'] = tiempo_alterno

    return result

#Pruebas
#print(calcular(False, 2.7, 700, 200, 100))