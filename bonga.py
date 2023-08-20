import time
from atproto import Client
from atproto.exceptions import AtProtocolError
import os
import logging

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

tweeted = False

USERNAME = os.getenv('BLUESKY_USERNAME')
PASSWORD = os.getenv('BLUESKY_PASSWORD')

while not tweeted:
	try:		
		client = Client()
		client.login(USERNAME, PASSWORD)

		client.send_post(text=sentence)
		
		tweeted = True
	except AtProtocolError as e:
		logging.error("Error posting to BlueSky", exc_info=e)
		pass
