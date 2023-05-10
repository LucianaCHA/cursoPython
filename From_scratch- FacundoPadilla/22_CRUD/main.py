from fastapi import FastAPI, Body, status, Query, Response, Path
from models import BaseProduct
from db import Basket
from typing import Optional

app = FastAPI()
basket = Basket()

def product_not_found():
    return Response(content='Product no found', status_code=status.HTTP_404_NOT_FOUND)

@app.post("/basket/add-product", status_code=status.HTTP_201_CREATED)
async def add_product(producto: BaseProduct = Body(...)):
    basket.add_product(producto)
    return {"message": "Product added successfully"}

@app.get("/basket", status_code=status.HTTP_200_OK)
async def get_products(id: Optional[str] = Query(default=None)): 
    if id:
        if basket.get_products(int(id)):
            return basket.get_products(int(id))
        return product_not_found()
    
    return basket.get_products()


@app.put("/basket/edit-produc/{id}", status_code=status.HTTP_200_OK)
async def edit_product(id : int = Path(...), new_prod_info: BaseProduct = Body(...)):
    product = basket.get_products(id)

    if product:
        basket.update_product(old_prod= product, new_prod = new_prod_info)
    return product_not_found()

# esencialmente put es lo mismo que patch, sin embargo requiere recibir todos los campos de nuevo

# en este caso se transforma el modelo de pydantic como optional ( para evitar valifdar en el cuerpo del patch y para no hacer un nuevo modelo solo para el patch)
@app.patch("/basket/edit-produc/{id}", status_code=status.HTTP_200_OK)
async def edit_product_data(id : int = Path(...), new_prod_info: BaseProduct.as_optional = Body(...)):
    product = basket.get_products(id)

    if product:
        basket.update_product(old_prod= product, new_prod = new_prod_info)
    return product_not_found()

@app.delete("/basket/delete-product/{id}", status_code=status.HTTP_200_OK)
async def delete_product(id: int = Path(...)):
    try:
        basket.delete_product(id)
    except ValueError:
        return product_not_found()