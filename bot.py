# bot.py

import cfg
import socket
import re
CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

def chat(sock, msg):
	sock.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))

def ban(sock, user):
	chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=600):
	chat(sock, ".timeout {}".format(user, secs))

while True:
	response = s.recv(1024).decode("utf-8")
	print(response)
	sleep(0.1)

while True:
	response = s.recv(1024).decode("utf-8")
	if response == "PING :tmi.twitch.tv\r\n":
		s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
	else:
		username = re.search(r"\w+", line).group(0) # return the entire match
		message = CHAT_MSG.sub("", line)
		print(username + ": " + message)
		if re.match(r"!AQroute", message)
			chat(s, "https://docs.google.com/document/d/11l_EJKb4KS6GnQt6MGnrCnApA0gIwP5ifJ4hbfKLg2c/edit?usp=sharing")
	sleep(1 / cfg.RATE)

