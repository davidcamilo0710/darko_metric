import pymysql.cursors
import ssl
import os
# Parámetros de conexión
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]

print(db_host)
ca_cert_path = "./cacert.pem"
if os.path.exists(ca_cert_path):
    print("El certificado se encuentra en la ruta: {}".format(ca_cert_path))
else:
    print("El certificado NO se encuentra en la ruta: {}".format(ca_cert_path))
# Configuración de la conexión
ssl_context = ssl.create_default_context(cafile=ca_cert_path)
config = {
    "host": db_host,
    "user": db_username,
    "password": db_password,
    "database": db_name,
    "ssl": {"ssl_context": ssl_context},
}

try:
    # Intentar establecer la conexión
    connection = pymysql.connect(**config)

    # Comprobar si la conexión fue exitosa
    if connection.open:
        print("Conexión exitosa a la base de datos {}".format(db_name))
except Exception as e:
    print("Error de conexión: {}".format(e))
finally:
    # Cerrar la conexión
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Conexión cerrada")

