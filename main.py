from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_marshmallow import Marshmallow
from calculos.aeropuerto import calcular as calcular_aeropuerto
from calculos.navegacion import calcular as calcular_navegacion
from calculos.combustible import calcular as calcular_combustible
from calculos.peso import calcular as calcular_peso
from calculos.limite_peso_aterrizaje import calcular as calcular_limite_peso_aterrizaje
from calculos.limite_peso_despegue import calcular as calcular_limite_peso_despegue
from calculos.peso_real import calcular as calcular_peso_real
from calculos.driftdown import calcular as calcular_driftdown

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost$myflight_db'
app.config['JWT_SECRET_KEY'] = 'sal_cifrado'

db = SQLAlchemy(app)
jwt = JWTManager(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.password = password

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Ruta para realizar los cálculos
@app.route('/calcular', methods=['POST'])
def get_data():
    first_flight = request.json['first_flight']
    mn_min = request.json['mn_min']
    f_f = request.json['f_f']
    distancia_destino = request.json['distancia_destino']
    distancia_alterno = request.json['distancia_alterno']
    oaci_despegue = request.json['oaci_despegue']
    temp_despegue = request.json['temp_despegue']
    qnh_despegue = request.json['qnh_despegue']
    oaci_aterrizaje = request.json['oaci_aterrizaje']
    temp_aterrizaje = request.json['temp_aterrizaje']
    qnh_aterrizaje = request.json['qnh_aterrizaje']
    CAD = request.json['CAD']
    CS = request.json['CS']
    trip = request.json['trip']
    aeronave = request.json['aeronave']
    carga_req_despegue = request.json['carga_req_despegue']
    carga_req_aterrizaje = request.json['carga_req_aterrizaje']
    peso_carga = request.json['peso_carga']
    cantidad_pax_200 = request.json['cantidad_pax_200']
    cantidad_pax_220 = request.json['cantidad_pax_220']
    cantidad_pax_250 = request.json['cantidad_pax_250']
    total_peso_pax_manual = request.json['total_peso_pax_manual']
    peso_despegue = request.json['peso_despegue']
    fuel_consumido = request.json['fuel_consumido']
    qnh_act = request.json['qnh_act']
    oat = request.json['oat']
    fl = request.json['fl']

    # Crear objeto de retorno
    result = {}

    # Traer datos de navegacion
    navegacion = calcular_navegacion(first_flight, mn_min, f_f, distancia_destino, distancia_alterno)

    # Traer datos de aeropuerto
    aeropuerto = calcular_aeropuerto(oaci_despegue, temp_despegue, qnh_despegue, oaci_aterrizaje, temp_aterrizaje, qnh_aterrizaje)
    aeropuerto['tora_1_despegue'] = float(aeropuerto['tora_1_despegue'])
    aeropuerto['tora_2_despegue'] = float(aeropuerto['tora_2_despegue'])
    aeropuerto['tora_1_aterrizaje'] = float(aeropuerto['tora_1_aterrizaje'])
    aeropuerto['tora_2_aterrizaje'] = float(aeropuerto['tora_2_aterrizaje'])
    aeropuerto['tora_1_despegue_ft'] = float(aeropuerto['tora_1_despegue_ft'])
    aeropuerto['tora_2_despegue_ft'] = float(aeropuerto['tora_2_despegue_ft'])
    aeropuerto['tora_1_aterrizaje_ft'] = float(aeropuerto['tora_1_aterrizaje_ft'])
    aeropuerto['tora_2_aterrizaje_ft'] = float(aeropuerto['tora_2_aterrizaje_ft'])
    aeropuerto['toda_1_despegue'] = float(aeropuerto['toda_1_despegue'])
    aeropuerto['toda_2_despegue'] = float(aeropuerto['toda_2_despegue'])
    aeropuerto['toda_1_aterrizaje'] = float(aeropuerto['toda_1_aterrizaje'])
    aeropuerto['toda_2_aterrizaje'] = float(aeropuerto['toda_2_aterrizaje'])
    aeropuerto['toda_1_despegue_ft'] = float(aeropuerto['toda_1_despegue_ft'])
    aeropuerto['toda_2_despegue_ft'] = float(aeropuerto['toda_2_despegue_ft'])
    aeropuerto['toda_1_aterrizaje_ft'] = float(aeropuerto['toda_1_aterrizaje_ft'])
    aeropuerto['toda_2_aterrizaje_ft'] = float(aeropuerto['toda_2_aterrizaje_ft'])
    aeropuerto['asda_1_despegue'] = float(aeropuerto['asda_1_despegue'])
    aeropuerto['asda_2_despegue'] = float(aeropuerto['asda_2_despegue'])
    aeropuerto['asda_1_aterrizaje'] = float(aeropuerto['asda_1_aterrizaje'])
    aeropuerto['asda_2_aterrizaje'] = float(aeropuerto['asda_2_aterrizaje'])
    aeropuerto['asda_1_despegue_ft'] = float(aeropuerto['asda_1_despegue_ft'])
    aeropuerto['asda_2_despegue_ft'] = float(aeropuerto['asda_2_despegue_ft'])
    aeropuerto['asda_1_aterrizaje_ft'] = float(aeropuerto['asda_1_aterrizaje_ft'])
    aeropuerto['asda_2_aterrizaje_ft'] = float(aeropuerto['asda_2_aterrizaje_ft'])
    aeropuerto['lda_1_despegue'] = float(aeropuerto['lda_1_despegue'])
    aeropuerto['lda_2_despegue'] = float(aeropuerto['lda_2_despegue'])
    aeropuerto['lda_1_aterrizaje'] = float(aeropuerto['lda_1_aterrizaje'])
    aeropuerto['lda_2_aterrizaje'] = float(aeropuerto['lda_2_aterrizaje'])
    aeropuerto['lda_1_despegue_ft'] = float(aeropuerto['lda_1_despegue_ft'])
    aeropuerto['lda_2_despegue_ft'] = float(aeropuerto['lda_2_despegue_ft'])
    aeropuerto['lda_1_aterrizaje_ft'] = float(aeropuerto['lda_1_aterrizaje_ft'])
    aeropuerto['lda_2_aterrizaje_ft'] = float(aeropuerto['lda_2_aterrizaje_ft'])
    aeropuerto['temp_ref_despegue'] = float(aeropuerto['temp_ref_despegue'])
    aeropuerto['temp_ref_aterrizaje'] = float(aeropuerto['temp_ref_aterrizaje'])

    # Traer datos de combustible
    combustible = calcular_combustible(navegacion, CAD, CS)

    # Traer datos de peso
    peso = calcular_peso(combustible, trip, aeronave)

    # Traer datos de limite de peso de despegue
    limite_peso_despegue = calcular_limite_peso_despegue(aeropuerto['alt_pres_despegue'], aeropuerto['temp_despegue'], combustible['CR'], combustible['CD'], peso['aeronave_tripulacion_combustible'], carga_req_despegue)
    limite_peso_despegue['max_to_weight_despegue'] = float(limite_peso_despegue['max_to_weight_despegue'])
    limite_peso_despegue['ldg_weight_despegue'] = float(limite_peso_despegue['ldg_weight_despegue'])
    limite_peso_despegue['carga_paga_limitada_despegue'] = float(limite_peso_despegue['carga_paga_limitada_despegue'])
    limite_peso_despegue['pasajeros_200_despegue'] = float(limite_peso_despegue['pasajeros_200_despegue'])
    limite_peso_despegue['pasajeros_220_despegue'] = float(limite_peso_despegue['pasajeros_220_despegue'])
    limite_peso_despegue['pasajeros_250_despegue'] = float(limite_peso_despegue['pasajeros_250_despegue'])

    # Traer datos de limite de peso de aterrizaje
    limite_peso_aterrizaje = calcular_limite_peso_aterrizaje(aeropuerto['elevacion_aterrizaje'], aeropuerto['alt_pres_aterrizaje'], aeropuerto['temp_aterrizaje'], combustible['CD'], combustible['CR'], peso['aeronave_tripulacion'], combustible['FUEL_EN_EL_DESTINO_LBS'], carga_req_aterrizaje)
    limite_peso_aterrizaje['max_ldg_weight_aterrizaje'] = float(limite_peso_aterrizaje['max_ldg_weight_aterrizaje'])
    limite_peso_aterrizaje['to_weight_aterrizaje'] = float(limite_peso_aterrizaje['to_weight_aterrizaje'])
    limite_peso_aterrizaje['carga_paga_limitada_aterrizaje'] = float(limite_peso_aterrizaje['carga_paga_limitada_aterrizaje'])
    limite_peso_aterrizaje['pasajeros_200_aterrizaje'] = float(limite_peso_aterrizaje['pasajeros_200_aterrizaje'])
    limite_peso_aterrizaje['pasajeros_220_aterrizaje'] = float(limite_peso_aterrizaje['pasajeros_220_aterrizaje'])
    limite_peso_aterrizaje['pasajeros_250_aterrizaje'] = float(limite_peso_aterrizaje['pasajeros_250_aterrizaje'])

    # Traer datos de peso real
    peso_real = calcular_peso_real(peso_carga, cantidad_pax_200, cantidad_pax_220, cantidad_pax_250, total_peso_pax_manual, peso['aeronave_tripulacion_combustible'], limite_peso_despegue['carga_paga_limitada_despegue'], limite_peso_aterrizaje['carga_paga_limitada_aterrizaje'])

    # Traer datos de driftdown
    driftdown = calcular_driftdown(peso_despegue, fuel_consumido, qnh_act, oat, fl)

    # Conversión de datos
    navegacion['tiempo_destino'] = navegacion['tiempo_destino'].strftime('%H:%M:%S')
    navegacion['tiempo_alterno'] = navegacion['tiempo_alterno'].strftime('%H:%M:%S')

    # Llenado de zero fuel weight
    peso['zero_fuel'] = peso['aeronave_tripulacion'] + peso_real['carga_disponible_limitado_despegue']

    # Llenado de datos de retorno
    result.update(navegacion)
    result.update(aeropuerto)
    result.update(combustible)
    result.update(peso)
    result.update(limite_peso_despegue)
    result.update(limite_peso_aterrizaje)
    result.update(peso_real)
    result.update(driftdown)

    # Ordenar diccionario
    result = dict(sorted(result.items()))

    return jsonify(result)

# Ruta de autenticación
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Falta el JSON en el body de la request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email:
        return jsonify({"msg": "Falta el correo"}), 400
    if not password:
        return jsonify({"msg": "Falta la contraseña"}), 400

    user = User.query.filter_by(email=email, password=password).first()
    if user is None:
        return jsonify({"msg": "Correo o contraseña incorrectos"}), 401

    user_data = {
        "id": user.id,
        "email": user.email,
        "access_token": create_access_token(identity=email)
    }

    return jsonify(user_data), 200
