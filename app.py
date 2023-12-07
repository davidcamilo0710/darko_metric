import mysql.connector
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
