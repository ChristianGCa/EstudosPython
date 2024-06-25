import mysql.connector
import banco

con = banco.getConexao()
cursor = con.cursor()

sql = "INSERT INTO cliente (id_cliente, nome_cliente, id_tipo_cliente) VALUES (default, %s, %s)"
par = ("Dionatan", 5)
cursor.execute(sql, par)

con.commit()

print(cursor.rowcount, "registro inserido")
print("id_cliente:", cursor.lastrowid)

con.close