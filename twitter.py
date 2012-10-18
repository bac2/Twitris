import pycurl, urllib

USER = "benaclive"
PASS = ""

class Twitter:
	def __init__(self):
		self.buffer = ""
		self.conn = pycurl.Curl()
		self.conn.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))
		self.conn.setopt(pycurl.URL, "https://stream.twitter.com/1.1/statuses/filter.json")
		self.conn.setopt(pycurl.WRITEFUNCTION, self.on_data)
		self.conn.setopt(pycurl.POSTFIELDS, urllib.urlencode( {"track": "raining"}) )
		self.conn.perform()

	def on_data(self, data):
		print data
		self.buffer += data
		if data.endswith("rn") and self.buffer.strip():
			content = json.loads(self.buffer);
			self.buffer = ""

			print content

twit = Twitter()
