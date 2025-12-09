from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from models import OrderStatus

# ===== Product Schemas =====
class ProductBase(BaseModel):
    name: str
    description: str
    short_description: Optional[str] = None
    price: float = Field(gt=0)
    category: str
    image_url: Optional[str] = None
    options: Optional[str] = None  # JSON string

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None

class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# ===== Order Item Schemas =====
class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)
    selected_options: Optional[str] = None  # JSON string
    custom_engraving: Optional[str] = None

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    order_id: int
    product_name: str
    product_price: float
    
    class Config:
        from_attributes = True

# ===== Order Schemas =====
class OrderBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    shipping_address: str
    note: Optional[str] = None

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class OrderUpdateStatus(BaseModel):
    status: OrderStatus

class Order(OrderBase):
    id: int
    status: OrderStatus
    total: float
    created_at: datetime
    updated_at: Optional[datetime] = None
    items: List[OrderItem] = []
    
    class Config:
        from_attributes = True

# ===== Auth Schemas =====
class AdminLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class AdminResponse(BaseModel):
    id: int
    email: str
    
    class Config:
        from_attributes = True
