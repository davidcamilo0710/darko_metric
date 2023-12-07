import os
import MySQLdb

# Parámetros de conexión
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]

connection = MySQLdb.connect(
  host= db_host,
  user= db_username,
  passwd= db_password,
  db= db_name,
  autocommit = True,
  ssl_mode = "VERIFY_IDENTITY",
  ssl      = {
    "ca": "/etc/ssl/certs/ca-certificates.crt"
  }
)
  
