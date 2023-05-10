from fastapi import FastAPI, Body

app = FastAPI() # instancia de fastapi

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books/mybook")#  decorador indic que es un verbo htt vinvulado a una ruta 
async def get_books():
    return BOOKS

@app.get('/books/{dynamic_params}')
async def get_books(dynamic_params : str):
    return {"'dynamic params'" : dynamic_params}

@app.get('/books/{title}')# dinamic parameters
async def get_book(title : str):
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold():
            return book

#query parameters
@app.get('/books/')

async def read_category_bby_query(category : str): # url /books/?category=maths
    books_to_return =[]
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
#post 

@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book')
async def update_book(updated_book =Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete(('/books/delete/{title}'))
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

        