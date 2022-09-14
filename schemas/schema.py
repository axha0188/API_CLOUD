from flask_marshmallow import Marshmallow;

sm = Marshmallow();

class EstudianteSchema(sm.Schema):
    class Meta:
        fields = ('id','cedula','nombre','apellido','edad');

estudiante_schema = EstudianteSchema();
estudiantes_schema = EstudianteSchema(many=True);

