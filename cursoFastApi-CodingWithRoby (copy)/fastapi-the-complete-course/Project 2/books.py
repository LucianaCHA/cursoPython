from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status
app = FastAPI()


class Book():
    id: int
    title: str
    author: str
    description: str
    published_date: int
    rating: int

    def __init__(self, id, title, author, description, published_date, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.published_date = published_date
        self.rating = rating


# class BaseModel:


class BookRequest(BaseModel):
    id: Optional[int] = Field(title='Id is not needed')
    title: str = Field(min_length=3, title="Books's title")
    author: str = Field(min_length=3, title="Books's author")
    description: str = Field(min_length=3, max_length=100,title="Books's summay or backpage")
    published_date: int = Field(gt=1900 , lt =2023)
    rating: int = Field(gt=0, lt=6)
    
    class Config:
        schema_extra ={
            'example': {
                'title': 'A title',
                'author': 'Lola Mola',
                'description': 'A funny book',
                'published_date': 2012,
                'rating': 4
            }
        }

BOOKS = [Book(1, 'Computer Science Introduction Book', 'John Doe', 'This is a book about computer science',2000, 5),
         Book(2, 'Gone with the wind', 'Margaret Mitchell',
              'This is a book about the civil war',1936, 4),
         Book(3, 'The fault in our stars', 'John Green',
              'This is a book about cancer',2012, 5),
         Book(4, 'The Hobbit', 'J.R.R. Tolkien',
              'This is a book about a hobbit and his adventures',1937, 5),
         Book(7, 'Neuroscience', 'Dale Purves',
              'This is a book about the brain',2004, 5),
         Book(12, 'Neuromancer', 'William Gibson',
              'This is a book about the future',1984, 5),
         Book(13, 'The Hitchhiker\'s Guide to the Galaxy',
              'Douglas Adams', 'This is a book about the galaxy', 1978, 5),
         Book(172, 'Bestiario', 'Julio Cortazar',
              'This is a book about ... not really sure',1951, 5),
         Book(451, 'Sissyphus', 'Albert Camus',
              'This is a book about the meaning of life',1942, 2),
         ]


@app.get('/books', status_code=status.HTTP_200_OK)
def read_all_books():
    return BOOKS

@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
def book_by_id(book_id : int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Book not found')

@app.get('/books/byyear/', status_code=status.HTTP_200_OK)
def get_books_by_published_year(year: int= Query(gt=1900 , lt =2023)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == year:
            books_to_return.append(book)
    return books_to_return

@app.get('/books/', status_code=status.HTTP_200_OK)
def get_books_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating :
            books_to_return.append(book)
    return books_to_return

@app.post('/new-book',status_code=status.HTTP_201_CREATED)
def create_new_book(book_request: BookRequest):
    # esto pasa el par clave valor del parametro en el constructor de la clase para inicializarlo
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    # book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1 #estilo ternario

    return book

@app.put('/books/update_book', status_code=status.HTTP_204_NO_CONTENT)
def update_book(updated_book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == updated_book.id:
            BOOKS[i] = updated_book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Book not found')

@app.delete('/books/{book_id}')
def delete_book(book_id : int = Path(gt=0)):
    book_changed : bool = False
    for i in range(len(BOOKS)):
       if BOOKS[i].id == book_id:
           BOOKS.pop(i)
           book_changed = True
           break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Book not found')
