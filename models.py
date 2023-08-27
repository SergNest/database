from repository import select
import sqlite3
   
class Students:
    TABLE_NAME = 'students'
    def __init__(self, _id: int, name: str):
        self._id = _id
        self.name = name
    
    @classmethod
    def get_all_users_from_db(cls):
        users = list()
        for user_data in select(cls.TABLE_NAME):
            users.append(cls(_id=user_data[0],name=user_data[1]))
        return users

    @classmethod
    def the_highest_average_score(cls, limit: int):
        # with sqlite3.connect('todo.db') as con:
        #     cur = con.cursor()
        #     cur.execute(f"SELECT s.id, s.name, AVG(r.rate) AS average_rating FROM students s JOIN rating r ON s.id = r.students_id GROUP BY s.id, s.name ORDER BY average_rating DESC LIMIT {limit};")
        #     return cur.fetchall()
        with open('query_1.sql', 'r') as f:
            sql = f.read()

        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(sql)
            return cur.fetchall()
    
    @classmethod
    def get_top_student_for_subject(cls, subject_id):
        
        with open('query_2.sql', 'r') as f:
            sql = f.read()
        
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(sql, (subject_id,))
            
            result = cur.fetchone()
            return result
        
    @classmethod
    def get_average_rating_by_group(cls, subject_id):
        
        with open('query_3.sql', 'r') as f:
            sql = f.read()
        
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(sql, (subject_id,))
            
            result = cur.fetchall()
            return result
    
    @classmethod
    def get_students_in_group(cls, group_name):
        
        with open('query_6.sql', 'r') as f:
            sql = f.read()
        
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(sql, (group_name,))
            
            result = cur.fetchall()
            return result
        
    @classmethod
    def get_last_class_ratings_for_group_and_subject(cls, group_name, subject_name):
        
        with open('query_12.sql', 'r') as f:
            sql = f.read()
        
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(sql, (group_name, subject_name))
            
            result = cur.fetchall()
            return result
        
# print(Students.the_highest_average_score(5))
# print(Students.get_top_student_for_subject(2))
# print(Students.get_average_rating_by_group(2))
# print(Students.get_students_in_group('First'))
print(Students.get_last_class_ratings_for_group_and_subject('Second', 'Інженерія програмного забезпечення'))