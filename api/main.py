from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from db import models

app = FastAPI(title="Smart Inventory Management System")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/inventory/{store_id}/{sku}")
def get_inventory(store_id: int, sku: str, db: Session = Depends(get_db)):
    inv = (
        db.query(models.Inventory)
        .join(models.Product)
        .filter(models.Product.sku == sku, models.Inventory.store_id == store_id)
        .first()
    )
    if not inv:
        return {"error": "Not found"}
    return {
        "store_id": store_id,
        "sku": sku,
        "on_hand": inv.on_hand,
        "on_order": inv.on_order,
        "reserved": inv.reserved,
    }
