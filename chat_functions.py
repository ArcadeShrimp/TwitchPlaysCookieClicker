''' Chat functions '''

def joinchat():
	Loading = True

	while Loading:
		readbuffer_join = irc.recv(1024)
		readbuffer_join = readbuffer_join.decode()
		for line in readbuffer_join.split("\n")[0:-1]:
			Loading = loadingComplete(line)
			print(line)

def loadingComplete(line):
	if("End of /NAMES list" in line):
		print("Bot has joined "+ CHANNEL + "'s Channel")
		sendMessage(irc,"Chat Room Joined")
		return False
	return True

def sendMessage(irc, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :"+message
	irc.send((messageTemp+ "\n").encode())


def getUser(line):
	separate = line.split(":",2)
	user = separate[1].split("!",1)[0]

	return user

def getMessage(line):
	try:
		message = (line.split(":",2))[2]
	except:
		messsage = ""
	return message

def Console(line):
	if "PRIVMSG" in line:
		return False
	else:
		return True
