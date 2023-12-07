import os
import MySQLdb

# Parámetros de conexión
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]

try:
  connection = MySQLdb.connect(
    host=db_host,
    user=db_username,
    passwd=db_password,
    db=db_name,
    autocommit=True,
    ssl_mode="VERIFY_IDENTITY",
    ssl={
        "ca": "/etc/ssl/certs/ca-certificates.crt"
    }
  )
  if connection:
      print("Conexión exitosa a la base de datos")
  else:
      print("No se pudo establecer la conexión a la base de datos")
except Exception as e:
  print("Error de conexión: {}".format(e))
finally:
  if connection:
    connection.close()
    print("Conexión cerrada")
