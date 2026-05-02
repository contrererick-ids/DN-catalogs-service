from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/domicilios", tags=["Domicilios"])

@router.get("/", response_model=list[schemas.DomicilioResponse])
def listar_domicilios(db: Session = Depends(get_db)):
    return db.query(models.Domicilio).all()

@router.get("/{domicilio_id}", response_model=schemas.DomicilioResponse)
def obtener_domicilio(domicilio_id: int, db: Session = Depends(get_db)):
    domicilio = db.query(models.Domicilio).filter(models.Domicilio.id == domicilio_id).first()
    if not domicilio:
        raise HTTPException(status_code=404, detail="Domicilio no encontrado")
    return domicilio

@router.get("/cliente/{cliente_id}", response_model=list[schemas.DomicilioResponse])
def listar_domicilios_por_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return db.query(models.Domicilio).filter(models.Domicilio.cliente_id == cliente_id).all()

@router.post("/", response_model=schemas.DomicilioResponse, status_code=201)
def crear_domicilio(domicilio: schemas.DomicilioCreate, db: Session = Depends(get_db)):
    db_domicilio = models.Domicilio(**domicilio.model_dump())
    db.add(db_domicilio)
    db.commit()
    db.refresh(db_domicilio)
    return db_domicilio

@router.put("/{domicilio_id}", response_model=schemas.DomicilioResponse)
def actualizar_domicilio(domicilio_id: int, domicilio: schemas.DomicilioCreate, db: Session = Depends(get_db)):
    db_domicilio = db.query(models.Domicilio).filter(models.Domicilio.id == domicilio_id).first()
    if not db_domicilio:
        raise HTTPException(status_code=404, detail="Domicilio no encontrado")
    for key, value in domicilio.model_dump().items():
        setattr(db_domicilio, key, value)
    db.commit()
    db.refresh(db_domicilio)
    return db_domicilio

@router.delete("/{domicilio_id}", status_code=204)
def eliminar_domicilio(domicilio_id: int, db: Session = Depends(get_db)):
    db_domicilio = db.query(models.Domicilio).filter(models.Domicilio.id == domicilio_id).first()
    if not db_domicilio:
        raise HTTPException(status_code=404, detail="Domicilio no encontrado")
    db.delete(db_domicilio)
    db.commit()
