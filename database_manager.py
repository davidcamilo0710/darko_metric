import os
import requests
import MySQLdb
from datetime import date

class DatabaseManager:
    def __init__(self, host, username, password, db_name, ssl_ca_path, token, chat_id):
        self.host = host
        self.username = username
        self.password = password
        self.db_name = db_name
        self.ssl_ca_path = ssl_ca_path
        self.connection = None
        self.cursor = None
        self.token = token
        self.chat_id = chat_id

    def connect(self):
        try:
            self.connection = MySQLdb.connect(
                host=self.host,
                user=self.username,
                passwd=self.password,
                db=self.db_name,
                autocommit=True,
                ssl_mode="VERIFY_IDENTITY",
                ssl={"ca": self.ssl_ca_path},
            )
            if self.connection:
                print("Conexión exitosa a la base de datos")
                self.cursor = self.connection.cursor()
            else:
                print("No se pudo establecer la conexión a la base de datos")
        except Exception as e:
            print("Error de conexión: {}".format(e))

    def test_connection(self):
        if self.connection:
            print("Conexión a la base de datos establecida.")
        else:
            texto_mensaje = "No hay conexión a la base de datos Darko."
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            print(texto_mensaje)
            params = {
                'chat_id': self.chat_id,
                'text': texto_mensaje
            }
            response = requests.post(url, params=params)
            print(response.json())

    def get_max_projection_date(self):
        if self.cursor:
            self.cursor.execute("SELECT COALESCE(MAX(date_of_projection), '1899-01-01') FROM darko_player_stats;")
            result = self.cursor.fetchone()
            max_date = result[0]
            print("Fecha máxima de proyección: {}".format(max_date))
            return max_date
        else:
            print("No hay cursor disponible. Conéctese a la base de datos primero.")

    def insert_player_stats(self, player_stats):
        if self.cursor:
            try:
                player_stats[-1] = date(*map(int, player_stats[-1].split('-')))
                query = """
                    INSERT INTO darko_player_stats 
                    (player_id, player_name, team_id, team_name, experience, minutes, pace, points, assists, defensive_rebounds, 
                    offensive_rebounds, blocks, steals, turnovers, field_goals_attempted, free_throws_attempted, 
                    three_pointers_attempted, rim_field_goals_attempted, personal_fouls, date_of_projection) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                self.cursor.execute(query, player_stats)
                print("Datos del jugador insertados correctamente.")
            except Exception as e:
                print("Error al insertar datos del jugador: {}".format(e))
        else:
            print("No hay cursor disponible. Conéctese a la base de datos primero.")

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Conexión cerrada.")
        else:
            print("No hay conexión para cerrar.")

# Fin de la clase DatabaseManager
