from fastapi import FastAPI
from woocommerce import API

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, welcome to the WooCommerce API with FastAPI!"}

@app.get("/products/{product_id}")
async def read_product(product_id: int):
    wcapi = API(
        url="https://rizosfelices.co",
        consumer_key="ck_71555cb7c8c3489cf2ea8b231cff6ea704001ac9",
        consumer_secret="cs_8cb1c962a51cd4feac1894987d5d8ccd5aa078f3",
        version="wc/v3"
    )
    product = wcapi.get("products/{}".format(product_id)).json()
    return product

@app.get("/products/")
async def read_products():
    wcapi = API(
        url="https://rizosfelices.co",
        consumer_key="ck_71555cb7c8c3489cf2ea8b231cff6ea704001ac9",
        consumer_secret="cs_8cb1c962a51cd4feac1894987d5d8ccd5aa078f3",
        version="wc/v3"
    )
    products = wcapi.get("products").json()
    return products


@app.get("/customers")
async def get_customers_from_orders():
    wcapi = API(
        url="https://rizosfelices.co",
        consumer_key="ck_71555cb7c8c3489cf2ea8b231cff6ea704001ac9",
        consumer_secret="cs_8cb1c962a51cd4feac1894987d5d8ccd5aa078f3",
        version="wc/v3"
    )
    
    orders = wcapi.get("orders").json()
    
    customers = []
    for order in orders:
        billing_info = order.get("billing")
        if billing_info:
            customer = {
                "id": billing_info.get("customer_id"),
                "first_name": billing_info.get("first_name"),
                "last_name": billing_info.get("last_name"),
                "email": billing_info.get("email"),
                # Agregar otros campos según sea necesario
            }
            customers.append(customer)
    
    return {"customers": customers}

@app.get("/orders")
async def read_orders():
    wcapi = API(
        url="https://rizosfelices.co",
        consumer_key="ck_71555cb7c8c3489cf2ea8b231cff6ea704001ac9",
        consumer_secret="cs_8cb1c962a51cd4feac1894987d5d8ccd5aa078f3",
        version="wc/v3"
    )
    
    orders = wcapi.get("orders").json()
    
    return orders
