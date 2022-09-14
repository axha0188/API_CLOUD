from flask import Blueprint,jsonify,request;
from controllers.controllers import EstudianteController;

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

@estudiante.route("/api/estudiante/obtener/<filtro>")
def ObtenerEstudianteAsync(filtro):
    respuesta = EstudianteController().ObtenerEstudiante(filtro);
    return jsonify(respuesta);

@estudiante.route("/api/estudiante/editar",methods=['PUT'])
def EditarEstudianteAsync():
    id = request.json['id'];
    cedula = request.json['cedula'];
    nombre = request.json['nombre'];
    apellido = request.json['apellido'];
    edad = request.json['edad'];
    respuesta = EstudianteController().EditarEstudiante(
        id,cedula,nombre,apellido,edad
    );
    return jsonify(respuesta);

@estudiante.route("/api/estudiante/eliminar/<id>",methods=['DELETE'])
def EliminarEstudianteAsync(id):
    respuesta = EstudianteController().EliminarEstudiante(id);
    return jsonify(respuesta);


