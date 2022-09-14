from dotenv import dotenv_values

CONFIG = dotenv_values(".env");

CONEXION = CONFIG['CONECCTION'];
DEBUG = CONFIG['DEBUG'] == 'TRUE';
PORT = CONFIG['PORT'];

