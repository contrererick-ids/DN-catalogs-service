import os
from fastapi import FastAPI
from .database import Base, engine
from .routes import clientes, domicilios, productos
from dotenv import load_dotenv

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Catalogs Service")

app.include_router(clientes.router)
app.include_router(domicilios.router)
app.include_router(productos.router)

@app.get("/health")
def health():
    return {"status": "ok", "service": "catalogs-service", "environment": os.getenv("ENVIRONMENT", "local")}
