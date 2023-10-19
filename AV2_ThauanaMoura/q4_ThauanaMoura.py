import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="87444597"
)

crs = mydb.cursor()

execsqlcmd = lambda cmd, crs : crs.execute(cmd)

execcreatetable = lambda table, attrs, crs : execsqlcmd("CREATE TABLE " + table + "(" + attrs + ");\n", crs)
execcreatedatabase = lambda dbname, crs : execsqlcmd("CREATE DATABASE " + dbname + ";\n", crs)
execdropdatabase = lambda dbname, crs : execsqlcmd("DROP DATABASE " + dbname + ";\n", crs)
execdroptable = lambda table, crs : execsqlcmd("DROP TABLE " + table + ";\n", crs)
execusedatabase = lambda dbname, crs: execsqlcmd("USE " + dbname + ";\n", crs)
execselectfromwhere = lambda cols, table, where, crs : execsqlcmd("SELECT " + cols + " FROM " + table + " WHERE " + where + ";\n", crs)
execinsertinto = lambda table, cols, values, crs : execsqlcmd("INSERT INTO " + table + "(" + cols + ") VALUES (" + values + ");\n", crs)                                             

execdelete = lambda table, where, crs : execsqlcmd("DELETE FROM " + table + " WHERE " + where + ";\n", crs)

#execcreatedatabase("mydatabase", crs)
execusedatabase("mydatabase", crs)

#execcreatetable("USUARIOS", "id INT, nome VARCHAR(255), console VARCHAR(255)", crs)
#execcreatetable("JOGOS", "id INT, nome VARCHAR(255), data_lancamento DATE", crs)

execinsertinto("USUARIOS", "id, nome, console", "1, \"João\", \"Nintendo\"", crs)
execinsertinto("USUARIOS", "id, nome, console", "2, \"Maria\", \"xbox\"", crs)

execinsertinto("JOGOS", "id, nome, data_lancamento", "1, \"minecraft\", '2012-04-11'", crs)
execinsertinto("JOGOS", "id, nome, data_lancamento", "2, \"the sims\", '2017-05-12'", crs)

execselectfromwhere("*", "USUARIOS", "true", crs)

res = crs.fetchall()
print_result = lambda res : [print (x) for x in res]

print_result(res)

mydb.commit()
