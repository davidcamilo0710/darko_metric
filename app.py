import pymysql.cursors
import ssl

# Parámetros de conexión
db_host = "aws.connect.psdb.cloud"
db_username = "don13ns8ywrna64tfkzm"
db_password = "pscale_pw_sNqDzzeyfMs8C81DTn14seWpJ3fH8Ha6i3845yvsyGS"
db_name = "darko"
ca_cert_path = "/etc/ssl/certs/ca-certificates.crt"

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

