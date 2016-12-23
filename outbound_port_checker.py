from __future__ import with_statement # Required in 2.5
import socket
import signal
from contextlib import contextmanager
from time import sleep
import sys

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

print "Welcome to my outbound port checker"
print "You want to do back connect tcp reverse shell, right? ;)"

try:
	timeout = int(raw_input('Set Timeout [3]: '))
except ValueError:
	timeout = 3

try:
	begin_port = int(raw_input('Beginning Port [1]: '))
except ValueError:
	begin_port = 1

try:
	end_port = int(raw_input('Beginning Port [65535]: '))
except ValueError:
	end_port = 65535

is_stop = raw_input("Write 'y' if you want to stop search when a port is already opened [n]: ")

print "========================================="
print "Configuration"
print "========================================="
print "Timeout: "+str(timeout)
print "Begin Port: "+str(begin_port)
print "Ending Port: "+str(end_port)

if (is_stop == "y"):
	print "[!] Scanner will stop whenever an opened port found"
else:
	print "[!] Scanner will do the scan from beginning port until the end"

for num in range(begin_port,end_port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		with time_limit(timeout):
			#sleep(5) #just for debug
			
			result = sock.connect_ex(('178.33.250.62',num))
			if result == 0:
				print "[+] Outbound Port " +str(num)+" is opened"
				if (is_stop == "y"):
					sys.exit()
			else:
				print "[-] Outbound Port " +str(num)+ "is blocked"
	except TimeoutException, msg:
		print "[-] Outbound Port " +str(num)+ " is timed out" 