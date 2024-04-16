import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import *

usuario = "Edwin"
asunto = "Mensaje enviado con Python"
destinatarios = ["emperatrizsccs@gmail.com", "aarontorre@gmail.com"]
mensaje = "Mensaje automático de prueba Python."

msg = MIMEMultipart()
msg["From"] = usuario
msg["Subject"] = asunto
msg["to"] = ", ".join(destinatarios)
msg.attach(MIMEText(mensaje))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(USER_EMAIL, APP_PASSWORD)
    server.sendmail(USER_EMAIL, destinatarios, msg.as_string())
    print("Correo enviado correctamente.")