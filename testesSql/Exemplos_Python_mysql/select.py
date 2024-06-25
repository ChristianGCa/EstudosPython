import mysql.connector
import banco

con = banco.getConexao()
cursor = con.cursor()

sql = "select * from cliente"
cursor.execute(sql)

resultado = cursor.fetchall()
print(type(resultado))
print("\n")

for x in resultado:
  print(x)

con.close