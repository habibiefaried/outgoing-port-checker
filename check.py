from __future__ import with_statement # Required in 2.5
import socket
import signal
from contextlib import contextmanager
from time import sleep

class TimeoutException(Exception): pass
@contextmanager
def time_limit(seconds):
	def signal_handler(signum, frame):
		raise TimeoutException, "Timed out!"
	signal.signal(signal.SIGALRM, signal_handler)
	signal.alarm(seconds)
	try:
		yield
	finally:
		signal.alarm(0)


timeout = 3 #timeout 3 second, you can modify this

for num in range(1,65535):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		with time_limit(timeout):
			#sleep(5) #just for debug
			
			result = sock.connect_ex(('178.33.250.62',num))
			if result == 0:
			   print "[+] Outbound Port " +str(num)+" is opened"
			else:
			   print "[-] Outbound Port " +str(num)+ "is blocked"
	except TimeoutException, msg:
		print "[-] Outbound Port " +str(num)+ " is timed out" 