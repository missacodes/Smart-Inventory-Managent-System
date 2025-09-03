
import random
from datetime import datetime
from sqlalchemy.orm import Session
from db.session import engine, SessionLocal, init_db
from db.models import Product, Store, Inventory

GROCERY_ITEMS = [
    ("Bananas", "Fruit"),
    ("Milk", "Dairy"),
    ("Bread", "Bakery"),
    ("Eggs", "Dairy"),
    ("Apples", "Fruit"),
]

def seed():
    init_db()
    db: Session = SessionLocal()

    # Add one store if none
    store = db.query(Store).first()
    if not store:
        store = Store(name="Main Branch", region="Central")
        db.add(store)
        db.commit()
        db.refresh(store)

    # Add grocery products + inventory
    for name, category in GROCERY_ITEMS:
        if not db.query(Product).filter(Product.name == name).first():
            p = Product(
                sku=name,   # use grocery name as SKU
                name=name,
                category=category,
                unit_cost=round(random.uniform(1, 10), 2),
                unit_price=round(random.uniform(10, 30), 2),
            )
            db.add(p)
            db.commit()
            db.refresh(p)

            inv = Inventory(
                store_id=store.store_id,
                product_id=p.product_id,
                on_hand=random.randint(10, 100),
                on_order=0,
                reserved=random.randint(0, 5),
                updated_at=datetime.utcnow(),
            )
            db.add(inv)
            db.commit()

    print("✅ Grocery data inserted!")

if __name__ == "__main__":
    seed()
