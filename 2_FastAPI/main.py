from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel

app=FastAPI()
connection=psycopg2.connect(
    host='localhost',
    port='5432',
    database='postgres',
    user='postgres',
    password='shiva1234'
)

print('db connectd..')
cursor=connection.cursor()


class Student(BaseModel):
    name:str
    age:int
    course:str

class PatchStudent(BaseModel):
    name:str=None # default value null
    age:int=None
    course:str=None    

@app.get('/')
def home():
    return "haha"


@app.get('/students')
def get_students():
    cursor.execute('SELECT * FROM student')
    data=cursor.fetchall()
    return data


@app.get('/students/{id}')
def get_unique_student(id: int):
    cursor.execute('SELECT * FROM student WHERE id=%s',(id,))
    data=cursor.fetchone()
    return {
        "id":data[0],
        "name":data[1],
        "age":data[2],
        "course":data[3],
    }

@app.post('/students')
def add_student(student: Student):
    data=student
    cursor.execute('INSERT INTO student(name,age,course) VALUES (%s,%s,%s)',(data.name,data.age,data.course))
    connection.commit()
    return f"Successfully added:{data}"
    print(data)


@app.put('/students/{id}')
def update_student_data(id: int, student:Student):
    cursor.execute('UPDATE student SET name=%s, age=%s, course=%s WHERE id=%s',(student.name,student.age,student.course,id))
    connection.commit()
    return f"Successfully updated :{student}"
    

@app.patch('/students/{id}')
def update_student_data(id: int,student: PatchStudent):
    if(student.name!=None):
        cursor.execute('UPDATE student SET name=%s WHERE id=%s',(student.name,id))
        connection.commit()
    if(student.age!=None):
        cursor.execute('UPDATE student SET age=%s WHERE id=%s',(student.age,id))
        connection.commit()
    if(student.course!=None):
        cursor.execute('UPDATE student SET course=%s WHERE id=%s',(student.course,id))
        connection.commit()
    return f"Successfully updated Partially"


