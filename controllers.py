from json import dumps;
from models import EstudianteModel;
from database import db;
from schema import estudiante_schema,estudiantes_schema;

class EstudianteController:
    def AgregarEstudiante(
        self,
        cedula: str,
        nombre: str,
        apellido:str,
        edad: int
    ) -> dict:
        try:
            registro = EstudianteModel(cedula,nombre,apellido,edad);
            db.session.add(registro);
            db.session.commit();
            return { "mensaje": "registro guardado" , "estado": True };
        except Exception as e:
            return { "mensaje": str(e) , "estado": False };
        finally:
            db.session.close();
    def ListarEstudiantes(self) -> dict:
        try:
            registros = EstudianteModel.query.all();
            datos = estudiantes_schema.dump(registros);
            return { 
                "mensaje": "listado de todos los estudiantes",
                "datos": datos,  
                "estado": True 
            };
        except Exception as e:
            return { "mensaje": str(e) , "estado": False };
        finally:
            db.session.close();