from models.models import EstudianteModel;
from database.database import db;
from schemas.schema import estudiante_schema,estudiantes_schema;

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
            db.session.rollback();
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
    def ObtenerEstudiante(self,filtro: str) -> dict:
        try:
            registro = EstudianteModel.query.filter_by(
                cedula=filtro
            ).first();
           
            datos = estudiante_schema.dump(registro);
            if datos == {}:
                return { 
                "mensaje": "estudiante no encontrado",
                "datos": datos,  
                "estado": True 
                };
            return { 
                "mensaje": "estudiante encontrado",
                "datos": datos,  
                "estado": True 
            };
        except Exception as e:
            return { "mensaje": str(e) , "estado": False };
        finally:
            db.session.close();
    def EditarEstudiante(
        self,
        id:int,
        cedula: str,
        nombre: str,
        apellido:str,
        edad: int
    ) -> dict:
        try:
            registro = EstudianteModel.query.get(id);
            registro.cedula=cedula;
            registro.nombre=nombre;
            registro.apellido=apellido;
            registro.edad=edad;
            datos = estudiante_schema.dump(registro);
            db.session.commit();
            return { 
                "mensaje": "registro editado",
                "datos": datos,   
                "estado": True 
            };
        except Exception as e:
            db.session.rollback();
            return { "mensaje": str(e) , "estado": False };
        finally:
            db.session.close();
    def EliminarEstudiante(self, id:int) -> dict:
        try:
            registro = EstudianteModel.query.get(id);
            db.session.delete(registro);
            db.session.commit();
            return { 
                "mensaje": "registro eliminado",  
                "estado": True 
            };
        except Exception as e:
            db.session.rollback();
            return { "mensaje": str(e) , "estado": False };
        finally:
            db.session.close();
    