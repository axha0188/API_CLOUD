from flask import Flask,jsonify;
from flask_cors import CORS;
from flask_sqlalchemy import SQLAlchemy;
from flask_marshmallow import Marshmallow;
from routers.routers import estudiante;
from configs import CONEXION;

# INSTANCIA DEL APP
app = Flask(__name__);

# CORS
CORS(app);

# CONFIGURACION DE LA BASE DE DATOS MYSQL
app = Flask(__name__);
app.config["SQLALCHEMY_DATABASE_URI"] = CONEXION;
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False;
db = SQLAlchemy(app);

# ESQUEMA
ma = Marshmallow(app);

# REGISTRO DE RUTAS
app.register_blueprint(estudiante);

# RUTA DE PRUEBA
@app.route("/")
def Inicio():
    return jsonify({"mensajeapp": "hola mundo"})
    