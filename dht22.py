#!/usr/bin/python3
#Importando librerias necesarias
import pymysql.cursors
import time
import datetime
import Adafruit_DHT

#Importando configuracion general
from config import *

#Configuracion modelo de sensor DHT
sensor = Adafruit_DHT.DHT22

#Metodo para insertar un nuevo registro en la base de datos MariaDB
def insertDataToDB(temperatura, humedad):
        connection = pymysql.connect(host=MYSQL_SERVIDOR,
                               user=MYSQL_USUARIO,
                               password=MYSQL_CONTRASENA,
                               db=MYSQL_BD,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                #Create a new record
                sql = "INSERT INTO datos (fecha, temperatura, humedad) values (now(),'" + str(temperatura) + "','" + str(humedad) + "');"
                cursor.execute(sql)

            # connection is not autocommit by default. So we must commit to our changes
            connection.commit()
        except:
            connection.rollback()
        finally:
            connection.close()

# Ejecutando el flujo principal del programa
try:
        # Ciclo principal infinito
        while True:
                #Obtiene la humedad y la temperatura desde el sensor
                humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

                #Si se obtiene lectura, registrar en log (pending)

                #Si se obtiene lectura del sensor, crear un nuevo registro en la BD
                if humedad is not None and temperatura is not None:
                        insertDataToDB(temperatura,humedad)
                else:
                        print("Ha ocurrido un error")

                # Delay 10 segundos
                time.sleep(10)
except Exception:
    print("Error")


