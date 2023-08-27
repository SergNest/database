import sqlite3

from faker import Faker 
import random
import datetime

def create_db():
    with open('init_todo.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(sql)



def populate_db():
    users_sql_command = "\n".join(f"INSERT INTO students (name, students_groups) VALUES ('{Faker(locale='uk_UA').name()}', '{random.randint(1, 3)}');" for _ in range(30))
    teachers_sql_command = "\n".join(f"INSERT INTO teachers (name) VALUES ('{Faker(locale='uk_UA').name()}');" for _ in range(5))
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(users_sql_command)
        cur.execute("SELECT id from students;")
        user_ids = [obj[0] for obj in cur.fetchall()]        
        print(user_ids)

        cur.executescript(teachers_sql_command)
        cur.execute("SELECT id from teachers;")
        teachers_ids = [obj[0] for obj in cur.fetchall()]        
        # print(teachers_ids)

        groups_list = ['First', 'Second', 'Third']

        for gp in groups_list:
            cur.executescript(f"INSERT INTO students_groups (name) VALUES ('{gp}')") 
        
        subjects_list = ['Прикладна математика', 'Інженерія програмного забезпечення', 'Комп’ютерні науки та інформаційні технології' 'Комп’ютерна інженерія', 
         'Кібербезпека', 'Інформаційні системи та технології', 'Іноземна мова', 'Історія України']
        for sb in subjects_list:
            cur.executescript(f"INSERT INTO subjects (name, teachers_id) VALUES ('{sb}', {random.choice(teachers_ids)})")
        cur.execute("SELECT id from subjects;")
        subjects_ids = [obj[0] for obj in cur.fetchall()]

        start_date = datetime.datetime(2023, 1, 1)
        end_date = datetime.datetime(2023, 8, 25)

        rating_sql_command = "\n".join(f"INSERT INTO rating (rate, students_id, subjects_id, created_at) VALUES ({random.randint(1, 5)}, {random.choice(user_ids)}, {random.choice(subjects_ids)}, '{random_date(start_date, end_date)}');" for i in range(100) )
        cur.executescript(rating_sql_command)
    
def check_db():
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from students;")
        result = cur.fetchall()
    print(result)

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    
    random_datetime = start + datetime.timedelta(seconds=random_second)
    formatted_datetime = random_datetime.strftime("%m/%d/%Y, %H:%M:%S")
    
    return formatted_datetime

def select(table_name:str, condition=None):
    if condition is not None:
        querry = f"SELECT * FROM {table_name} WHERE {condition};"
    else:
        querry = f"SELECT * FROM {table_name};"


    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        result = cur.fetchall()
    return result

def delete(table_name:str, condition=None):
    if condition is not None:
        querry = f"DELETE  FROM {table_name} WHERE {condition};"
    else:
        querry = f"DELETE  FROM {table_name};"


    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        result = cur.fetchall()
    return result



def init_db():
    create_db()
    populate_db()
    # check_db()

    init_db()