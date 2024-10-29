import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

# dados do EmailMessage
password = open ("senha", "r").read()
from_email="ysrael.k99@gmail.com"
to_email="ysrael.k99@gmail.com"
subject="automaçao planilha"
body = """
hello, segue em anexo a automaçao da planilha para a empresa xy automaçao.

qualquer duvida estou a disposiçao.
"""
# montando estrutura de EmailMessage

message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()

# adicionar anexo
anexo = "test.xlsx"
mime_types, mime_subtype = mimetypes.guess_type(anexo)[0].split("/")
with open(anexo, "rb") as a:
    message.add_attachment(
        a.raed(),
        maintype=mimetypes,
        subtype=mime_subtype,
        filename=anexo
    )

    # envio do email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
        smtp.login(from_email, password)
        smtplib.sendmail(
            from_email,
            to_email,
            message.as_string()
        )