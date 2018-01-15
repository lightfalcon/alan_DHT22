import pymysql.cursors

# Connect to the database.
connection = pymysql.connect(host='localhost',
                             user='pi',
                             password='marte2122',
                             db='TempHumDB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print ("connect successful!!")

