# -*- coding:utf-8 -*-
import os
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def insert_img(driver,filename):
    func_path=os.path.dirname(__file__)
    # print(func_path)
    base_dir=os.path.dirname(func_path)
    # print(base_dir)

    # 将路径转化为字符串
    base_dir = str(base_dir)

    # 对路径的字符串进行替换
    base_dir = base_dir.replace('\\', '/')
    # print(base_dir)

    base=base_dir.split('/Website')[0]

    # print(base)
    filepath=base+'/Website/test_report/screenshot/'+filename
    # print(filepath)
    driver.get_screenshot_as_file(filepath)

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = 'smtp.qq.com'

    user = '396321556@qq.com'
    password = 'qgtlypdphibpcahj' #根据自己邮箱密码来设置

    sender = '396321556@qq.com'
    receives = '396321556@qq.com'

    subject = 'Web Selenium 自动化测试报告'


    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send email end!")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file


if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get("http://mp.flins.com.cn")
    insert_img(driver,'index.png')