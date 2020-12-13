import sqlite3
import time

try:
    sqliteconn = sqlite3.connect("sql.db")
    cursor = sqliteconn.cursor()
    print("__DB created__")

    my_execution = sqliteconn.execute("create a table netzwerkDB('id'integer,'name'string,'contact number'integer,)""")

    sql_insert = """insert into netzwerk DB
                   (id,name,contactnumber)

                   values
                   (2,'sree sudha',9390435012)"""
                   

    count = cursor.execute(sql_insert)
    sqliteconn.commit()
    print("data hasbeen inserted")
    cursor.close()

except sqlite3.error as c:
    print("__failed__",c)

finally:
    if(sqliteconn):
        sqliteconn.close()
        print("the sql connection is close")
    
