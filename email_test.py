#encoding:utf-8

import smtplib
from email.mime.text import MIMEText
import schedule


#发送邮件
def sendMail():
    # 通过email模块构建邮件体，总共有3个类：MIMEText、MIMEImage、MIMEMultipart，这里采用了最简单的方式.
    # 详情请参考：https://blog.csdn.net/chinesepython/article/details/82465947?ops_request_misc=%7B%22request%5Fid%22%3A%22158152203719725219955221%22%2C%22scm%22%3A%2220140713.130056874..%22%7D&request_id=158152203719725219955221&biz_id=0&utm_source=distribute.pc_search_result.none-task
    text_info = '这是一封测试邮件！'
    msg = MIMEText(text_info,'plain','utf8')
    #设置邮件主题
    msg['Subject']='测试邮件'
    #配置邮件相关配置项
    sender_passwd = 'tmjzjn' #邮箱的授权码，请填写自己的
    receiver_mail = 'cpengwei@126.com'
    sender_mail = '406845011@qq.com'
    mail_server = 'smtp.qq.com' #发件人邮箱的SMTP服务器
    port = 25 #SMTP服务器的端口
    #连接邮件服务器错误验证
    try:
        sftp_obj = smtplib.SMTP(mail_server,port)
        sftp_obj.login(sender_mail,sender_passwd)
        sftp_obj.sendmail(sender_mail,receiver_mail,msg.as_string())
        sftp_obj.quit()
        print('邮件发送成功！')
    except Exception as e:
        print('连接邮件服务器失败，邮件发送失败！')

#创建定时器实现定时
def clock_task():
    schedule.every().minute.do(sendMail) #每分钟运行一次
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    clock_task()