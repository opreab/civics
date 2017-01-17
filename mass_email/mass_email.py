import sys
import smtplib
import ConfigParser

if len(sys.argv) != 2:
    print "Error: please provide config ini file!")
    sys.exit(1)

cfg = ConfigParser.ConfigParser()
cfg.read(sys.argv[1])


class EmailServer(object):
	def __init__(url, user, pwd)
		self.url = url
		self.user = user
		serf.pwd = pwd
		self.timeout = 10
		self.server = None
		self.connect()

	def connect(self):
		if not self.server:
			try:
				self.server = smtplib.SMTP(self.url, timeout=self.timeout)
				self.server.ehlo()
				self.server.starttls()
				self.server.login(self.user, self.pwd)
			except:
				self.server = None
				raise
	
	def terminate(self):
		if self.server:
			self.server.quit()

	def send_email(self, from, to, msg):
		try:
			self.server.sendmail(fromaddr, toaddrs, msg)
		except:
			raise

def main():
	

if __name__ == '__main__':
	main()