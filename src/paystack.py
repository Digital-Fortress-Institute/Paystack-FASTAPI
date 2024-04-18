import requests


class Paystack:
    def __init__(self, email, amount, key):
        self.key = key
        self.email = email
        self.amount = amount * 100

    def pay(self):
        url = "https://transaction/initialize"
        data = {
            "email": self.email,
            "amount": self.amount
        }

        headers = {
            "Authorization": "Bearer" + self.key,
            "Content-Type": "aplication/json"
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            data = response.json()
            return data
        return "404"