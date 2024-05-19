import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Función para enviar un correo de phishing simulado
def send_phishing_email(sender, recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:
        # Conexión al servidor SMTP (puede requerir configuración específica)
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender, 'password')
            server.sendmail(sender, recipient, msg.as_string())
            print(f"Correo de phishing enviado a {recipient}")
    except Exception as e:
        print(f"Error al enviar correo: {e}")

if __name__ == "__main__":
    # Configuración del correo de phishing
    sender_email = "phisher@example.com"
    recipient_email = "victim@example.com"
    email_subject = "Notificación Importante"
    email_body = """
    <html>
    <body>
        <p>Estimado usuario,</p>
        <p>Por favor, haga clic en el siguiente enlace para actualizar su información:</p>
        <a href="http://malicious-link.com">Actualizar Información</a>
    </body>
    </html>
    """
    send_phishing_email(sender_email, recipient_email, email_subject, email_body)
