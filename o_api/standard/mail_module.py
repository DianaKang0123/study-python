import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



port = 587 # 포트번호는 고정
smtp_server = "smtp.gmail.com"
sender_email = "dianakang0123@gmail.com"  # 보내는사람 메일
receiver_email = "rlfehdtmddnr@naver.com"  # 받는사람 메일
password = "pbwj oskr tkwq zwmw" # 앱 비밀번호/ 임시비번 발급
message = "<h1>보고시퍼</h1>"


msg = MIMEText(message, 'html')
data = MIMEMultipart()
data.attach(msg)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, data.as_string())