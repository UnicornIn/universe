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

@app.get("/products")
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
async def read_customers():
    wcapi = API(
        url="https://rizosfelices.co",
        consumer_key="ck_71555cb7c8c3489cf2ea8b231cff6ea704001ac9",
        consumer_secret="cs_8cb1c962a51cd4feac1894987d5d8ccd5aa078f3",
        version="wc/v3"
    )
    customers = wcapi.get("customers").json()
    return customers
