import os
import MySQLdb

# Parámetros de conexión
chromedriver_path = os.environ["CHROMEDRIVER_DIR"]
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]

print(chromedriver_path)
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
      cursor = connection.cursor()
      cursor.execute("SHOW TABLES;")
      tables = cursor.fetchall()
      if tables:
        print("Nombres de las tablas:")
        for table in tables:
          print(table[0])
      else:
        print("No hay tablas en la base de datos.")
  else:
      print("No se pudo establecer la conexión a la base de datos")
except Exception as e:
  print("Error de conexión: {}".format(e))
finally:
  if connection:
    cursor.close()
    connection.close()
    print("Conexión cerrada")
