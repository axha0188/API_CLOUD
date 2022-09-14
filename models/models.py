from database.database import db;
# TABLA DE ESTUDIANTE
class EstudianteModel(db.Model):
    id = db.Column(db.Integer,primary_key=True);
    cedula = db.Column(db.String(10),unique=True);
    nombre = db.Column(db.String(100));
    apellido = db.Column(db.String(100));
    edad = db.Column(db.Integer);
    def __init__(
        self,
        cedula: str,
        nombre: str,
        apellido:str,
        edad: int
    ) -> None:
        self.cedula = cedula;
        self.nombre = nombre;
        self.apellido = apellido;
        self.edad = edad;