import mysql.connector
from configmysq import DB_CONFIG

conexion = mysql.connector.connect(**DB_CONFIG)

print(conexion)
