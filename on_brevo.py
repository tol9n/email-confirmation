import requests
from fastapi import FastAPI

import random

import config


api_key = config.api_key
app = FastAPI()


def send_mail(name:str,from_email:str,to_email:str,subject:str,content:str):
    headers = {
        'accept': 'application/json',
        'api-key': api_key,
        'content-type': 'application/json'
    }

    data = {
        'sender': {'name': name, 'email': from_email},
        'to': [{'email': to_email}],
        'subject': subject,
        'htmlContent': content  #your HTML content here
    }

    response = requests.post('https://api.brevo.com/v3/smtp/email', json=data, headers=headers)

    if response.status_code != 201:
        raise ValueError(f"Failed to send email {to_email}")

@app.get("/")
def read_root(target:str = 'default'):
    try:
        code = random.randint(100000, 999999)
        name = "name"
        from_email = config.address
        to_email = target
        subject = 'Verification code'
        send_mail(name,from_email,to_email,subject,f'Your verification code is {code}')
        return {'status' : 'sent','target':target, 'code' : code}
    except ValueError as e:
        return {'status':'error during sending','error': str(e)}