import os
import requests
from dotenv import load_dotenv


# load_dotenv()
# sk = os.environ.get("secrete_key")

class Paystack:
    def __init__(self, email, amount, key):
        self.key = key
        self.email = email
        self.amount = amount * 100

    def pay(self):
        url = "https://api.paystack.co/transaction/initialize"
        data = {
            "email": self.email,
            "amount": self.amount
        }

        headers = {
            "Authorization": "Bearer "  + self.key,
            "Content-Type": "aplication/json"
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            data = response.json()
            ref = data['data']['reference']
            auth_link = data['data']['authorization_url']
            result = {
                'reference_id': ref,
                'auth_url': auth_link
                }
            return result
        return "404"
    
# {
#   "email": "davidoiekunle@gmail.com",
#   "amount": 40000
# }

# test = Paystack("davidoiekunle@gmail.com", 40000, sk)
# print(test.pay())