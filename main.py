from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from woocommerce import API
from database.connection import execute_query

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/")
async def read_root():
    return {"message": "Hello, welcome to the WooCommerce API with FastAPI!"}


@app.get("/products/{product_id}")
async def read_product(product_id: int):
    wcapi = API(
        url="https://rizosfelices.co",
        consumer_key="ck_71555cb7c8c3489cf2ea8b231cff6ea704001ac9",
        consumer_secret="cs_8cb1c962a51cd4feac1894987d5d8ccd5aa078f3",
        version="wc/v3",
    )
    product = wcapi.get(f"products/{product_id}").json()
    return product


@app.get("/products/")
async def read_products():
    wcapi = API(
        url="https://rizosfelices.co",
        consumer_key="ck_71555cb7c8c3489cf2ea8b231cff6ea704001ac9",
        consumer_secret="cs_8cb1c962a51cd4feac1894987d5d8ccd5aa078f3",
        version="wc/v3",
    )
    products = wcapi.get("products").json()
    return products


@app.get("/customers")
async def get_customers_from_orders():
    wcapi = API(
        url="https://rizosfelices.co",
        consumer_key="ck_71555cb7c8c3489cf2ea8b231cff6ea704001ac9",
        consumer_secret="cs_8cb1c962a51cd4feac1894987d5d8ccd5aa078f3",
        version="wc/v3",
    )

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

    return {"customers": customers}


def save_customer_to_database(customer):
    # Formatear la consulta SQL para insertar el cliente en la tabla customers
    query = f"INSERT INTO customers (first_name, last_name, email, phone) VALUES ('{customer['first_name']}', '{customer['last_name']}', '{customer['email']}', '{customer['phone']}')"
    # Ejecutar la consulta
    execute_query(query)


@app.get("/orders")
async def read_orders():
    wcapi = API(
        url="https://rizosfelices.co",
        consumer_key="ck_71555cb7c8c3489cf2ea8b231cff6ea704001ac9",
        consumer_secret="cs_8cb1c962a51cd4feac1894987d5d8ccd5aa078f3",
        version="wc/v3",
    )

    orders = wcapi.get("orders").json()

    return orders
