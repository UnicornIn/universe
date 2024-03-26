from fastapi import APIRouter, Depends, HTTPException, Request
from .models import User
from ...database.connection import create_user, get_user

router = APIRouter()

@router.post("/")
async def create_user(request: Request, user_data: User = Depends()):
    user = create_user(user_data)
    return {"success": True, "user": user}

@router.get("/{username}")
async def get_user(username: str):
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}
