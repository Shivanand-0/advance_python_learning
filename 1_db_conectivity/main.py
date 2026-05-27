import psycopg2


# step 1: connect to database
connection= psycopg2.connect(
    host='localhost',
    port='5432',
    database='postgres',
    user='postgres',
    password='shiva1234'
)

#step2: make cursor(its object or pointer to the databasewhich make changes) to execute the query.
cursor=connection.cursor()

#step3: preform operation
# #create 
# cursor.execute('INSERT INTO student(name, age, course) VALUES (%s,%s,%s)',('Elon',32,'Airospace'))
# connection.commit() # it confirms to perfom changes to database

# print('Record Inserted....')

# #Read
# cursor.execute('SELECT * FROM student')
# data=cursor.fetchall()
# print(data)

# # #Update
# cursor.execute('UPDATE student SET course=%s WHERE id=%s',('React',3))
# connection.commit()

# Delete
cursor.execute('DELETE student WHERE id=%s',(3,))
connection.commit()