import smtplib

from flask import Flask, request, jsonify
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

app = Flask(__name__)


def send_test_mail(body):
    sender_email = "sender@email.com"
    receiver_email = "receiver@email.com"

    msg = MIMEMultipart()
    msg['Subject'] = '[Email Test]'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)

    # Text Attachment - CSV or TXT file
    filename = "testFile.txt"
    msg.attach(MIMEText(open(filename).read()))

    # Image Attachment - JPG or PNG file
    with open('example.jpg', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment',
                       filename="example.jpg")
        msg.attach(img)

    # Binary Attachment - PDF or PPT file
    pdf = MIMEApplication(open("example.pdf", 'rb').read())
    pdf.add_header('Content-Disposition', 'attachment', filename="example.pdf")
    msg.attach(pdf)

    try:
        with smtplib.SMTP('smtp.office365.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("sender@email.com", "password")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)


# Simple POST Route
@app.route('/', methods=['POST'])
def hello_world():
    send_test_mail("Welcome to you Email Attachment!")
    return 'Hello, world!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=8910)
