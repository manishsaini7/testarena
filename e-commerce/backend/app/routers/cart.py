# backend/app/routers/cart.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.CartItem])
def read_cart_items(user_id: int, db: Session = Depends(get_db)):
    return crud.get_cart_items(db, user_id=user_id)


@router.post("/", response_model=schemas.CartItem)
def add_cart_item(cart_item: schemas.CartItemCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.add_cart_item(db=db, cart_item=cart_item, user_id=user_id)


@router.delete("/{cart_item_id}", response_model=schemas.CartItem)
def remove_cart_item(cart_item_id: int, db: Session = Depends(get_db)):
    crud.remove_cart_item(db=db, cart_item_id=cart_item_id)
    return {"message": "Item removed from cart"}
