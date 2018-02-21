import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "passionboy"  # 用户名
mail_pass = "Good"  # 密码

sender = 'passion@163.com'  # 发件人邮箱(最好写全, 不然会失败)
receivers = ['1732865@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

#创建一个带附件的实例
message = MIMEMultipart()

'''
 rar 文件             ctype,encoding值：None None（ini文件、csv文件、apk文件） 
 txt text/plain None 
 py  text/x-python None 
 gif image/gif None 
 png image/x-png None 
 jpg image/pjpeg None 
 pdf application/pdf None 
 doc application/msword None 
 zip application/x-zip-compressed None
 未知类型 application/octet-stream
'''

#构造附件1
att1 = MIMEText(open("/Users/anderson/testcode/python/apiauto/testresult.html", 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="result.html"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
message.attach(att1)


me = 'contentpart'
title = 'Python SMTP Mail Test'  # 邮件主题
body = MIMEText(me)
message.attach(body)
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
message['Subject'] = title

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
    print("mail has been send successfully.")
    smtpObj.quit()
except smtplib.SMTPException as e:
    print(e)