import sqlite3
from faker import Faker
from random import randint
from faker.providers import job

def create_db():
    sql = None
    with open('tables.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

def create_record(conn, sql, values):
    cur = conn.cursor()
    try:
        cur.execute(sql, values)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid

def create_student(conn,profile):
    sql = "INSERT INTO students(name,age,gender,group_id) VALUES(?,?,?,?);"
    create_record(conn, sql, profile)

def create_group(conn,data):
    sql = "INSERT INTO groups(name) VALUES(?);"
    create_record(conn, sql, data)

def create_subject(conn,data):
    sql = "INSERT INTO subjects(name,teacher_id) VALUES(?,?);"
    create_record(conn, sql, data)

def create_teacher(conn,profile):
    sql = "INSERT INTO teachers(name,age,gender) VALUES(?,?,?);"
    create_record(conn, sql, profile)

def create_mark(conn,data):
    sql = "INSERT INTO marks(value,student_id,subject_id) VALUES(?,?,?);"
    create_record(conn, sql, data)

def fake_db_data():
    with sqlite3.connect('tables.db') as conn:
        for i in range(3):
            data = (f'Group {i + 1}',)
            create_group(conn,data)

        students = randint(30,50)
        for i in range(students):
            fake = Faker()
            profile = (fake.name(), randint(17,54), 'binary', randint(1,3))
            create_student(conn,profile)

        teachers = randint(3,5)
        for i in range(teachers):
            fake = Faker()
            profile = (fake.name(), randint(25,90), 'binary')
            create_teacher(conn,profile)
            
        subjects = randint(5,8)
        for i in range(subjects):
            fake = Faker()
            fake.add_provider(job)
            profile = (fake.job(), randint(1, teachers + 1))
            create_subject(conn,profile)

        for curr_stud in range(1, students + 1):
            for i in range(randint(1,20)):
                mark = (randint(1,12),curr_stud, randint(1, subjects + 1))
                create_mark(conn,mark)

if __name__ == '__main__':
    create_db()
    fake_db_data()
