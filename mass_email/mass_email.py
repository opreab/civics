import smtplib
fromaddr = '@gmail.com'
toaddrs  = '@gmail.com'
msg = 'Why,Oh why!'
username = '@gmail.com'
password = 'pwd'
server = smtplib.SMTP('smtp.gmail.com:587', timeout=10)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
