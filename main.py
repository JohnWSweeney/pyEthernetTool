# main.py
import time
import socket

def server(ipAddr, port):
	print("server started")
	buf = 100

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((ipAddr, port))
	server.listen(1)
	print("listening")

	try:
		while True:
			conn, addr = server.accept()
			print('address: ', addr)
			data = conn.recv(buf)
			stringData = data.decode('utf-8')
			if data:
				if(stringData == "close"):
					conn.shutdown(socket.SHUT_WR)
					conn.close()
					print("socket closed.")
					break
				else:
					print("data:", stringData)
	except KeyboardInterrupt:
		print("asdf")
	
	server.close()
	print("server closed.")

def client(ipAddr, port, msg):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ipAddr, port))
	try:
		s.send(msg.encode('utf-8'))
	except:
		print("client send failed.")
	s.close()

def main():
	print("pyEthernetTool")
	# server:
	ipAddr = "127.0.0.1"
	port = 1234
	server(ipAddr, port)

	# client:
	# msg = "hellyeah"
	# client(ipAddr, port, msg)

if __name__ == "__main__":
	main()