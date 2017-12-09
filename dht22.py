import pymysql.cursors

# Connect to the database.
connection = pymysql.connect(host='192.168.1.73',
                             user='roberto',
                             password='marte2122',
                             db='dht22_alan',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print ("connect successful!!")

