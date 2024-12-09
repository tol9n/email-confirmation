import random
import smtplib


from fastapi import FastAPI

import config

app = FastAPI()


def send_mail(mes_to: str, code: any):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(config.address, config.password)
    code = str(code)
    smtp.sendmail(config.address, mes_to, code)
    smtp.quit()


@app.get("/")
def read_root(adr: str = 'default'):
    code = random.randint(100000, 999999)
    send_mail(adr, code)
    return {"adrs" : adr, "code" : code}
