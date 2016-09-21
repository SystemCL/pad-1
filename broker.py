import socket

def Main():
	#Broker addres
	host = '127.0.0.1'
	port = 5000
	
	#Send to all IP who listen to port 5001
	rec = ('0.0.0.0', 5001)

	print "========= Broker started =========="
	print "== My adress is: " + str(host) +": " + str(port) + " =="
	print "==================================="
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	while True:
		data, addr = s.recvfrom(1024)
		print " Message: [ " + str(data) +  " ] from: " + str(addr)
		data = str(data).upper()
		s.sendto(data, rec)
	s.close()

if __name__ == "__main__":
	Main()

