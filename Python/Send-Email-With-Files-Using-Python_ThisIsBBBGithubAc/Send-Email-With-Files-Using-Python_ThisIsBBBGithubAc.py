# AUTHOR: ThisIsBBBGithubAc
# Python3 Concept: Send-Email-With-Files-Using-Python
# GITHUB: https://github.com/ThisIsBBBGithubAc


import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail():
    sender_email = input("Type Sender Email Address Here and Press Enter:\t") 
    receiver_email = input("Type Receiver Email Address Here and Press Enter:\t")
    password = input("Type Sender Email's Password Here and Press Enter:\n") 
    subject = input("Write The Subject for This Mail:\n")
    body = input("Write The Body for This Mail:\n")

    message = MIMEMultipart()

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    isFile = input("Do You Want To Attach Any File With This Mail? ( Type 'YES' or 'NO' ):\t")
    if isFile == "YES":
        filename = input("Type The File Path Here: ( Eg: '/home/Download/Images.zip' )\n") 

        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        message.attach(part)


    text = message.as_string()
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


if __name__ == '__main__':
    send_mail()