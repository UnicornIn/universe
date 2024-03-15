from fastapi import FastAPI, Request, HTTPException, Depends, Query
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from woocommerce import API as woocommerce
from woocommerce import API
from database.connection import execute_query


app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

templates = Jinja2Templates(directory="templates")

wcapi = API(
        url="https://rizosfelices.co",
        consumer_key="ck_71555cb7c8c3489cf2ea8b231cff6ea704001ac9",
        consumer_secret="cs_8cb1c962a51cd4feac1894987d5d8ccd5aa078f3",
        version="wc/v3",
    )

fake_users_db = {
    "user@example.com": {
        "username": "user@example.com",
        "password": "password",
        "full_name": "Usuario de Ejemplo",
    }
}


@app.get("/register", response_class=HTMLResponse)
async def show_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def show_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/productos", response_class=HTMLResponse)
async def show_dashboard(request: Request):
    # Obtén datos de la API de WooCommerce (aquí obtengo productos como ejemplo)
    products = wcapi.get("products").json()

    return templates.TemplateResponse("productos.html", {"request": request, "products": products})

@app.get("/ordenes", response_class=HTMLResponse)
async def show_dashboard(request: Request):
    # Obtén datos de la API de WooCommerce (aquí obtengo productos como ejemplo)
    orders = wcapi.get("products").json()

    return templates.TemplateResponse("ordenes.html", {"request": request, "orders": orders})



@app.get("/dashboard", response_class=HTMLResponse)
async def show_dashboard(request: Request):
    # Obtén datos de la API de WooCommerce (aquí obtengo productos como ejemplo)
    orders = wcapi.get("orders").json()
    customers = wcapi.get("customers").json()

    # Renderiza el template del dashboard con los datos
    return templates.TemplateResponse("dashboard.html", {"request": request, "orders": orders, "customers": customers})

@app.get("/")
async def read_root():
    return {"message": "Hello, welcome to the WooCommerce API with FastAPI!"}

@app.get("/products/{product_id}")
async def read_product(product_id: int):

    product = wcapi.get(f"products/{product_id}").json()
    return product

@app.get("/products/")
async def read_products():
    
    products = wcapi.get("products").json()
    return products


"""@app.get("/customers")
async def get_customers_from_orders():

    orders = wcapi.get("orders").json()

    customers = []
    for order in orders:
        billing_info = order.get("billing")
        if billing_info:
            customer = {
                "first_name": billing_info.get("first_name"),
                "last_name": billing_info.get("last_name"),
                "email": billing_info.get("email"),
                "phone": billing_info.get("phone"),  # Incluir el dato del teléfono
            }
            customers.append(customer)
            # Guardar el cliente en la base de datos
            save_customer_to_database(customer)

    return {"customers": customers}"""

def save_customer_to_database(customer):
    # Formatear la consulta SQL para insertar el cliente en la tabla customers
    query = f"INSERT INTO customers (first_name, last_name, email, phone) VALUES ('{customer['first_name']}', '{customer['last_name']}', '{customer['email']}', '{customer['phone']}')"
    # Ejecutar la consulta
    execute_query(query)

"""@app.get("/customers", response_class=HTMLResponse)
async def get_customers( 
    request: Request,
    order_id: int = Query (None, alias= "order_id")

):
    if  order_id:
        order_data = woocommerce.get( f"orders/{order_id}" ).json()
        orders = [order_data]
    else:
        orders = wcapi.get("orders").json
    return  templates.TemplateResponse("dashboard.html")
"""
@app.get("/customers")
async def get_customers_from_orders( request :Request ,
    order_id: int = Query(None, alias="order_id")
):
    

    if order_id:
        # Obtener datos de un pedido específico
        order = wcapi.get(f"orders/{order_id}").json()
        orders = [order]
    else:
        # Obtener todos los pedidos
        orders = wcapi.get("orders").json()

    customers = []
    for order in orders:
        if order.get("id") == order_id:
            billing_info = order.get("billing")
            if billing_info:
                customer = {
                    "id": order_id,
                    "first_name": billing_info.get("first_name"),
                    "last_name": billing_info.get("last_name"),
                    "email": billing_info.get("email"),
                    "phone": billing_info.get("phone"),
                    "address_1": billing_info.get("address_1"),
                }
                customers.append(customer)

    return templates.TemplateResponse("dashboard.html", {"request": request, "orders": orders})


@app.get("/orders")
async def read_orders():
    
    orders = wcapi.get("orders", params={"per_page": 15}).json()
    return orders

#Reports de las ventas al año

# @app.get("/reports/sales")
# async def get_sales():
          
    
#     reports = wcapi.get("reports/sales?date_min=2023-05-03&date_max=2024-05-04").json()

#     return reports

#Reports de las ventas al mes

# @app.get("/reports/sales/monthly")
# async def get_sales_month():
          
    
#     reports = wcapi.get("reports/sales?filter[period]=month").json()

#     return reports

#Reports de las ventas de la week

# @app.get("/reports/sales/week", response_class=HTMLResponse)
# async def get_sales_week(request :Request):
          
    
#     total_sales = wcapi.get("reports/sales?filter[period]=week").json()

#     return templates.TemplateResponse("dashboard.html", {"request": request, "reports": total_sales })

# @app.get("/reports")
# async def get_sales():


#     reports = wcapi.get("reports").json()

#     return reports

@app.get("/reports/sales/week", response_class=HTMLResponse)
async def get_sales_week(request: Request):
    
        response = wcapi.get("reports/sales?filter[period]=week")
        
        reports = response.json()
        
        return templates.TemplateResponse("dashboard.html", {"request": request, "reports": reports})
    

