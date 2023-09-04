import sqlite3
import datetime
con=sqlite3.connect("da.db")
curs=con.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS  deneme(tarih DATE)")
curs.execute("SELECT * from deneme where tarih BETWEEN ? and ?",("2015-01-01","2020-05-15"))
print(curs.fetchall())