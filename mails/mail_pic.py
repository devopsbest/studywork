
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



mailto_list = ["sh@F.com"]  # 邮件接收方的邮件地址
mail_host = "smtp.office365.com"    # 邮件传送协议服务器
smtp_port = 587
mail_user = "sh@f.com"  # 邮件发送方的邮箱账号
mail_pass = "Good"  # 邮件发送方的邮箱密码

def send_mail(to_list, sub, content):
    me = "Mobile QA"+"<"+mail_user+">"

    msg = MIMEMultipart()
    msg['Subject'] = sub    # 邮件主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    txt = MIMEText("Devices", _subtype='plain', _charset='utf8')
    msg.attach(txt)

    # <b>：黑体  <i>：斜体
    msgText = MIMEText('<b><i>This is a testing email</i> for mobile device management</b> mobile QA team.<img alt="" src="cid:image1" />please ignore it!', 'html', 'utf-8')
    msg.attach(msgText)

    file1 = "/Users/anderson/testcode/device_management/PieChart.png"
    image = MIMEImage(open(file1, 'rb').read())
    image.add_header('Content-ID', '<image1>')
    msg.attach(image)

    try:
        server = smtplib.SMTP(mail_host,smtp_port)
        #server.connect(mail_host,)
        server.starttls()
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        print("pass")
        return True

    except Exception:
        print("fail")
        return False

if __name__ == '__main__':

    sub = "mobile device management test email"

    html = '<html></html>'

    if send_mail(mailto_list, sub, html):

        print("发送成功")
    else:

        print("发送失败")