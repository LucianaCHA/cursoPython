import requests
from fastapi import Body, FastAPI
from typing import Union

app = FastAPI()

#https://fakestoreapi.com/docs
url : str = 'https://fakestoreapi.com/products'

#make a request to the url

response = requests.get(url)

# BOOKS = [
#     {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
#     {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
#     {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
#     {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
#     {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
#     {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
# ]


@app.get('/products')
async def get_all_products():
    '''
    Get all products from the fakestoreapi
    return: json'''
    return response.json()

@app.get('/product/{product_id}')
async def get_product_by_id(product_id: int):
    '''
    Get product by id from the fakestoreapi
    return: a single product as json 
    '''
    for product in response.json():
        if product.get('id') == product_id:
            return product
        
@app.get('/products/{keyword}')
async def get_products_by_keyword(keyword: str):
    '''
    Get products by keyword from the fakestoreapi looking in the title
    return: a list of products
    '''

    products_to_return = []
    for product in response.json():
        if keyword.casefold() in product.get('title').casefold():
            products_to_return.append(product)
    return products_to_return

@app.get('/products/bycategory/{category}')
async def get_products_by_category(category: str):
    '''
    Get products by category from the fakestoreapi
    return: json
    '''

    products_to_return = []
    for product in response.json():
        if category.casefold() in product.get('category').casefold():
            products_to_return.append(product)
    return products_to_return

#ver como mostrar queries opcoonales e documentacion

@app.get('/products/byprice/')
async def get_products_by_price_range(min_price: int, max_price: int, sort: str = 'asc', number_of_products: Union[int, None]= None):
    '''
    Get products between a range, sorted from min to max as default,
    and a number of products as default 10
    return: list of products
    '''

    products_to_return = []
    number_of_products = number_of_products if number_of_products else 10
    for product in response.json():
        if product.get('price') >= min_price and product.get('price') <= max_price:
            products_to_return.append(product)
    if sort == 'asc':
        products_to_return.sort(key=lambda x: x['price'])
    elif sort == 'desc':
        products_to_return.sort(key=lambda x: x['price'], reverse=True)
    return products_to_return[:number_of_products]

@app.post("/products/create_product")
async def create_product(product=Body(
    ...
)):
    '''
    Create a product in the fakestoreapi
    this is not a real post  it will return an object with a new id
    body example 
    {"title": "test product",
                    "price": 13.5,
                    "description": "lorem ipsum set",
                    "image": "https://i.pravatar.cc",
                    "category": "electronic"
                }
    '''
    try:
        response_post = requests.post(url, data=product, timeout=5)
    except requests.ConnectionError:
        return {'message': 'Error creating product'}
    return response_post.json()


@app.put("/products/update_product/{product_id}")
async def update_product(product_id: int, product=Body(
    ...
)):
    '''
    Update a product it will return an object with sent id but 
    the updated values won't persist
    {"title": "test product",
                    "price": 13.5,
                    "description": "lorem ipsum set",
                    "image": "https://i.pravatar.cc",
                    "category": "electronic"
                }
    '''
    try:
        response_put = requests.put(f'{url}/{product_id}', data=product, timeout=5)
    except requests.ConnectionError:
        return {'message': 'Error updating product'}
    return response_put.json()
