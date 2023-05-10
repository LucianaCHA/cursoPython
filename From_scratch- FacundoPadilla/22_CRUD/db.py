from typing import List, NoReturn, Optional
from models import BaseProduct, Product

class Basket(object): # clase que representa el carrito de compras, es concreta y padre por eso va object
    products : List[Product] = [] # lista de productos
    id_maker : int = 0

    def add_product(self, producto: BaseProduct) -> NoReturn: # recibe un producto de tipo BaseProduct y retorna un producto de tipo Product
        new_product = Product(id=self.id_maker, **producto.dict()) # **producto.dict() es un diccionario con los atributos de producto
        self.products.append(new_product)
        self.id_maker += 1

    def get_products(self, id: Optional[int] = None): #  puede recibir un id o no
        if id is not None:
            for product in self.products:
                if product.id == id:
                    return product
            return None
        return self.products
    
    def update_product(self, old_prod: Product,  new_prod: BaseProduct ) -> NoReturn:
        index = self.products.index(old_prod)
        self.products[index] = old_prod.copy(new_prod.dict(exclude_unset=True)) # excludeUnset excluye los campos en null ( es decir lo que se reciban sin modificar) 

    def delete_product(self, id: int) -> NoReturn:
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                return
        raise ValueError("El producto no existe")