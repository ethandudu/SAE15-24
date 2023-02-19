import mysql.connector
import config
conn = mysql.connector.connect(host=config.host, user=config.user, password=config.password, database=config.database)
cursor = conn.cursor()

#recup de donnée dans la bdd
cursor.execute("SELECT * FROM `table`")
table = cursor.fetchall()