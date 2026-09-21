from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.item import Item
from app.schemas.item import ItemResponse, ItemCreate

router = APIRouter()

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(title=item.title)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[ItemResponse])
def read_items(db:Session = Depends(get_db)):
    items = db.query(Item).all()
    return items