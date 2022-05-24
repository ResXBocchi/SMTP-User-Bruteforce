#!/usr/bin/python3
import sys, socket;

if len(sys.argv) != 3:
	print("Modo de uso:\r\n./smtpenum.py <ip> <userlist>")
else:
	list = open(sys.argv[2],"r+")

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	tcp.connect((sys.argv[1],25))

	banner = tcp.recv(1024)

	print(banner)

	for i in list:

		msg = "VRFY {}\r\n".format(i)

		tcp.send(msg.encode('utf-8'))

		exists = tcp.recv(1024)

		if "252" in str(exists):
			print(exists)
