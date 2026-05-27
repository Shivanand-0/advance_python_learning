from fastapi import FastAPI, HTTPException, status
import psycopg2
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_load_env, load_dotenv

# Load variables from the .env file
load_dotenv()
app = FastAPI(title="Library Management System")

# Establish connection to your PostgreSQL database
connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)


print('Database connected successfully...')
cursor = connection.cursor()

# Automatically create the 'books' table if it doesn't exist on startup
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        published_year INT NOT NULL,
        isbn VARCHAR(50) UNIQUE NOT NULL
    );
''')
connection.commit()


# --- Pydantic Schemas for Request Body Validation ---

class Book(BaseModel):
    title: str
    author: str
    published_year: int
    isbn: str

class PatchBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None
    isbn: Optional[str] = None


# --- API Endpoints ---

@app.get('/')
def home():
    return {"message": "Welcome to the Library Management System"}


# 1. READ ALL BOOKS (GET)
@app.get('/books')
def get_all_books():
    cursor.execute('SELECT * FROM books ORDER BY id ASC')
    data = cursor.fetchall()
    
    # Map the tuples back to readable dictionaries
    books_list = []
    for row in data:
        books_list.append({
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "published_year": row[3],
            "isbn": row[4]
        })
    return books_list


# 2. READ A SINGLE BOOK BY ID (GET)
@app.get('/books/{id}')
def get_book_by_id(id: int):
    cursor.execute('SELECT * FROM books WHERE id=%s', (id,))
    data = cursor.fetchone()
    
    if data is None:
        raise HTTPException(status_code=404, detail="Book not found")
        
    return {
        "id": data[0],
        "title": data[1],
        "author": data[2],
        "published_year": data[3],
        "isbn": data[4]
    }


# 3. ADD A NEW BOOK (POST)
@app.post('/books', status_code=status.HTTP_201_CREATED)
def add_book(book: Book):
    try:
        cursor.execute(
            'INSERT INTO books (title, author, published_year, isbn) VALUES (%s, %s, %s, %s) RETURNING id',
            (book.title, book.author, book.published_year, book.isbn)
        )
        generated_id = cursor.fetchone()[0]
        connection.commit()
        return {"message": f"Successfully added book with ID: {generated_id}", "book": book}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=f"Database Error: {str(e)}")


# 4. COMPLETE UPDATE (PUT)
@app.put('/books/{id}')
def update_complete_book(id: int, book: Book):
    cursor.execute(
        'UPDATE books SET title=%s, author=%s, published_year=%s, isbn=%s WHERE id=%s',
        (book.title, book.author, book.published_year, book.isbn, id)
    )
    connection.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
        
    return {"message": f"Successfully updated book ID {id}", "updated_data": book}


# 5. PARTIAL UPDATE (PATCH)
@app.patch('/books/{id}')
def patch_book_data(id: int, book: PatchBook):
    # Convert Pydantic model into a dictionary, skipping values that weren't supplied (None)
    update_data = book.model_dump(exclude_unset=True)
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields provided for update")
        
    # Dynamically build SQL SET statement based on incoming attributes
    set_clause = ", ".join([f"{key}=%s" for key in update_data.keys()])
    values = list(update_data.values())
    values.append(id) # Add ID for the WHERE constraint
    
    query = f"UPDATE books SET {set_clause} WHERE id=%s"
    
    cursor.execute(query, tuple(values))
    connection.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
        
    return {"message": "Successfully updated partially", "updated_fields": update_data}


# 6. DELETE A BOOK (DELETE)
@app.delete('/books/{id}', status_code=status.HTTP_200_OK)
def delete_book(id: int):
    cursor.execute('DELETE FROM books WHERE id=%s', (id,))
    connection.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
        
    return {"message": f"Successfully deleted book with ID {id}"}