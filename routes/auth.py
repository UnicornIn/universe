from fastapi import APIRouter, requests, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="main/templates")

@router.get("/login", response_class=HTMLResponse)   
async def show_login(request:requests.Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register", response_class=HTMLResponse)   
async def show_register(request:requests.Request):
    return templates.TemplateResponse("register.html", {"request": request})