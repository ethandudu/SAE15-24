import mysql.connector
import config

conn = mysql.connector.connect(host=config.host, user=config.user, password=config.password, database=config.database)
cursor = conn.cursor()

cursor.execute("TRUNCATE TABLE `frames`")
table = cursor.fetchall()

cursor.execute("INSERT INTO `frames` (`FileNumber`, `FrameNumber`, `Size`, `Type`) VALUES (%s, %s, %s, %s)", (0, 0, 0, "Ukn"))
conn.commit()

cursor.execute("TRUNCATE TABLE `arp`")
table = cursor.fetchall()
print("BDD nettoyée")