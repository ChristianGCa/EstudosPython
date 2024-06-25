import mysql.connector
import banco

con = banco.getConexao()
cursor = con.cursor(prepared=True)

sql = "INSERT INTO cliente (id_cliente, nome_cliente, id_tipo_cliente) VALUES (default, ?, ?)"
par = [ ("Ana", 5),
        ("Maria", 5),
        ("Paulo", 5)
]

print(sql, par)
cursor.executemany(sql, par)
con.commit()
print(cursor.rowcount, "registros inseridos")

con.close