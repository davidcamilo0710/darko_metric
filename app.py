import mysql.connector

config = {
    "host": "aws.connect.psdb.cloud",
    "user": "5tdoaohudj6ik07ht98u",
    "password": "pscale_pw_EROWJXUbgQQHA5dUQpnrD8Z0Ue5UperUDrMqjDkGo4t",
    "database": "darko",
    "autocommit": True,
    "ssl_mode": "VERIFY_IDENTITY",
    "ssl_ca": "/etc/ssl/certs/ca-certificates.crt",
}

try:
    # Intentar establecer la conexión
    connection = mysql.connector.connect(**config)

    # Comprobar si la conexión fue exitosa
    if connection.is_connected():
        print("Conexión exitosa a la base de datos 'darko'")
except Exception as e:
    print("Error de conexión: {}".format(e))
finally:
    # Cerrar la conexión
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexión cerrada")
