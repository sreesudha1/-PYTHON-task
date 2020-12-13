import sqlite3

def insert(id,name,salary,joindate,email):


    try:
        sqliteconnect = sqlite3.connect('SQLite_python.db')
        cursor = sqliteconnect.cursor()
        print("connect to SQLite")
        sqlite_insert = """insert to sql_DB
                         (id,name,salary,joindate,email)

                         VALUES
                         (345,sreesudha,30000,june2021,sreesudha1997@gmail.com)"""
        count=cursor.execute(sqlite_insert)
        sqliteconnect.commit()
        print("python variables are inserted")

        cursor.close()
    except sqlite3.error as e:
        print("failed to insert python",e)

    finally:
        if (sqliteconnect):
            sqliteconnect.close()
            print("the SQLite connect is closed")
