from fastapi import FastAPI


app = FastAPI()

@app.get('/') # el metodo 
async def index(): # la corutina/ vista 
    return {'key': 'value'}