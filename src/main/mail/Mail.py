import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

class Mail:

    def send_mail(self, file):
                
        # server= "localhost"
        # port=1025
        send_from="selenium_email@email.com"
        send_to=[""] #Enter your email
        subject="Hi you got bot mail"
        text="Nothing really"

        assert isinstance(send_to, list)

        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        # PDF attachment
        fp=open(file,'rb')
        att = MIMEApplication(fp.read(),_subtype="png")
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=file)
        msg.attach(att)            


        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("", "") #Gmail username and app password (Create app password: https://support.google.com/accounts/answer/185833?visit_id=637927400050587854-3245696262&p=InvalidSecondFactor&rd=1)
        server.sendmail(send_from, send_to, msg.as_string())
        server.close()