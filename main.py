import smtplib
import config

def send_mail(mes_to:str, code:str):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(config.address, config.password)
    smtp.sendmail(config.address,mes_to,code)
    smtp.quit()

