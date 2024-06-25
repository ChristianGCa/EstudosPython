import mysql.connector

def getConexao():
  con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="estoque"
  )
  return con
