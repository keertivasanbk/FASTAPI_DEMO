from fastapi import FastAPI,HTTPException,Form
from enum import Enum
from typing import *

app = FastAPI()

BOOKS={
    'book_1':{'title':'title one','author':'author one'},
    'book_2':{'title':'title two','author':'author two'},
    'book_3':{'title':'title three','author':'author three'},
    'book_4':{'title':'title four','author':'author four'},
    'book_5':{'title':'title five','author':'author five'},
}



class DirectionName(str,Enum):    #it is an dropdown model
    north='north'
    south='south'
    east='east'
    west='west'

@app.get('/direction/{directionName}')                        # to display or to retrieve the model
async def get_direction(directionName:DirectionName):
    if directionName==DirectionName.north:
        return{'direction':directionName}
    if directionName==DirectionName.south:
        return{'direction':directionName}
    if directionName==DirectionName.west:
        return{'direction':directionName}
    return{'direction':directionName}
@app.get("/")
async def read_all_books(skip_book: Optional[str]=None):
    if skip_book:
        New_bk=BOOKS.copy()
        del New_bk[skip_book]
        return New_bk
    return BOOKS

@app.get('/{book_name}')            # to get the book list
async def read_book(book_name:str):
    return BOOKS[book_name]



@app.get('/books/mybook')
async def read_fav_book():
    return {'book_title':'my favourite book'}

@app.get('/books/{book_id}')
async def read_book(book_id:int):
    return {'book_title':book_id}


@app.post('/')
async def create_book(book_title,book_author):
    current_book_id=0

    if len(BOOKS) > 0:
        for book in BOOKS:
            x=int(book.split('_')[-1])
            if x> current_book_id:
                current_book_id=x
    BOOKS[f'book_{current_book_id +1 }']={'title':book_title,'author':book_author}
    return BOOKS[f'book_{current_book_id + 1}']

@app.put('/')
async def update_book(book_name:str,title:str,author:str):
    info_book={"title":title,"author":author}
    BOOKS[book_name]=info_book
    return info_book

@app.delete('/{final}')
async def delete_book(book_name:str):
    if book_name in BOOKS:
        final=BOOKS.copy()
        del final[book_name]
        return final
    raise HTTPException(status_code=404,detail="book not found please enter valid book",headers={'x-header-error':'nothing'})

@app.post('/books/login')
async def books_login(username:str=Form(),password:str=Form()):
    return{"username":username,"password":password}





