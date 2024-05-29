# backend/app/routers/orders.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.Order])
def read_orders(user_id: int, db: Session = Depends(get_db)):
    return crud.get_orders(db, user_id=user_id)


@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order, user_id=user_id)
