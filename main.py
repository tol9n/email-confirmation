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
    try:
        smtp.sendmail(config.address, mes_to, code)
    except smtplib.SMTPException as e:
        print(f"Error sending email {e}")
        raise ValueError(f"Failed to send email {mes_to}")


@app.get("/")
def read_root(target: str = 'default'):
    try:
        code = random.randint(100000, 999999)
        send_mail(target, code)
        return {'status' : 'sent', 'code' : code}
    except ValueError as e:
        return {'status':'error during sending','error': str(e)}
