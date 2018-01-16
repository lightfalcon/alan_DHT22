# Configuracion para sensor DHTxx
#
# Estas variables se sobre escriben en el archivo config_local.py
# que debe contener estas mismas variables exceptuando las 5
# ultimas lineas

# Configuracion del puerto GPIO al cual esta conectado (GPIO 23)
pin = 4

# Configuracion de la carpeta para la creacion de los archivos log
log_path = "/var/log/alan_DHT22/"

# Configuracion credenciales MySQL
MYSQL_SERVIDOR = "localhost"
MYSQL_BD = "TempHumDB"
MYSQL_USUARIO = "pi"
MYSQL_CONTRASENA = "marte2122"

# Carga la configuracion local desde el archivo config_local.py
#try:
#	from config_local import *
#except Exception, e:
#	print str(e)