import time
import tweepy as twitter
import os

superhour = time.localtime().tm_hour
hour = superhour % 12
if hour == 0:
	hour = 12

sentence = "Tenho %d lágrima%s no canto do mostrador, %s nos Açores%s" 

if superhour >= 12:
	if hour == 1:
		sentence = sentence % (hour, "", "12 lágrimas", "")
	else:
		sentence = sentence % (hour, "s", "menos uma lágrima", "")
else:
	if hour == 1:
		sentence = sentence % (hour, "", "12 lágrimas", ".")
	else:
		sentence = sentence % (hour, "s", "menos uma lágrima", ".")

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = twitter.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = twitter.API(auth)
api.update_status(status=sentence)
