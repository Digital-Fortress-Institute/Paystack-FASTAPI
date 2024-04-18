import os
from fastapi import FastAPI
from pydantic import BaseModel
from paystack import Paystack
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware



load_dotenv()
sk = os.environ.get("secrete_key")


class Data(BaseModel):
    email : str
    amount : float

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.post("/pay")
def pay(data : Data):
    Email = data.email
    Amount = data.amount
    checkout = Paystack(Email, Amount, sk)
    response = checkout.pay()
    return response


