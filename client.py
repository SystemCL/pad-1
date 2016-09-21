import socket

def Main():
	host = '127.0.0.1'
	port = 0

	server = ('0.0.0.0', 5000)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	print "============ Client started ================"
	print "==== My adress is: " + str(s.getsockname()) + " ===="
	print "============================================"
	print str(u"\u263A")
	message = raw_input('-> ')
	while message != 'q':
		s.sendto(message, server)
		#data = s.recv(1024)
		#print "Recieved from server : " + str(data)
		message = raw_input('-> ')
	s.close()

if __name__ == '__main__':
	Main()
	
