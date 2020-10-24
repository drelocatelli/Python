import mysql.connector

db = input("Nome da db: ")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database=db
)

mycursor = mydb.cursor()

val = input("Digite um valor: ")
cmd = f'INSERT INTO log (log) VALUES ("{val}")'
sql = cmd
print(cmd)

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted")