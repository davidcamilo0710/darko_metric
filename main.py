import os
from database_manager import DatabaseManager
from datetime import date

# Definir parámetros de conexión
token = os.environ["BOT_TOKEN"]
chat_id = os.environ["TELEGRAM_CHANEL_ID"]
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]
ssl_ca_path = "/etc/ssl/certs/ca-certificates.crt"

# Crear una instancia de DatabaseManager
db_manager = DatabaseManager(db_host, db_username, db_password, db_name, ssl_ca_path, token, chat_id)

# Probar la conexión
db_manager.connect()
db_manager.test_connection()

# Obtener la fecha máxima de proyección
max_projection_date = db_manager.get_max_projection_date()

# Insertar datos de prueba (puedes definir tus propios datos aquí)
player_stats = (
    1, "Jugador1", 1, "Equipo1", "Experiencia1", 30.5, 100.0, 20.5, 5.5, 8.0,
    2.5, 1.0, 1.5, 2.0, 15.0, 10.0, 5.0, 7.0, 3.0, 4.0, date(max_projection_date)
)
db_manager.insert_player_stats(player_stats)

# Cerrar la conexión
db_manager.close_connection()
