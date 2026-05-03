from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TipoDireccion(str, Enum):
    FACTURACION = "FACTURACIÓN"
    ENVIO = "ENVÍO"

# Cliente
class ClienteBase(BaseModel):
    razon_social: str
    nombre_comercial: Optional[str] = None
    rfc: str
    correo: str
    telefono: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int
    class Config:
        from_attributes = True

# Domicilio
class DomicilioBase(BaseModel):
    domicilio: str
    colonia: str
    municipio: str
    estado: str
    tipo: TipoDireccion
    cliente_id: int

class DomicilioCreate(DomicilioBase):
    pass

class DomicilioResponse(DomicilioBase):
    id: int
    class Config:
        from_attributes = True

# Producto
class ProductoBase(BaseModel):
    nombre: str
    unidad_medida: str
    precio_base: float

class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: int
    class Config:
        from_attributes = True