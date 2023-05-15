import json
from typing import Union, Optional, List
from fastapi import FastAPI, HTTPException, Path, Query
from starlette import status
import requests

from pydantic import BaseModel, Field, validator


app = FastAPI()

# utils


def validate_decimal_places(value, decimal_places) -> Union[int, float]:
    '''Check if a float number has more than decimal_places decimal positions'''
    if value % 1 != 0 and len(str(value).split('.')[-1]) > decimal_places:
        raise ValueError(
            f"Max of decimal positions must be at most {decimal_places}")
    return value

# models


class Product(BaseModel):
    '''Product model'''

    @validator('price')
    def check_two_decimals(cls, price):
        '''Check if rate has more than 2 decimal positions'''
        return validate_decimal_places(price, 2)

    @validator('min_price', 'max_price', check_fields=False)
    def min_max_validator(cls, min_price, max_price):
        # min_price, max_price = values
        if min_price > max_price:
            raise ValueError('Min price must be less than max price')
        return min_price, max_price

    id: Optional[int] = Field(title='Id is not needed')
    title: str = Field(min_length=3, title="Product's name")

    price: float = Field(gt=0, title='Product price', allow_reuse=True)

    description: str = Field(
        min_length=3, title="Product's name")
    category: str = Field(min_length=3)
    image: str = Field(min_length=3, title='image url')

    class Config:
        '''Config class'''
        schema_extra = {
            'example': {
                'title': 'A title',
                'price': 12.99,
                'description': 'A fancy prduct',
                'category': 'electronics',
                'image': 'https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg',
                'rating': {
                    'rate': 4.5,
                    'count': 120
                }
            }

        }


# https://fakestoreapi.com/docs
url: str = 'https://fakestoreapi.com/products'


def get_response(url_request: str):
    '''
    Try to make a request to url provided as parameter
    Return whatever the url response is
    '''
    try:
        # Set a timeout value because pylint se queja 0-0
        response = requests.get(url_request, timeout=5)
        response.raise_for_status()
    except requests.HTTPError as err:
        # HTTP (4XX or 5XX)
        # (este from err es opcional pero pylint se queja si no le explicito de donde viene el error \*_*/))
        raise SystemExit(err) from err
    except requests.Timeout as err:
        raise SystemExit(f"Request timed out: {err}") from err
    except requests.RequestException as err:
        # el resto, estará bien así ?
        raise SystemExit(f"Network error occurred: {err}") from err
    return response


api_response = get_response(url).json()

products_list: List[Product] = [Product(**product) for product in api_response]


@app.get('/products', status_code=status.HTTP_200_OK)
def get_all_products() -> List[Product]:
    '''
    Get all products from the fakestoreapi
    return a Products list
    '''

    return products_list
    # my_product = Product(
    #     id=api_response[0]['id'],
    #     title=api_response[0]['title'],
    #     price=api_response[0]['price'],
    #     description=api_response[0]['description'],
    #     category=api_response[0]['category'],
    #     image=api_response[0]['image'],

    # )
    # print(my_product)

    # list_my_products = [Product(**product) for product in api_response]

    # return list_my_products


@app.get('/product/{product_id}', status_code=status.HTTP_200_OK)
def get_product_by_id(product_id: int = Path(gt=0)) -> Product:
    '''
    Get product by id from the fakestoreapi
    return: a single product as json
    '''
    for product in products_list:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail='Product not found')


@app.get('/products/{keyword}', status_code=status.HTTP_200_OK)
def get_products_by_keyword(keyword: str = Path(min_length=3)) -> List[Product]:
    '''
    Get products by keyword from the fakestoreapi looking in the title
    return: a list of products
    '''

    products_to_return: List[Product] = []
    for product in products_list:
        if keyword.casefold() in product.title.casefold():
            products_to_return.append(product)
    return products_to_return


@app.get('/products/filter-by/', status_code=status.HTTP_200_OK)
def get_selected_products(
        category: Union[str, None] = Query(None, min_length=3, max_length=15),
        min_price: Union[float, None] = Query(None, gt=0),
        max_price: Union[float, None] = Query(None, gt=0),
        keyword: Union[str, None] = Query(None, min_length=3, max_length=15),
        sort: str = 'asc') -> List[Product]:
    '''
    Get products by category,
    price range and keyword, sorted by increasing (default) or decreasing price
    return: json
    '''

    products_to_return: List[Product] = []
    if category:
        for product in products_list:
            if category.casefold() in product.category.casefold():
                products_to_return.append(product)
    if min_price and max_price:
        for product in products_list:
            if product.price >= min_price and product.price <= max_price:
                products_to_return.append(product)
    if min_price and not max_price:
        for product in products_list:
            if product.price >= min_price:
                products_to_return.append(product)

    if max_price and not min_price:
        for product in products_list:
            if product.price <= max_price:
                products_to_return.append(product)
    if keyword:
        for product in products_list:
            if keyword.casefold() in product.title.casefold():
                products_to_return.append(product)
    if sort == 'asc':
        products_to_return.sort(key=lambda x: x.price)
    elif sort == 'desc':
        products_to_return.sort(key=lambda x: x.price, reverse=True)

    return products_to_return

# ver como mostrar queries opcoonales e documentacion


@app.get('/products/byprice/', status_code=status.HTTP_200_OK)
def get_products_by_price_range(
    min_price: int, max_price: int, sort: str = 'asc', number_of_products: Union[int, None] = None
) -> List[Product]:
    '''
    Get products between a range, sorted from min to max as default,
    and a number of products as default 10
    return: list of products
    '''

    products_to_return = []
    number_of_products = number_of_products if number_of_products else 10
    for product in products_list:
        if product.price >= min_price and product.price <= max_price:
            products_to_return.append(product)
    if sort == 'asc':
        products_to_return.sort(key=lambda x: x.price)
    elif sort == 'desc':
        products_to_return.sort(key=lambda x: x.price, reverse=True)
    return products_to_return[:number_of_products]


@app.post('/products/create_product', status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    '''
    Create a product in the fakestoreapi
    this is not a real post  it will return an object with the created id
    '''
    new_product: Product = Product(**product.dict())
    try:
        response_post = requests.post(
            url, data=json.dumps(new_product.dict()), timeout=5)

    except requests.ConnectionError:
        return {'message': 'Error creating product'}
    return {
        'message': f'Product created succesfully! New id product{response_post.json()}'
    }


@app.put('/product/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
def update_product(product_id: int, product_data: Product):
    '''
     Update a product it will return an object with sent id but
     the updated values won't persist
     '''

    new_product_data: Product = Product(**product_data.dict())

    try:
        response_put = requests.put(
            f'{url}/{product_id}', data=json.dumps(new_product_data.dict()), timeout=5)
    except requests.ConnectionError:
        return {'message': 'Error updating product'}
    return response_put.json()
