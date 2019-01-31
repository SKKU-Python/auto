import smtplib 

from email.mime.text import MIMEText

msg = MIMEText('내용', _charset='euc-kr')
msg['Subject']='제목입니다'
msg['From']='hwoarang67@naver.com'
msg['To']='상대방 메일'

naver_server = smtplib.SMTP_SSL('smtp.naver.com', 465)
naver_server.login('hwoarang67','비밀번호')
naver_server.sendmail('hwoarang67@naver.com','상대방 메일',msg.as_string())
naver_server.quit()
