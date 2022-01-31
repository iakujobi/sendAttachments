# Send Email with Attachments

This is how to send email with attachments using Python with Outlook as the SMTP server, and the connection is based on TLS.

## Setup

1. Install Flask Server (optional)

- It is highly recommended to setup a virtual environment before you proceed. Please be noted that `Flask` is not needed to run `smtplib` module. It was included in this piece as I was testing on sending email via Flask server at the time of this writing.

[Documentation on how to setup a virtual environment](https://docs.python-guide.org/dev/virtualenvs/)

2. Implementation

- SMTP Object
- MIME
- Text Attachments
- Image Attachments
- Binary Attachments

3. Call the route using a POST route on Postman.

<mark>NOTE:</mark> Microsoft is moving away from simple authentication. Even though the code works, the mail will not send and you will get an authentication error.

Created by Ikechukwu Akujobi on 01/26/2022
