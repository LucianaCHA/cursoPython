from pydantic import BaseModel, Field, constr,confloat, create_model
from typing import Optional

validate_str = constr(min_length=3, max_length=50, strict=True)

validate_float = confloat(gt=0, strict=True)

class BaseProduct(BaseModel):
    # name: StrictStr = Field(..., max_length=50, min_length=3)# no es posible asignar la validacion a Field porque pydatic intenta validar el valor None, es decir valida antes de asignar el valor. Por ese motivo se crea una variable validate_str que valida el string y se asigne a la variable
    name: validate_str = Field(...)
    brand: validate_str = Field(...)
    price: validate_float = Field(...)

    @classmethod
    def as_optional(cls):
        annonations = cls.__fields__ # field trae un dict con los atributos y valores de los misms 
        fields = {attribute : (Optional[data_type.type_], None) for attribute, data_type in annonations.items()}

        OptionalModel = create_model(f"Optional{cls.__name__}", **fields) # crea un modelo con todos los campos

        return OptionalModel

class Product(BaseProduct): # hereda de BaseProduct
    id: int = Field(None, ge=0)