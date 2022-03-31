from constants import URL_FRONT_END_DEEPRESPRED
from constants import EMAIL_TOKEN
from emailTemplates.TemplateNoResults import getTemplateNoResults
from emailTemplates.TemplateReceivedRequest import getTemplateReceivedRequest
from emailTemplates.TemplateResults import getTemplateResults
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import ssl
import sys
import os

def sendEmail (receiver, files, type, idRequest, inputType, inputContent):

    # User configuration   
    sender_email = "deeprespred@gmail.com"
    sender_name = "DeepReSPred"
    password = EMAIL_TOKEN

    subject = ""
    if type==1:
        subject = "[DeepReSPred] Confirmation of registered prediction request"
        body = getTemplateReceivedRequest(str(idRequest), str(inputType),str(inputContent), URL_FRONT_END_DEEPRESPRED)
        files = []
    else:
        subject="[DeepReSPred] Results of prediction request"

        if len(files)>0:
            body = getTemplateResults(str(idRequest), str(inputType),str(inputContent), URL_FRONT_END_DEEPRESPRED)
        else:
            body = getTemplateNoResults(str(idRequest), str(inputType),str(inputContent), URL_FRONT_END_DEEPRESPRED)

    html = body 


    # Email body
    email_body = html

    print("Sending the email...")
    # Configurating user's info
    msg = MIMEMultipart()
    msg['To'] = formataddr((receiver, receiver))
    msg['From'] = formataddr((sender_name, sender_email))
    msg['Subject'] = subject

    msg.attach(MIMEText(email_body, 'html'))

    #Images in html
    fp = open('emailTemplates/images/deeprespred_logo.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<imageLogo>')
    msg.attach(msgImage)

    fp = open('emailTemplates/images/4801551865294269.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<imageMail>')
    msg.attach(msgImage)

    fp = open('emailTemplates/images/26531551864324009.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<imageTelf>')
    msg.attach(msgImage)

    fp = open('emailTemplates/images/grainsvg.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<imageGrain>')
    msg.attach(msgImage)
    
    #attachments
    for filename in files:
        try:
            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            reducedName=os.path.basename(os.path.normpath(filename))
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {reducedName}",
            )

            msg.attach(part)
        except Exception as e:
            print("Oh no! We didnt found the attachment!n{e}")
            break

    try:
        # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Encrypts the email
        context = ssl.create_default_context()
        server.starttls(context=context)
        # We log in into our Google account
        server.login(sender_email, password)
        # Sending email from sender, to receiver with the email body
        server.sendmail(sender_email, receiver, msg.as_string())
        print('Email sent!')
    except Exception as e:
        print(f'Oh no! Something bad happened!n{e}')
        sys.exit()
    finally:
        print('Closing the server...')
        server.quit()

#sendEmail("correo@dominio.com", [],1,"ASDOW","PFAMCode","PF20291")