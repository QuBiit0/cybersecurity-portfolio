import smtplib
from email.mime.text import MIMEText

def send_phishing_email(smtp_server, smtp_port, username, password, from_address, to_address, subject, body):
    """
    Esta función envía un correo electrónico de phishing.
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()

# Ejemplo de uso:
send_phishing_email('smtp.example.com', 587, 'username', 'password', 'from@example.com', 'to@example.com', 'Asunto', 'Cuerpo del correo')
