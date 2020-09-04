import socket
from chat_functions import *
import threading
import time

from selm import *

SERVER = "inc.twitch.tv"
PORT = 6667
PASS = #OAUTH

BOT = "TwitchBot"
CHANNEL = "globalcookieclicker"
OWNER = "globalcookieclicker"
message = ""
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(("PASS "+PASS+ "\n"+"NICK "+BOT+"\n"+"JOIN #"+ CHANNEL + "\n").encode())

def twitch():
	joinchat(irc)

	# This loop will constantly read commands from chat
	while True:
		try:
			readbuffer = irc.recv(1024).decode()
		except:
			readbuffer = ""

		for line in readbuffer.split("\r\n"):
			if line == "":
				continue

			if "PING" in line and Console(line):
				msgg = "PONG tmi.twitch.tv\r\n".encode()
				irc.send(msgg)
				#print(msgg)
				continue

			user = getUser(line)
			message = getMessage(line)
			print(user+" : " +message)
	

def cookieclicker():
	global message
	



	while True:
		# Get cookies
		# parse message
		if message[0] !='/':
			continue
		all_commands[message[1:]].click	




if __name__=="__main__":
	t1 = threading.Thread(target=twitch)
	t1.start()

	t2 = threading.Thread(target=cookieclicker)
	t2.start()

	refresh_building = threading.Thread(target=selm.update_building)
	refresh_upgrades = threading.Thread(target=selm.update_upgrades)

	while True:

		time.sleep(7)
		refresh_building.start()

