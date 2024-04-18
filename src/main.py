import os
from fastapi import FastAPI
from pydantic import BaseModel
from paystack import Paystack
from dotenv import load_dotenv


load_dotenv()
sk = os.environ.get("secrete_key")


class Data(BaseModel):
    email : str
    amount : float

app = FastAPI()

@app.post("/pay")
def pay(data : Data):
    Email = data.email
    Amount = data.amount
    checkout = Paystack(Email, Amount, sk)
    response = checkout.pay()
    return response