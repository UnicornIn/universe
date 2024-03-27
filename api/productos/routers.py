from fastapi import APIRouter, Depends, HTTPException, Request
from .models import Product
from ...database.connection import create_product, get_product

router = APIRouter()

@router.post("/")
async def create_product(request: Request, product_data: Product = Depends()):
    product = create_product(product_data)
    return {"success": True, "product": product}

@router.get("/{product_id}")
async def get_product(product_id: int):
    return get_product(product_id)
    
