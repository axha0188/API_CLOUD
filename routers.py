from flask import Blueprint,jsonify,request;
from controllers import EstudianteController;

estudiante = Blueprint("estudiante",__name__);

@estudiante.route("/api/estudiante/agregar",methods=['POST'])
def AgregarEstudianteAsync():
    cedula = request.json['cedula'];
    nombre = request.json['nombre'];
    apellido = request.json['apellido'];
    edad = request.json['edad'];
    respuesta = EstudianteController().AgregarEstudiante(
        cedula,nombre,apellido,edad
    )
    return jsonify(respuesta);

@estudiante.route("/api/estudiante/listartodos")
def ListarEstudiantesAsync():
    respuesta = EstudianteController().ListarEstudiantes();
    return jsonify(respuesta);


