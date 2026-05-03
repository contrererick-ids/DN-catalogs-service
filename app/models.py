from sqlalchemy import Column, Integer, String, Enum as SAEnum, ForeignKey, DECIMAL
from .database import Base
import enum

class TipoDireccion(enum.Enum):
    FACTURACION = "FACTURACIÓN"
    ENVIO = "ENVÍO"

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    razon_social = Column(String(255), nullable=False)
    nombre_comercial = Column(String(255))
    rfc = Column(String(13), nullable=False, unique=True)
    correo = Column(String(255), nullable=False)
    telefono = Column(String(20))

class Domicilio(Base):
    __tablename__ = "domicilios"

    id = Column(Integer, primary_key=True, index=True)
    domicilio = Column(String(255), nullable=False)
    colonia = Column(String(100), nullable=False)
    municipio = Column(String(100), nullable=False)
    estado = Column(String(100), nullable=False)
    tipo = Column(SAEnum(TipoDireccion), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    unidad_medida = Column(String(50), nullable=False)
    precio_base = Column(DECIMAL(10, 2), nullable=False)
