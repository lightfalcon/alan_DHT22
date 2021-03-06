#!/usr/bin/python

#Importando librerias necesarias
import sys
import MySQLdb
import time
import datetime
import Adafruit_DHT

#Importando configuracion general
from config import *

#Configuracion modelo de sensor DHT
sensor = Adafruit_DHT.DHT22

#Metodo para insertar un nuevo registro en la base de datos MariaDB
def insertDataToDB(temperatura, humedad):
        connection = MySQLdb.connect(host=MYSQL_SERVIDOR,
                        user=MYSQL_USUARIO,
                        passwd=MYSQL_CONTRASENA,
                        db=MYSQL_BD)

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
            connection.close

# Ejecutando el flujo principal del programa
try:
        # Ciclo principal infinito
        while True:
                #Obtiene la humedad y la temperatura desde el sensor
                humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

                #Si se obtiene lectura, registrar en log (pending task)

                #Si se obtiene lectura del sensor, crear un nuevo registro en la BD
                if humedad is not None and temperatura is not None:
                        insertDataToDB(temperatura,humedad)
                else:
                        print("Ha ocurrido un error")#Mejorar mensajes de log

                #Delay 10 segundos
                time.sleep(10)
except Exception:
    print("Error")


