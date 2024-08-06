# main.py
import time
import socket

print("pyEthernetTool")

# def server():
# 	print("server started")
# 	HOST = "127.0.0.1"
# 	PORT = 1234
# 	buf = 20

# 	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	server.bind((HOST, PORT))
# 	server.listen(1)
# 	print("listening")

# 	while True:
# 		conn, addr = server.accept()
# 		print('address: ', addr)
# 		data = conn.recv(buf)
# 		if data:
# 			print("data: ", data)

def client():
	print("client started")
	host = "127.0.0.1"
	port = 1234
	msg = "hellyeah"
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	while True:
		s.send(msg.encode('utf-8'))
		time.sleep(1)
	print("client stopped")

def main():
	print("sdfg")
	# server()
	client()

if __name__ == "__main__":
	main()