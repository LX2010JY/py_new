import socket
import time
import threading

def tcplink(sock,addr):
	print("Accept new connection from %S:%S..."%addr)
	sock.send('Welcome!')
	while True:
		sock.re
