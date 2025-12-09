# week1/day1_types.py
"""
Day 1: Type Hints + Dataclasses + Pydantic

Goal: Master professional Python with proper typing and validation.
"""

from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator


# Task 1: Create User dataclass
@dataclass
class User:
    """A user in the system"""

    # TODO: Add fields with type hints
    name: str
    email: str
    age: int


# Task 2: Create Pydantic model for validation
class UserCreate(BaseModel):
    """Model for creating a new user"""

    # TODO: Add fields with validation
    name: str
    email: EmailStr
    age: int

    @field_validator("age")
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Age must be a positive integer")
        return v

class ProductCreate(BaseModel):
    """Model for creating a new product"""
    name: str
    price: float
    quantity: int

    @field_validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be greater than zero")
        return v

    @field_validator("quantity")
    def quantity_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError("Quantity cannot be negative")
        return v

class OrderCreate(BaseModel):
    """Model for creating a new order"""
    order_id: int
    user_id: int
    product_ids: list[int]
    total_amount: float

    @field_validator("total_amount")
    def total_amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Total amount must be greater than zero")
        return v

    @field_validator("product_ids")
    @classmethod
    def must_have_products(cls, v):
        if not v:
            raise ValueError("Order must contain at least one product")
        return v

# Task 3: Create Product dataclass
@dataclass
class Product:
    # TODO: Add fields
    name: str
    price: float
    quantity: int


# Task 4: Create Order dataclass
@dataclass
class Order:
    # TODO: Add fields
    order_id: int
    user_id: int
    product_ids: list[int]
    total_amount: float


# Task 5: Write a function that takes Pydantic input, returns dataclass
def process_user(user_data: UserCreate) -> User:
    """Convert Pydantic model to dataclass"""
    # TODO: Implement
    return User(name=user_data.name, email=user_data.email, age=user_data.age)

def process_product(product_data: ProductCreate) -> Product:
    """Convert Pydantic model to dataclass"""
    return Product(name=product_data.name, price=product_data.price, quantity=product_data.quantity)

def process_order(order_data: OrderCreate) -> Order:
    """Convert Pydantic model to dataclass"""
    return Order(order_id=order_data.order_id, user_id=order_data.user_id, product_ids=order_data.product_ids, total_amount=order_data.total_amount)



if __name__ == "__main__":
    # Test your implementations
    valid_user = UserCreate(name="Alice", email="alice@example.com", age=30)
    user = process_user(valid_user)
    print(f"User created: {user}")

    try:
        invalid_user = UserCreate(name="Bob", email="invalid-email", age=-5)
    except Exception as e:
        print(f"Validation error: {e}")

    valid_product = ProductCreate(name="Laptop", price=999.99, quantity=10)
    product = process_product(valid_product)
    print(f"Product created: {product}")

    try:
        invalid_product = ProductCreate(name="Phone", price=-199.99, quantity=-5)
    except Exception as e:
        print(f"Validation error: {e}")

    valid_order = OrderCreate(order_id=1, user_id=1, product_ids=[1, 2], total_amount=1199.98)
    order = process_order(valid_order)
    print(f"Order created: {order}")

    try:
        invalid_order = OrderCreate(order_id=2, user_id=1, product_ids=[], total_amount=-50.00)
    except Exception as e:
        print(f"Validation error: {e}")
