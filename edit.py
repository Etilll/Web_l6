import sqlite3
from contextlib import contextmanager

database = './test.db'

@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()

def select_table(conn, name:str):
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM " + name)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_table_by(conn, name:str, field_name:str, field_value:str):
    rows = None
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM {name} WHERE {field_name}=?", (field_value))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def edit_table(conn, sql, parameters):
    cur = conn.cursor()
    try:
        cur.execute(sql, parameters)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()

if __name__ == '__main__':
        ###Update call:
        # sql = "UPDATE tablename SET priority = ?, begin_date = ?, end_date = ? WHERE id = ?"
        # parameters = ('1','2','3')
        # edit_table(conn, sql, parameters)
        ###Delete seqence:
        #sql = 'DELETE FROM tablename WHERE id=?'
        # parameters = ('1')
        # edit_table(conn, sql, parameters)
    with create_connection(database) as conn:
        pass