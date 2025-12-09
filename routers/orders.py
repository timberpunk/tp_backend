from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from models import Order, OrderItem, Product, Admin, OrderStatus
from auth import get_current_admin
import schemas

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=schemas.Order, status_code=status.HTTP_201_CREATED)
def create_order(order_data: schemas.OrderCreate, db: Session = Depends(get_db)):
    """Create a new order (public checkout)"""
    # Validate products and calculate total
    total = 0.0
    items_to_create = []
    
    for item in order_data.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Product with id {item.product_id} not found"
            )
        
        item_total = product.price * item.quantity
        total += item_total
        
        items_to_create.append({
            "product_id": product.id,
            "product_name": product.name,
            "product_price": product.price,
            "quantity": item.quantity,
            "selected_options": item.selected_options,
            "custom_engraving": item.custom_engraving
        })
    
    # Create order
    db_order = Order(
        first_name=order_data.first_name,
        last_name=order_data.last_name,
        email=order_data.email,
        phone=order_data.phone,
        shipping_address=order_data.shipping_address,
        note=order_data.note,
        total=total,
        status=OrderStatus.NEW
    )
    db.add(db_order)
    db.flush()  # Get the order ID
    
    # Create order items
    for item_data in items_to_create:
        db_item = OrderItem(order_id=db_order.id, **item_data)
        db.add(db_item)
    
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=List[schemas.Order])
def get_orders(
    status: Optional[OrderStatus] = None,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    """Get all orders (admin only), optionally filtered by status"""
    query = db.query(Order).order_by(Order.created_at.desc())
    if status:
        query = query.filter(Order.status == status)
    orders = query.all()
    return orders

@router.get("/{order_id}", response_model=schemas.Order)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    """Get a single order by ID (admin only)"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/{order_id}", response_model=schemas.Order)
def update_order_status(
    order_id: int,
    order_update: schemas.OrderUpdateStatus,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    """Update order status (admin only)"""
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db_order.status = order_update.status
    db.commit()
    db.refresh(db_order)
    return db_order
