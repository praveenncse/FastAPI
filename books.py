from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()
books=[
    {"id":1,"title":"Book 1","author":"Auhor1","price":"100"},
    {"id":2,"title":"Book 2","author":"Auhor2","price":"200"},
    {"id":3,"title":"Book 3","author":"Auhor3","price":"300"},
    {"id":4,"title":"Book 4","author":"Auhor1","price":"150"}
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    price: str


@app.get("/books")
async def show_books():
    return books

@app.get("/books/{book_author}/")
async def get_book_author(author:str,title:str):
    match=[]
    for b in books:
        if b.get('author') == author and b.get('title') == title:
            match.append(b)
    if match:
        return match
    return {"message":"Author or title not found"}

@app.post('/books/create')
async def create_book(book: Book = Body(...)):
    books.append(book.model_dump())
    return {"message": "Book created successfully"}