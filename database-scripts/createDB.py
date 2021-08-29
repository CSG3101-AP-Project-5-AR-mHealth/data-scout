import mysql.connector

db = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password=''
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE vitalsdb")
cursor.execute("USE vitalsdb")
cursor.execute("DROP TABLE IF EXISTS vitals;")
cursor.execute("CREATE TABLE vitals (id int(11) NOT NULL,"+
  "heart_rate int(11) NOT NULL," +
  "body_temp int(11) NOT NULL," +
  "time timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()" +
");")

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)