from twitter import Twitter, TwitterStream, OAuth
import time
import pprint
import requests
import array
from KnuthMorrisPratt import KMP

CREDS = {
	"consumer_key": "Eq7v6Xwduh1WOQ2lnzvrFA",
	"consumer_secret": "qFkOF7PHiPowM4BnjI52Q3OJ4o3kARinzT9YOLRX7YY",
	"token": "16179632-MoUVJ1nJnVWscwECeFM0FfCScCtbTJiAj0i3VTzHI",
	"token_secret": "PIxELGKZc2zPIITlXS4BvsqpwFnp5pJi9m3vJ4xgRsJ9e"
}

auth = OAuth(
	consumer_key = CREDS["consumer_key"],
	consumer_secret = CREDS["consumer_secret"],
	token = CREDS["token"],
	token_secret = CREDS["token_secret"]
)

#buff = array.array('c')
pat = "weapons"
kmp = KMP(pat)
pattern_index = 0

id_dict = {"wikileaks": "16589206", "aljazeera": "76067316", "NYFBI": "211635204", "reutersiran": "47633485", "WhiteHouse":"30313925"}
public_stream = TwitterStream(auth = auth, domain='stream.twitter.com')
iterator = public_stream.statuses.filter(language="en", follow=','.join(id_dict.values()), track="terrorism, weapons, drone attack, i want to kill")
for item in iterator:
	if item['retweeted'] == False:
		try:
			#print (''.join((item['user']['screen_name'], ':', item['text'])))
			text = item['text']
			for c in text.encode():
				print c
				pattern_index = kmp.stream(c, pattern_index)
				print int(pattern_index), len(pat)
				if int(pattern_index) == len(pat):
					print 'passed'
					print "match found"
					break
		except:
			continue



def charsfromfile(f):
	'''a generator for reading a buffered file'''
	while True:
		a = array.array('c')
		a.fromstring(f.read(1000))
		if not a:
			break
		for x in a:
			yield x


	
