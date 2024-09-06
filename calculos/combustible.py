# Calculos relacionados a los datos del combustible
# Importar las librerias
import datetime

# *************** PARAMETROS ***************
# CAD: Valor dado por el usuario (int)
# CS: Valor dado por el usuario (int)

def calcular(navegacion, CAD, CS):
    # Objeto de retorno
    result = {
        'CAD': CAD,
        'CS': CS
    }

    # Calculo de CR
    CR = 110 if navegacion['first_flight'] else "FALSO"
    result['CR'] = CR
    # Calculo de CD
    CD = ((navegacion['f_f']*((navegacion['tiempo_destino'].hour + navegacion['tiempo_destino'].minute / 60 + navegacion['tiempo_destino'].second / 3600))/24)/60)*24*60
    result['CD'] = CD
    # Calculo de CA
    CA = ((navegacion['f_f']*((navegacion['tiempo_alterno'].hour + navegacion['tiempo_alterno'].minute / 60 + navegacion['tiempo_alterno'].second / 3600))/24)/60)*24*60
    result['CA'] = CA
    # Calculo de CRN
    CRN = 525
    result['CRN'] = CRN
    # Calculo de CE
    CE = 200
    result['CE'] = CE
    # Calculo de CMRN
    CMRN = CR + CD + CA + CRN + CE if CR == 110 else CD + CA + CRN + CE
    result['CMRN'] = CMRN
    # Calculo de TMRN
    TMRN = CMRN + CAD + CS
    result['TMRN'] = TMRN
    # Calculo de TMRN EN
    TMRN_EN = TMRN / 6.7
    result['TMRN_EN'] = TMRN_EN
    # Calculo FUEL EN EL DESTINO LBS
    FUEL_EN_EL_DESTINO_LBS = TMRN - (CR + CD) if CR == 110 else TMRN - CD
    result['FUEL_EN_EL_DESTINO_LBS'] = FUEL_EN_EL_DESTINO_LBS
    # Calculo FUEL EN EL DESTINO USG
    FUEL_EN_EL_DESTINO_USG = FUEL_EN_EL_DESTINO_LBS / 6.7
    result['FUEL_EN_EL_DESTINO_USG'] = FUEL_EN_EL_DESTINO_USG

    return result

#Pruebas
#print(calcular({
#    'first_flight': True,
#    'mn_min': 2.7,
#    'f_f': 700,
#    'distancia_destino': 200,
#    'distancia_alterno': 100,
#    'vel_crucero': 162,
#    'tiempo_destino': datetime.time(1, 14, 4),
#    'tiempo_alterno': datetime.time(0, 37, 2)
#}, 150, 0))




