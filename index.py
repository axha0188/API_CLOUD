from app import app;
from database.database import db;
from configs import DEBUG,PORT

# CREAR EL ESQUEMA DE LA BASE DE DATOS
with app.app_context():
    db.create_all();

# INICIO DE LA APLICACION
if __name__ ==  "__main__":
    app.run(debug=DEBUG, port=PORT);