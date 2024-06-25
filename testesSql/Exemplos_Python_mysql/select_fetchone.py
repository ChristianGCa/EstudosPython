import mysql.connector
import banco

con = banco.getConexao()
cursor = con.cursor()

sql = "select * from cliente"
cursor.execute(sql)

resultado = cursor.fetchone()
print(type(resultado))
print("\n")
print(resultado)

con.close