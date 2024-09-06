# Calculos relacionados con los datos del aeropuerto de despegue y de aterrizaje

# Importar librerias
import pandas as pd 

# *************** PARAMETROS ***************
# oaci_despegue: Valor dado por el usuario (String)
# temp_despegue: Valor dado por el usuario (int)
# qnh_despegue: Valor dado por el usuario (int)
# oaci_aterrizaje: Valor dado por el usuario (String)
# temp_aterrizaje: Valor dado por el usuario (int)
# qnh_aterrizaje: Valor dado por el usuario (int)

def calcular(oaci_despegue, temp_despegue, qnh_despegue, oaci_aterrizaje, temp_aterrizaje, qnh_aterrizaje):
    # Objeto de retorno
    result = {
        'oaci_despegue': oaci_despegue,
        'temp_despegue': temp_despegue,
        'qnh_despegue': qnh_despegue,
        'oaci_aterrizaje': oaci_aterrizaje,
        'temp_aterrizaje': temp_aterrizaje,
        'qnh_aterrizaje': qnh_aterrizaje
    }
    # Carga el archivo CSV
    df = pd.read_csv(filepath_or_buffer='data/pistas.csv', delimiter=';')
    # Busca los datos del aeropuerto de despegue
    aeropuerto_despegue = df.loc[df['oaci'] == oaci_despegue]
    # Busca los datos del aeropuerto de aterrizaje
    aeropuerto_aterrizaje = df.loc[df['oaci'] == oaci_aterrizaje]
    # Trae el nombre de la ciudad de despegue
    ciudad_despegue = aeropuerto_despegue['nombre'].iloc[0]
    result['ciudad_despegue'] = ciudad_despegue
    # Trae el nombre de la ciudad de aterrizaje
    ciudad_aterrizaje = aeropuerto_aterrizaje['nombre'].iloc[0]
    result['ciudad_aterrizaje'] = ciudad_aterrizaje
    # Trae la elevacion del aeropuerto de despegue
    elevacion_despegue = float(aeropuerto_despegue['elevacion'].iloc[0])
    result['elevacion_despegue'] = elevacion_despegue
    # Trae la elevacion del aeropuerto de aterrizaje
    elevacion_aterrizaje = float(aeropuerto_aterrizaje['elevacion'].iloc[0])
    result['elevacion_aterrizaje'] = elevacion_aterrizaje
    # Calcula ALT PRES en el aeropuerto de despegue
    alt_pres_despegue = (elevacion_despegue - ((qnh_despegue-29.92)* 1000))
    result['alt_pres_despegue'] = alt_pres_despegue
    # Calcula ALT PRES en el aeropuerto de aterrizaje
    alt_pres_aterrizaje = (elevacion_aterrizaje - ((qnh_aterrizaje-29.92)* 1000))
    result['alt_pres_aterrizaje'] = alt_pres_aterrizaje
    # Trae el RWY_1 del aeropuerto de despegue
    rwy_1_despegue = aeropuerto_despegue['pista_1'].iloc[0]
    result['rwy_1_despegue'] = rwy_1_despegue
    # Trae el RWY_2 del aeropuerto de despegue
    rwy_2_despegue = aeropuerto_despegue['pista_2'].iloc[0]
    result['rwy_2_despegue'] = rwy_2_despegue
    # Trae el RWY_1 del aeropuerto de aterrizaje
    rwy_1_aterrizaje = aeropuerto_aterrizaje['pista_1'].iloc[0]
    result['rwy_1_aterrizaje'] = rwy_1_aterrizaje
    # Trae el RWY_2 del aeropuerto de aterrizaje
    rwy_2_aterrizaje = aeropuerto_aterrizaje['pista_2'].iloc[0]
    result['rwy_2_aterrizaje'] = rwy_2_aterrizaje
    # Trae el TORA_1 en metros del aeropuerto de despegue
    tora_1_despegue = aeropuerto_despegue['tora_1'].iloc[0]
    result['tora_1_despegue'] = tora_1_despegue
    # Trae el TORA_2 en metros del aeropuerto de despegue
    tora_2_despegue = aeropuerto_despegue['tora_2'].iloc[0]
    result['tora_2_despegue'] = tora_2_despegue
    # Trae el TORA_1 en metros del aeropuerto de aterrizaje
    tora_1_aterrizaje = aeropuerto_aterrizaje['tora_1'].iloc[0]
    result['tora_1_aterrizaje'] = tora_1_aterrizaje
    # Trae el TORA_2 en metros del aeropuerto de aterrizaje
    tora_2_aterrizaje = aeropuerto_aterrizaje['tora_2'].iloc[0]
    result['tora_2_aterrizaje'] = tora_2_aterrizaje
    # Calcula el TORA_1 en pies del aeropuerto de despegue
    tora_1_despegue_ft = tora_1_despegue * 3.2808399
    result['tora_1_despegue_ft'] = tora_1_despegue_ft
    # Calcula el TORA_2 en pies del aeropuerto de despegue
    tora_2_despegue_ft = tora_2_despegue * 3.2808399
    result['tora_2_despegue_ft'] = tora_2_despegue_ft
    # Calcula el TORA_1 en pies del aeropuerto de aterrizaje
    tora_1_aterrizaje_ft = tora_1_aterrizaje * 3.2808399
    result['tora_1_aterrizaje_ft'] = tora_1_aterrizaje_ft
    # Calcula el TORA_2 en pies del aeropuerto de aterrizaje
    tora_2_aterrizaje_ft = tora_2_aterrizaje * 3.2808399
    result['tora_2_aterrizaje_ft'] = tora_2_aterrizaje_ft
    # Trae el TODA_1 en metros del aeropuerto de despegue
    toda_1_despegue = aeropuerto_despegue['toda_1'].iloc[0]
    result['toda_1_despegue'] = toda_1_despegue
    # Trae el TODA_2 en metros del aeropuerto de despegue
    toda_2_despegue = aeropuerto_despegue['toda_2'].iloc[0]
    result['toda_2_despegue'] = toda_2_despegue
    # Trae el TODA_1 en metros del aeropuerto de aterrizaje
    toda_1_aterrizaje = aeropuerto_aterrizaje['toda_1'].iloc[0]
    result['toda_1_aterrizaje'] = toda_1_aterrizaje
    # Trae el TODA_2 en metros del aeropuerto de aterrizaje
    toda_2_aterrizaje = aeropuerto_aterrizaje['toda_2'].iloc[0]
    result['toda_2_aterrizaje'] = toda_2_aterrizaje
    # Calcula el TODA_1 en pies del aeropuerto de despegue
    toda_1_despegue_ft = toda_1_despegue * 3.2808399
    result['toda_1_despegue_ft'] = toda_1_despegue_ft
    # Calcula el TODA_2 en pies del aeropuerto de despegue
    toda_2_despegue_ft = toda_2_despegue * 3.2808399
    result['toda_2_despegue_ft'] = toda_2_despegue_ft
    # Calcula el TODA_1 en pies del aeropuerto de aterrizaje
    toda_1_aterrizaje_ft = toda_1_aterrizaje * 3.2808399
    result['toda_1_aterrizaje_ft'] = toda_1_aterrizaje_ft
    # Calcula el TODA_2 en pies del aeropuerto de aterrizaje
    toda_2_aterrizaje_ft = toda_2_aterrizaje * 3.2808399
    result['toda_2_aterrizaje_ft'] = toda_2_aterrizaje_ft
    # Trae el ASDA_1 en metros del aeropuerto de despegue
    asda_1_despegue = aeropuerto_despegue['asda_1'].iloc[0]
    result['asda_1_despegue'] = asda_1_despegue
    # Trae el ASDA_2 en metros del aeropuerto de despegue
    asda_2_despegue = aeropuerto_despegue['asda_2'].iloc[0]
    result['asda_2_despegue'] = asda_2_despegue
    # Trae el ASDA_1 en metros del aeropuerto de aterrizaje
    asda_1_aterrizaje = aeropuerto_aterrizaje['asda_1'].iloc[0]
    result['asda_1_aterrizaje'] = asda_1_aterrizaje
    # Trae el ASDA_2 en metros del aeropuerto de aterrizaje
    asda_2_aterrizaje = aeropuerto_aterrizaje['asda_2'].iloc[0]
    result['asda_2_aterrizaje'] = asda_2_aterrizaje
    # Calcula el ASDA_1 en pies del aeropuerto de despegue
    asda_1_despegue_ft = asda_1_despegue * 3.2808399
    result['asda_1_despegue_ft'] = asda_1_despegue_ft
    # Calcula el ASDA_2 en pies del aeropuerto de despegue
    asda_2_despegue_ft = asda_2_despegue * 3.2808399
    result['asda_2_despegue_ft'] = asda_2_despegue_ft
    # Calcula el ASDA_1 en pies del aeropuerto de aterrizaje
    asda_1_aterrizaje_ft = asda_1_aterrizaje * 3.2808399
    result['asda_1_aterrizaje_ft'] = asda_1_aterrizaje_ft
    # Calcula el ASDA_2 en pies del aeropuerto de aterrizaje
    asda_2_aterrizaje_ft = asda_2_aterrizaje * 3.2808399
    result['asda_2_aterrizaje_ft'] = asda_2_aterrizaje_ft
    # Trae el LDA_1 en metros del aeropuerto de despegue
    lda_1_despegue = aeropuerto_despegue['lda_1'].iloc[0]
    result['lda_1_despegue'] = lda_1_despegue
    # Trae el LDA_2 en metros del aeropuerto de despegue
    lda_2_despegue = aeropuerto_despegue['lda_2'].iloc[0]
    result['lda_2_despegue'] = lda_2_despegue
    # Trae el LDA_1 en metros del aeropuerto de aterrizaje
    lda_1_aterrizaje = aeropuerto_aterrizaje['lda_1'].iloc[0]
    result['lda_1_aterrizaje'] = lda_1_aterrizaje
    # Trae el LDA_2 en metros del aeropuerto de aterrizaje
    lda_2_aterrizaje = aeropuerto_aterrizaje['lda_2'].iloc[0]
    result['lda_2_aterrizaje'] = lda_2_aterrizaje
    # Calcula el LDA_1 en pies del aeropuerto de despegue
    lda_1_despegue_ft = lda_1_despegue * 3.2808399
    result['lda_1_despegue_ft'] = lda_1_despegue_ft
    # Calcula el LDA_2 en pies del aeropuerto de despegue
    lda_2_despegue_ft = lda_2_despegue * 3.2808399
    result['lda_2_despegue_ft'] = lda_2_despegue_ft
    # Calcula el LDA_1 en pies del aeropuerto de aterrizaje
    lda_1_aterrizaje_ft = lda_1_aterrizaje * 3.2808399
    result['lda_1_aterrizaje_ft'] = lda_1_aterrizaje_ft
    # Calcula el LDA_2 en pies del aeropuerto de aterrizaje
    lda_2_aterrizaje_ft = lda_2_aterrizaje * 3.2808399
    result['lda_2_aterrizaje_ft'] = lda_2_aterrizaje_ft
    # Trae el ancho del aeropuerto de despegue
    ancho_despegue = aeropuerto_despegue['ancho'].iloc[0]
    result['ancho_despegue'] = ancho_despegue
    # Trae el ancho del aeropuerto de aterrizaje
    ancho_aterrizaje = aeropuerto_aterrizaje['ancho'].iloc[0]
    result['ancho_aterrizaje'] = ancho_aterrizaje
    # Trae la temperatura de referencia del aeropuerto de despegue
    temp_despegue = aeropuerto_despegue['temperatura'].iloc[0]
    result['temp_ref_despegue'] = temp_despegue
    # Trae la temperatura de referencia del aeropuerto de aterrizaje
    temp_aterrizaje = aeropuerto_aterrizaje['temperatura'].iloc[0]
    result['temp_ref_aterrizaje'] = temp_aterrizaje

    return result

# Pruebas
#print('Escenario 1: Datos suministrados (SKCL, 24, 29.9, SKBQ, 30, 29.92)')
#var = calcular('SKCL', 24, 29.9, 'SKBQ', 30, 29.92)
#print('Datos calculados por el módulo:')
#print(var)
#print('Prueba superada exitosamente')