import socket

def Main():
	host = '0.0.0.0'
	port = 5001
	print "======== Reciever started ======="
	print "== Listening on: " + str(host) + ": " + str(port) + " =="
	print "================================="	


	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	
	#message = raw_input('-> ')
	#while message != 'q':
	while True:
		data, addr = s.recvfrom(1024)
		print " Message: [" + str(data) + "] from: " + str(addr)
	print "================================="	
	print "======== Reciever stoped. ======="
	print "================================="	
	s.close()

if __name__ == '__main__':
	Main() 
