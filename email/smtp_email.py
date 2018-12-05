#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'xxx@163.com'
receivers = ['xxx@qq.com']

message = MIMEMultipart()
message['From'] = Header("python book", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = "python SMTP test"
message['Subject'] = Header(subject, 'utf-8')

message.attach(MIMEText('这是Python book 邮件发送测试……', 'plain', 'utf-8'))
#message.attach(MIMEText('这是Python book 邮件发送测试……', 'html', 'utf-8'))

att1 = MIMEText(open('temp.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

att2 = MIMEText(open('temp.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="w3cschool.txt"'
message.attach(att2)

try:
	smtpObject = smtplib.SMTP() 
	smtpObject.connect('smtp.163.com', 25)
	smtpObject.login('xxx@163.com','password')	
	#smtpObject = smtplib.SMTP('smtp.163.com')
	smtpObject.sendmail(sender, receivers, message.as_string())
	print("send email success")
except smtplib.SMTPException as e:
	print("error: can not send the email", e)